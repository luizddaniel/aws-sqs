"""producer.py"""
import os
import boto3
from decouple import config

class MessagesHandler:

    def __init__(self):
        self._sqs_client = boto3.client(
            "sqs",
            aws_access_key_id=config("AWS_ACCESS_KEY_ID"), 
            aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
            region_name=config("AWS_REGION_NAME"),
        )
        self._queue_url = config("AWS_QUEUE_URL")

    def send_message_from_sqs_queue(self, message_json: str):
        message = self._sqs_client.send_message(
            QueueUrl=self._queue_url,
            MessageBody=message_json,
            MessageAttributes={
                "Notification": {
                    "DataType": "String", 
                    "StringValue": "Notification Status"
                }
            }
        )
        return message

    def read_from_sqs_queue(self):
        messages = self._sqs_client.receive_message(
            QueueUrl=self._queue_url,
            MaxNumberOfMessages=1,
        )
        return messages

    def delete_from_sqs_queue(self, receipt_handle: str):
        response = self._sqs_client.delete_message(QueueUrl=self._queue_url, ReceiptHandle=receipt_handle)
        return response
