import React, { useState } from "react";
import "../style.css";

const AddContactForm = ({ addContact }) => {
  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    phone: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.first_name || !form.last_name || !form.phone) return;
    addContact(form);
    setForm({ first_name: "", last_name: "", phone: "" });
  };

  return (
    <form className="contact-form" onSubmit={handleSubmit}>
      <input
        type="text"
        name="first_name"
        placeholder="First Name"
        value={form.first_name}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="last_name"
        placeholder="Last Name"
        value={form.last_name}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="phone"
        placeholder="Phone"
        value={form.phone}
        onChange={handleChange}
        required
      />

      <div className="contacts-header">
        <h2>Contacts</h2>
        <button type="submit" className="add-contact-btn">
          + Add Contact
        </button>
      </div>
    </form>
  );
};

export default AddContactForm;
