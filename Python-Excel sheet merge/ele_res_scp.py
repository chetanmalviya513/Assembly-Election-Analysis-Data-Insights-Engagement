import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://results.eci.gov.in/AcResultGenDecNew2023/partywisewinresult-369S12.htm"

r = requests.get(url)

print(r)