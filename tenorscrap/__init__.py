import json
import re
import requests
from bs4 import BeautifulSoup


class Tenor:
    url = ""
    result = ""
    base_url = "https://tenor.com"
    base_search = "/search/"
    tag = ""

    url_list = []
    result_list = []

    def __init__(self):
        pass

    class Result():
        result_list = []
        def __init__(self, result):
            self.result_list = result

        def result(self, mode: str = "dict"):
            if mode.lower() == "dict":
                return self.result_list
            elif mode.lower() == "json":
                return json.dumps(self.result_list, indent=2, sort_keys=True)

    def search(self, tag, limit: int = 3) -> list(result_list):
        tag = re.sub('[\!\@\#\$\%\^\&\*\(\)\_\-\=\+\`\~\." ]', '-', tag)
        self.tag = tag
        self.set_url()
        self.__set_result(limit)
        return self.Result(self.result_list)

    def set_url(self):
        self.base_search = f"/search/{self.tag}-gifs"
        self.url = f"{self.base_url}{self.base_search}"
        self.set_search()
    
    def set_search(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "lxml")
        self.giflist = soup.find("div", attrs={"class": "GifList"})
        return soup
    
    def __get_list_url(self) -> list(url_list):
        self.url_list.clear()
        urllist = self.giflist.find_all("a")
        [self.url_list.append(self.base_url + value.attrs["href"]) for value in urllist if "/search" not in value.attrs["href"]]
        self.__cleansing_view()
        return self.url_list

    def __get_list_gif(self) -> list:
        Gif = self.giflist.find_all("div", attrs={"class": "Gif"})
        gif = [value.findChildren("img")[0].attrs for value in Gif]
        return gif
    
    def __set_result(self, limit):
        self.result_list = []
        gif = self.__get_list_gif()
        url = self.__get_list_url()
        if limit != None:
            for idx in range(limit):
                gif[idx]["url"] = url[idx]
                self.result_list.append(gif[idx])
        else:
            for idx in range(len(gif)):
                gif[idx]["url"] = url[idx]
                self.result_list.append(gif[idx])

    def __cleansing_view(self):
        for idx, value in enumerate(self.url_list):
            if "{}/view".format(self.base_url) not in value:
                del self.url_list[idx]

    def __str__(self):
        return json.dumps(self.result_list, indent=2, sort_keys=True)

    def __call__(self):
        return json.dumps(self.result_list, indent=2, sort_keys=True)
