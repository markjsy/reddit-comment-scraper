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
  2. Change *reddit_url* , *reddit_sub* and *output_path* at the top
  3. (Optional) Change the bottom to pipeline to your database. [Default ouput CSV]
  4. Run on command line:
  ```
  scrapy crawl rthread
  ```
  
## Advance Usage
  * The *reddit_url* variable can use regular expressions to scrape comments. Example:
  ```
  reddit_url = "reddit/r/politics/comments/w+\/w+"
  subreddit = "/r/politics"
  ```
  This will use https://www.reddit.com/r/politics as the starting point for the Scrapy spider, and it will look for every link that has the pattern https://www.reddit.com/r/politics/comments/sometext/sometext. This will allow you to scrape every single comment thread on the first page of */r/politics*
  
