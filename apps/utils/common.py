# coding: utf-8


def smart_split(text, comma=','):
    if isinstance(text, (str, unicode)):
        text = text.strip()
        text = text.split(comma)
        text = map(lambda x: x.strip(), text)
        text = filter(str, text)
    return text


def to_lower_case(text):
    if text:
        if isinstance(text, (str, unicode)):
            text = text.lower()
        elif isinstance(text, (list, set)):
            text = map(lambda x: x.lower(), text)
    return text
