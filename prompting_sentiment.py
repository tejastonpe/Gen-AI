import time
from connection import model
from read_review import reviews, output_file_path, email_output_file_path

def generate_sentiment(review):
    prompt = f"""
    Your task is to generate a sentiment i.e only give positive, negative or normal,on the following review:
    i want output in json format dont add '''json in response & follow below sequence for output:
    -review
    -brand
    -product
    -sentiment
    if brand and product is not found , then give unknown
    {review}
    """
    response = model.generate_content(prompt)
    return response.text

def generate_mail(review,sentiment):
    prompt = f"""
    You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email delimited by ```, 
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for their review.
    If the sentiment is negative, apologize and suggest that 
    they can reach out to customer service. 
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: ```{review}```
    Review sentiment: {sentiment}"""

    response = model.generate_content(prompt)
    return response.text

with open(output_file_path, 'a', encoding='utf-8') as output_file:
    for review in reviews:
        sentiment_responce = generate_sentiment(review)
        output_file.write(f"{sentiment_responce }")
        time.sleep(4)
    print('sentiments saved ')

with open(email_output_file_path, 'a', encoding='utf-8') as output_file:
    for review in reviews:
        email_responce = generate_mail(review,sentiment_responce)
        output_file.write(f"\n{email_responce}"+"-"*80)
        time.sleep(4)    
    print('emails saved ')    