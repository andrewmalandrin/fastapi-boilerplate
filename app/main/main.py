from fastapi import FastAPI

app = FastAPI(
    title='YourDietAuth',
    version='1.0.0'
)

from app.main.routes import *
