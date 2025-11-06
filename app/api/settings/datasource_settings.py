from pydantic_settings import BaseSettings

class DatasourceSettings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASS: str
    NAME: str

    @property
    def url(self) -> str:
        return f"postgresql://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"
    

    class Config: 
        env_prefix = "DB_"
        frozen = True