# 📞 Phone Book App

A **full-stack** phone book application built with **FastAPI, PostgreSQL, and React**.  
It allows users to **add, search, update, and delete contacts** with a **modern UI**.

## **🚀 Technologies Used**

- **Frontend**: React.js, Axios
- **Backend**: FastAPI, Uvicorn
- **Database**: PostgreSQL, SQLAlchemy

---

## **📌 Setup Instructions**

Follow these steps to **install and run the application** on your local machine.

---

## **🛠️ 1. Clone the Repository**

```sh
git clone git@github.com:Emanuel6424/TaskFlow.git
cd phonebook-app
```

## **🐍 2. Backend Setup (FastAPI + PostgreSQL)**

### 📌 2.1 Create a Virtual Environment For Backend

Navigate to the server directory:

```sh
cd server
```

Create a virtual environment:

Mac/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

Windows (Command Prompt):

```sh
python -m venv venv
venv\Scripts\activate
```

### 📌 2.2 Install Required Python Packages

Run the following command to install all backend dependencies:

```sh
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install psycopg2
pip install pydantic
```

### 📌 2.3 Setup PostgreSQL Database

#### Step 1: Install PostgreSQL

Mac:

```sh
brew install postgresql
```

Windows: Download and install PostgreSQL.

#### Step 2: Start PostgreSQL Service

Mac:

```sh
brew services start postgresql
```

Windows:

```sh
net start postgresql
```

#### Step 3: Login to PostgreSQL

```sh
psql -U postgres
```

#### Step 4: Execute SQL Commands

Inside PostgreSQL, run:

```sql
CREATE DATABASE phonebook;

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(100)
);
```

#### Step 5: Modify `database.py`

Open `database.py` and update `DATABASE_URL` with your PostgreSQL username and password:

```python
DATABASE_URL = "postgresql://your_username:your_password@localhost/phonebook"
```

Replace `your_username` and `your_password` with your actual PostgreSQL credentials.

### 📌 2.4 Run FastAPI Backend

Now, start the backend server:

```sh
uvicorn main:app --reload
```

The API should be running at:

- **Base URL**: http://127.0.0.1:8000
- **Swagger Docs (copy url on to web to make sure backend is working)**: http://127.0.0.1:8000/docs

## **⚛️ 3. Frontend Setup (React.js)**

Navigate to the client directory:

```sh
cd ../client
```

### 📌 3.1 Install Required NPM Packages

```sh
npm install
```

### 📌 3.2 Start the React App

```sh
npm start
```

**if it doesn't work run **:

```sh
npm run start
```

The frontend should now be running at:  
http://localhost:3000 🎉

## **📌 4. API Endpoints**

| HTTP Method | Endpoint                 | Description                |
| ----------- | ------------------------ | -------------------------- |
| GET         | `/contacts`              | Fetch all contacts         |
| POST        | `/contacts`              | Add a new contact          |
| PUT         | `/contacts/{contact_id}` | Update an existing contact |
| DELETE      | `/contacts/{contact_id}` | Delete a contact           |

## **✅ 5. Full Project Structure**

```
phonebook-app/
│-- client/              # React Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── AddContactForm.js
│   │   │   ├── ContactList.js
│   │   │   ├── SearchBar.js
│   │   ├── services/
│   │   │   ├── api.js
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── style.css
│   ├── public/
│   ├── package.json
│   ├── README.md
│
│-- server/              # FastAPI Backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── contacts_routes.py
│   ├── requirements.txt
│
└── README.md
```

## **🎯 6. Common Issues & Fixes**

### ⚠️ Issue: "ModuleNotFoundError: No module named 'fastapi'"

**Fix:** Run:

```sh
pip install fastapi
```

### ⚠️ Issue: "psycopg2 OperationalError: Could not connect to server"

**Fix:** Ensure PostgreSQL is running:

```sh
brew services start postgresql  # Mac
net start postgresql            # Windows
```

✅ Verify your database credentials in `DATABASE_URL` inside `database.py`.

### ⚠️ Issue: "npm ERR! missing script: start"

**Fix:** Make sure you're in the `client/` folder and run:

```sh
npm start
```

## **📌 7. How to Deploy**

```sh
npm run build
```

## **🎉 8. Contributors**

- **Emanuel Sanchez** - Developer
