"""Server module for generating interview questions using Gradio."""

import gradio as gr
from application.interview import InterviewQuestionMaker


def generate_interview_questions(resume_pdf):
    """Generate interview questions based on the given resume PDF."""
    question_maker = InterviewQuestionMaker()
    questions = question_maker.create_questions(resume_pdf.name)
    questions_html = display_questions(questions)
    return questions_html


def display_questions(questions):
    """Display the questions in an HTML format."""
    html = "<div>"
    for category, question_list in questions.items():
        html += f"<h2>{category.replace('_', ' ').title()}:</h2><div>"
        for i, question in enumerate(question_list):
            html += f"<div class='block'><p class='question'>{i+1}. {question}</p></div>"
        html += "</div>"
        html += "<br/>"
    html += "</div>"
    return html


STYLE = """
.block {
    border-bottom: 0.5px solid lightgrey;
    margin: 8px 8px 20px 8px;
    padding: 16px 16px 16px 0px;
}
.question {
    font-size: 18px;
}
"""

INTRO_MD = """
# CVQuest -- Generate personal interview questions from your resume

[![GitHub stars](https://img.shields.io/github/stars/Naereen/StrapDown.js.svg?style=social&label=Star&maxAge=2592000)](https://github.com/odysa/CVQuest)![GitHub followers](https://img.shields.io/github/followers/Naereen.svg?style=social&label=Follow&maxAge=2592000)

[CVQuest](https://github.com/odysa/CVQuest) is an open-source project. If you want to control you know data, please run locally or deploy your own. We will **NOT** store your personal data.

Sponsor: Want preparations beyond interview questions? Check out __[Baynana's AI resume builder](https://baynana.co/)__ to 10x your interview rate.
"""

with gr.Blocks(css=STYLE) as demo:
    gr.Markdown(INTRO_MD)

    input_pdf = gr.inputs.File(type="file")
    generate_btn = gr.Button("Generate")
    output_html = gr.outputs.HTML()
    generate_btn.click(fn=generate_interview_questions,
                       inputs=input_pdf, outputs=output_html)

demo.launch()
