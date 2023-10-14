import boto3


def send_message_queue(
    queue_name: str,
    message: str,
    delay_seconds: int = 0,
) -> dict:
    sqs = boto3.resource("sqs")
    if queue_name is None:
        pass
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    response = queue.send_message(MessageBody=message, DelaySeconds=delay_seconds)
    return response
