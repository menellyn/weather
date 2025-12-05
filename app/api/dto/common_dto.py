from caseconverter import camelcase 
from pydantic import BaseModel


class JSONDto(BaseModel):

    class Config:  
        alias_generator = camelcase
        allow_population_by_field_name = True
        use_enum_values = True
