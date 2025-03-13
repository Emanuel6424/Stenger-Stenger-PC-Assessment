from sqlalchemy.orm import Session
from models import Contact
from schemas import ContactCreate, ContactUpdate

# Function to add a new contact to the database


def create_contact(database_session: Session, contact_data: ContactCreate):
    new_contact = Contact(
        first_name=contact_data.first_name,
        last_name=contact_data.last_name,
        phone=contact_data.phone,
    )
    database_session.add(new_contact)
    database_session.commit()
    database_session.refresh(new_contact)
    return new_contact

# Function to retrieve all contacts


def get_contacts(database_session: Session):
    return database_session.query(Contact).all()

# Function to update an existing contact


def update_contact(database_session: Session, contact_id: int, contact_data: ContactUpdate):
    contact = database_session.query(Contact).filter(
        Contact.id == contact_id).first()
    if contact:
        contact.first_name = contact_data.first_name
        contact.last_name = contact_data.last_name
        contact.phone = contact_data.phone
        database_session.commit()
        database_session.refresh(contact)
    return contact

# Function to delete a contact


def delete_contact(database_session: Session, contact_id: int):
    contact = database_session.query(Contact).filter(
        Contact.id == contact_id).first()
    if contact:
        database_session.delete(contact)
        database_session.commit()
    return contact
