from constants import JWT_ALG, JWT_SECRET
import jwt
from service.user import UserService

class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if not user



