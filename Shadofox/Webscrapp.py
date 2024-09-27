import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'

try:
    r = requests.get(url)
    r.raise_for_status()  # Check for HTTP errors

    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # Print the prettified HTML for inspection
    print(soup.prettify())  # This will help you understand the structure

    # Get title
    title = soup.title
    print(f"Title: {title.string if title else 'No title found'}")

    # Attempt to find the first paragraph
    first_paragraph = soup.find('p')
    if first_paragraph:
        print(f"First paragraph: {first_paragraph.get_text()}")
    else:
        print("No <p> tag found.")

    # Get all paragraphs
    paras = soup.find_all('p')
    print(f"Total paragraphs found: {len(paras)}")
    for p in paras[:5]:  # Print only the first 5 paragraphs
        print(p.get_text())

    # Get all anchor tags
    anchors = soup.find_all('a')
    print(f"Total anchor tags found: {len(anchors)}")
    for link in anchors[:5]:  # Print only the first 5 links
        print(link.get('href'))

    # Find all elements with class 'lead'
    lead_paragraphs = soup.find_all("p", class_="lead")
    if lead_paragraphs:
        print("Lead paragraphs:")
        for lead in lead_paragraphs:
            print(lead.get_text())
    else:
        print("No paragraphs with class 'lead' found.")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


title = soup.title
# get all paragraphs
paras = soup.find_all('p')
print(paras)
# get all anchor tag
anchors = soup.find_all('a')
print(anchors)

# get first element in html page
print(soup.find('p'))


# find all the elements with class lead
print(soup.find_all("p", class_="lead"))



# get all the links on the page:
for link in anchors:
    print(link.get('href'))

