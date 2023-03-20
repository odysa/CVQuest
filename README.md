# CVQuest
<div align="center">
<h3>Let AI interview you!</h3>
<strong>
<samp>

[English](README.md) -
[简体中文](README.zh-Hans.md)
</samp>
</strong>
</div>
<br>
<br>
This command line interface (CLI) tool is designed to help interviewers and recruiters by automatically generating interview questions based on a candidate's resume. The tool uses a combination of a resume parser to extract information from the resume and an interview question maker to create relevant questions.

CVQuest also provides a Gradio-based user interface that allows users to upload their resume in PDF format and receive a list of interview questions organized by category.

## Features ✨
* Parse resume files in PDF format and convert them into a JSON format
* Generate interview questions based on the information extracted from the resume
* Gradio-based user interface for generating personalized interview questions

## Dependencies
* Python 3.8 or later
* typer
* OpenAI
* Gradio

## Installation

1. Clone the repository:
```bash
git clone https://github.com/odysa/CVQuest-CLI
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. This application depends on OpenAI. Please set your api key
```
export OPENAI_API_KEY = <you-api-key>
```
## Usage

There are two main commands available in the CLI:

1. q: Generate interview questions based on the information extracted from a resume
2. json: Parse a resume PDF file and convert it into JSON format

### Generate Interview Questions from resume (CLI)
```bash
python main.py q <file_path>
```
Example:
```json
{
  "technical_questions": [
    "Can you discuss your experience with LSM-based storage engines? What are the main benefits of this approach, and how did you apply it in your work on AgateDB?",
    "In your work on Zone-Aware Garbage Collection for TerarkDB, what were the key performance metrics you used to evaluate the effectiveness of your implementation? How did it compare to other approaches?"
    ......
  ],
  "behavior_questions": [
    "How do you approach working in a team environment? Can you provide an example of a successful collaboration with team members on a challenging project?",
    "As a RisingLight Project Maintainer, how do you balance your responsibilities as a maintainer with your other commitments? How do you ensure that you are meeting the needs of the project and the community while also managing your own workload?"
    ......
  ]
}
```

### Generate Json Output from resume (CLI)
```bash
python main.py json <file_path>
```
Example:

_Available soon_

### Generate Interview Questions from resume (Gradio UI)

To launch the Gradio UI for generating personalized interview questions based on a user's resume, simply execute the following command in your terminal:

```python3 server.py```

After running the command, the Gradio UI will be launched in your default web browser, allowing you to upload a resume in PDF format and generate interview questions.

#### UI Preview
<img width="1422" alt="image" src="https://user-images.githubusercontent.com/61036578/226255002-a1a661fa-86a8-4a82-9b29-3da68b088920.png">



## You may also enjoy our AI Resume Builder: baynana.co 🚀

[Baynana.co](https://baynana.co) is an AI-powered resume builder that helps you create a professional resume tailored to your industry. With Baynana AI, you can:

- Build your resume with zero effort by chatting with Baynana AI, your personal resume assistant
- Get real-time ATS feedback as you edit, so you can be sure your resume is ATS-friendly
- Export your resume in PDF, LaTex, and even website-ready HTML formats

👉 [Get started with Baynana.co today!](https://baynana.co)
