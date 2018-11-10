from weather import Weather, Unit

def weather_api(city)

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    condition = location.condition
    return condition.text