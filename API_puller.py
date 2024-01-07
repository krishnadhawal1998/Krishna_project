import requests
import csv


api_url = 'https://dummyjson.com/products'

# Make the API request
response = requests.get(api_url)
if response.status_code != 200:
    print('Failed to access data:', response.status_code) # if failed to connect with API, this message will be displayed
    exit()
    
# This extratcs the data from the API response
data = response.json()
items = data['items'] 

# Write the data to a CSV file
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'title', 'description', 'price'])

    for item in items:
        # Extracting the required parameters
        id = item.get('id', '')
        title = item.get('title', '')
        description = item.get('description', '')
        price = item.get('price', '')

        writer.writerow([id, title, description, price])

print('Data written to output.csv')

pip install virtualenvwrapper-win
