from typing import Generic, TypeVar, Type, List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from model.base import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class RepoBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete
        :param model: SQLAlchemy model
        """
        self._model = model

    def get(self, db_session: Session, id: int) -> Optional[ModelType]:
        return db_session.query(self._model).filter(self._model.id == id).first()

    def list(self, db_session: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db_session.query(self._model).offset(skip).limit(limit).all()

    def create(self, db_session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self._model(**obj_in_data)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def update(self, db_session: Session, *, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        obj_data = jsonable_encoder(obj_in)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def remove(self, db_session: Session, *, id: int) -> ModelType:
        obj = db_session.query(self._model).get(id)
        db_session.delete(obj)
        db_session.commit()
        return obj
