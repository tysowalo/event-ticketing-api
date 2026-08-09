import json
import boto3
import uuid
import logging
import re
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb")

registrations_table = dynamodb.Table("Registrations")
events_table = dynamodb.Table("Events")


def lambda_handler(event, context):

    try:
        # Get data sent by the user
        body = json.loads(event.get("body", "{}"))

event_id = body.get("eventId")
name = body.get("name")
email = body.get("email")
phone = body.get("phone")

event_id = event_id.strip()
name = name.strip()
email = email.strip().lower()
phone = phone.strip()

        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

if not re.match(email_pattern, email):
    return {
        "statusCode": 400,
        "body": json.dumps({
            "message": "Invalid email address"
        })
    }

        # Check required fields
        if not event_id or not name or not email or not phone:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "eventId, name, email and phone are required"
                })
            }

        # Check whether the event exists
        event_response = events_table.get_item(
            Key={
                "eventId": event_id
            }
        )

        if "Item" not in event_response:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "Event not found"
                })
            }

        # Generate registration ID
        registration_id = "REG-" + str(uuid.uuid4())

        # Save registration
        registrations_table.put_item(
            Item={
                "registrationId": registration_id,
                "eventId": event_id,
                "name": name,
                "email": email,
                "phone": phone,
                "registeredAt": datetime.utcnow().isoformat()
            }
        )

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Registration completed successfully",
                "registrationId": registration_id
            })
        }

    except Exception as e:

        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Internal server error"
            })
        }
