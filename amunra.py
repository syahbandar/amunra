from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import json

class Scrapper:

    def __init__(self):
        pass

    def get_urls(self, output_file_name, query, site, number_of_pages=1):
        
        url = "https://www.detik.com/search/searchall?query={}&sortby=time&page=".format(query)
        output_file = open(output_file_name, "a")

        for page_number in range(1, number_of_pages+1):

            resp = requests.get(url+str(page_number))
            soup = BeautifulSoup(resp.content, 'html.parser')

            for a in soup.find_all('a', href=True):
                if "finance.detik.com" in a["href"]:
                    output_file.write(a["href"] + "\n")

            output_file.flush()
    
    def parse_from_url(self, output_file_name, url, count=1):
        output_file = open(output_file_name, "a")

        if count == 1:
            output_file.write("\"id\", \"url\", \"title\", \"body\", \"word_count\"\n")
            output_file.flush()

        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')

        status = True

        article= soup.find('div',{'class':'itp_bodycontent detail_text'})
        try:
            article.find('center').extract()
            article.find('div',{'class':'detail_tag'}).extract()
            article.find('script').extract()
            article.find('script').extract()
            article.find('table').extract()
        except AttributeError:
            pass
        
        try :
            line = f'"{count}"'+","+json.dumps(url)+","+json.dumps(soup.title.string.replace('"', '').replace(',', ''))+","+json.dumps(article.text.replace('"', '').replace(',', ''))+","+str(len(article.text.replace('"', '').replace('"', '')))+"\n"
            output_file.write(line)
        except AttributeError:
            status = False
            pass

        output_file.close()
        return status
    
    def parse_from_file(self, output_file_name, file_name):
        output_file = open(output_file_name, "a")
        list_of_urls = [url for url in open(file_name, "r")]

        count = 1
        for url in list_of_urls:
            if(self.parse_from_url(output_file_name, url, count)):
                count += 1


