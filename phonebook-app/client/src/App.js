import React, { useState, useEffect } from "react";
import { getContacts, addContact, deleteContact } from "./services/api";
import ContactList from "./components/ContactList";
import AddContactForm from "./components/AddContactForm";
import SearchBar from "./components/SearchBar";
import "./style.css";

function App() {
  const [contacts, setContacts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetchContacts();
  }, []);

  const fetchContacts = async () => {
    const data = await getContacts();
    setContacts(data);
  };

  const handleAddContact = async (contact) => {
    await addContact(contact);
    fetchContacts();
  };

  const handleDeleteContact = async (id) => {
    await deleteContact(id);
    fetchContacts();
  };

  const filteredContacts = contacts.filter((contact) =>
    `${contact.first_name} ${contact.last_name}`
      .toLowerCase()
      .includes(searchTerm.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Phone Book App</h1>
      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      <AddContactForm addContact={handleAddContact} />
      <ContactList
        contacts={filteredContacts}
        handleDelete={handleDeleteContact}
      />
    </div>
  );
}

export default App;
