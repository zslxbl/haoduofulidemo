from scrapy.spiders import CrawlSpider, Rule, Request ##CrawlSpider与Rule配合使用可以骑到历遍全站的作用、Request干啥的我就不解释了
from scrapy.linkextractors import LinkExtractor ##配合Rule进行URL规则匹配
from haoduofuli.items import HaoduofuliItem ##不解释
from scrapy import FormRequest ##Scrapy中用作登录使用的一个包



account = '你的帐号'
password = '你的密码'

class myspider(CrawlSpider):

    name = 'haoduofuli'
    allowed_domains = ['haoduofuli.wang']
    start_urls = ['http://www.haoduofuli.wang/wp-login.php']

    def parse_start_url(self, response):
        ###
        # 如果你登录的有验证码之类的，你就可以在此处加入各种处理方法；
        # 比如提交给打码平台，或者自己手动输入、再或者pil处理之类的
        ###
        formdate = {
                'log': account,
                'pwd': password,
                'rememberme': "forever",
                'wp-submit': "登录",
                'redirect_to': "http://www.haoduofuli.wang/wp-admin/",
                'testcookie': "1"
         }
        return [FormRequest.from_response(response, formdata=formdate, callback=self.after_login)]


    def after_login(self, response):
        ###
        # 可以在此处加上判断来确认是否登录成功、进行其他动作。
        ###
        lnk = 'http://www.haoduofuli.wang'
        return Request(lnk)

    rules = (
        Rule(LinkExtractor(allow=('\.html',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HaoduofuliItem()
        try:
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/font/text()').extract()[0]
            return item
        except:
            item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/span[2]/a/text()').extract()[0]
            item['title'] = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()[0]
            item['imgurl'] = response.xpath('//*[@id="post_content"]/p/img/@src').extract()
            item['yunlink'] = response.xpath('//*[@id="post_content"]/blockquote/p/a/@href').extract()[0]
            item['password'] = response.xpath('//*[@id="post_content"]/blockquote/p/span/text()').extract()[0] 
            return item