import logging 
from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)
class UserService:


    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository    
    def create_user(self, db, user_data):
        logger.info("Creating a new user with email: %s", user_data["email"])
        existing_user=self.user_repository.get_user_by_email(db, user_data["email"])
        if existing_user:
            logger.warning(
                "User already exists with email: %s",
                user_data["email"])
            raise Exception("Email already exists")

                    
        return self.user_repository.create_user(db, user_data)
    
    def get_user(self,db,user_id:int):
        user =self.user_repository.get_user(db,user_id)
        if not user:
            logger.error("User not found with ID: %s", user_id)
            raise Exception("User not found")
        return user
    def get_all_users(self,db):
        return self.user_repository.get_all_users(db)
    
    def update_user(self,db,user_id:int,update_data:dict):
        user=self.user_repository.get_user(db,user_id)
        if not user:
            return {"error": "user not found"}
        return self.user_repository.update_user(db,user_id,update_data)
    
    def delete_user(self, db, user_id: int):

        user = self.user_repository.get_user(db, user_id)

        if not user:
            return {"error": "User not found"}

        return self.user_repository.delete_user(db, user_id)