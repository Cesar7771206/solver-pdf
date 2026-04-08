from fastapi import FastAPI

app = FastAPI(title="Solver PDF", description="Un api que permite analizar y resolver las actividades de un pdf", version='1.0.0.0')

@app.get("/")
def Home():
    return {
        'message':'Wellcome to solver-pdf'
    }