from urllib import parse
import re
import json

import scrapy
from scrapy import Request
import requests
import undetected_chromedriver

from ArticleSpider.utils import common
from ArticleSpider.items import JobBoleArticleItem


def process_image_url(url):
    if url.startswith('//'):
        return 'https:' + url  # 或者 'http:' 根据需要选择
    return url


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    # 手动登录拿到cookie,并放入到scrapy,降低难度
    # 1. simple case cnblogs这个网站
    # 2. 知乎 关键
    # 3. 拉钩 反扒 导致crawlspider 用处不大

    def start_requests(self):
        # 入口可以模拟登录拿到cookie, selenium控制浏览器会被一些网站识别出来
        # import undetected_chromedriver as uc
        # browser = uc.Chrome(headless=True, use_subprocess=False)
        # browser.get('https://account.cnblogs.com/signin')
        import undetected_chromedriver as uc
        browser = uc.Chrome(use_subprocess=True)
        browser.get("https://account.cnblogs.com/signin")
        # 自动化输入，自动化识别滑动验证码并拖动整个自动化过程
        input("回车继续：")
        cookies = browser.get_cookies()  # 要先获取到cookies 才可以关模拟器
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']

        for url in self.start_urls:
            # 将cookie交给scrapy
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers, dont_filter=True)

    # 模拟不使用手动获取cookie，会出现什么异常
    # 2024-01-09 15:52:25 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (302) to <GET https://account.cnblogs.com:443/signin?ReturnUrl=https%3A%2F%2Fnews.cnblogs.com%2Fn%2F761849%2F> from <GET https://news.cnblogs.com/n/761849/>
    # 抛出异常会重定向到登录页面
    # def start_requests(self):
    #     # # 入口可以模拟登录拿到cookie, selenium控制浏览器会被一些网站识别出来
    #     # import undetected_chromedriver as uc
    #     # browser = uc.Chrome(headless=True, use_subprocess=False)
    #     # browser.get('https://account.cnblogs.com/signin')
    #     # # 自动化输入，自动化识别滑动验证码并拖动整个自动化过程
    #     # input("回车继续：")
    #     # cookies = browser.get_cookies()
    #     # cookie_dict = {}
    #     # for cookie in cookies:
    #     #     cookie_dict[cookie['name']] = cookie['value']
    #
    #     for url in self.start_urls:
    #         # 将cookie交给scrapy
    #         headers = {
    #             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    #         }
    #         yield scrapy.Request("https://news.cnblogs.com/n/761849/", headers=headers, dont_filter=True)

    def parse(self, response):
        """
        1. 获取新闻列表中的新闻url 并交给scrapy进行下载后调用相应的解析方法
        2. 获取下一页的url并交给scrapy进行下载，下载完成后交给parse继续跟进
        :param response:
        :return:
        """
        post_nodes = response.css('#news_list .news_block')[:1]
        for post_node in post_nodes:
            image_url = process_image_url(post_node.css('.entry_summary a img::attr(src)').extract_first(''))
            post_url = post_node.css('h2 a::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        # next_url = response.css('dev.pager a::last-child::text').extract_first('')
        # next_url = response.xpath('//a[contains(text(), "Next >")]/@href').extract_first('')
        # yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        match_re = re.match(".*?(\d+)", response.url)
        if match_re:
            article_item = JobBoleArticleItem()
            # title = response.css("#news_title a::text").extract_first("")
            title = response.xpath("//*[@id='news_title']//a/text()").extract_first("")
            # create_date = response.css("#news_info .time::text").extract_first("")
            create_date = response.xpath("//*[@id='news_info']//*[@class='time']/text()").extract_first("")
            # match_re = re.match(".*?(\d+.*)", create_date)
            # if match_re:
            #     create_date = match_re.group(1)

            # content = response.css("#news_content").extract()[0]
            content = response.xpath('//*[@id="news_body"]//p/text()').extract()[0]  # 直接从网页上获取XPATH
            # tag_list = response.css(".news_tags a::text").extract()
            tag_list = response.xpath("//*[@class='news_tags']//a/text()").extract()
            tags = ",".join(tag_list)

            # Ajax中获取数据
            post_id = match_re.group(1)
            # html = requests.get(url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)))
            # j_data = json.loads(html.text)

            article_item['title'] = title
            article_item['create_date'] = create_date
            article_item['content'] = content
            article_item['tags'] = tags
            article_item['url'] = response.url
            article_item['front_image_url'] = [response.meta.get("front_image_url", "")]

            yield Request(url=parse.urljoin(response.url, "/NewsAjax/GetAjaxNewsInfo?contentId={}".format(post_id)),
                          meta={"article_item": article_item}, callback=self.parse_num)

            # praise_num = j_data["DiggCount"]
            # fav_nums = j_data["TotalView"]
            # comment_nums = j_data["CommentCount"]

    def parse_num(self, response):
        j_data = json.loads(response.text)
        article_item = response.meta.get("article_item", "")

        praise_num = j_data["DiggCount"]
        fav_nums = j_data["TotalView"]
        comment_nums = j_data["CommentCount"]

        article_item['praise_nums'] = praise_num
        article_item['fav_nums'] = fav_nums
        article_item['comment_nums'] = comment_nums

        article_item['url_object_id'] = common.get_md5(article_item['url'])

        yield article_item
        pass
