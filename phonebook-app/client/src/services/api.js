import axios from "axios";

const API_URL = "http://127.0.0.1:8000/contacts/";

export const getContacts = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const addContact = async (contact) => {
  const response = await axios.post(API_URL, contact, {
    headers: { "Content-Type": "application/json" },
  });
  return response.data;
};

export const updateContact = async (id, contact) => {
  const response = await axios.put(`${API_URL}${id}`, contact);
  return response.data;
};

export const deleteContact = async (id) => {
  const response = await axios.delete(`${API_URL}${id}`);
  return response.data;
};
