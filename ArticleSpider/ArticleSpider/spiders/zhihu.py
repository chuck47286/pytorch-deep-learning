import scrapy
from ArticleSpider.utils import zhihu_login_sel
from ArticleSpider.settings import USER, PASSWORD


class ZhihuSpider(scrapy.Spider):
    """
        jobbole: 快速学习scrapy的各个组件
        zhihu: 模拟登录  验证码（英文，数字，倒立文字点击）， 滑动验证码
        lagou: scrapy 中的 crawlspider(全站拉取)，以后不再讲解crawlspider（优点：框架封装完整，书写代码较少； 缺点：不够灵活）
        模拟登录的难度UP
        1.识别出chromedriver
        2.加验证码
        解析和分析请求几乎没有变
    """
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ["https://www.zhihu.com/"]
    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def start_requests(self):
        #模拟登录拿到cookie
        # 两种滑动验证码识别方案：1.使用opencv识别 2.使用机器学习方法识别
        l = zhihu_login_sel.Login(USER, PASSWORD, 6)
        cookie_dict = l.login()
        for url in self.start_urls:
            # 将cookie交给scrapy
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            yield scrapy.Request(url, cookies=cookie_dict, headers=headers, dont_filter=True)

    def parse(self, response, **kwargs):
        pass

    def parse_detail(self, response):
        pass

    def parse_num(self, response):
        pass