import requests
from bs4 import BeautifulSoup as bs

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup()

from limitedframes.models import Lifefourcut

def parse_lifefourcut():
    result = []
    pagenames = ["Frame01","multi","Frame03","58","81","82"]
    for pagename in pagenames:
        print(pagename)
        url = "https://lifefourcuts.com/"+pagename
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        lifeitems = soup.select(".item_gallary")

        for lifeitem in lifeitems:
                lifephoto = lifeitem.select_one(".img-responsive").get("data-original")
                if pagename != '82':
                    lifecontext = lifeitem.select_one(".body").text
                else:
                    lifecontext = lifeitem.select_one(".title").text
                lifeid = lifephoto.split('/')[-1]

                item_obj = {
                    'lifephotourl': lifephoto,
                    'lifecontext': lifecontext,
                    'lifeid': lifeid,
                    'lifepagename': pagename,
                }
                print(lifecontext)
                result.append(item_obj)

    return result

if __name__ == '__main__':
    parse_lifefourcut()

def add_new_items(crawled_items):
    last_inserted_items = Lifefourcut.objects.last()
    if last_inserted_items is None:
        last_inserted_specific_id = ""
    else:
        last_inserted_specific_id = getattr(last_inserted_items, 'lifeid')

    items_to_insert_into_db = []
    for item in crawled_items:
        if item['lifeid'] == last_inserted_specific_id:
            break
        items_to_insert_into_db.append(item)
    items_to_insert_into_db.reverse()

    for item in items_to_insert_into_db:
        print("new item added!! : " + item['lifecontext'])

        Lifefourcut(lifephotourl=item['lifephotourl'],
                  lifecontext=item['lifecontext'],
                  lifeid=item['lifeid'],
                  lifepagename = item['lifepagename']).save()

    return items_to_insert_into_db

if __name__ == '__main__':
# fetch_latest_data()
    add_new_items(parse_lifefourcut())