# QHack-CFN

CloudFormation templates to help setup AWS and Amazon Braket for QHack hackathon 2023. 

## How to setup AWS Account for Amazon Braket
### 1. Setup IAM Groups and Users
Here, we will setup required groups, users and roles required to login to AWS account and use Amazon Braket. 

#### <u>Instructions to run Cloudformation</u>
1. Login to AWS using root account and nagive to CloudFormation console. 
2. Download `1_IAM_Groups_Users_Setup.yaml` file to your local machine.
3. Select `1_IAM_Groups_Users_Setup.yaml` file in CloudFormation console. 
4. Accept default parameters or overwrite default parameters in next screen.
    * **Users**: Comma separate list of users. A list of users that will have permission to login to AWS account and use Braket and S3 services. Default password for all users is `P@$$w0rd`. They will be prompted to change password after their first login. 
    * **ServiceLinkedRole**: Whether to create Amazon Braket service linked role.
    * **QPUAccess**: Whether to enable access to QPU hardware
5. Click Next, Next and select checkbox to accept conditions that IAM users and roles will be created.
6. Submit. Takes around 5 mins for the setup to finish. 
7. Once the setup is finished, Login using Administrative user created and provide access keys, secret keys, login URL to respective users to be able to login to AWS console or access programmatically. 

### 2. Setup AWS billing alert
In this step, login as Administrative user and launch `2_Enable_Billing_Alert.yaml` to setup AWS Billing alert. 

#### <u>Instructions to run CloudFormation</u>
1. Login to AWS account using Administrative user created in above step. 
2. Navigate to `us-east-1` region and go to CloudFormation console and select `2_Enable_Billing_Alert.yaml` template.
3. Fill in below list of parameters
    * **BillingAlarmName**: Name of Billing alarm. Default is `BillingAlarm`. 
    * **BillingAlarmThreshold**: Value to send alert when AWS bill goes above this threshold value. 
    * **BillingAlertEmail**: Email where billing alerts will be sent. Default is `name@example.com`. 
4. Click Next, Next and select checkbox to accept conditions that IAM roles will be created.
5. Submit. Takes around 5 mins for the notebook creation to finish.
6. Repeat for each user that you would like to provide Notebook instance.

