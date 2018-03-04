import scrapy


class Test(scrapy.Spider):
    name = "test"   #爬虫名字，执行时使用scrapy crawl [name]
    # start_urls是我们准备爬的初始页
    start_urls = [
        "http://bj.ganji.com/fang1/chaoyang",
    ]
    print("this process not be in crawl")

    def parse(self, response):
        print("begin to run crawl")
        print(response)
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd/a/text()").extract()
        price_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for title, price in zip(title_list, price_list):
            print(title, ":", price)