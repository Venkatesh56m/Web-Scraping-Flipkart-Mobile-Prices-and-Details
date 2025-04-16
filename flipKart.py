#-----------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd

Names = []
Prices = []
Desc = []
Reviews = []
for i in range(1,11):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    print(r)



    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "DOjaWF gdgoEp") # imp very very imp
    names = box.find_all("div", class_ ="KzDlHZ")
    #print(names)

    for i in names:
        name = i.text
        Names.append(name)
    #print(Names)


    prices = box.find_all("div", class_ = "Nx9bqj _4b5DiR")
    for i in prices:
        price = i.text
        Prices.append(price)
    #print(Prices)

    descriptions = box.find_all("div", class_ = "_6NESgJ")
    for i in descriptions:
        description = i.text.strip()
        Desc.append(description)
    #print(Desc)


    reviews = box.find_all("div", class_ = "XQDdHH")
    for i in reviews:
        review = i.text.strip()
        Reviews.append(review)
    #print(Reviews)

min_len = min(len(Names), len(Prices), len(Desc), len(Reviews))

Names = Names[:min_len]
Prices = Prices[:min_len]
Desc = Desc[:min_len]
Reviews = Reviews[:min_len]


df = pd.DataFrame({"Product Name":Names,"Product Prices":Prices,"Product Description":Desc,"Product Ratings":Reviews})
print(df)

# Save to CSV
df.to_csv(r'D:\BS4_PDF\flipkart_mobiles.csv', index=False)

print("Data saved to CSV!")