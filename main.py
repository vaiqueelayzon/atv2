from fastapi import FastAPI
app = FastAPI(title='API do layzon')
@app.get("/")
def hello():
    return{"message": "Hello Word!"}
