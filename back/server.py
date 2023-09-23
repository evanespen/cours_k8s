from os import getenv

import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PG_HOST=getenv('PG_HOST')
PG_USER=getenv('PG_USER')
PG_PASS=getenv('PG_PASS')
PG_DB=getenv('PG_DB')

class User:
    username: str
    name: str
    address: str
    mail: str
    birthdate: str

    def __init__(self, username, name, address, mail, birthdate):
        self.username = username
        self.name = name
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
    
    def __repr__(self) -> str:
        return f'<User "{self.name}">'
    

@app.get('/users')
def get_users():
    conn = psycopg2.connect(f"dbname={PG_DB} user={PG_USER} password={PG_PASS} host={PG_HOST}")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users_in_db = cur.fetchall()

    users = []
    for u in users_in_db:
        users.append(User(*u))
    
    return users