from fastapi import FastAPI
import ceps
import functools

app = FastAPI()

@app.get("/")
def cep(theirs: str, mine: str):
    if not ceps.valid(mine):
        return {"error": f"Your CEP {mine} seems to be invalid"}

    if not ceps.valid(theirs):
        return {"error": f"Their CEP {theirs} seems to be invalid"}

    if theirs == mine: 
        return {"error": "It will not be funny if you provide the same CEP as yours"}

    resemblances = ceps.compare(theirs, mine, [])
    if len(resemblances) <= 0:
        return "Y'all live really far from each other"

    return f"Y'all live in the same {functools.reduce(lambda rsb, acc: f'{acc}, {rsb}', resemblances)}"