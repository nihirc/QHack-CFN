# QHack-CFN

CloudFormation templates to help setup AWS and Amazon Braket for QHack hackathon 2023. 

## How to setup AWS Account for Amazon Braket

### Pre-requisite
Before deploying Cloudformation templates, please ensure below pre-requisite steps are performed - 
1. Ensure that you have applied provided credits code to your account. To do so, please follow below steps - 
    * Sign in to your AWS account using email address you used to register for the account. Then visit link (https://console.aws.amazon.com/billing/home?#/credits) to apply credits code.
    * After visiting, you will be directed to the page as shown in below image.
    ![AWS Credits](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*U4ylVteTRJf66kZqh-HhRg.jpeg)
    * Click on "Redeem credit" as shown in the image below.
    ![AWS Credits](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NEQ382KPoucHaqkuSwsI1w.jpeg)
    * Enter the provided promotional code of AWS Credits, provide the security code and click on "Redeem credit" as shown in the image below.
    ![AWS Credits](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hrCHGTCSqQtd_qnpK1I4zg.jpeg)
    * At this point, your AWS credits are successfully applied to your account. 

2. After successfully applying AWS credits, we will enable AWS billing alerts. 
    * Sign in to your AWS account using email address you used to register for the account. Then visit link (https://console.aws.amazon.com/billing/home).
    * On the left navigation panel, select **Preferences** and check the **Receive Billing Alerts** feature settings. If it is unchecked, it means that AWS Billing alerts feature is currently disabled in your account. 
    ![AWS Billing Alerts](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2021/10/05/fig3rbil.png)

3. To enable and access third party QPUs such as IonQ, Rigetti, etc you must agree to certain terms and conditions. To do so, please follow below steps - 
    * Sign in to your AWS account using email address you used to register for the account. Then visit link (https://us-west-1.console.aws.amazon.com/braket/home?region=us-west-1#/dashboard)
    * On the left nagivation panel, select **Permissions and Settings**. Under **General** tab, please click on "Accept terms and enable" button. 
    ![AWS Braket](https://docs.aws.amazon.com/images/braket/latest/developerguide/images/General.png)

4. Next, we will walk through the steps using AWS CloudFormation to automate creation of AWS resources for Amazon Braket. To do so, please clone this repository to your local machine.

### 1. Setup IAM Groups and Users
Here, we will setup required groups, users and roles, Amazon Braket roles, Amazon Braket cost alerts, Amazon Braket notebook.

#### <u>Instructions to run Cloudformation</u>
1. Login to AWS using the email address used to create AWS account and navigate to AWS CloudFormation console.
2. We will deploy `1_IAM_Users_Braket_Setup.yaml` file from repository cloned to your local machine.
3. Select `1_IAM_Users_Braket_Setup.yaml` file in CloudFormation console. 
4. Accept default parameters or overwrite default parameters in next screen.
    * **Users**: Comma separate list of users. A list of users that will have permission to login to AWS account and use Braket and S3 services. Default password for all users is `P@$$w0rd`. They will be prompted to change password after their first login. 
    * **ServiceLinkedRole**: Whether to create Amazon Braket service linked role.
    * **QPUAccess**: Whether to enable access to QPU hardware
    * **BraketCostThreshold**: USD amount threshold if when breached, will shut down Amazon Braket jobs and tasks. 
    * **BillingAlertEmail**: Email to send notifications when Amazon Braket cost threshold is breached.
5. Click Next, Next and select checkbox to accept conditions that IAM users and roles will be created.
6. Submit. Takes around 5-10 mins for the setup to finish. 
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


## Track Braket cost globally
Enter below code snippet at the end of each notebook or script to track Braket cost globally.

```
import boto3

cloudwatch = boto3.client("cloudwatch")

def submit_braket_cost(t):
    """Puts braket cost for a session to CloudWatch as a custom metrics"""
    response = cloudwatch.put_metric_data(
        Namespace="Braket",
        MetricData=[{
            'MetricName': 'Braket_Cost',
            'Unit': 'Count',
            'Value': t.qpu_tasks_cost() + t.simulator_tasks_cost()
        }]
    )
    print(response)

submit_braket_cost(t)
```

## Setting up local development environment

If you would like to run Braket jobs and/or tasks from your local machine, please follow below steps - 
1. Install AWS SDK, AWS CLI and Braket SDK by running below commands - 
```
pip3 install awscli boto3 amazon-braket-sdk
```

2. Reach out to your AWS Administrator to get access key and secret key. As an AWS Administrator, you will find access keys and secret keys in DynamoDB table. In AWS Console, type DynamoDB in search bar and navigate to DynamoDB console. On the left navigational menu, click on "Explore items" and select table "UserAccessKeysTable" and you should see keys for each user.

3. Configure access keys and secret keys on your machine by running command. Choose `us-west-1` as region when prompted and use `json` as output format.
```
aws configure
```

4. You're all set to develop locally and run jobs and tasks on Amazon Braket. 





