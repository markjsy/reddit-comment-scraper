# reddit-comment-scraper
Fast asynchronous reddit comment scraper. Handles dynamic comment loading.


## Installation
  1. Follow docker installation at: http://splash.readthedocs.io/en/stable/install.html
  2. Follow scrapy installation at: https://doc.scrapy.org/en/latest/intro/install.html
  3. Run on command line:
  ```
  pip install scrapy-splash
  ```
  4. Run on command line:
  ```
  docker run -p 8050:8050 scrapinghub/splash --max-timeout 10000
  ```
  
## Use
  1. Go into spiders folder and edit *rthread.py* 
  2. Change *reddit_url* and *reddit_sub* at the top
  3. Change the bottom to your data pipeline or output to desired format (Default is CSV)
  4. Run on command line:
  ```
  scrapy crawl rthread
  ```
  

  
