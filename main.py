from fastapi import FastAPI, HTTPException
import crud
from schemas import Livro
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/livros", response_model=list[Livro])
def listar_livros():
    return crud.listar_livros()

@app.get("/livros/{id}", response_model=Livro, responses={ 404: {"description": "Livro não encontrado"} })
def buscar_livro(id: int):
    livro_encontrado = crud.buscar_livro(id)

    if livro_encontrado is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    return livro_encontrado


@app.post("/livros", status_code=201, response_model=Livro, responses={ 409: {"description": "Livro já cadastrado"} })
def adicionar_livro(livro: Livro):
    livro_adicionado = crud.adicionar_livro(livro)

    if livro_adicionado is None:
        raise HTTPException(
            status_code=409,
            detail="Livro já cadastrado"
        )

    return livro_adicionado

@app.put("/livros/{id}", response_model=Livro, responses={ 404: {"description": "Livro não encontrado"} })
def atualizar_livro(id: int, livro: Livro):
    livro_atualizado = crud.atualizar_livro(id, livro)

    if livro_atualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro_atualizado

@app.delete("/livros/{id}", response_model=Livro, responses={ 404: {"description": "Livro não encontrado"} })
def excluir_livro(id: int):
    livro_deletado = crud.excluir_livro(id)
    if livro_deletado is None:
        raise HTTPException(status_code = 404, detail= "Livro não encontrado")
    
    return {"mensagem": "Livro excluído com sucesso"}