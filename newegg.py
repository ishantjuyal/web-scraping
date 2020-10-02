from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/global/in-en/p/pl?d=graphic+cards&N=101300350"

# Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    # print("Brand: " + brand)
    # print("Product Name: " + product_name)
    f.write(brand + "," + product_name.replace(",", "|") + "\n")