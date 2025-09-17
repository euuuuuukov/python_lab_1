from sys import getsizeof
from CityClass import City


# Генерация списка данных всех городов
high_precision_coordinates_data = [
    City('Екатеринбург', 'Свердловская область',
         56.85190, 60.61220, 'Asia/Yekaterinburg', True),
    City('Реж', 'Свердловская область',
         57.37005, 61.40428, 'Asia/Yekaterinburg', False),
    City('Артемовский', 'Свердловская область',
         57.35550, 61.86865, 'Asia/Yekaterinburg', False),
    City('Асбест', 'Свердловская область',
         57.00993, 61.45776, 'Asia/Yekaterinburg', False),
    City('Березовский', 'Свердловская область',
         56.90830, 60.80190, 'Asia/Yekaterinburg', False),
    City('Петрозаводск', 'Республика Карелия',
         61.78491, 34.34691, 'Europe/Moscow', True),
    City('Сегежа', 'Республика Карелия',
         63.74147, 34.32218, 'Europe/Moscow', False),
    City('Костомукша', 'Республика Карелия',
         64.57100, 30.57667, 'Europe/Moscow', False),
    City('Медвежьегорск', 'Республика Карелия',
         62.91713, 34.45689, 'Europe/Moscow', False),
    City('Кондопога', 'Республика Карелия',
         62.20565, 34.26138, 'Europe/Moscow', False),
    City('Владивосток', 'Приморский край',
         43.10562, 131.87353, 'Asia/Vladivostok', True),
    City('Трудовое', 'Приморский край',
         43.29823, 132.06877, 'Asia/Vladivostok', False),
    City('Большой Камень', 'Приморский край',
         43.11283, 132.35400, 'Asia/Vladivostok', False),
    City('Артем', 'Приморский край',
         43.35950, 132.18887, 'Asia/Vladivostok', False),
    City('Уссурийск', 'Приморский край',
         43.80291, 131.94578, 'Asia/Vladivostok', False)
]

# Генерация того же списка с округлением до 2 знаков после запятой с помощью округления
low_precision_coordinates_data = []
for city in high_precision_coordinates_data:
    low_precision_coordinates_data.append(City(city.name, city.subject, round(city.latitude, 2),
                                               round(city.longitude, 2), city.timezone, city.is_capital))

if __name__ == '__main__':
    # Выводим результат расчета памяти, занимаемой объектами в каждом из списков
    print(f'Размер списка с более точными координатами: '
          f'{sum([getsizeof(city) for city in high_precision_coordinates_data])} байт; с менее точными - '
          f'{sum([getsizeof(city) for city in low_precision_coordinates_data])} байт.')
