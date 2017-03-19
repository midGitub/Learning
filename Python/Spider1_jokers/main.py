import jokesSpider
import config

spider=jokesSpider.jokespider(config.url,config.url_agent,config.pattern)
spider.start()