from bs4 import BeautifulSoup
import requests

URL = "http://www.etender.ir/user.php?section=auction&keyword=&catid=10&subcategory=0&province%5B%5D=8&orgname=&date=&date2=&etc=&st=1&rows=100"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find()
print(results.prettify())
