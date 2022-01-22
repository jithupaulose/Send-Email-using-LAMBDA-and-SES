import json
import boto3
def lambda_handler(event, context):
    file_name = event['Records'][0]['s3']['object']['key']
    bucketName=event['Records'][0]['s3']['bucket']['name']
    print("Event details : ",event)
    print("File Name : ",file_name)
    print("Bucket Name : ",bucketName)
    subject = 'Event from ' + bucketName
    client = boto3.client("ses")
    body = """
                 <br>
                 This is a notification mail to inform you regarding s3 event.
                 The file {} is inserted in the {} bucket .
         """.format(file_name, bucketName)
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "Put the sender's mail id", Destination = {"ToAddresses": ["Put Destination Mail id"]}, Message = message) 
    print("The mail is sent successfully")