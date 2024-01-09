import scrapy


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    def parse(self, response):
        # '//*[@id="entry_761661"]/div[2]/h2/a' # Xpath相对路径
        # "/html/body/div[2]/div[2]/div[4]/div[1]/div[2]/h2/a" # Xpath全路径
        # Xpath的实现方式
        # 1. 通过元素id直接获取（不推荐，由于无法直接知道id的属性）
        # url = response.xpath('//*[@id="entry_761661"]/div[2]/h2/a/@href').extract_first("")
        # 2. 通过不变的属性的相对路径获取
        # url = response.xpath('//div[@id="news_list"]/div[1]/div[2]/h2/a/@href').extract_first("")
        # url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract_first("")

        # url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract()
        # 3. css选择器写法
        url = response.css('div#news_list h2 a::attr(href)').extract()
        pass
