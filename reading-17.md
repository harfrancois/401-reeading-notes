# Web Scrape

source - https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/
Web scraping is a technique to automatically access and extract large amounts of information from a website, 
which can save a huge amount of time and effort.

Important notes about web scraping:
Read through the website’s Terms and Conditions to understand how you can legally use the data. Most sites prohibit 
you from using the data for commercial purposes.

Make sure you are not downloading data at too rapid a rate because this may break the website. You may potentially be 
blocked from the site as well.

Web scraping is a task that has to be performed responsibly so that it does not have a detrimental effect on the sites 
being scraped. Web Crawlers can retrieve data much quicker, in greater depth than humans, so bad scraping practices 
can have some impact on the performance of the site. While most websites may not have anti-scraping mechanisms, some 
sites use measures that can lead to web scraping getting blocked, because they do not believe in open data access.

If a crawler performs multiple requests per second and downloads large files, an under-powered server would have a 
hard time keeping up with requests from multiple crawlers. Since web crawlers, scrapers or spiders 
(words used interchangeably) don’t really drive human website traffic and seemingly affect the performance of the 
site, some site administrators do not like spiders and try to block their access.

Web spiders should ideally follow the robot.txt file for a website while scraping.

Scraping too fast and too many pages, faster than a human ever can

Following the same pattern while crawling. For example – go through all pages of search results, and go to each 
result only after grabbing links to them. No human ever does that.

Too many requests from the same IP address in a very short time

Not identifying as a popular browser. You can do this by specifying a ‘User-Agent’.

using a user agent string of a very old browser

Web scraping bots fetch data very fast, but it is easy for a site to detect your scraper, as humans cannot browse that 
fast. The faster you crawl, the worse it is for everyone. If a website gets too many requests than it can handle it 
might become unresponsive.

Do not follow the same crawling pattern
Humans generally will not perform repetitive tasks as they browse through a site with random actions.

Make requests through Proxies and rotate them as needed
When scraping, your IP address can be seen. A site will know what you are doing and if you are collecting data.
