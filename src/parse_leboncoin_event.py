import json
import re
from lxml import etree
from typing import List, Union
from data_type import Parser, Email, Contact, EmailParsed
import datetime


class ParserLeBoncoin(Parser):
    def get_subject(self, raw_subject: str) -> str:
        return raw_subject.replace("\r\n", "").replace("\n", "")

    def get_from_email(self, raw_email: str) -> Email:
        return Email(raw_email)

    def get_to_emails(self, raw_emails: str) -> List[Email]:
        emails = raw_emails.replace("\r\n\t", " ").split(',')
        result = []
        for e in emails:
            result.append(Email(e))
        return result

    def get_message(self, raw_text: str) -> str:
        return raw_text.replace("\r\n", " ")
    
    def get_firstname(self, raw_html:str) -> str:
        pass

    def get_lastname(self, raw_html:str) -> str:
        pass

    def get_contacts(self, raw_html:str) -> List[Contact]:
        pass

    def get_email_parsed(self, raw) -> EmailParsed:
        subject = self.get_subject(raw['subject'])
        from_email = self.get_from_email(raw['from'])
        to_email = self.get_to_emails(raw['to'])
        message = self.get_message(raw['text'])
        return EmailParsed(subject, from_email, to_email, message)



def parse_leboncoin_event(read_data: str) -> dict:
    email: dict = json.loads(read_data)
    parser = ParserLeBoncoin()
    email_parsed = parser.get_email_parsed(email)
    result: dict = {}
    result['channel'] = email_parsed.from_email.get_channel()
    result['from_email'] = email_parsed.from_email.get_email()
    result['to_email'] = email_parsed.to_email[-1].get_email()
    result['workspace_name'] = email_parsed.to_email[-1].get_workspace_name()
    result['workspace_id'] = email_parsed.to_email[-1].get_workspace_id()
    result['message'] = email_parsed.message
    result['subject'] = email_parsed.subject

    return result


def main():
    with open("src/events/leboncoin.json", "r") as f:
        read_data: str = f.read()
    res = parse_leboncoin_event(read_data)
    for key in res: 
        print(f"[{key}]: {res[key]}")
    
if __name__ == '__main__':
    main()