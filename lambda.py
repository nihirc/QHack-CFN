import boto3, json
import logging
import cfnresponse

logger = logging.getLogger(__name__)
iam = boto3.client("iam")

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

def handler(event, context):
    logger.info(json.dumps(event))

    if event['RequestType'] == 'Create':
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
        response = 'SUCCESS'
        responseData = {}
        responseData['Data'] = response
        cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")