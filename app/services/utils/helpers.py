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


def convert_dict_to_camel_case(src_dict: dict):
    camel_case_dict = {}
    for k, v in src_dict.items():
        camel_case_dict[_to_lower_camel_case(k)] = v
    return camel_case_dict


def _to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def _to_lower_camel_case(snake_str):
    camel_string = _to_camel_case(snake_str)
    return snake_str[0].lower() + camel_string[1:]
