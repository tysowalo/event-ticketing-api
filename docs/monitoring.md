# Phase 4: Monitoring and Security

## 1. CloudWatch Monitoring

Amazon CloudWatch is used to monitor the AWS Lambda functions used by the Event Registration and Ticketing System.

CloudWatch provides:

- Lambda execution logs
- Lambda invocation metrics
- Lambda error metrics
- Lambda duration metrics
- Monitoring and alarms

---

## 2. CloudWatch Logs

The registration Lambda function sends execution information to CloudWatch Logs.

The application logs:

- Registration requests
- Successful registrations
- Registration errors

Sensitive information is not intentionally included in application logs.

Example log messages include:

- Registration request received
- Registration successful
- Registration failed

---

## 3. CloudWatch Alarm

A CloudWatch alarm is configured to monitor Lambda errors.

The purpose of the alarm is to detect an increase in failed Lambda executions and alert the system administrator.

The project requirement is to trigger an alert when the registration error rate exceeds 5%.

The alarm uses CloudWatch metrics to monitor Lambda performance and errors.

---

## 4. Amazon SNS Notifications

Amazon SNS is used to send monitoring notifications.

The notification flow is:

CloudWatch Alarm
        |
        v
       SNS
        |
        v
Email Notification

An email subscription is configured for the SNS topic.

The administrator receives an email when the CloudWatch alarm enters the ALARM state.

---

## 5. Input Validation

The registration API validates incoming user information before storing it in DynamoDB.

The API checks that the following fields are provided:

- Event ID
- Name
- Email
- Phone number

Requests containing missing required fields return a 400 Bad Request response.

---

## 6. Email Validation

The API checks that the submitted email follows a basic valid email format.

For example:

Valid:

test@example.com

Invalid:

test@example

Invalid:

wrong-email

Invalid email addresses are rejected with a 400 Bad Request response.

---

## 7. Input Sanitization

Input data is cleaned before being stored.

The application:

- Removes unnecessary whitespace
- Removes leading and trailing spaces
- Converts email addresses to lowercase

For example:

"  TEST@EXAMPLE.COM  "

is converted to:

"test@example.com"

---

## 8. IAM and Least Privilege

The project follows the principle of least privilege.

IAM permissions should provide a service only with the permissions required to perform its function.

The Lambda function requires access to the DynamoDB resources used by the application and CloudWatch logging.

Unnecessary access to other AWS services should not be granted.

---

## 9. AWS Budgets

AWS Budgets is used to monitor project costs.

A monthly budget is configured to help prevent unexpected AWS charges.

Budget notifications are configured to alert the administrator when spending approaches the defined budget threshold.

---

## 10. Security Summary

The Phase 4 security measures include:

- CloudWatch monitoring
- CloudWatch alarms
- SNS email notifications
- Input validation
- Email validation
- Input sanitization
- IAM least-privilege principles
- AWS Budget monitoring

These controls improve the reliability, security, and cost management of the Event Registration and Ticketing System.