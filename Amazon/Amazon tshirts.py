from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.request

my_url = "https://www.amazon.in/s/ref=QANav11CTA_en_IN_1/ref=QANav11CTA_en_IN_1/ref=QANav11CTA_en_IN_1?pf_rd_r=FRNMJWMZ7N73NGJDE455&pf_rd_p=e9193858-3bf6-4a65-868b-f007b6df6c7b&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-6&pf_rd_t=&pf_rd_i=1968024031&pf_rd_r=0KPR4TKVJT89WSP8CBP6&pf_rd_p=1160e840-50dc-4acb-a56c-24d42f2546c0&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=mobile-hybrid-5&pf_rd_t=30901&pf_rd_i=1968024031&pf_rd_r=MVRZ05YTVNBGQNVGSSKZ&pf_rd_p=8b97601b-3643-402d-866f-95cc6c9f08d4&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-6&pf_rd_t=&pf_rd_i=1968024031&keywords=Men%27s+T-Shirts&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_72%3A1318477031&s=popularity-rank&dc&c=ts&ts_id=1968123031&ref=sr_nr_p_72_2"

# Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grabs each product
containers = page_soup.findAll("div", {"class":"a-section aok-relative s-image-tall-aspect"})

filename = "amazon.csv"
f = open(filename, "w")

headers = "file_name,Description,link\n"

f.write(headers)
count = 1
for container in containers:
    description = container.img["alt"]
    image_source = container.img["srcset"]
    link = image_source.split(',')[-1][1:-3]
    file_name = "image" + str(count) + ".jpg"
    urllib.request.urlretrieve(link, file_name)
    f.write(file_name + "," + description.replace(",", " ") + "," + link + "\n")
    count += 1

