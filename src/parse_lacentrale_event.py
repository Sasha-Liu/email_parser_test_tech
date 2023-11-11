import json
import re
from lxml import etree
from typing import List, Union
from data_type import Parser, Email, Contact, EmailParsed, BodyParsed
import datetime


class ParserLaCentrale(Parser):
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
    
    def get_body_parsed(self, raw_html) -> BodyParsed:
        root = etree.HTML(raw_html)
        data = root[1][0][0][0][1][0][0][2][0][0][0]
        name = data[1][0].text.split(':')[1].strip(' -')
        mail = data[2][0].text.split(':')[1].strip(' ')
        fname, lname = name.split(' ')
        contact = Contact('email', mail)
        return BodyParsed(fname, lname, [contact], None)

    def get_email_parsed(self, raw) -> EmailParsed:
        subject = self.get_subject(raw['subject'])
        from_email = self.get_from_email(raw['from'])
        to_email = self.get_to_emails(raw['to'])
        message = self.get_message(raw['text'])
        body = self.get_body_parsed(raw['html'])
        return EmailParsed(subject, from_email, to_email, message, body)



def parse_lacentrale_event(read_data: str) -> dict:
    email: dict = json.loads(read_data)

    parser = ParserLaCentrale()
    email_parsed = parser.get_email_parsed(email)
    result: dict = {}
    result['channel'] = email_parsed.from_email.get_channel()
    result['from_email'] = email_parsed.from_email.get_email()
    result['to_email'] = email_parsed.to_email[-1].get_email()
    result['workspace_name'] = email_parsed.to_email[-1].get_workspace_name()
    result['workspace_id'] = email_parsed.to_email[-1].get_workspace_id()
    result['message'] = email_parsed.message
    result['firstname'] = email_parsed.body.first_name
    result['lastname'] = email_parsed.body.last_name
    result['customer_email'] = email_parsed.body.contacts[0].value
    result['subject'] = email_parsed.subject
    result['contact_info'] = [c.__dict__ for c in email_parsed.body.contacts]

    return result


def main():
    with open("src/events/lacentrale.json", "r") as f:
        read_data: str = f.read()
    res = parse_lacentrale_event(read_data)
    for key in res: 
        print(f"[{key}]: {res[key]}")
    
if __name__ == '__main__':
    main()