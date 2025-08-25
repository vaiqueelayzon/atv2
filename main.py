from fastapi import FastAPI
app = FastAPI(title='API do layzon')
@app.get("/")
def hello():
    return{"message": "Hello Word!"}

@app.get("/aluno")
def get_aluno():
    return{"insira na rota após a '/' o nome do aluno"}

@app.get("/aluno/{nome_aluno}")
def get_aluno_by_name(nome_aluno: str):
    return{"o nome do aluno é": nome_aluno}

