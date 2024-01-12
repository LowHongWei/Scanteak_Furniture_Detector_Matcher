# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# import numpy as np
# import re
# import pandas as pd
# import requests
# import json
# import os
# from pathlib import Path
#
# def getdetails(x):
#     df=pd.DataFrame()
#     for item in x.find_all(class_="card px-0 px-md-4"):
#         item_name = (json.loads(item.find(class_='itemInfo').input['value'])['name'])
#         item_price = (json.loads(item.find(class_='itemInfo').input['value'])['price'])
#         item_cat = (json.loads(item.find(class_='itemInfo').input['value'])['category'])
#         item_url = (item.find(class_='bc-sf-filter-product-item-image').img['src'])
#         prod_url = "https://www.ikea.com.hk"+item.find(class_='card-header').a['href']
#
#         df = df.append({"item_name":item_name, "item_price":item_price, "item_cat":item_cat,"item_url":item_url,"prod_url":prod_url},ignore_index=True)
#         return df
#
# def ikeascrape(productlist):
#     ikeadf = pd.DataFrame()
#     driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
#     for product in productlist:
#         URL = "https://www.ikea.com.hk/en/products/"+product
#         driver.get(URL)
#         subhtml = driver.page_source
#         soup = BeautifulSoup(subhtml, "html.parser")
#
#         # try:
#         while True:
#             itemdf = getdetails(soup)
#             ikeadf = pd.concat([ikeadf,itemdf])
#             WebDriverWait(driver, 30)
#
#             nextlink = soup.find(class_='page-item next')
#
#             if nextlink:
#                 newurl = nextlink.find('a',{'class':"page-link"})['data-sitemap-url']
#                 driver.get(newurl)
#                 newhtml = driver.page_source
#                 soup = BeautifulSoup(newhtml, "html.parser")
#             else:
#                 break
#     return ikeadf
#
# def cleansing(df):
#     #clean unwanted category
#     excludeli = ['0126 Footstools','0917 Baby highchairs',"0951 Children's beds (8-14)","1233 Chairpads","0211 Living room storage"]
#     dfclean = df[~df["item_cat"].isin(excludeli)]
#
#     #drop duplicated images
#     dfclean.drop_duplicates(subset ="item_url",keep=False, inplace = True)
#
#     dfclean['item_cat'].replace(
#     {'0113 Sofa beds': 'sofas',
#     '0111 Sofas': 'sofas',
#     '0125 Armchairs': 'chairs',
#     '0521 Bed frames..': 'beds',
#     '0423 Wardrobes': 'dressers',
#      '0212 Living room cabinets':'dressers',
#     '0811 Dining tables': 'tables',
#     '0822 Dining stools': 'chairs',
#     '0821 Dining chairs and folding chairs': 'chairs',
#     '0823 Bar stools': 'chairs',
#     '1012 Table lamps': 'lamps',
#     '1011 Floor lamps': 'lamps',
#     '1016 Wall lamps and wall spotlights': 'lamps'},inplace=True
#     )
#
#     return dfclean.reset_index()
#
# def savecleandf(df):
#     df.to_csv("ikeadata2/"+'ikea_scrape.csv',index=False)
#
# def getscrapeimage(newdf):
#     for index, row in newdf.iterrows():
#         try:
#             os.makedirs(Path("ikeadata2/"+str(row['item_cat'])))
#         except FileExistsError:
#             # directory already exists
#             pass
#
#         with open("ikeadata2/"+str(row['item_cat'])+'/'+str(index)+'.jpg','wb') as f:
#             image = requests.get(row['item_url'])
#             f.write(image.content)
# from bs4 import BeautifulSoup
# import requests

