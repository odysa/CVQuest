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
p {
    font-size: 16px;
}

.block {
    border-bottom: 0.5px solid lightgrey;
    margin: 8px 8px 20px 8px;
    padding: 16px 16px 16px 0px;
}

.question {
    font-size: 18px;
}
"""

INTRO_HTML = """
<h1>CVQuest -- Generate personal interview questions from your resume</h1>

<p style="display:flex">
<a href="https://github.com/odysa/CVQuest">
<img style="margin-left:3px" src="https://img.shields.io/github/stars/odysa/CVQuest.svg?style=social&label=Star&maxAge=2592000" />
</a>
<a href="https://github.com/odysa">
<img style="margin-left:3px" src="https://img.shields.io/github/followers/odysa.svg?style=social&label=Follow&maxAge=2592000" />
</a>
</p>

<p>
<a href="https://github.com/odysa/CVQuest">CVQuest</a> is an open-source project. Feel free to run locally or deploy your own if you want to control your personal data,
</p>
<p>
We will <b>NOT</b> store your personal data.
</p>
"""

SPONSOR_HTML = """
Sponsor: Want preparations beyond interview questions? Check out <a href="https://baynana.co/">Baynana's AI resume builder</a> to 10x your interview rate.
"""


with gr.Blocks(css=STYLE, title="CVQuest", theme=gr.themes.Soft()) as demo:
    gr.HTML(INTRO_HTML)
    input_pdf = gr.File(file_types=[".pdf"],)
    generate_btn = gr.Button("Generate🎲")
    output_html = gr.outputs.HTML()
    generate_btn.click(fn=generate_interview_questions,
                       inputs=input_pdf, outputs=output_html)

    gr.HTML(SPONSOR_HTML)

demo.launch()
