from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Resp(BaseModel):
    val_1: float
    val_2: float
    operacao: str




@app.post("/")
async def operacoes(resp: Resp):
    op = resp.operacao[:3].lower()
    if op == "som" or op == "adi" or op == "mai":
        return f"{resp.val_1} + {resp.val_2} = {resp.val_1 + resp.val_2}"
    elif op == "sub" or op == "men":
        return f"{resp.val_1} - {resp.val_2} = {resp.val_1 - resp.val_2}"
    elif op == "mul" or op == "vez":
        return f"{resp.val_1} x {resp.val_2} = {resp.val_1 * resp.val_2}"
    elif op == "div":
        try:
            div = resp.val_1 / resp.val_2
            return f"{resp.val_1} / {resp.val_2} = {div}"

        except ZeroDivisionError:
            return "Não existe divisão por 0"
    else:
        return "Operação inválida!"
