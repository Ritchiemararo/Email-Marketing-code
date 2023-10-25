from datetime import datetime
from pydantic import BaseModel


class userBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    org_id: int
    date_created: datetime

    class Config:
        orm_mode = True

class userCreate(userBase):
    pass
    

class outboxBase(BaseModel):
    date_created: datetime
    
    class Config:
        orm_mode = True

class outbox(outboxBase):
    id: int
    user_id: int
    template_id:int
    emailaddress_id :int
    org_id :int
    status_id:int


class outboxCreate(outboxBase):
    pass

    class Config:
        orm_mode = True

class organizationBase(BaseModel):
    name:str
    date_created: datetime

class organization(organizationBase):
    id:int

    class Config:
        orm_mode = True

class organizationCreate(organizationBase):
    pass


class templateBase(BaseModel):
    data:str
    date_created: datetime

    class Config:
        orm_mode = True


class templatecreate(templateBase):
    pass

  
class emailaddressBase(BaseModel):
    email:str

class emailaddress(emailaddressBase):
    id: int
    date_created: datetime

class emailaddresscreate(emailaddressBase):
    pass

    class Config:
        orm_mode = True

class statusBase(BaseModel):
    status:str

class status(statusBase):
    id: int

class statuscreate(statusBase):
    pass

    class Config:
        orm_mode = True

class subscriberBase(BaseModel):
    name:str
    email:str

class subscriber(subscriberBase):
    id: int
    date_created: datetime

class subscribercreate(subscriberBase):
    pass

    class Config:
        orm_mode = True

