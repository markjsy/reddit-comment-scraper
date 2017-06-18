# -*- coding: utf-8 -*-
import scrapy
import re
import pprint
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest

############
# CHANGE ME#
############
reddit_url = "https://www.reddit.com/r/politics/comments/6hw8b3/six_people_have_resigned_from_trumps_hivaids/"
reddit_sub = 'politics'
path_to_output = ""

import csv

# encodes and strips tags from scraped data
def stripper(raw_html):
    cleantext = re.sub('<.*?>', '', raw_html)
    cleanertext = re.sub("\n",'', cleantext)
    cleanertext = cleanertext.encode('ascii', 'ignore').decode('ascii')
    return cleanertext

def strip_points(text):
    cleantext = ""
    if text == " points":
        cleantext = re.sub(' points', '', text)
    else:
        cleantext = re.sub(' point', '', text)
    cleantext = cleantext.encode('ascii', 'ignore').decode('ascii')
    return cleantext

class RthreadSpider(scrapy.Spider):
    name = "rthread"
    allowed_domains = ["reddit.com"]
    start_urls = ['https://www.reddit.com/r/'+reddit_sub]

    def parse(self, response):
        hdr = { 'User-Agent' : 'My Agent'}

        # lua script that clicks 'load more comments' button
        script = """
        function main(splash)
              local url = splash.args.url
              assert(splash:go(url))
              
              local elems = splash:select_all('a[onclick^="return morechildren"]')
              
              for _, e in ipairs(elems) do
                e.node.click()
                splash:wait(1)
              end

              return {
               html = splash:html(),
              }
            end
        """

        link = LinkExtractor( allow=['('+ reddit_url + ')'] )
        for link in link.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint='execute',
                headers=hdr,
                args={
                    'timeout': 10000.0,
                    'lua_source': script,
                })

    def parse_link(self, response):
        # the really hard stuff -- Xpath queries optimized for Reddit
        time_list = response.xpath('//div[@class="commentarea"]//p[@class="tagline"]/time[position()=1]/@datetime').extract()        
        score_list = response.xpath('//div[@class="commentarea"]//p[@class="tagline"]/span[contains(@class, "score") and contains(@class, "unvoted")]|//div[@class="commentarea"]//p[@class="tagline"]/span[contains(@class, "score-hidden")]|//div[@class="commentarea"]//p[@class="tagline"]/following-sibling::div//div[contains(@class, "usertext")]/div[@class="md"]').extract()
        comment_list = response.xpath('//div[@class="commentarea"]//p[@class="tagline"]/following-sibling::form//div[contains(@class, "usertext-body")]/div[@class="md"]|//div[@class="commentarea"]//p[@class="tagline"]/following-sibling::div//div[contains(@class, "usertext")]/div[@class="md"]').extract()

        # creating new lists to store cleansed text
        stripped_time = list()
        stripped_score = list()
        stripped_comment = list()

        # cleansing list
        for i in range(0, len(time_list)):
        	stripped_time.append(stripper(time_list[i]))
        	stripped_score.append(strip_points(stripper(score_list[i])))
        	stripped_comment.append(stripper(comment_list[i]))

        #######################################	
        # CHANGE ME -- DATAPIPE LINE OR OUTPUT#
        #######################################

        with open(path_to_output, 'w') as outcsv:   
            #configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['url', 'subreddit', 'date', 'score', 'comment'])
            
            for i in range(0, len(stripped_time)):
                writer.writerow([ reddit_url, reddit_sub, stripped_time[i], stripped_score[i], stripped_comment[i] ])

