# CVQuest

Let AI generate your interview questions!
<br>
<br>
This command line interface (CLI) tool is designed to help interviewers and recruiters by automatically generating interview questions based on a candidate's resume. The tool uses a combination of a resume parser to extract information from the resume and an interview question maker to create relevant questions.

## Features
* Parse resume files in PDF format and convert them into a JSON format
* Generate interview questions based on the information extracted from the resume

## Dependencies
* Python 3.8 or later
* typer
* OpenAI

# Installation

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

## Generate Interview Questions from resume
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

## Generate Json Output from resume
```bash
python main.py json <file_path>
```
Examples:

Available soon
