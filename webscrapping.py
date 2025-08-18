import requests
from bs4 import BeautifulSoup
import  re
#import pandas as pd
import utils

def info_looking_url(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        emails = re.findall(utils.pattern_email(), soup.get_text())
        phone_numbers = re.findall(utils.pattern_phone_number(), soup.get_text())
        phone_numbers = list(map(lambda x: x.replace(' ',''), phone_numbers))
        contacts = [*list(set(emails)), *phone_numbers]
        return contacts

def url_exists(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

