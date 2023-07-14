''' 
Your task is to build a web scraper that retrieves basic beauty product data 
 from popular websites like Sephora, Ulta or any other similar website of your 
 choice and writes the data to a local database. We are interested in the 
 following product information:
 
Name
Brand
Price
Ingredients
Images

Sephora XPath Price: /html/body/div[2]/main/div[1]/div[1]/div[1]/div[2]/p/span/span[1]/b
/html/body/div[2]/main/div[1]/div[1]/div[1]/div[2]/p/span/span[1]/b
<b class="css-0">$84.00</b>
document.querySelector("body > div:nth-child(3) > main > div:nth-child(1) > div.css-1v7u6og.eanm77i0 > div:nth-child(1) > div.css-1tzthcm.eanm77i0 > p > span > span.css-18jtttk > b")
document.querySelector("body > div:nth-child(3) > main > div:nth-child(1) > div.css-1v7u6og.eanm77i0 > div:nth-child(1) > div.css-1tzthcm.eanm77i0 > p > span > span.css-18jtttk > b")
body > div:nth-child(3) > main > div:nth-child(1) > div.css-1v7u6og.eanm77i0 > div:nth-child(1) > div.css-1tzthcm.eanm77i0 > p > span > span.css-18jtttk > b

Please ensure that your scraper is able to handle bot detection mechanisms and 
rate limiting by implementing appropriate strategies, such as using rotating 
user agents, managing request intervals, and handling CAPTCHAs if encountered.

Please follow the guidelines below for completing the challenge:
Choose a programming language that you are comfortable with.
Store the scraped data in a local database.
Implement strategies to avoid bot detection and respect rate limiting. You can use libraries like undetected-chrome etc.
Ensure that the code is well-organized and easy to understand.
Include instructions on how to set up and run your code in a README file.
To submit, email Ivana (ivana@getiris.app) with a link to your public github repo.

ASSUMPTIONS:
    - I want to store the data in a local database (sqlite3)
    - Ideally, I want to store the images in a local folder with the location to the images stored in the database
      However, for the purposes of this exercise, I will store the images' url in the database instead
    - Ingredients will be stored as a string (comma separated) for the purposes of the exercise
      This would normally be stored in a separate table with a foreign key to a ProductIngredients table
      and that table would be linked to the Products table.  In this way we would have a mapping of Ingredients that
      are used in multiple products.  This would be a many to many relationship.
    - I will store brands
    - I will store companies for scraping purposes. 


    
    - I will use selenium to scrape the data
    - I will use undetected-chrome to avoid bot detection
    - I will use proxies to avoid bot detection
    - I will use sqlite3 to store the data
'''

import os
import sqlite3
import random
import sys
import time
from db.db_helper import DBHelper
# from db.DBHelper import get_company_brand_list_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager



def custom_wait_time():
    return random.uniform(min_wait_time, max_wait_time)
    

def simulate_human_behavior():
    wait_time = custom_wait_time()

    time.sleep(wait_time)
    

def add_random_hesitations(action_chains, element):
    num_hesitations = random.randint(3, 6)

    for _ in range(num_hesitations):
        action_chains.move_to_element(element).perform()
        simulate_human_behavior()
        
        
# # performing an HTTP request with a proxy 
# response = requests.get(url, proxies=proxies)

def get_random_user_agent():
    return random.choice(user_agents_chrome)

def get_random_proxy():
    return random.choice(proxies)

def get_random_https_proxy():
    return random.choice(https_proxies)



def scrape(url, company_id):

    driver.get(url)

    
    # Find all the <div> elements with the id format "brands-#" using XPath
    div_elements = driver.find_elements("xpath", '//div[starts-with(@id, "brands-")]')

    for div_element in div_elements:
        # Find the <li> elements within the <div> element
        li_elements = div_element.find_elements("xpath",'.//li[@class]')
        for li_element in li_elements:

            brand_url = li_element.find_element("xpath",'.//a[@data-at="brand_link"]').get_attribute('href')
            span_element = li_element.find_element("xpath",'.//span')
            brand_name = span_element.text

            brand_id = db.get_brand_id_by_name(brand_name)
            
            if brand_id is None:
                brand_id = db.insert_brand(brand_name)
                

            db.insert_company_brand(company_id, brand_id, brand_url)

            current_brand_url = driver.current_url
            # We have the brand and company, now we need to get the products
            scrape_products(brand_url, company_id, brand_id, driver)
            driver.get(current_brand_url)

    # Print or use the page source as needed
    #print(page_source)

    driver.quit()

