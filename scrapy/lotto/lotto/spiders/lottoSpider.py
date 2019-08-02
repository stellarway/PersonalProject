# -*- coding: utf-8 -*-
import scrapy


class LottospiderSpider(scrapy.Spider):
    name = 'lottoSpider'
    allowed_domains = ['dhlottery.co.kr']
    start_urls = ['https://www.dhlottery.co.kr/gameResult.do?method=byWin']

    def parse(self, response):
        lastNum = response.css('div.win_result h4 strong::text').get().replace('회','')

        url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'
        for i in range(1,lastNum+1):
            start_urls.append('{}&drwNo={}'.format(url,i))

        numList = response.css('span.ball_645::text').getall()
        yield {'lastNum' : lastNum, 'numList' : numList}
        
