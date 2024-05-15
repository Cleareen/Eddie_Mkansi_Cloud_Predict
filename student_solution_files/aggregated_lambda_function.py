
"""
    Final AWS Lambda function skeleton. 
    
    Author: Explore Data Science Academy.
    
    Note:
    ---------------------------------------------------------------------
    The contents of this file should be added to a AWS  Lambda function 
    created as part of the EDSA Cloud-Computing Predict. 
    For further guidance around this process, see the README instruction 
    file which sits at the root of this repo.
    ---------------------------------------------------------------------

"""

# Lambda dependencies
import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data
import numpy as np # Array manipulation
# <<< You will need to add additional libraries to complete this script >>> 

# ** Insert key phrases function **
def extract_key_phrases(text):
    comprehend = boto3.client(service_name='comprehend')
    response = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
    return response

# ** Insert sentiment extraction function **
def extract_sentiment(text):
    comprehend = boto3.client(service_name='comprehend')
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    return response

# ** Insert email responses function **
def generate_email_response(sentiment, key_phrases):
    if sentiment == 'POSITIVE':
        email_text = "Thank you for your message. We appreciate your interest and will get back to you shortly."
    elif sentiment == 'NEGATIVE':
        email_text = "We're sorry to hear that you're not satisfied with our service. We'll do our best to address your concerns."
    else:
        email_text = "We've received your message and will respond as soon as possible."
    return email_text

# Lambda function orchestrating the entire predict logic
def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    # ** Insert code to write to DynamoDB **
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Eddie_Mkansi_Portfolio_Project')
    db_response = table.put_item(Item=dec_dict)
    # -----------------------------
    
    # ** Use the `extract_sentiment` and `extract_key_phrases` functions to analyze the message **
    enquiry_text = dec_dict['message']
    sentiment_response = extract_sentiment(enquiry_text)
    key_phrases_response = extract_key_phrases(enquiry_text)
    
    # Extract sentiment
    sentiment = sentiment_response['Sentiment']
    
    # Extract key phrases
    key_phrases = [phrase['Text'] for phrase in key_phrases_response['KeyPhrases']]
    
    # ** Use the `generate_email_response` function to generate the email response **
    email_text = generate_email_response(sentiment, key_phrases)
    
    # ** Perform SES functionality to send an email **
    ses_client = boto3.client('ses')
    response = ses_client.send_email(
        Destination={
            'ToAddresses': [dec_dict['email']]
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': email_text,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Response to your inquiry',
            },
        },
        Source='cleareen@gmail.com'
    )
    ses_response = response['ResponseMetadata']
    
    # ** Create a response object to inform the website that the workflow executed successfully.**
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
            'Name': dec_dict['name'],
            'Email': dec_dict['email'],
            'Cell': dec_dict['phone'], 
            'Message': dec_dict['message'],
            'DB_response': db_response,
            'SES_response': ses_response,
            'Email_message': email_text
        })
    }
    
    return lambda_response
