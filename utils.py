import  re
def pattern_email():
    return r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def pattern_phone_number():
    return r'[\+]243[\s]?[0-9|\s]{2,3}[\s]?[0-9|\s]{2,3}[\s]?[0-9|\s]{2,3}[\s]?[0-9|\s]{2,3}'

def pattern_url():
    return r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\/\b([-a-zA-Z0-9()!@:%_+.~#?&=]*)'

def is_valid_email(value: str) -> bool:
    return re.match(pattern_email(), value) is not None

def is_valid_phone_number(value: str) -> bool:
    return re.match(pattern_phone_number(), value) is not None

def is_valid_url(value: str) -> bool:
    return re.match(pattern_url(), value) is not None
