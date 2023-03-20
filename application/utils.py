"""
A module for managing OpenAI API configuration parameters.

This module provides a dataclass, OpenAIConfig, to store and manage the
configuration parameters required for making requests to the OpenAI API.
The OpenAIConfig dataclass can be used to organize and pass these parameters
to other classes or functions that interact with the API.
"""
import json
from dataclasses import dataclass
import openai


@dataclass
class OpenAIConfig:
    """
    A dataclass for storing OpenAI API configuration parameters.

    Attributes:
        model (str): The OpenAI model to be used, default is "gpt-3.5-turbo".
        temperature (float): Sampling temperature for the model, default is 0.0.
        max_tokens (int): Maximum number of tokens in the model's response, default is 1000.
        top_p (float): Nucleus sampling parameter to
        control the randomness of the model's response,
        default is 1.
        frequency_penalty (float): Penalty for token frequency, default is 0.
        presence_penalty (float): Penalty for token presence, default is 0.
    """

    model: str = "gpt-3.5-turbo"
    temperature: float = 0.0
    max_tokens: int = 1000
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0


def query_ai(config: OpenAIConfig, prompt: str):
    """
    Query the OpenAI API with the provided configuration and prompt.

    Args:
        config (OpenAIConfig): Configuration parameters for the OpenAI API request.
        prompt (str): The prompt to be sent to the API.

    Returns:
        dict: Parsed JSON response from the API.
        str: Error message in case of an exception.

    Raises:
        openai.APIError: Exception related to the OpenAI API.
        json.JSONDecodeError: Exception related to JSON decoding.
    """
    try:
        response = openai.ChatCompletion.create(
            model=config.model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            top_p=config.top_p,
            frequency_penalty=config.frequency_penalty,
            presence_penalty=config.presence_penalty,
            messages=[{"role": "user", "content": prompt}],
        )

        response_str = response.choices[0].message.content.strip()
        return json.loads(response_str)

    except openai.APIError as api_exc:
        # Handle exceptions related to the OpenAI API
        return f"API Error: {api_exc}"
    except json.JSONDecodeError as json_exc:
        # Handle exceptions related to JSON decoding
        return f"JSON Decode Error: {json_exc}"
