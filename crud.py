from schemas import Livro
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine
from models import Livro as LivroModel

def adicionar_livro(livro: Livro):
    db = Session(engine)

    new_livro = LivroModel(
        titulo = livro.titulo,
        autor = livro.autor,
        disponivel = livro.disponivel,
        ano = livro.ano
    )

    db.add(new_livro)
    db.commit()
    db.refresh(new_livro)
    db.close()

    return new_livro


def excluir_livro(id):
    db = Session(engine)
    stmt = select(LivroModel).where(LivroModel.id == id)
    livro = db.execute(stmt).scalar_one_or_none()

    if livro == None:
        return None

    db.delete(livro)
    db.commit()
    db.close()
    
    return True


def buscar_livro(id):
    db = Session(engine)
    stmt = select(LivroModel).where(LivroModel.id == id)
    livro = db.execute(stmt).scalar_one_or_none()
    db.close()

    return livro


def listar_livros():
    db = Session(engine)
    stmt = select(LivroModel)
    livros = db.execute(stmt).scalars().all()
    db.close()

    return livros


def atualizar_livro(id, livro_atualizado: Livro):
    db = Session(engine)
    stmt = select(LivroModel).where(LivroModel.id == id)
    livro = db.execute(stmt).scalar_one_or_none()

    if livro == None:
        return None

    livro.titulo = livro_atualizado.titulo
    livro.autor = livro_atualizado.autor
    livro.ano = livro_atualizado.ano
    livro.disponivel = livro_atualizado.disponivel

    db.commit()
    db.refresh(livro)
    db.close()

    return livro