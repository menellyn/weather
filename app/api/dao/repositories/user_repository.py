from collections.abc import Callable
from contextlib import AbstractContextManager
from sqlalchemy.orm import Session

from app.api.dao.models.users_orm import UsersOrm
from app.api.dao.repositories.base.base_repository import BaseRepository
from app.api.constants.error_constants import USER_LOGIN_NOT_FOUND_ERROR
from app.api.exceptions.not_found_exception import NotFoundException

class UserRepository(BaseRepository):
    
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        super.__init__(session_factory, UsersOrm)
        self.session_factory = session_factory
        
    def get_by_login(self, login: str) -> UsersOrm:
        with self.session_factory() as session:
            user = (
                session.query(UsersOrm)
                .filter(UsersOrm.login == login)
                .first()
            )
            if not user:
                raise NotFoundException(
                    USER_LOGIN_NOT_FOUND_ERROR.format(
                        entity_class=self.entity_class.__name__,
                        entity_login=login,
                    )
                )
            return user