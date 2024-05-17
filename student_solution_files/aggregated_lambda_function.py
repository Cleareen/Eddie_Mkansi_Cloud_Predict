# Lambda dependencies
import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data
import numpy as np # Array manipulation
# <<< You will need to add additional libraries to complete this script >>> 

# ** Insert key phrases function **
def key_phrase_finder(list_of_important_phrases, list_of_extracted_phrases):

    listing = []
    PhraseChecker = None

    res = str(list_of_extracted_phrases).split()

    for important_word in list_of_important_phrases:
        names = res
        names2 = [word for word in names if important_word in word]
        isnot_empty = np.array(names2).size > 0
        
        if isnot_empty == True:
            listing = np.append(listing, names2)
            
        else:
            listing = listing
            
    if np.array(listing).size > 0:
        PhraseChecker = True
        
    else:
        PhraseChecker = False
    
    return listing, PhraseChecker
# -----------------------------

# ** Insert sentiment extraction function **
def find_max_sentiment(Comprehend_Sentiment_Output):
    
    sentiment_score = 0

    if Comprehend_Sentiment_Output['Sentiment'] == 'POSITIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Positive']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEGATIVE':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Negative']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEUTRAL':
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Neutral']

    else:
        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Mixed']

    print(sentiment_score, Comprehend_Sentiment_Output['Sentiment'])
    
    return Comprehend_Sentiment_Output['Sentiment'], sentiment_score
# -----------------------------

# ** Insert email responses function **
 if overwhelming_sentiment == 'POSITIVE':
        if  ((Matched_Phrases_Checker_CV == True) & \
            (Matched_Phrases_Checker_Article == True) & \
            (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Article_Text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, CV_text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == True) & \
             (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)       
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == False)):

            mytuple = (Greetings_text, Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif ((Matched_Phrases_Checker_CV == False) & \
             (Matched_Phrases_Checker_Article == False) & \
             (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, Project_Text ,Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        elif  ((Matched_Phrases_Checker_CV == True) & \
              (Matched_Phrases_Checker_Article == True) & \
              (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, CV_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        else:
            mytuple = (Greetings_text, Project_Text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
    elif overwhelming_sentiment == 'NEGATIVE':
            mytuple = (Greetings_text, Negative_Text)
            Text = "\n \n".join(mytuple)
            
    else:
            mytuple = (Greetings_text, Neutral_Text)
            Text = "\n \n".join(mytuple)
    
    return Text
 
# -----------------------------

# Lambda function orchestrating the entire predict logic
def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    

    # ** Insert code to write to dynamodb **
    # <<< Ensure that the DynamoDB write response object is saved 
    #    as the variable `db_response` >>> 

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    
    # --- Write to dynamodb ---
    
    # ** Create a variable that can take a random value between 1 and 1 000 000 000. 
    # This variable will be used as our key value i.e the ResponsesID and should be of type integer.
    # It is important to note that the ResponseID i.e. the rid variable, should take
    # on a unique value to prevent errors when writing to DynamoDB. **
    
    # --- Insert your code here ---
    rid = None # <--- Replace this value with your code.
    # -----------------------------
    
    # ** Instantiate the DynamoDB service with the help of the boto3 library **
    
    # --- Insert your code here ---
    dynamodb = None # <--- Replace this value with your code.
    # -----------------------------
    
    # Instantiate the table. Remember pass the name of the DynamoDB table created in step 4
    table = dynamodb.Table('# Insert the name of your generated DynamoDB table here')
    
    # ** Write the responses to the table using the put_item method. **

    # Complete the below code so that the appropriate 
    # incoming data is sent to the matching column in your DynamoDB table
    # --- Insert your code here ---
    db_response = table.put_item(Item={'ResponsesID': None, # <--- Insert the correct variable
                        'Name': None, # <--- Insert the correct variable
                        'Email': None, # <--- Insert the correct variable
                        'Cell': None, # <--- Insert the correct variable
                        'Message': None # <--- Insert the correct variable
    })
    # -----------------------------

    # ** Create a response object to inform the website 
    #    that the workflow executed successfully. **
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message'],
        'DB_response': db_response
        })
    }
    
    return lambda_response


    # Do not change the name of this variable
    db_response = None
    # -----------------------------
    

    # --- Amazon Comprehend ---
    comprehend = boto3.client(service_name='comprehend')
    
    # --- Insert your code here ---
    enquiry_text = None # <--- Insert code to place the website message into this variable
    # -----------------------------
    
    # --- Insert your code here ---
    sentiment = None # <---Insert code to get the sentiment with AWS comprehend
    # -----------------------------
    
    # --- Insert your code here ---
    key_phrases = None # <--- Insert code to get the key phrases with AWS comprehend
    # -----------------------------
    
    # Get list of phrases in numpy array
    phrase = []
    for i in range(0, len(key_phrases['KeyPhrases'])-1):
        phrase = np.append(phrase, key_phrases['KeyPhrases'][i]['Text'])


    # ** Use the `email_response` function to generate the text for your email response **
    # <<< Ensure that the response text is stored in the variable `email_text` >>> 
    # --- Insert your code here ---
    # Do not change the name of this variable
    email_text = None 

    
    # -----------------------------
            

    # ** SES Functionality **

    # Insert code to send an email, using AWS SES, with the above-defined 
    # `email_text` variable as it's body.
    # <<< Ensure that the SES service response is stored in the variable `ses_response` >>> 
   def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))

    # Sample text that you would like to email to your recipient 
    # address from your sender address.
    email_text = 'Insert your sample email here'

    # ** SES Functionality **

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    # --- Insert your code here ---
    SENDER = 'sender@example.com'
    # -----------------------------

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    # --- Insert your code here ---
    RECIPIENT = 'recipient@example.com' 
    # -----------------------------


    # The subject line for the email.
    # --- DO NOT MODIFY THIS CODE ---
    SUBJECT = f"Data Science Portfolio Project Website - Hello {dec_dict['name']}"
    # -------------------------------

    # The email body for recipients with non-HTML email clients
    BODY_TEXT = (email_text)

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES service resource
    client = boto3.client('ses')

    # Try to send the email.
    try:
        #Provide the contents of the email.
        ses_response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                    # 'edsa.predicts@explore-ai.net', # <--- Uncomment this line once you have successfully tested your predict end-to-end
                ],
            },
            Message={
                'Body': {

                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )

    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(ses_response['MessageId'])

    # ** Create a response object to inform the website 
    #    that the workflow executed successfully. **
    lambda_response = {
        'statusCode': 200,
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message'],
        'SES_response': ses_response,
        'Email_message': email_text
        })
    }

    return lambda_response

    # Do not change the name of this variable
    ses_response = None
    
    # ...

    # Do not modify the email subject line
    SUBJECT = f"Data Science Portfolio Project Website - Hello {dec_dict['name']}"

    # -----------------------------


    # ** Create a response object to inform the website that the 
    #    workflow executed successfully. Note that this object is 
    #    used during predict marking and should not be modified.**
    # --- DO NOT MODIFY THIS CODE ---
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
    # -----------------------------
    
    return lambda_response   
    
