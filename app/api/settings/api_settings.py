from pydantic import Field
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):

    OPEN_WEATHER_URL: str = Field(
        description="URL of OpenWeatherMap API.",
    )

    KEY: str = Field(
        description="API key for OpenWeatherMap"
    )

    def getByCoordinates(self):
        return self.OPEN_WEATHER_URL + "?lat={lat}&lon={lon}" + f"&appid={self.KEY}"
    
    def getByCity(self):
        return self.OPEN_WEATHER_URL + "q={city_name}" + f"&appid={self.KEY}"


    class Config: 
        env_prefix = "API_"
        frozen = True
