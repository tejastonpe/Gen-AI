import pandas as pd
import time
from connection import model
from read_email import read_email_bodies, emails, read_file_path

output_file_path = r'C:\Users\LENOVO\Desktop\Git\Gen_AI\Gen-AI\SummarizedEmails.xlsx'
email_data=[]

for email in emails:
    prompt = f"""
    Your task is to generate a short summary of the email body.
    Summarize the email body,in at most 30 words.
    {email['Body']}
    """
    response = model.generate_content(prompt)
    summary = response.text.strip()

    prompt_translate = f"""
    Translate the following English text to Spanish:
    {summary}
    """
    spanish_response = model.generate_content(prompt_translate)
    summary_spanish = spanish_response.text.strip()

    email_data.append({
                'From': email['From'],
                'To': email['To'],
                'Subject': email['Subject'],
                'Body': email['Body'],
                'Body Summary (English)': summary,
                'Body Summary (Spanish)': summary_spanish
            })

    df = pd.DataFrame(email_data)
    df.to_excel(output_file_path, index=False)
    time.sleep(10)
print('Email summarization & translation completed.')