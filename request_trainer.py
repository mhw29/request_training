import boto3

client = boto3.client('comprehend')

response = client.batch_detect_dominant_language(
    TextList=[
        'string',
    ]
)

print(response)