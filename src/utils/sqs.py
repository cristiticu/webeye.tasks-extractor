import json
from typing import TYPE_CHECKING, Mapping, Sequence
from uuid import uuid4

import boto3
if TYPE_CHECKING:
    from types_boto3_sqs.type_defs import SendMessageBatchRequestEntryTypeDef


def send_messages(queue_url: str, messages: Sequence[Mapping]):
    sqs = boto3.client("sqs")

    for i in range(0, len(messages), 10):
        chunk = messages[i: i + 10]

        entries: list["SendMessageBatchRequestEntryTypeDef"] = [
            {
                "Id": str(uuid4()),
                "MessageBody": json.dumps(message),
            }
            for message in chunk
        ]

        print(entries)

        response = sqs.send_message_batch(
            QueueUrl=queue_url,
            Entries=entries
        )

        if 'Failed' in response and response['Failed']:
            print("Failed messages:", response['Failed'])
