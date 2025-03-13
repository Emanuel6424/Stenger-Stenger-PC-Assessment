from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud
import schemas

router = APIRouter()


@router.post("/contacts", response_model=schemas.ContactResponse)
def add_contact(contact_data: schemas.ContactCreate, database_session: Session = Depends(get_db)):
    return crud.create_contact(database_session, contact_data)


@router.get("/contacts", response_model=list[schemas.ContactResponse])
def get_all_contacts(database_session: Session = Depends(get_db)):
    return crud.get_contacts(database_session)


@router.put("/contacts/{contact_id}", response_model=schemas.ContactResponse)
def edit_contact(contact_id: int, contact_data: schemas.ContactUpdate, database_session: Session = Depends(get_db)):
    contact = crud.update_contact(database_session, contact_id, contact_data)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/contacts/{contact_id}")
def remove_contact(contact_id: int, database_session: Session = Depends(get_db)):
    contact = crud.delete_contact(database_session, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Deleted successfully"}
