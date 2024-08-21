import pandas as pd  
import datetime  
import requests  
from requests.exceptions import ConnectionError  
from bs4 import BeautifulSoup  

# Function to extract specific text data from the HTML content
def webContent_div(webContent, classPath):
    webContent_div = webContent.find_all('div', {'class': classPath})  # Find all div elements with the specified class
    try:
        spans = webContent_div[0].find_all('span')  
        texts = [span.get_text() for span in spans]  # Extract the text from each span element
    except IndexError:  
        texts = []
    return texts

# Function to get real-time stock price and change for a given stock code
def real_time(stockCode):
    url = 'https://finance.yahoo.com/quote/' + stockCode  # Construct the URL for the stock
    try:
        r = requests.get(url)  # Send a GET request to the URL
        webContent = BeautifulSoup(r.text, 'lxml')  
        texts = webContent_div(webContent, 'bottom svelte-ezk9pj')  # Extract price and change from the parsed content
        if texts != []:
            price, change = texts[0], texts[1]  # Assign price and change if found
        else:
            price, change = [], []  
    except ConnectionError: 
        price, change = [], []
    return price, change

# Prompt the user to enter a stock code and print the real-time data
Stock = input("Enter the stock: ")
print(real_time(Stock))
