import requests
from bs4 import BeautifulSoup

url = "http://metservice.intnet.mu/forecast-bulletin-french-mauritius.php"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful [[(status code 200)]]
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all paragraphs within the forecast section
    paragraphs = soup.select('div.left_content p')

    # Check if paragraphs are found
    if paragraphs:

        # Extract and print the text within <p> tags
        for paragraph in paragraphs:
            print(paragraph.get_text(strip=True))

        # Extract text within <p> tags
        text_content = "\n".join(paragraph.get_text(strip=True) for paragraph in paragraphs)

        # Save the text content to a Notepad file
        with open("Weather News.txt", "w", encoding="utf-8") as file:
            file.write(text_content)

        print('\n----------------------------------------')
        print("Weather news saved to 'weather_news.txt'")
        print('----------------------------------------')


    else:
        print("No paragraphs found within the weather section.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
