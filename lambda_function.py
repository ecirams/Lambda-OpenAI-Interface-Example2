import boto3

s3_client = boto3.client('s3')

def lambda_handler(event,context):
    s3_Bucket_Name = "TO-REPLACE-ME"
    s3_File_Name = "index.html"
    base_url = "TO-REPLACE-ME"

    object = s3_client.get_object(Bucket=s3_Bucket_Name, Key=s3_File_Name)
    body = object['Body']
    html_output = body.read().decode('utf-8')
    html_output = html_output.replace ('$BASE_URL$',base_url)

    return {
        'statusCode' : 200,
        'body': html_output,
        'headers' : {
            'Content-Type' : 'text/html',
        }
    }