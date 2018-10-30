#  Scrapy beyond the first steps - Eugenio Lacuesta

*The following is the proposal I submitted for the talk. I had to remove some topics because I had not enough time :-)*

Scrapy is the most popular web scraping / web crawling framework out there. It provides several out-of-the box configurable features for the most common needs for web crawlers in general. 

However, when your project starts growing up, you will feel the need to tailor Scrapy further to your needs. You'll need to create custom request/response processors, data validators, etc.

In this talk you will learn how to take the best out of Scrapy in terms of design by taking advantage of built-in components like signals and extensions to respond to events that happen during the crawl.

We will also cover how to plug functionality into Scrapy by using a few additional components like:
- spider middlewares (customize resources going in and out of spiders, like requests, responses and scraped items)
- downloader middlewares (customize Scrapy's request/response processing)
- item exporters (serialize the extracted data into files)
- item pipelines (custom post processing/validation of extracted items)


### Code and slides

The final version of this presentation is available [here](presentation_v3.1.pdf)

The Scrapy project in which the talk is based can be found at https://github.com/elacuesta/scrapy-beyond-first-steps, along with some older presentations.


### Acknowledgments

Thanks to [Valdir](https://github.com/stummjr) and [Raphael](https://github.com/raphapassini) for their encouragement and comments!