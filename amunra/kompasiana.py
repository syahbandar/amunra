import requests
import json
import re
import os
import csv
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class KompasianaScrapper:

    def __init__(self):
        pass
    
    def gather_data(self, output_file_name, query, number_of_pages=1, print_progress=True, keep_urls=False):
        output_urls_file_name = "urls_{}.txt".format(output_file_name.split(".")[0])
        self.get_urls(output_urls_file_name, query, number_of_pages, print_progress)
        self.parse_from_file(output_file_name, output_urls_file_name, print_progress)
        if keep_urls == False:
            os.remove(output_urls_file_name)
    
    def get_urls(self, output_file_name, query, number_of_pages=1, print_progress=True):

        url = "https://www.kompasiana.com/ajax/tag/posts?per_page=20&tags={}&page=".format(query)
        
        with open(output_file_name, "w") as output_file:

            for page_number in range(1, number_of_pages+1):

                if print_progress: 
                    print("Page Number {}".format(page_number))

                resp = requests.get(url+str(page_number))
                parsed_response = json.loads(resp.text)["data_array"]["view"]
                soup = BeautifulSoup(parsed_response, "html.parser")

                pattern = re.compile('http(s):\\/\\/(www.kompasiana.com)/(.*)\\/(.*)')
                
                urls = [a["href"] for a in soup.find_all("a", href=True)]
                urls = list(set([a for a in urls if pattern.search(a)]))

                for a in urls:
                    output_file.write(a + "\n")

                output_file.flush()
    #TODO
    def parse_from_url(self, output_file_name, url, count=1, print_progress=True):
        
        with open(output_file_name, "a") as output_file:

            writer = csv.writer(output_file, delimiter=',')

            if count == 1:
                writer.writerow(["url","title","body","word_count"])
                output_file.flush()

            s = requests.Session()
            s.mount('http://', HTTPAdapter(max_retries=Retry(total=5)))
            resp = s.get(url)
                
            soup = BeautifulSoup(resp.content, 'html.parser')

            status = True

            try :
                article = soup.find('div',{'class':'read-content'}).find_all('p')
                for a in article:
                    for div in a.find_all("div", {'class': 'title'}):
                        div.decompose()

                url = url.replace('\n', '')
                title = str(soup.title.string.replace(" - Kompasiana.com", ""))
                body = re.sub("<.*?>", "", ' '.join(map(str,article))).encode('ascii', 'ignore').decode("utf-8").replace("\n", " ").lower()
                word_count = len(body.split())

                writer.writerow([url, title, body, word_count])

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