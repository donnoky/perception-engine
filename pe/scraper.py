from lxml import html
from random import randint
import requests
import json
import urllib2
import time

output = open('articles.csv', 'a')
readLog = open('cars.log', 'r')
processedLog = readLog.readlines();
print processedLog
readLog.close()
carlog = open('cars.log', 'a')

homePage = requests.get('http://www.caranddriver.com/reviews')
tree = html.fromstring(homePage .content)
makeIds = tree.xpath('//select[@name="make"]/option/@value')

for makeId in makeIds:
    if makeId:
        data = json.load(urllib2.urlopen('http://www.caranddriver.com/api/vehicles/models-by-make/' + makeId + '/json'))
        make = data["vehicles"]["make"]
        models = data["vehicles"]["models"]

# print json.dumps(data, indent=4, sort_keys=True);
        for model in models:
            url = make["url_alias"] + "/" + model["url_alias"]
            page = requests.get('http://www.caranddriver.com/list-reviews/' + url)
            tree = html.fromstring(page.content)
            reviews = tree.xpath('//div[@class="feature-listings"]/div[starts-with(@id, "feature-listing-item-")]//a[@class="hed"]/@href')
            for reviewURL in reviews:
                if reviewURL in processedLog:
                    print "skipping " + reviewURL
                else: 
                    page = requests.get('http://www.caranddriver.com' + reviewURL)
                    tree = html.fromstring(page.content)
                    title = tree.xpath('//h1[@class="article-title" or @class="model-name"]/text()')
                    body = tree.xpath('//div[@class="article-body--text" or @id="fullreview"]')
                    if title and body:
                        article = ""
                        for line in body:
                            article += html.tostring(line).replace('\n', ' ').replace('\r', '') + " "
                        lineItem = [make['name'], model['name'], reviewURL, title[0], article]
                        print reviewURL
                        output.write('%s\n' % (','.join(lineItem)))
                        carlog.write('%s' % (reviewURL))
                    time.sleep(randint(0,29));
output.close()
carlog.close()