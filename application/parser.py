"""
A module to parse resume PDF files and convert them into JSON format using GPT-3.

This module provides a ResumeJsonParser class that can be used to convert
resume PDF files into JSON format. The conversion is performed using the GPT-3
language model provided by the OpenAI API.
"""
import re
import PyPDF2
from application.prompts import PARSER_PROMPT
from application.utils import OpenAIConfig, query_ai


class ResumeJsonParser:
    """A class to parse resume PDF files and convert them into JSON format using GPT-3."""

    def __init__(self, config: OpenAIConfig = OpenAIConfig(), prompt: str = PARSER_PROMPT):
        """
        Initialize the ResumeJsonParser with the specified configuration.

        Args:
            config (OpenAIConfig): OpenAI API configuration.
            prompt (str): Custom prompt for GPT-3.
        """
        self.config = config
        self.prompt = prompt

    def pdf2json(self, pdf_path: str):
        """
        Convert the PDF resume file to a JSON representation.

        Args:
            pdf_path (str): Path to the PDF resume file.

        Returns:
            dict: JSON representation of the resume.
        """
        pdf_str = self.pdf2str(pdf_path)
        json_data = self.__str2json(pdf_str)
        return json_data

    def __str2json(self, pdf_str: str):
        """
        Convert the resume string to a JSON representation using GPT-3.

        Args:
            pdf_str (str): Resume string.

        Returns:
            dict: JSON representation of the resume.
        """
        prompt = self.__complete_prompt(pdf_str)
        return query_ai(self.config, prompt)

    def __complete_prompt(self, pdf_str: str) -> str:
        """
        Create a complete prompt by appending the resume string to the initial prompt.

        Args:
            pdf_str (str): Resume string.

        Returns:
            str: The complete prompt.
        """
        return self.prompt + pdf_str

    def pdf2str(self, pdf_path: str) -> str:
        """
        Convert a PDF file to a plain text string.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Plain text string representing the PDF content.
        """
        with open(pdf_path, "rb") as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            pages = [self.__format_pdf(p.extract_text()) for p in pdf.pages]
            return "\n\n".join(pages)

    def __format_pdf(self, pdf_str: str) -> str:
        """
        Clean and format the PDF text string by applying pattern replacements.

        Args:
            pdf_str (str): Original PDF text string.

        Returns:
            str: Cleaned and formatted PDF text string.
        """
        pattern_replacements = {
            r'\s[,.]': ',',
            r'[\n]+': '\n',
            r'[\s]+': ' ',
            r'http[s]?(://)?': ''
        }

        for pattern, replacement in pattern_replacements.items():
            pdf_str = re.sub(pattern, replacement, pdf_str)

        return pdf_str
