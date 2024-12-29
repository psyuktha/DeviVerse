import requests
from bs4 import BeautifulSoup

url = "https://manblunder.com/articlesview/soundarya-lahari-verse-1"  

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve content: {response.status_code}")
    exit()
soup = BeautifulSoup(html_content, 'html.parser')

post_content = soup.find('div', class_='post-content')

if post_content:

    heading = post_content.find('h2').text.strip()
    print(f"Heading: {heading}\n")

    verses = post_content.find_all('p', style="text-align:center")
    print("Sanskrit Verse:")
    for verse in verses:
        print(verse.text.strip())
    print()

    paragraphs = post_content.find_all('p', style="text-align:justify")
    for idx, para in enumerate(paragraphs, 1):
        print(f"Paragraph {idx}:")
        print(para.text.strip())
        print()
    with open('/Users/yuktha/Documents/Soundarya_Lahari/soundarya_lahari_verse_1.txt', 'w', encoding='utf-8') as file:
        file.write(f"Heading: {heading}\n\n")
        file.write("Sanskrit Verse:\n")
        for verse in verses:
            file.write(verse.text.strip() + '\n')
        file.write('\n')
        for idx, para in enumerate(paragraphs, 1):
            
            file.write(para.text.strip() + '\n\n')
else:
    print("Content not found!")
