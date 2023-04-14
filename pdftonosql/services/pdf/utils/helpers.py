def clean_text(text: str) -> str:
    """
    Remove unwanted characters from text
    """
    import re
    return (re.sub("([,'.#\"])", "", text)).strip()
