import json
import re
from lxml import etree
from typing import List, Union


class Email:
    wksp:str
    id:str
    channel:channel

class EmailAddr:
    """
    Class representing an email address.

    An email can contains a name and an address, for example:
    Foo bar <foobar@gmail.com>
    Foo bar is the optional name
    <foobar@gmail.com> is the email address
    Angle bracket should be stripped
    """
    name: Union[str, None]
    email_addr: str

    def get_wksp(self)->str:
        pass

    def get_wksp_id(self)->str:
        pass

    def get_channel(self)->str:
        pass

class Body:
    from_name:str


class EmailParsed:
    """
    Class for representing the parsed email.

    Newline should be replaced with space
    """
    subject: str
    from_email: EmailAddr
    to_email: List[EmailAddr]
    date: str
    text: str
    body:Body
    html: etree

class Parser:

    def get_subject(self, email:dict) -> str:
        pass

def get_from_email(raw_from:str) -> EmailAddr:
    pass

def get_to_email(raw_to:str) -> List[EmailAddr]:
    pass

def get_date(raw_date:str) -> datetime:
    pass

def get_text(raw_text:str) -> str:
    pass

def get_body_from_html(raw_html:str) -> Body:

    import etree
    
    

    pass


def ParserLaCentrale(Parser):


def parse_lacentrale_event(read_data: str) -> dict:
    email: dict = json.loads(read_data)
    
    return {}


def main():
    with open("src/events/lacentrale.json", "r") as f:
        read_data: str = f.read()
    res = parse_lacentrale_event(read_data)
    for key in res: 
        print(f"[{key}]: {res[key]}")
    
if __name__ == '__main__':
    main()