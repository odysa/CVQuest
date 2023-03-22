"""
This is the server of CVQuest
"""

import requests

from fastapi import FastAPI, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from application.interview import InterviewQuestionMaker
from application.utils import OpenAIConfig

question_maker = InterviewQuestionMaker(config=OpenAIConfig(temperature=0.7))

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/public/', StaticFiles(directory="./site/build",
                                  html=True), name="static")


@app.post("/questions/")
async def create_questions(file: UploadFile):
    """
    Create interview questions from a text file uploaded via HTTP POST.

    Args:
        file (UploadFile): The uploaded text file.

    Returns:
        str: The generated interview questions.
    """
    answers = question_maker.create_questions(file.file)
    return answers

static = FastAPI()
static.mount('', StaticFiles(directory="./site/build",
                             html=True), name="static")

little_nginx = FastAPI()
origins = ["*"]
little_nginx.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

little_nginx.mount("/public", static, name="static")
little_nginx.mount("/api", app, name="api")


@little_nginx.get("/")
async def root(req: Request):
    url = req.url._url
    return RedirectResponse(url + "public")
