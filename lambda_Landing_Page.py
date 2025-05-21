#------------------------------------------------------------------------------------
# Created by Rama Subramanyam based on video at youtube at https://www.youtube.com/watch?v=XX6ADwJBGgY&t=95s
# This is the second example in the series to learn implementation serverless app at AWS
# Following are the features of this lambda function
# a) This is lambda_function when access by suer using function url,
#    which reads index.html from S3 return the same to user screen.  
# b) The index.html page has a form for the user to select the location and submit
#    When submitted, it calls another lambda function.  
# 
# date : May 2025
# usage: over ride default variable values
#------------------------------------------------------------------------------------

###################################################
# AWS CLI Parameters (For Terraform users)
# aws_acount_id = "       "
# tags = {
#   "terraform" = "true"
#   "project" = "Lambda-OpenAI-Interface-Example2"
#   "contact" = "ecirams@gmail.com"
# }
# aws_region = "us_east_1"
# aws_profile = "ecirams"
###################################################

###################################################
# Lambda Runtime Settings  
# lambda_python_runtime = "python3.9"
# debug_mode = true
# lambda_siz = 256
# lambda_timeout = 400
###################################################

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