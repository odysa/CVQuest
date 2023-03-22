"""
Module for generating interview questions from a PDF file.
"""

import re
import PyPDF2
from application.prompts import QUESTION_PROMPT
from application.utils import OpenAIConfig, query_ai
from typing import Union, IO

class InterviewQuestionMaker:
    """
    Class to create interview questions based on a PDF resume.
    """

    def __init__(self, config: OpenAIConfig = OpenAIConfig(), prompt: str = QUESTION_PROMPT):
        """Initialize the InterviewQuestionMaker with the specified configuration."""
        self.config = config
        self.prompt = prompt

    def create_questions(self, pdf_stream: Union[str, IO]) -> str:
        """
        Create interview questions for the given PDF resume file.

        Args:
            pdf_stream (IO): The PDF file as a stream.
        """
        pdf_str = self.pdf_to_str(pdf_stream)
        prompt = self.complete_prompt(pdf_str)
        return query_ai(self.config, prompt)

    def complete_prompt(self, pdf_str: str) -> str:
        """
        Complete the prompt with the given PDF string.

        Args:
            pdf_str (str): PDF content as a string.
        """
        return self.prompt.format(resume=pdf_str)

    def pdf_to_str(self, pdf_stream: Union[str, IO]) -> str:
        """
        Convert the given PDF file to a string.

        Args:
            pdf_stream (IO): The PDF file as a stream.
        """
        pdf = PyPDF2.PdfReader(pdf_stream)
        pages = [self.format_pdf(p.extract_text()) for p in pdf.pages]
        return "\n\n".join(pages)

    def format_pdf(self, pdf_str: str) -> str:
        """
        Format the given PDF string by applying pattern replacements.

        Args:
            pdf_str (str): PDF content as a string.
        """

        pattern_replacements = {
            r"\s[,.]": ",",
            r"[\n]+": "\n",
            r"[\s]+": " ",
            r"http[s]?(://)?": "",
        }

        for pattern, replacement in pattern_replacements.items():
            pdf_str = re.sub(pattern, replacement, pdf_str)

        return pdf_str
