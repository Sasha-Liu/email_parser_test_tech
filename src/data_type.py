from typing import List, Union
from dataclasses import dataclass
import datetime


@dataclass
class Email:
    """
    Class representing an Email.

    Email has the form:
    [nickname]  <[name]@[domain]>
    nickname is optional
    """
    nickname: str
    name: str
    domain: str

    def __init__(self, raw_email: str):
        data = raw_email.split("<")
        self.nickname = data[0].strip(' ')
        self.name = data[1].split('@')[0]
        self.domain = data[1].split('@')[1].strip('>')

    def get_workspace_name(self) -> Union[str, None]:
        if '.' not in self.name:
            return None
        return self.name.split('.')[0]

    def get_workspace_id(self) -> Union[str, None]:
        if '.' not in self.name:
            return None
        return self.name.split('.')[1]

    def get_channel(self) -> str:
        if '.' not in self.domain:
            return self.domain
        return self.domain.split('.')[0]
    
    def get_email(self) -> str:
        return f"{self.name}@{self.domain}"



@dataclass
class Contact:
    """
    Class for contact info
    """
    type: str
    value: str


@dataclass
class BodyParsed:
    """
    Information parsed from the html body.
    """
    last_name: str
    first_name: str
    contacts: List[Contact]
    links: List[str]



@dataclass
class EmailParsed:
    """
    Class for representing the parsed email.
    """
    subject: str
    from_email: Email
    to_email: List[Email]
    # date: datetime
    message: str
    body: BodyParsed


class Parser:
    """
    Base Class for different parser. 
    """
    def get_subject(self, raw_subject: str) -> str:
        pass

    def get_from_email(self, raw_email: str) -> Email:
        pass

    def get_to_emails(self, raw_emails: str) -> List[Email]:
        pass

    def get_message(self, raw_text:str) -> str:
        pass

    def get_date(self, raw_date: str) -> datetime:
        pass

    def get_body_parsed(self, raw_html) -> BodyParsed:
        pass
    
    def get_email_parsed(self, raw) -> EmailParsed:
        pass

