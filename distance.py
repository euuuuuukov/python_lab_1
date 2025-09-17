from math import cos, asin, radians
from CityClass import City


# Вычисление гаверсинуса, a - угол в радианах
def haversine(a: float) -> float:
    return (1 - cos(a)) / 2


# Вычисление расстояния между двумя городами
def distance(city1: City, city2: City) -> float:
    lat1, lon1, lat2, lon2 = city1.latitude, city1.longitude, city2.latitude, city2.longitude
    # 6371 км - средний радиус Земли
    return 2 * 6371 * asin((haversine(radians(lat2 - lat1)) + cos(radians(lat1)) * cos(radians(lat2)) *
                            haversine(radians(lon2 - lon1))) ** 0.5)
