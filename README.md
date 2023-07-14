
# Technologies used
 - Python 3.9.1
 - Selenium 4.10
 - Undetected ChromeDriver 3.5.0

# Installation
    - Clone this repository
    - Install the requirements
        -- `pip install -r requirements.txt`
    

# Usage
- Run the scraper.py file
    -- `python scraper.py`

# Considerations
I never scraped a site before so there was a lot of research that I had to do in order to get up to speed on the ins and outs of site scraping and site crawling (which I'm still learning and am quite fascinated with honestly)

## Why Selenium?
Selenium allowed me to interact with the page as if I was a user. I could interact with the links and get the data I needed. I could have used the requests library to get the data, but I would have to deal with the cookies and the headers, which would be a lot of work. Selenium also allowed me to use the undetected chromedriver, which is a chromedriver that is not detected by the website, so I could scrape the data without being blocked.

##  Proxy Servers
At first, I set up a series of proxy servers to use with the undetected chromedriver, but I found out that the undetected chromedriver might already have an option to rotate through proxy servers.  The issue with the proxy servers are that they normally are not free and the ones that are free are not very reliable.  I likely would have to pay for a proxy server service in order to get reliable servers to use in the long run.


## Rotating User Agents
I added a list of user agents to the file to rotate through. The idea is that the user agent would change with a new request so it would not appear to be the same user making the request.  I thought about using a library to rotate the user agents, but I decided to just use a list and rotate through the list. Also considered having that rotation tied to the proxy server rotation, but decided against it for now.

## Products
I decided to scrape the products from the brands page, because I thought it would be more comprehensive. I could have scraped the products from the products page, but I would have to scrape each product individually without knowing the links for the products.  

## Data
I decided to save the data to a sqlite3 database.  One because it comes with python.  Two because it is a lightweight option that can be used as a reference to continue with scraping should any disconnects occur.

I have a set of 3 beauty sites to test with, Sephora, Ulta and Nordstrom.  I was only able to advance with Sephora.  I'd likely set up a Factory type of class for the Beauty sites so that their scraping methods would be tied directly to the class instead of bloating the scraper.py file.
