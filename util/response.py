from typing import TypeVar, Optional, Generic
from pydantic import validator
from pydantic.generics import GenericModel

from util import status


DataT = TypeVar('DataT')


class DataListModel(GenericModel, Generic[DataT]):
    total: int
    result: DataT


class Response(GenericModel, Generic[DataT]):
    code: int
    data: Optional[DataT]
    message: Optional[str] = None

    @validator('code', always=True)
    def check_consistency(cls, v, values):
        if v == status.HTTP_200_OK and values['data'] is None:
            raise ValueError('must provide data')
        if v != status.HTTP_200_OK and values.get('message') is None:
            raise ValueError('must provide message')
        return v
