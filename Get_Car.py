import boto3

def get_car(event, context):
    try:
        s3 = boto3.resource('s3')
        client_s3 = boto3.client('s3')
        brand_upper = event["brand"].upper()
        bucket = s3.Bucket("car-images-hd")
        for obj in bucket.objects.filter(Prefix=brand_upper + '/'):
            s3_object = client_s3.get_object(
            Bucket=bucket,
            Key=obj.key + '/'
            )
            return s3_object
    except BaseException as error:
        print("*** Failure to retrieve Car Image - Please check your request ***")
        print(error)
        return "*** Failure to retrieve Car Image - Please check your request ***"
