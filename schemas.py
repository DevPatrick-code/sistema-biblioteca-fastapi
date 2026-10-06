from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Livro(BaseModel):
    id: int = Field(gt=0)
    titulo: str = Field(min_length=1)
    autor: str = Field(min_length=1)
    disponivel: bool = True
    ano: int = Field(gt=0)

    @field_validator("titulo", "autor")
    @classmethod
    def validar_texto(cls, valor):
        if not valor.strip():
            raise ValueError("O campo não pode ficar vazio")

        return valor.strip()

    @field_validator("ano")
    @classmethod
    def validar_ano(cls, valor):
        ano_atual = datetime.now().year

        if valor > ano_atual:
            raise ValueError("O ano não pode ser maior que o ano atual")

        return valor