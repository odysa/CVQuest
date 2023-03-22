from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from application.interview import InterviewQuestionMaker
from application.utils import OpenAIConfig
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

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
async def create_upload_file(file: UploadFile):
    answers = question_maker.create_questions(file.filename)
    return answers
