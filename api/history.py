from http.server import BaseHTTPRequestHandler
from typing import final
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'by_postal' in dic:
            url =  'https://api.openbrewerydb.org/breweries?'
            r = requests.get(url + dic['by_postal'])
            data = r.json()
            brewery = []
            for brew_data in data:
                event = brew_data[0]
                # birth = today_data['data'][0]['Births'][0]['text']
                # death = today_data['data'][0]['Deaths'][0]['text']
                brewery.append(event)
                # today.append(birth)
                # today.append(death)
            message = str(brewery)
        else:
            message ="Please enter a month and day"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return