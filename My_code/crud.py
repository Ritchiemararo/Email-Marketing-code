from sqlalchemy.orm import Session

import models, schemas


def create_user(db: Session, user: models.user):
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.user).filter(models.user.id == user_id).first()


def create_outbox(db: Session, outbox: models.outbox):
    db_outbox= models.outbox(*outbox.dict())
    db.add(db_outbox)
    db.commit()
    db.refresh(db_outbox)
    return db_outbox

def get_outbox(db: Session, outbox_id: int):
    return db.query(models.outbox).filter(models.outbox.id == outbox_id).first()

def create_organization(db: Session, organization: models.organization):
    db_organization= models.organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def get_organization(db: Session, organization_id: int):
    return db.query(models.organization).filter(models.organization.id == organization_id).first()

def create_template(db: Session, template: models.template):
    db_template= models.template(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

def get_template(db: Session, template_id: int):
    return db.query(models.template).filter(models.template.id == template_id).first()

def create_emailaddress(db: Session, emailaddress: models.emailaddress):
    db_emailaddress= models.emailaddress(**emailaddress.dict())
    db.add(db_emailaddress)
    db.commit()
    db.refresh(db_emailaddress)
    return db_emailaddress

def get_emailaddress(db: Session, emailaddress_id: int):
    return db.query(models.emailaddress).filter(models.emailaddress.id == emailaddress_id).first()

def create_status(db: Session, status: models.status):
    db_status= models.status(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

def get_status(db: Session, status_id: int):
    return db.query(models.status).filter(models.status.id == status_id).first()

def create_subscriber(db: Session, subscriber: models.subscriber):
    db_subscriber= models.subscriber(**subscriber.dict())
    db.add(db_subscriber)
    db.commit()
    db.refresh(db_subscriber)
    return db_subscriber

def get_subscriber(db: Session, subscriber_id: int):
    return db.query(models.subscriber).filter(models.subscriber.id == subscriber_id).first()









