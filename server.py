import gradio as gr
from application.interview import InterviewQuestionMaker

# Define the function to be used in the Gradio UI
def generate_interview_questions(resume_pdf):
    question_maker = InterviewQuestionMaker()
    questions = question_maker.createQuestions(resume_pdf.name)
    # Process the questions dict using display_questions
    questions_html = display_questions(questions)
    return questions_html
    
# Define a custom output component for displaying questions in cards
def display_questions(questions):
    html = "<div>"
    for category, question_list in questions.items():
        html += f"<h2>{category.replace('_', ' ').title()}:</h2><div>"
        for i, question in enumerate(question_list):
            html += f"<div class='block'><p class='question'>{i+1}. {question}</p></div>"
        html += "</div>"
        html += "<br/>"
    html += "</div>"
    return html

# Create the Gradio UI using block syntax
style = """
.block {
    border-bottom: 0.5px solid lightgrey;
    margin: 8px 8px 20px 8px;
    padding: 16px 16px 16px 0px;
}
.question {
    font-size: 18px;
}
"""

with gr.Blocks(css=style) as demo:
    gr.Markdown("# Generate personal interview questions with your resume")
    gr.Markdown("_We will not store your resume; it will only be used to generate interview questions._")
    input_pdf = gr.inputs.File(type="file")
    generate_btn = gr.Button("Generate")
    output_html = gr.outputs.HTML()
    generate_btn.click(fn=generate_interview_questions, inputs=input_pdf, outputs=output_html)

demo.launch()