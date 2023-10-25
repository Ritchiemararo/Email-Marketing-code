from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()

@app.post("/template/", response_model=schemas.templateBase)
def create_template(template: schemas.templatecreate, db: Session = Depends(get_db)):
    return crud.create_template(db, template)

@app.post("/user/", response_model=schemas.userCreate)
def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/user/{user_id}", response_model=schemas.userBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/outbox/", response_model=schemas.outbox)
def create_outbox(outbox: schemas.outboxCreate, db: Session = Depends(get_db)):
    return crud.create_outbox(db, outbox)

@app.get("/outbox/{outbox_id}", response_model=schemas.outbox)
def read_outbox(outbox_id: int, db: Session = Depends(get_db)):
    db_outbox = crud.get_outbox(db, outbox_id)
    if db_outbox is None:
        raise HTTPException(status_code=404, detail="Outbox not found")
    return db_outbox

@app.post("/organization/", response_model=schemas.organization)
def create_organization(organization: schemas.organizationCreate, db: Session = Depends(get_db)):
    return crud.create_organization(db, organization)

@app.get("/organization/{organization_id}", response_model=schemas.organization)
def read_organization(organization_id: int, db: Session = Depends(get_db)):
    db_organization = crud.get_organization(db, organization_id)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="organization not found")
    return db_organization

@app.post("/emailaddress/", response_model=schemas.emailaddress)
def create_emailaddress(emailaddress: schemas.emailaddresscreate, db: Session = Depends(get_db)):
    return crud.create_emailaddress(db, emailaddress)

@app.get("/emailaddress/{emailaddress_id}", response_model=schemas.emailaddress)
def read_emailaddress(emailaddress_id: int, db: Session = Depends(get_db)):
    db_emailaddress = crud.get_emailaddress(db, emailaddress_id)
    if db_emailaddress is None:
        raise HTTPException(status_code=404, detail="emailaddress not found")
    return db_emailaddress

@app.post("/status/", response_model=schemas.status)
def create_status(status: schemas.statuscreate, db: Session = Depends(get_db)):
    return crud.create_status(db, status)

@app.get("/status/{status_id}", response_model=schemas.status)
def read_status(status_id: int, db: Session = Depends(get_db)):
    db_status = crud.get_emailaddress(db, status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="status not found")
    return db_status

@app.post("/subscriber/", response_model=schemas.subscriber)
def create_subscriber(subscriber: schemas.subscribercreate, db: Session = Depends(get_db)):
    return crud.create_subscriber(db, subscriber)

@app.get("/subscriber/{subscriber_id}", response_model=schemas.subscriber)
def read_subscriber(subscriber_id: int, db: Session = Depends(get_db)):
    db_subscriber = crud.get_emailaddress(db, subscriber_id)
    if db_subscriber is None:
        raise HTTPException(status_code=404, detail="subscriber not found")
    return db_subscriber

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
