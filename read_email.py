from email.parser import Parser  

def read_email_bodies(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    emails = []
    emails_list = content.strip().split('|')

    for email in emails_list:
        email_parts =Parser().parsestr(email.strip())
        email = {
            'From': email_parts['From'],
            'To': email_parts['To'],
            'Subject': email_parts['Subject'],
            'Body': email_parts.get_payload()
        }
        emails.append(email)

    return emails

read_file_path = r'C:\Users\LENOVO\Desktop\Git\Gen_AI\Gen-AI\Emails.txt'
emails = read_email_bodies(read_file_path)
