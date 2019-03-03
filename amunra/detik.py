import requests
import json
import re
import os
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

class DetikScrapper:

    def __init__(self):
        pass
    
    def gather_data(self, output_file_name, query, number_of_pages=1, print_progress=True, keep_urls=False):
        output_urls_file_name = "urls_{}.txt".format(output_file_name.split(".")[0])
        self.get_urls(output_urls_file_name, query, number_of_pages, print_progress)
        self.parse_from_file(output_file_name, output_urls_file_name, print_progress)
        if keep_urls == False:
            os.remove(output_urls_file_name)

    def get_urls(self, output_file_name, query, number_of_pages=1, print_progress=True):

        url = "https://www.detik.com/search/searchall?query={}&sortby=time&page=".format(query)
        
        with open(output_file_name, "w") as output_file:

            for page_number in range(1, number_of_pages+1):

                if print_progress: 
                    print("Page Number {}".format(page_number))

                resp = requests.get(url+str(page_number))
                soup = BeautifulSoup(resp.content, 'html.parser')

                for a in soup.find_all('a', href=True):
                    if ("finance.detik.com" in a["href"]) or ("news.detik.com" in a["href"]) :
                        output_file.write(a["href"] + "\n")

                output_file.flush()
    
    def parse_from_url(self, output_file_name, url, count=1, print_progress=True):
        
        with open(output_file_name, "a") as output_file:

            if count == 1:
                output_file.write("url,title,body,word_count\n")
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
                
                url = (json.dumps(url)).replace('\\n', '')
                title = json.dumps(soup.title.string.replace('"', '').replace(',', ''))
                body = re.sub(r'[^\w\s]','', re.split(r'\(...\/...\)', json.dumps(article.text))[0].replace("\\n", "").replace("\\t", "").lower())
                word_count = len(body.split())

                line = "{},{},{},{}\n".format(url, title, body, word_count)
                output_file.write(line)

                if print_progress:
                    print("Extracted: {}".format(url.replace('\\n', '')))

            except AttributeError:
                status = False
                pass

        return status
    
    def parse_from_file(self, output_file_name, file_name, print_progress=True):
        list_of_urls = [url for url in open(file_name, "r")]

        count = 1
        for url in list_of_urls:

            self.parse_from_url(output_file_name, url, count, print_progress)
            count += 1