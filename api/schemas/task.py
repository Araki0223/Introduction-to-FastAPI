from typing import Optional

from pydantic import BaseModel, Field


'''
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

#class TaskCreate(BaseModel):
class TaskCreate(TaskBase):
    #title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    pass


#class Task(BaseModel):
class Task(TaskBase):
    id: int
    #title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    #title: Optional[bool] = Field(None, example="クリーニングを取りに行く") こっちはエラー起きる
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
'''
'''
class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
'''

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

''''''
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
