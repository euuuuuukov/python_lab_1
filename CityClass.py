class City:
    # Входные данные - название, республика (строки), широта, долгота (десятичные дроби), часовой пояс (строка),
    # является ли столицей (булево значение)
    def __init__(self,
                 name: str, subject: str, latitude: float, longitude: float, timezone: str, is_capital: bool) -> None:
        self.name, self.subject, self._latitude, self._longitude, self.timezone, self.is_capital = \
            name, subject, latitude, longitude, timezone, is_capital

    # Защищаем широту и долготу
    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude
