import scrapy

class Bbhot100spider(scrapy.Spider):
    name = "bbhot100"
    start_urls = ["https://www.billboard.com/charts/hot-100"]

    def parse(self, response):
        rank = response.css('span.chart-element__rank__number::text').getall()
        title = response.css('span.chart-element__information__song::text').getall()
        artist = response.css('span.chart-element__information__artist::text').getall()
        meta = response.css('li.chart-list__element')

        for i in range(len(rank)):

            yield {
                'Rank': rank[i],
                'Song Title': title[i],
                'Artist': artist[i],
                'Previous Week Rank': meta[i].css('span.chart-element__meta::text')[0].getall(),
                'Peak Position': meta[i].css('span.chart-element__meta::text')[1].getall(),
                '# of Weeks': meta[i].css('span.chart-element__meta::text')[2].getall()
            }
