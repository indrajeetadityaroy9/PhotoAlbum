import sys
import urllib
import json

sys.tracebacklimit = 0

from pip._vendor.distlib.compat import raw_input

serviceurl = "https://jsonplaceholder.typicode.com/photos?"

while True:
    ia = raw_input("> photo-album: ")

    if ia == 'exit':
        sys.exit()

    if ia.isnumeric():
        try:
            url = serviceurl + urllib.parse.urlencode({"albumId": ia})
            uh = urllib.request.urlopen(url)
            data = uh.read()

            try:
                js = json.loads(data)
            except:
                js = None

            i = 0
            while i < 50:
                print("[{}] {} \n".format(js[i]['id'], js[i]['title']))
                i += 1
        except IndexError:
            continue




