from .handler import MessagesHandler
import json


def consumer():
    messages_handler = MessagesHandler()
    response = messages_handler.read_from_sqs_queue()
    print("Response: ", response)
    processed = False
    for message in response.get("Messages", []):
        data_json = message.get("Body")
        data = json.loads(data_json)
        if data:
            processed = True
            receipt_handle = message.get("ReceiptHandle", '')
            response = messages_handler.delete_from_sqs_queue(receipt_handle=receipt_handle)
            response_metadata = response.get("ResponseMetadata", {})
            if response_metadata:
                print("HTTP Status Code:", response_metadata.get("HTTPStatusCode"))
    return processed