
from fastapi import FastAPI, Response,status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..schemas import users
from .. import models, utils
from ..database import get_db


router =  APIRouter(
    prefix="/users",
    tags= ['Users'],
    
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=users.UserOut)
async def create_user(user: users.UserCreate, db: Session = Depends(get_db)):
    
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get("/{id}", response_model=users.UserOut)
async def get_user(id: int, db: Session = Depends(get_db)):
   user = db.query(models.User).filter(models.User.id == id).first()
   
   if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} not found")
    
   return user