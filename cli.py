"""
This script provides a command-line interface to process PDF resumes and generate
interview questions or convert the resumes to JSON format using the `InterviewQuestionMaker`
and `ResumeJsonParser` classes.

The script offers two commands:
- `json`: Converts a given PDF resume file to JSON format.
- `q`: Generates interview questions based on the content of a given PDF resume file.

Example usage:

python script_name.py json /path/to/resume.pdf
python script_name.py q /path/to/resume.pdf

"""

import typer
from rich import print as pprint
from rich.progress import Progress, SpinnerColumn, TextColumn
from application.interview import InterviewQuestionMaker
from application.parser import ResumeJsonParser

app = typer.Typer()

json_parser: ResumeJsonParser = ResumeJsonParser()
question_maker: InterviewQuestionMaker = InterviewQuestionMaker()


@app.command()
def json(file_path: str):
    """
    Convert a PDF resume file to JSON format.

    Args:
        file_path (str): The path to the PDF resume file.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(json_parser.pdf2json(file_path))


@app.command("q")
def question(file_path: str):
    """
    Generate interview questions based on the content of a PDF resume file.

    Args:
        file_path (str): The path to the PDF resume file.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(question_maker.create_questions(file_path))


if __name__ == "__main__":
    app()
