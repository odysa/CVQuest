import PyPDF2
import re
import openai
import json
from application.prompts import PARSER_PROMPT


class ResumeJsonParser:
    def __init__(self, prompt: str = PARSER_PROMPT,
                 temperature: float = 0.0,
                 max_tokens: int = 1000,
                 top_p: float = 1,
                 frequency_penalty: float = 0,
                 presence_penalty: float = 0,):

        self.prompt = prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def pdf2json(self, pdf_path: str):
        pdf_str = self.__pdf2str(pdf_path)
        json = self.__str2json(pdf_str)
        return json

    def __str2json(self, pdf_str: str):
        prompt = self.__completePrompt(pdf_str)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
                messages=[{"role": "user", "content": prompt}],
            )

            response: str = response.choices[0].message.content.strip()
            return json.loads(response)
        except Exception as e:
            return e

    def __completePrompt(self, pdf_str: str) -> str:
        return self.prompt + pdf_str

    def __pdf2str(self, pdf_path: str) -> str:
        with open(pdf_path, "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            pages = [self.__formatPdf(p.extract_text()) for p in pdf.pages]
            # join pages
            return "\n\n".join(pages)

    def __formatPdf(self, pdf_str: str) -> str:

        pattern_replacements = {
            r'\s[,.]': ',',
            r'[\n]+': '\n',
            r'[\s]+': ' ',
            r'http[s]?(://)?': ''
        }

        for pattern, replacement in pattern_replacements.items():
            pdf_str = re.sub(pattern, replacement, pdf_str)

        return pdf_str
