

from datetime import time
from numpy import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import re
driver = webdriver.Chrome() 

df=pd.read_excel('data1.xlsx', engine='openpyxl',dtype={'URL': str})
# df=df.tail()
# df=df.reset_index()
# df=df[0:1]
print(df.columns)
print(df['/'])

data_len=len(df)


product_availability=[]
def procut_content(url):

    global product_availability
    driver.get("https://www.markastok.com"+str(url))
    try:
        time.sleep(5)
        pageID = driver.find_element_by_xpath("//meta[@property='og:type']").get_attribute("content")
        if pageID=="product":
            print(str(url)+" bu bir ürün")
            ####################### product name
            product_name=driver.find_element_by_id("product-name").text
            print("product_name "+product_name)
            time.sleep(2)
            ###########################  offer
            offer=driver.find_element_by_class_name("detay-indirim").text
            print("offer Oranı "+offer)
            time.sleep(3)
            ######################################
            
            sale_price=driver.find_element_by_class_name("discountPrice").text
            print("sale_price "+sale_price)
            time.sleep(3)

            old_price=driver.find_element_by_xpath("//span[@class='currencyPrice discountedPrice']").text

            print("old_price "+old_price)
            time.sleep(3)

            
            urun_secenekleri=driver.find_element_by_xpath("//div[contains(@class,'new-size-variant fl')]").text


            urun_secenekleri=urun_secenekleri.split("\n")
            print(urun_secenekleri)
            time.sleep(3)

            
            bonus =driver.find_element_by_class_name("product-feature-content").text
            time.sleep(3)
            product_code=driver.find_element_by_xpath("//b[text()='YERLİ ÜRETİM']").text
            time.sleep(3)


            for match in re.finditer(product_code, bonus):
               

                product_code_start=match.start()
                

            product_code=(bonus[product_code_start::])


            print(product_code)





        else:
            print(str(url)+"Bu bir ürün degil Bu bir category")
    except Exception as e:
        print(str(url)+"Content çekemedik , Bu bir ürün degil ")
       
            return product_name, offer,sale_price,old_price,urun_secenekleri,product_code

for i in range(data_len):

    procut_content(str(df['/'][i]))
    
   
