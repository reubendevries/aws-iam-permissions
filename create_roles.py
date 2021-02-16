#!/usr/bin/env python3

__doc__ = """ A group of functions designed to help end users organize and control their permissions
through a document called iam_permission.json, which should be found within the root of the repository. All
your team will need to do is clone this repository, make a pull request (usually based off of a Jira ticket
and then they can make the requested changes, and create a merge request, after a DevOps engineer has looked over
the format of the iam_permissions.json document and approved it they can either run it or create a bunch of lambda
functions that would automate the changes. This is what I like to describe as essentially permissions with 'guard rails' """
__author__ = """ Reuben deVries """
__version__ = """ 0.01 """

#importing built in python modules
import argparse
import json
import subprocess

# importing 3rd party python modules
import boto3
from   botocore.exceptions import ClientError

def read_permission_documents():
    """ a function that will take a json formated document that people can use to request permissions.
    of course the person requesting permissions will need to be familiar with the how AWS orgainizes their 
    permission structures, if they don't know then this whole streamlined process will be quite useless. """

    with open("./aws-iam-permissions/create_policy.json") as policy_doc:
        policy = json.load(policy_doc)
        return policies
    
    with open("./aws-iam-permissions/create_user.json") as user_doc:
        user = json.loads(user_doc)
        return users

    with open("./aws-iam-permissions/create_user.json") as group_doc:
        group = json.loads(group_doc)
        return groups
    
    with open("./aws-iam-permissions/create_role.json") as role_doc:
        role = json.loads(role_doc)
        return roles
    
    with open("./aws-iam-permissions/attach_policies_to_roles.json") as role_doc:
        role = json.loads(role_doc)
        return attach_to_roles
    
def create_iam_policy(policy):
    """ a function that will create a new iam policy based on the parameters given from the 
    /"iam_permissions.json/" file """
    
            

if __name__ == "__main__":
    policy, user, group, role, attach_to_group, attach_to_role, attach_to_user, attach_to_policy = read_permission_documents()
    create_iam_policy(policies)
    create_iam_

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