# QHack-CFN

CloudFormation templates to help setup AWS and Amazon Braket for QHack hackathon 2023. 

## How to setup AWS Account for Amazon Braket
### 1. Setup IAM Groups and Users
Here, we will setup required groups, users and roles required to login to AWS account and use Amazon Braket. Following list of resources are created as part of Cloudformation - 
* IAM Group with permission Full access permission to Amazon Braket and S3
* Administrative IAM user to manage AWS resources
* Lambda function and role to create IAM users
* IAM users that will be part of IAM group with full access to Amazon Braket and S3
* DynamoDB table that contains access keys and secret key of IAM users. Can only be accessed by Administrative IAM user.
* Billing alarm with default threshold of $50. Sends alerts to email address when AWS bill breaches the specified threshold.

#### <u>Instructions to run Cloudformation</u>
1. Login to AWS using root account and nagive to CloudFormation console. 
2. Download `1_IAM_Groups_Users_Setup.yaml` file to your local machine.
3. Select `1_IAM_Groups_Users_Setup.yaml` file in CloudFormation console. 
4. Accept default parameters or overwrite default parameters in next screen.
    * **paramGroupName**: Unique name of IAM group with full access to Amazon Braket and S3. Default is `QHackTeam`. 
    * **paramAdminUser**: Unique name of Administrative user. Default is `QHackTeamAdmin`. 
    * **paramAdminUserPassword**: Password for Administrative user. This is a first time password and after your first login, you will be prompted to change password. Default is `P@$$w0rd`. 
    * **paramUsers**: Comma separate list of users. A list of users that will have permission to login to AWS account and use Braket and S3 services. Default password for all users is `P@$$w0rd`. They will be prompted to change password after their first login. 
    * **paramDynamoDBTable**: Name of DynamoDB table that contains access key and secret key of all IAM users. Only Administrative user has access to DynamoDB table.
    * **paramBillingAlarmName**: Name of Billing alarm. Default is `BillingAlarm`. 
    * **paramBillingAlarmThreshold**: Value to send alert when AWS bill goes above this threshold value. 
    * **paramBillingAlertEmail**: Email where billing alerts will be sent. Default is `name@example.com`. 
5. Click Next, Next and select checkbox to accept conditions that IAM users and roles will be created.
6. Submit. Takes around 5 mins for the setup to finish. 
7. Once the setup is finished, Login using Administrative user created and provide access keys, secret keys, login URL to respective users to be able to login to AWS console or access programmatically. 

### 2. Setup Amazon Braket Notebook for users
In this step, login as Administrative user and launch `2_Amazon_Braket_Notebook_Setup.yaml` for each user that you would like to create Amazon Braket Notebook. 

#### <u>Instructions to run CloudFormation</u>
1. Login to AWS account using Administrative user created in above step. 
2. Navigate to CloudFormation console and select `2_Amazon_Braket_Notebook_Setup.yaml` template.
3. Fill in below list of parameters
    * **paramNotebookInstanceName**: Name of the notebook instance. Starts with `amazon-braket-`. Append Name of the user to create user specific notebook instance.
    * **paramInstanceType**: Instance type for notebook instance. Default is `ml.t3.medium`. 
4. Click Next, Next and select checkbox to accept conditions that IAM roles will be created.
5. Submit. Takes around 5 mins for the notebook creation to finish.
6. Repeat for each user that you would like to provide Notebook instance.

