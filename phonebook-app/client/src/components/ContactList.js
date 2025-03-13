import React from "react";

const ContactList = ({ contacts, handleDelete }) => {
  return (
    <div className="contact-list">
      {contacts.length === 0 ? (
        <p>No contacts found.</p>
      ) : (
        contacts.map((contact) => (
          <div key={contact.id} className="contact-card">
            <div className="contact-info">
              <h3>
                {contact.first_name} {contact.last_name}
              </h3>
              <p>{contact.phone}</p>
            </div>
            <button
              onClick={() => handleDelete(contact.id)}
              className="delete-btn"
            >
              X
            </button>
          </div>
        ))
      )}
    </div>
  );
};

export default ContactList;
