from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from chatketi import ChatKeti
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
chatketi_instance = ChatKeti()

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
    return {"message": "Redirect!"}

@app.post("/query")
def get_chatketi_response(query_model: QueryModel):
    response = chatketi_instance.get_response(query_model.query)
    return response
