import requests
from bs4 import BeautifulSoup

# Get actor's name
actor_name = input('Enter actor\'s name and last name: ')
# Convert to lowercase and split
actor_name = actor_name.lower().split()
# Concat name and last name with dash
actor_name = actor_name[0] + '-' + actor_name[1]
url = "https://www.celebritynetworth.com/richest-celebrities/actors/"
# construct the final url
url = url + actor_name + '-net-worth'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

net_worth_element = soup.find('div', {'class': 'value'})
if net_worth_element is not None:
    net_worth_string = net_worth_element.text
    net_worth_string = net_worth_string.replace('$', '')\
        .replace(' Million', '000000').replace(',', '')
    net_worth = int(net_worth_string)
    actor_name_element = soup.find('div', {'class': 'profile_details'})
    if actor_name_element is not None:
        actor_name = actor_name_element.find('h1').text
        print(f"{actor_name} has a net worth of ${net_worth}")
    else:
        print("Could not find actor name information.")
else:
    print("Could not find net worth information.")
