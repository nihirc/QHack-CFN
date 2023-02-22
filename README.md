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
    * Sign in to your AWS account using email address you used to register for the account. Then visit link (https://us-west-1.console.aws.amazon.com/braket/home?region=us-west-2#/dashboard)
    * On the left nagivation panel, select **Permissions and Settings**. Under **General** tab, please click on "Accept terms and enable" button. 
    ![AWS Braket](https://docs.aws.amazon.com/images/braket/latest/developerguide/images/General.png)

4. Next, we will walk through the steps using AWS CloudFormation to automate creation of AWS resources for Amazon Braket. To do so, please clone this repository to your local machine.

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

