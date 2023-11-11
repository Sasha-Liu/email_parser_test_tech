import json
import re
from lxml import etree

# This regex match <hello@gmail.com>, with < and > removed
EMAIL_REGEX = r'(?<=<)[\.\w-]+@[\w-]+\.\w+(?=>)'

# This regex capture the string between @ and .
DOMAIN_REGEX = r'(?<=@)[\.\w-]+(?=\.)'

# This regex capture the workspace, from begin to the point .
WORKSPACE_NAME = r'^[\w-]+(?=\.)'

# This regex capture the workspaceId, from point to @
WORKSPACE_ID = r'(?<=\.)[\w-]+(?=@)'

def parse_leboncoin_event(event):
    event = json.loads(event)
    result = {}
    result['from_email'] = re.search(EMAIL_REGEX, event['from']).group()
    if (result['from_email']):
        result['channel'] = re.search(DOMAIN_REGEX, result['from_email']).group()
    result['to_email'] = re.search(EMAIL_REGEX, event['to'].splitlines()[-1]).group()
    result['message'] = event['text'].replace("\r\n", " ").replace("\n", " ")
    result['subject'] = event['subject'].replace("\r\n", "").replace("\n", "")
    if (result['to_email']):
        result['workspace_name'] = re.search(WORKSPACE_NAME, result['to_email']).group()
        result['workspace_id'] = re.search(WORKSPACE_ID, result['to_email']).group()
    return result





def main():
    with open("src/events/leboncoin.json", "r") as f:
        event = f.read()
    res = parse_leboncoin_event(event)
    for key in res: 
        print(f"[{key}]: {res[key]}")
    
if __name__ == '__main__':
    main()