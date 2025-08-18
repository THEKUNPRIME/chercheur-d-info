import pdfplumber
import re
import utils

def info_looking_pdf(pdf):
    with pdfplumber.open(pdf) as PDF:
        text = ""
        for page in PDF.pages:
            text += page.extract_text() or ""
    emails = re.findall(utils.pattern_email(), text)
    phone_numbers = re.findall(utils.pattern_phone_number(), text)
    phone_numbers = [x.replace(" ", "") for x in phone_numbers]
    return list(set(emails)) + list(set(phone_numbers))

def is_valid_pdf(path) -> bool:
    try:
        with pdfplumber.open(path) as PDF:
            _ = PDF.pages[0]
        return True
    except Exception:
        return False
