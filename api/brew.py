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

        if 'by_city' in dic:
            url =  'https://api.openbrewerydb.org/breweries?by_city='
            r = requests.get(url + dic['by_city'])
            data = r.json()
            brewery = []
            for brew_data in data:
                event = brew_data["name"]
                brewery.append(event)
            message = str(brewery)
        else:
            message ="Please enter a city"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return