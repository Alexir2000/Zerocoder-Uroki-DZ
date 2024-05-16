import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars-dz"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css("div.WdR1o")
        for divan in divans:
            yield {
                "name": divan.css("div.lsooF span::text").get(),
                "cena": divan.css("div.q5Uds span.ui-LD-ZU::text").get(),
                "url": divan.css("a").attrib["href"]
            }


