import requests
import os
import time
from  bs4 import BeautifulSoup

session = requests.session()

response = session.get("https://facebook.com")

response = session.post("https://www.facebook.com/login.php?login_attempt=1&lwv=110", data={
    'email': '',
    'pass': ''

}, allow_redirects=False)



if 'c_user' in response.cookies:

    while True:
        homepage_resp = session.get("https://www.facebook.com/home.php")
        hp = homepage_resp.text
        pretty = BeautifulSoup(hp,'lxml')
        benachrichtung = pretty.find('div',{'class': 'uiToggle _4962 _1z4y _330i _4kgv hasNew'})

        # print(benachrichtung)
        # print (type(benachrichtung))

        if benachrichtung != None:
            os.system("play " + os.path.dirname(os.path.realpath(__file__)) + "/light.mp3 -q")
            print("imas poruku")
            time.sleep(10)

        # print(pretty)