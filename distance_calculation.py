from CityClass import City
from cities_data import high_precision_coordinates_data, low_precision_coordinates_data
from distance import distance

# Вводим Москву
high_moscow = City('Москва', 'Москва',
                   55.76167, 37.60667, 'Europe/Moscow', True)
low_moscow = City('Москва', 'Москва',
                  55.76, 37.61, 'Europe/Moscow', True)

# Рассчитываем по более точным координатам расстояние от Москвы до каждого города
high_to_moscow = {}
for city in high_precision_coordinates_data:
    high_to_moscow[city.name] = distance(city, high_moscow)

# Рассчитываем по более точным координатам расстояние от столиц республик до каждого города в ней
high_to_republic_capital = {}
for city in high_precision_coordinates_data:
    if not city.is_capital:
        for city2 in high_precision_coordinates_data:
            if city2.is_capital and city2.subject == city.subject:
                high_to_republic_capital[city.name] = distance(city, city2)
                break

# Рассчитываем по менее точным координатам расстояние от Москвы до каждого города
low_to_moscow = {}
for city in low_precision_coordinates_data:
    low_to_moscow[city.name] = distance(city, low_moscow)

# Рассчитываем по менее точным координатам расстояние от столиц республик до каждого города в ней
low_to_republic_capital = {}
for city in low_precision_coordinates_data:
    if not city.is_capital:
        for city2 in low_precision_coordinates_data:
            if city2.is_capital and city2.subject == city.subject:
                low_to_republic_capital[city.name] = distance(city, city2)
                break

if __name__ == '__main__':
    print(f'Город, наиболее удаленный от столицы страны: по более точным координатам - '
          f'{max(high_to_moscow, key=high_to_moscow.get)}, по менее точным - '
          f'{max(low_to_moscow, key=low_to_moscow.get)}.')
    print(f'Город, наиболее удаленный от столицы республики: по более точным координатам - '
          f'{max(high_to_republic_capital, key=high_to_republic_capital.get)}, по менее точным - '
          f'{max(low_to_republic_capital, key=low_to_republic_capital.get)}.')
    print(f'Среднее расстояние между городами в рамках одной республики: по более точным координатам - '
          f'{sum(high_to_republic_capital.values()) / len(high_to_republic_capital):.5f} км, по менее точным - '
          f'{sum(low_to_republic_capital.values()) / len(low_to_republic_capital):.2f} км.')
    print(f'Относительная погрешность расчетов: '
          f'{(100 * abs(sum(high_to_republic_capital.values()) - sum(low_to_republic_capital.values())) /
              max(sum(high_to_republic_capital.values()), sum(low_to_republic_capital.values()))):.2f}%.')
