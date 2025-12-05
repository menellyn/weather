from pydantic import Field

from app.api.dto.common_dto import JSONDto

class UserCommonDTO(JSONDto):
    login: str = Field(description="User's login")
    
class UserRequest(UserCommonDTO):
    password: str = Field(description="User's password")
    
class UserResponse(UserCommonDTO):
    id: int = Field(description="User's id")