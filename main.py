"""
This is the server of CVQuest
"""
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from application.interview import InterviewQuestionMaker
from application.utils import OpenAIConfig

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static = FastAPI()
static.mount('', StaticFiles(directory="./site/build",
                             html=True), name="static")

question_maker = InterviewQuestionMaker(config=OpenAIConfig(temperature=0.7))


@app.post("/questions/")
async def create_questions(file: UploadFile):
    """
    Create interview questions from a text file uploaded via HTTP POST.

    Args:
        file (UploadFile): The uploaded text file.

    Returns:
        str: The generated interview questions.
    """
    answers = question_maker.create_questions(file.filename)
    return answers
