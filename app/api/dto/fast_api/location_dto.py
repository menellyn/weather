from pydantic import Field
from decimal import Decimal

from app.api.dto.common_dto import JSONDto

class LocationCommonDTO(JSONDto):
    name: str = Field(description="Name of location")
    user_id: int = Field(description="The ID of the user who added the location")
    latitude: Decimal = Field(description="Latitude of location")
    longitude: Decimal = Field(description="Longitude of location")
    
    
class LocationRequest(LocationCommonDTO):
    pass
    
class LocationResponse(LocationCommonDTO):
    id: int = Field(description="Id of location")