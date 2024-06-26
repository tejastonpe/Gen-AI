def read_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    reviews = content.strip().split('|')
    return reviews

read_file_path = r'C:\Users\LENOVO\Desktop\Git\Gen_AI\Gen-AI\Reviews.txt'
output_file_path = r'C:\Users\LENOVO\Desktop\Git\Gen_AI\Gen-AI\sentiments.txt'
email_output_file_path = r'C:\Users\LENOVO\Desktop\Git\Gen_AI\Gen-AI\email_response.txt'
reviews = read_reviews(read_file_path)

