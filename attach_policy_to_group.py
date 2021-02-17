#!/usr/bin/env python3

__doc__ = """ A pair of functions designed to help end users organize and control their permissions
through a document called iam_permission.json, which should be found within the root of the repository. All
your team will need to do is clone this repository, make a pull request (usually based off of a Jira ticket
and then they can make the requested changes, and create a merge request, after a DevOps engineer has looked over
the format of the iam_permissions.json document and approved it they can either run it or create a bunch of lambda
functions that would automate the changes. This is what I like to describe as essentially permissions with 'guard rails' """
__author__ = """ Reuben deVries """
__version__ = """ 0.01 """

#importing built in python modules
import json

# importing 3rd party python modules
import boto3
from   botocore.exceptions import ClientError

def read_permission_documents():
    """ a function that will take a json formated document that people can use to request permissions.
    of course the person requesting permissions will need to be familiar with the how AWS orgainizes their 
    permission structures, if they don't know then this whole streamlined process will be quite useless. """

    with open("./aws-iam-permissions/attach_policy_to_group.json") as attach_policy_to_group_doc:
        attach_policy_to_group = json.load(attach_policy_to_group_doc)
        return attach_policy_to_group
    
def attach_policy_to_group(attach_policy_to_group):
    """ a function that will attach a iam policy to a group based on the parameters given from the 
    \"/aws-iam-permissions/attach_policy_to_group.json\" file """
    print(attach_policy_to_group)
    for policy_arn in attach_policy_to_group:
        print(policy_arn)
    for group_name in attach_policy_to_group:
        print(group_name)
    #iam = boto3.client("iam")
    #iam.attach_group_policy

if __name__ == "__main__":
    attach_policy_to_group = read_permission_documents()
    attach_policy_to_group(attach_policy_to_group)

#TODO:

"""
-
-
-
-
-
-
-
"""