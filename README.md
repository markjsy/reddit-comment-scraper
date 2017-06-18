# reddit-comment-scraper
Fast reddit comment scraper. Handles dynamic comment loading.

## Output
  * comment date (UTC format)
  * comment text
  * upvote score
  * subreddit
  * url

## Installation
  1. Follow docker installation at: http://splash.readthedocs.io/en/stable/install.html
  2. Follow scrapy installation at: https://doc.scrapy.org/en/latest/intro/install.html
  3. Run on command line:
  ```
  pip install scrapy-splash
  ```
  4. Run on command line:
  ```
  docker run -p 8050:8050 scrapinghub/splash
  ```
  
## How to run
  1. Go into spiders folder and edit *rthread.py* 
  2. Change *reddit_url* and *reddit_sub* at the top
  3. Change the bottom to your data pipeline or output to desired format
  

  
