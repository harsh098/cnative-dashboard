import boto3
client = boto3.client('ecr')

response = client.create_repository(
    repositoryName='cnative-dashboard',
    tags=[
        {
            'Key': 'project-name',
            'Value': 'cnative-dashboard'
        },
    ],
    imageTagMutability='MUTABLE',
    imageScanningConfiguration={
        'scanOnPush': False
    }
)

uri = response['repository']['repositoryUri']
print(uri)