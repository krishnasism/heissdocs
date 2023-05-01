def preprocess_parsed_text(text: str) -> str:
    text = clean_text(text)
    text = text.lower()
    return text


def clean_text(text: str) -> str:
    """
    Remove unwanted characters from text
    """
    import re
    return (re.sub("([,'.#\"])", "", text)).strip()
