from fastapi import FastAPI
import pymongo
from password import PASSWORD

app = FastAPI()
client = pymongo.MongoClient(f"mongodb+srv://httpsmilenar:{PASSWORD}@cluster0.jgp9d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mila.users

app = FastAPI()

@app.get("/rodrigues")
async def root():
    return "ok"

# Create 
@app.post("/cor")
def create_color(color: dict):
    print(db)
    db.insert_one(color)
    return f"cor adicionada com sucesso!"

# Read
@app.get("/usuarios/{cor}")
def read_username(cor: str):
    user = db.find_one({"cor": cor})
    if user != None:
        return "sim, temos essa cor!"
    else:
        return "cor não encontrada!"

# Update
@app.put("/alterar/")
def update_username(cor: str, nova_cor: str):
    db.update_one({"cor": cor}, {"$set": {"cor": nova_cor}})
    return "cor alterada com sucesso!"

# Delete
@app.delete("/deletar/")
def delete_username(cor: str):
    db.delete_one({"cor": cor})
    return "cor deletada com sucesso!"