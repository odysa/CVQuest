import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
from application.interview import InterviewQuestionMaker
from application.parser import ResumeJsonParser

app = typer.Typer()

json_parser = ResumeJsonParser()
question_maker = InterviewQuestionMaker()


@app.command()
def json(file_path: str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        print(json_parser.pdf2json(file_path))


@app.command()
def q(file_path: str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        print(question_maker.createQuestions(file_path))


if __name__ == "__main__":
    app()
