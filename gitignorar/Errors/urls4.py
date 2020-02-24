import scrapy
class WikipediaCrawler(scrapy.Spider):
    name = "wikipedia-crawler"
    start_urls = ['https://en.wikipedia.org/wiki/Special:Random']

    def start_requests(self):
        for page_counter in range(0, 10):
            yield scrapy.Request(url='https://en.wikipedia.org/wiki/Special:Random')

    def parse(self, response):
        urls = []

        for link in response.css('a::attr(href)'):
            urls.append(link.extract())

        file_name = response.url.split("/")[-1] + '.html'
        file_name = file_name.replace(':', '_')

        with open('crawled/' + file_name, 'wb') as f:
            f.write(response.body)

        yield {
            str(response.url):
            {
                'ranking': 5,
                'links': urls
            }
        }

    def save_url(self, response):
        self.start_urls.append(response.url)
ob=WikipediaCrawler()
limbo=ob.start_requests
print(limbo)
    
