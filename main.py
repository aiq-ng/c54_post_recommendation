import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.recommendation.router import recommendation as recommendation_router

app = FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(recommendation_router)

