from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    autor: Mapped[str] = mapped_column(String(100))
    ano: Mapped[int] = mapped_column(Integer)
    disponivel: Mapped[bool] = mapped_column(Boolean, default=True)
    
    def __repr__(self) -> str:
        return f"Livro(id={self.id!r}, titulo={self.titulo!r}, autor={self.autor!r}, ano={self.ano!r}, disponivel={self.disponivel!r})"

