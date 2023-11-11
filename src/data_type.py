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
    nickname: Union[str, None]
    name: str
    domain: str

    def get_workspace_name(self) -> Union[str, None]:
        pass

    def get_workspace_id(self) -> Union[str, None]:
        pass

    def get_channel(self) -> str:
        pass


@dataclass
class Contact:
    """
    Class for contact info
    """
    type: str
    value: str


@dataclass
class EmailParsed:
    """
    Class for representing the parsed email.
    """
    subject: str
    from_email: Email
    to_email: List[Email]
    date: datetime
    message: str
    firstname: str
    lastname: str
    contacts: List[Contact]


class Parser:
    """
    Base Class for different parser. 
    """
    def get_subject(self, raw_subject: str) -> str:
        pass

    def get_from_emails(self, raw_email: str) -> Email:
        pass

    def get_to_emails(self, raw_emails: str) -> List[Email]:
        pass

    def get_message(self, raw_text:str) -> str:
        pass

    def get_date(self, raw_date: str) -> datetime:
        pass

    def get_firstname(self, raw_html:str) -> str:
        pass

    def get_lastname(self, raw_html:str) -> str:
        pass

    def get_contacts(self, raw_html:str) -> List[Contact]:
        pass

