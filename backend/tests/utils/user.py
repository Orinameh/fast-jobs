from db.repository.user import create_new_user
from schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_random_user(db: Session):
    user = UserCreate(email="user@random.com", password="Random!")
    new_user = create_new_user(user=user, db=db)
    return new_user
