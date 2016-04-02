#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import json


def make_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    return soup

def print_title(soup):
    title = soup.find('h3')
    print title.get_text()

def phrases(soup):

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    for row in rows:
        data = row.find_all('td')
        english = data[0].get_text()
        other = data[1].get_text()

        yield english, other

if __name__ == '__main__':

    language = 'bulgarian'
    url = 'http://www.linguanaut.com/english_{0}.htm'.format(language)

    print "{0} and {1}".format('English', language.title())
    soup = make_soup(url)
    phrases = phrases(soup)

    phrase_list = []
    for phrase in phrases:
        if "English Greetings" not in phrase:
            eng, othr = phrase
            ditto = {"key": eng, "val": othr}
            phrase_list.append(ditto)

    print phrase_list

    # init a [{"val":"othr","key":"eng"}]

    my_dict = { "id": "{0}_cheat_sheet".format(language),
                "name": "{0} Cheat Sheet".format(language.title()),
                "metadata": { 
                    "sourceName": "Linguanaut",
                    "sourceUrl": url
                },
                   "section_order" : [
                      "Basics",
                      "Getting Help",
                      "Travelling",
                      "Etiquette",
                      "Dinner on the Town"
                    ],
                    "description": "Basic {0} words and phrases".format(language.title()),
                    "sections": {
                        "Etiquette": "list of dicts with key-value pairs",
                        "Getting Help": "etc etc",
                        "Basics": "etc etc etc",
                        "Dinner on the Town": "etc",

                    }
    }

    #print json.dumps(my_dict)






