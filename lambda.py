import boto3, json
import logging
import cfnresponse
import os
import time

logger = logging.getLogger(__name__)
iam = boto3.client("iam")
ddb = boto3.client("dynamodb")

def create_iam_user(user):
    response = iam.create_user(
        UserName=user
    )
    logger.info(response)
    if response['User']['Arn']:
        return True
    else:
        return False

def create_iam_user_profile(user):
    response = iam.create_login_profile(
        UserName=user,
        Password='P@$$w0rd',
        PasswordResetRequired=True
    )
    logger.info(response)
    if response['LoginProfile']:
        return True
    else:
        return False

def create_iam_user_key(user):
    response = iam.create_access_key(
        UserName=user
    )
    return response

def put_ddb_item(item):
    response = ddb.put_item(
        TableName=os.environ["DDB_TABLE"],
        Item=item
    )
    logger.info(response)

def get_ddb_items():
    response = ddb.scan(TableName=os.environ["DDB_TABLE"])
    print(response)
    return response

def handler(event, context):
    logger.info(json.dumps(event))

    if event['RequestType'] == 'Create':
        users = event['ResourceProperties']['Users']
        users = users.split(",")
        for user in users:
            if create_iam_user(user):
                if create_iam_user_profile(user):
                    response = ddb.add_user_to_group(GroupName=os.environ["GROUP_NAME"], UserName=user)
                    print(response)
                    response = create_iam_user_key(user)
                    item = {}
                    item["Username"] = user
                    item["access_key"] = response["AccessKey"]["AccessKeyId"]
                    item["secret_key"] = response["AccessKey"]["SecretAccessKey"]
                    put_ddb_item(item)
        response = 'SUCCESS'
        responseData = {}
        responseData['Data'] = response
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
    
    if event['RequestType'] == 'Update':
        response = 'SUCCESS'
        responseData = {}
        responseData['Data'] = response
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")

    if event['RequestType'] == 'Delete':
        response = get_ddb_items()
        response = 'SUCCESS'
        responseData = {}
        responseData['Data'] = response
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")