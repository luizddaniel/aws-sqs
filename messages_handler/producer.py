from .handler import MessagesHandler
import json


def producer():
    messages_handler = MessagesHandler()
    messages_handler.send_message_from_sqs_queue(
        message_json=json.dumps(
            {"message": "My Notification message to AWS SQS", "subject": "Test SQS"}, 
            ensure_ascii=False
        )
    )
