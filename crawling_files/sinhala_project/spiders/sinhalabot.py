# -*- coding: utf-8 -*-
import scrapy


class SinhalabotSpider(scrapy.Spider):
    name = 'sinhalabot'
    allowed_domains = ['https://www.bbc.com/sinhala/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53']
    start_urls = ['https://www.bbc.com/sinhala/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53']

    def parse(self, response):
        #Extracting the content using css selectors
        title = response.css("span.title-link__title-text::text").extract()
        summary = response.css("p.eagle-item__summary::text").extract()
        date = response.css("ul.mini-info-list li.mini-info-list__item div::text").extract()
       
        #Give the extracted content row wise
        for item in zip(title, summary, date):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0].strip(),
                'summary' : item[1].strip(),
                'date' : item[2].strip()
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
			
