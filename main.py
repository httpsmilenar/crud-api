from fastapi import FastAPI
import pymongo
from password import PASSWORD

app = FastAPI()
client = pymongo.MongoClient(f"mongodb+srv://httpsmilenar:{PASSWORD}@cluster0.jgp9d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mila.users

@app.get("/rodrigues")
async def root():
    return "ok"

    # Create
@app.post("/sabor")
def create_taste(taste: dict):
    db.insert_one(taste)
    return "sabor de sorvete adicionado com sucesso!"

    # Read
@app.get("/sabores/{sabor}")
def read_taste(sabor: str):
    taste = db.find_one({"sabor": sabor})
    if taste != None:
        return "sim. temos esse sabor de sorvete!"
    else:
        return "que pena! não temos esse sabor de sorvete."

    # Update
@app.put("/alterar/")
def update_taste(sabor: str, novo_sabor: str):
    db.update_one({"sabor": sabor}, {"$set": {"sabor": novo_sabor}})
    return "sabor alterado com sucesso!"

    # Delete
@app.delete("/deletar/")
def delete_taste(sabor: str):
    db.delete_one({"sabor": sabor})
    return "sabor deletado com sucesso!"