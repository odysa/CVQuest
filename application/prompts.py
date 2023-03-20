"""
A module of pre-defined prompts
"""

PARSER_PROMPT = """
I want to you extract information from a PDF resume.
Summarize it into a JSON with EXACTLY the following structure
///
{"personal_detail":{"first_name":"","last_name":"","email":"","phone_number":"","location":"","portfolio_website_url":"","linkedin_url":"","github_main_page_url":""},"education_history":[{"university":"","education_level":"","graduation_year":"","graduation_month":"","majors":"","GPA":""}],"work_experience":[{"job_title":"","company":"","location":"","begin_time":"","end_time":"","job_summary":""}],"project_experience":[{"project_name":"","project_description":""}]}
///
My original resume is as below
"""

QUESTION_PROMPT = """
You are an experienced interviewer who specializes in generating specific interview questions based on a candidate's resume text. Your task is to provide thought-provoking and relevant questions that help assess a candidate's suitability for a job, including both behavioral and technical aspects. For each provided resume text, generate unique technical interview questions and unique behavioral interview questions. Make behavioral questions related to resume. Please structure your response as follows:

Output:
{{
  "technical_questions":[],
  "behavior_questions":[],
}}

My resume text is as below
\"\"\"
{resume}
\"\"\"

Follow the Examples. Be careful that examples may include some details not provided in abode resume:
{{
  "technical_questions":[
    "Can you discuss your experience with LSM-based storage engines? What are the main benefits of this approach, and how did you apply it in your work on AgateDB?",
    "As a Database System R&D Intern at Singularity Data, Inc., what challenges did you face when designing and implementing shared state for streaming index in RisingWave? How did you overcome these challenges?",
    "In your work on Zone-Aware Garbage Collection for TerarkDB, what were the key performance metrics you used to evaluate the effectiveness of your implementation? How did it compare to other approaches?,
  ],
  "behavior_questions":[
    "Can you describe a time when you had to work on a project with a tight deadline? How did you prioritize your tasks and manage your time effectively to ensure successful completion of the project?",
    "How do you approach working in a team environment? Can you provide an example of a successful collaboration with team members on a challenging project?",
    "As a RisingLight Project Maintainer, how do you balance your responsibilities as a maintainer with your other commitments? How do you ensure that you are meeting the needs of the project and the community while also managing your own workload?"
  ]
}}
"""
