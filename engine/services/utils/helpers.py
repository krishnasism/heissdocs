def preprocess_parsed_text(text: str) -> str:
    text = clean_text(text)
    text = text.lower()
    return text


def clean_text(text: str) -> str:
    """
    Remove unwanted characters from text
    params: text: Text to be cleaned
    return: str: Cleaned text
    """
    import re

    return (re.sub("([,'.#\"])", "", text)).strip()
