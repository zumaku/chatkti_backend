from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from chatketi import ChatKeti

app = FastAPI()
chatketi_instance = ChatKeti()

class QueryModel(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Redirect!"}

@app.post("/query")
def get_chatketi_response(query_model: QueryModel):
    response = chatketi_instance.get_response(query_model.query)
    return response