#------------------------------------------------------------------------------------
# Created by Rama Subramanyam based on video at youtube at https://www.youtube.com/watch?v=Lf98s3NczBE
# This is the second example in the series to learn implementation serverless app at AWS
# 
# date : May 2025
# usage: over ride default variable values
#------------------------------------------------------------------------------------

###################################################
# AWS CLI Parameters (For Terraform users)
# aws_acount_id = "       "
# tags = {
#   "terraform" = "true"
#   "project" = "Lambda-OpenAI-Interface-Example1"
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

####################################################
# Lambda Environment Variable Settings
# API_KEY = "<openai-key>" 
####################################################


import openai
import os
import json


def lambda_handler(event, context):
    #Get Environment variable  
    openai.api_key = os.getenv("API_KEY")


    #Set value for location for which you would like to display interesting fact to user
    location = event['locationId']
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Tell me interesting fact about {location} in less than 200 characters "}
    ]

    # chat = openai.Completion.create(model="gpt-3.5-turbo", messages = messages)
    chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages = messages)

    gpt_response = chat.choices[0].message.content

    return {
        'statusCode': 200,
        'gpt_response' : gpt_response
    }

    #html_output = f"<html><body><h1>Interesting Fact about the place {location}</h1><p>{gpt_response}</p></body></html>"
    #print("gpt_response:",gpt_response)
    #return { 
    #    'statusCode': 200,
    #    'body': html_output,
    #    'headers': {
    #        'Content-Type': 'text/html'
    #    }
    #}