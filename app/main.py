from fastapi import FastAPI
from .routers import conversion_to_md

app = FastAPI(title="Solver PDF", description="Un api que permite analizar y resolver las actividades de un pdf", version='1.0.0.0')

app.include_router(conversion_to_md.router)

@app.get("/")
def Home():
    return {
        'message':'Wellcome to solver-pdf'
    }