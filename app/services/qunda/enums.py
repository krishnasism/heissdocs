from enum import Enum


class OpenAIModels(str, Enum):
    davinci = "text-davinci-003"
    chatgpt35turbo = "gpt-3.5-turbo"
    chatgpt4 = "gpt-4"
