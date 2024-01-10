import scrapy
import undetected_chromedriver


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
        import undetected_chromedriver as uc
        browser = uc.Chrome(headless=True, use_subprocess=False)
        browser.get('https://account.cnblogs.com/signin')
        # 自动化输入，自动化识别滑动验证码并拖动整个自动化过程
        input("回车继续：")
        cookies = browser.get_cookies()
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']

        for url in self.start_urls:
            # 将cookie交给scrapy
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
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
