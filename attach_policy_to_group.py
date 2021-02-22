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
import argparse

# importing 3rd party python modules
import boto3
from   botocore.exceptions import ClientError
    
def attach_policy_to_group(args.add, args.delete, args.group, args.policy):
    """ a function that will attach a iam policy to a group based on the parameters given via the cli"""
    iam = boto3.client("iam")
    if args.add in attach_policy_to_group():
         iam.attach_group_policy(
             GroupName = args.group,
             PolicyArn = args.policy
         )
    else:
        iam.delete_group_policy(
             GroupName = args.group,
             PolicyArn = args.policy
         )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass through the name of the Policy you wish to add and which group you would like to add it too.")
    parser.add_argument("-a", "--add", help="will add the policy to the group.")
    parser.add_argument("-d", "--delete", help="will delete the policy from the group.")
    parser.add_argument("-g", "--group", help="sets the group that you would want to add the policy.")
    parser.add_argument("-p", "--policy", help="sets the policy arn that you would want to add the group.")
    args = parser.parse_args()
    attach_policy_to_group(args.add, args.delete, args.group, args.policy)

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