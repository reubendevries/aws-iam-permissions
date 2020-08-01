#!/usr/bin/python3

import  json
import  boto3
from    botocore.exceptions import ClientError
iam = boto3.client("iam")
with open("./iam_permissions.json") as iam_permissions:
    read_content = json.load(iam_permissions)
create_policy = read_content["CreatePolicy"]
for data in create_policy:
    policy_document = data["PolicyDocument"]
    for version in policy_document:
        index = version["Statement"]
        
                