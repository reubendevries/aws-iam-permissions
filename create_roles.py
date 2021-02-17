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
    
    with open("./aws-iam-permissions/create_role.json") as role_doc:
        roles = json.loads(role_doc)
        return roles
    
def create_iam_roles(roles):
    """ a function that will create a new iam policy based on the parameters given from the 
    /"iam_permissions.json/" file """

if __name__ == "__main__":
    roles = read_permission_documents()
    create_iam_roles(roles)

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