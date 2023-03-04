import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage you want to scrape
url = "https://careers.google.com/jobs/results/?company=Google&company=YouTube&employment_type=FULL_TIME&hl=en_US&jlo=pt-BR&q=Software+Engineer&sort_by=relevance&loc=Brazil"
response = requests.get(url)

# Parse the HTML content of the webpage using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant information on the page using Beautiful Soup's find() or find_all() methods
data = []
for item in soup.find_all('div', class_='ressarcimento-item'):
    ressarcimento = item.find('h2').text
    descricao = item.find('p', class_='descricao').text
    valor = item.find('span', class_='valor').text
    data.append({'Ressarcimento': ressarcimento, 'Descrição': descricao, 'Valor': valor})
    
    # Find and extract email addresses from the description
    email = ''
    for word in descricao.split():
        if '@' in word:
            email = word

    # Append email to dictionary if found
    if email:
        data[-1]['Email'] = email

# Print the scraped data
print(data)