def popup_modal_close():
    # find the close button
    try:
        close_button = driver.find_element("xpath",'.//button[@data-at="close_button"]')
        action_chains = ActionChains(driver)
        simulate_human_behavior()
        add_random_hesitations(action_chains,close_button)

    except:
        print("No close button found")

def scrape_products(url, company_id, brand_id, driver):

    driver.get(url)

    try:
        #find grid elements
        grid_elements = driver.find_elements("xpath",'.//a[@data-comp="ProductTile"]')
        for product_element in grid_elements:
            simulate_human_behavior()
            action_chains = ActionChains(driver)
            product_link = product_element.get_attribute('href')
            product_name = product_element.find_element("xpath",".//span[@class='ProductTile-name']").text
            print(product_link)
            print(product_name)
            picture = product_element.find_element("xpath",".//img")
            picture_url = picture.get_attribute('src')
            print(picture_url)
            add_random_hesitations(action_chains, product_element)
            # product_element.click()
            # driver.get(product_link)
        
    except:
        print("No grid elements found")

    driver.back()
        
# def get_company_brand_list_urls(company):
#     brand_url = db.get_company_brand_list_url(company)
#     print(brand_url)
#     return brand_url

def populate_brand_table():
    pass

def populate_product_table():
    pass

def populate_ingredient_table():
    pass

def populate_image_table():
    pass


def get_images():
    pass

if __name__ == "__main__":

    # get first argument from command line
    if len(sys.argv) > 1:
        company_name = sys.argv[1]


    # defining the proxies servers (to avoid bot detection) I'd likely put this into a separate file or database table

    proxies = [
        '162.240.76.92:80',
        '207.2.120.19:80',
        '137.184.41.250:80',
        '47.88.3.19:8080',    
        '216.137.184.253:80',
        '/18.222.211.211:3128'
        '134.209.29.120:3128',
        '65.20.189.144:8080',
        '65.111.241.211:80',
        '154.85.58.149:80',
        '170.187.227.16:844',
        '143.198.209.148:80',
        '18.190.21.166:80',
        '198.199.86.11:3128',
        '172.93.213.177:80',
        '155.94.149.220:811',
        '18.214.66.210:80',
        '142.129.136.189:29',
        '162.223.94.163:80',
        '104.248.50.192:777',
        '65.111.241.219:80',
        '209.97.150.167:312',
        '104.166.186.164:31',
        '193.122.0.244:80',
        '20.219.137.240:300',
        '47.243.242.70:9090',
        '143.198.209.149:80',
        '20.157.194.61:80',
        '209.97.150.167:808',
        '202.5.16.44:80',
        '47.243.242.70:5544',
        '134.209.29.120:808',
        '47.251.48.42:8888',
        '34.36.96.83:3128',
        '20.120.240.49:80',
        '65.111.241.215:80',
        '138.68.60.8:3128',
        '64.227.30.208:3128',
        '216.137.184.253:80',
        '47.88.11.3:1099',
        '152.67.103.55:8080',
        '34.88.86.0:8888',
        '49.51.184.233:8080',
        '35.213.91.45:80',
        '47.243.50.83:7777',
        '63.42.112.155:8001',
        '66.29.154.103:3128',
        '198.44.191.202:457',
        '158.101.113.18:80',
        '165.225.206.248:10',
        '207.2.120.19:80',
        '198.11.175.192:80',
        '50.193.140.151:80'
        ]

    https_proxies = [
        '64.225.4.29:9814',
        '68.181.13.130:80',
    ]

    user_agents_chrome = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    ]

    min_wait_time = 2 # minimum wait time in seconds
    max_wait_time = 7 # maximum wait time in seconds

    #Create chrome options with random user agent
    chrome_options = Options()
    user_agent = get_random_user_agent()
    proxy = get_random_https_proxy()
    print(f"Using proxy: {proxy}")
    print(f"Using user agent: {user_agent}")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    # Create ChromeService with ChromeDriverManager
    chrome_service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.implicitly_wait(custom_wait_time())

    db = DBHelper('newness_scraping.db')
    # brand_url = get_company_brand_list_urls(company)
    company_id, url, brand_url = db.get_company_info(company_name)
    scrape(brand_url, company_id)

    db.close()
    
    driver.quit()


