from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from chatkti import ChatKTI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
chatkti = ChatKTI()

class QueryModel(BaseModel):
    query: str

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Anda bisa mengganti "*" dengan daftar domain yang diizinkan
    allow_credentials=True,
    allow_methods=["*"],  # Mengizinkan semua metode HTTP
    allow_headers=["*"],  # Mengizinkan semua header
)

@app.get("/")
def read_root():
    return {"message": "ChatKTI is running!"}

@app.post("/query")
def get_chatkti_response(query_model: QueryModel):
    response = chatkti.get_response(query_model.query)
    return response
