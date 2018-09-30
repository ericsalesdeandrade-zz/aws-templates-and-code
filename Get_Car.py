import boto3

def get_car(event, context):
    print("The Brand you selected is {0}".format(event['brand']))