# def get_scanteak_products(url):
#     """
#     Scrapes product details from Scanteak Singapore website.
#
#     Args:
#         url: The URL of the Scanteak Singapore product page or category.
#
#     Returns:
#         A list of dictionaries containing product details.
#     """
#     product_data = []
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#
#     products = soup.find_all("div", class_="bc-sf-filter-product-item-inner")
#     print(products)
#     for product in products:
#         data = {}
#         name = product.find("a", class_="bc-sf-filter-product-item-title").text.strip()
#         # price = product.find("span", class_="money").text.strip()
#         # category = product.find("div", class_="product-vendor").text.strip()
#         # item_url = (item.find(class_='bc-sf-filter-product-item-image').img['src'])
#         # bc - sf - filter - product - item - flip - image
#         image_url = "https://scanteak.com.sg" + product.find("img")["src"]
#         # product_url = "https://scanteak.com.sg" + product.find("a")["href"]
#         print(image_url)
#         data["name"] = name
#         # data["price"] = price
#         # data["category"] = category
#         data["image_url"] = image_url
#         # data["product_url"] = product_url
#
#         product_data.append(data)
#
#     return product_data
#
#
# # Example usage
# scanteak_url = "https://scanteak.com.sg/collections/all"
# products = get_scanteak_products(scanteak_url)
# print(products)
# # Print product details
# for product in products:
#     print(f"Name: {product['name']}")
#     # print(f"Price: {product['price']}")
#     # print(f"Category: {product['category']}")
#     # print(f"Image URL: {product['image_url']}")
#     # print(f"Product URL: {product['product_url']}")
#     # print("---")


import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_scanteak_products(url):
    """
    Scrapes product details from Scanteak Singapore website.

    Args:
        url: The URL of the Scanteak Singapore product page or category.

    Returns:
        A list of dictionaries containing product details.
    """
    product_data = []
    page_number = 1
    while page_number < 2:
        print(page_number)
        page_url = f"{url}?page={page_number}"
        print(page_url)
        page = requests.get(page_url)
        soup = BeautifulSoup(page.content, "html.parser")

        products = soup.find_all("div", class_="bc-sf-filter-product-item-inner")
        for product in products:
            data = {}
            name = product.find("a", class_="bc-sf-filter-product-item-title").text.strip()
            price = product.find("span", class_="bc-sf-filter-product-item-sale-price").text.strip()
            item_cat = product.find("h1", class_="page-title").text.strip()
            item_url = "https://scanteak.com.sg/" + product.find("a")["href"]
            image_url = product.find("img")["src"]

            data["name"] = name
            data["price"] = price
            data["item_cat"] = item_cat
            data["item_url"] = item_url
            data["image_url"] = image_url
            #         item_name = (json.loads(item.find(class_='itemInfo').input['value'])['name'])
            #         price = product.find("span", class_="bc-sf-filter-product-item-sale-price").text.strip()
            #         item_cat = (json.loads(item.find(class_='itemInfo').input['value'])['category'])
            #         item_url = (item.find(class_='bc-sf-filter-product-item-image').img['src'])
            #         prod_url = "https://www.ikea.com.hk"+item.find(class_='card-header').a['href']

            product_data.append(data)
        page_number += 1

    return product_data

def save_to_csv(product_data, csv_filename):
    df = pd.DataFrame(product_data)
    df.to_csv(csv_filename, index=False)
    print(f"Data saved to {csv_filename}")

def download_images(product_data, output_directory):
    for product in product_data:
        print(product)
        category = product.get('category', 'uncategorized')  # Default to 'uncategorized' if category is not available
        try:
            os.makedirs(os.path.join(output_directory, category))
        except FileExistsError:
            pass
        image_url = product["image_url"]
        image_filename = os.path.join(output_directory, category, f"{product['name']}.jpg")
        response = requests.get(image_url)
        with open(image_filename, 'wb') as f:
            f.write(response.content)

def main():
    scanteak_url = "https://scanteak.com.sg/collections/sofa-and-daybeds"
    output_csv_filename = "scanteak_products.csv"
    output_image_directory = "scanteak_images"

    products = get_scanteak_products(scanteak_url)
    save_to_csv(products, output_csv_filename)
    download_images(products, output_image_directory)

if __name__ == "__main__":
    main()
