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

        if 'month' in dic and 'day' in dic:
            url =  'https://today.zenquotes.io/api/'
            final = (url + dic['month']+'/'+dic['day'])
            r = requests.get(url + dic['month']+'/'+dic['day'])
            data = r.json()
            today = []
            for today_data in data:
                event = today_data['data'][0]['Events'][0]['text']
                birth = today_data['data'][0]['Births'][0]['text']
                death = today_data['data'][0]['Deaths'][0]['text']
                today.append(event)
                today.append(birth)
                today.append(death)
            message = str(final)
        else:
            message ="Please enter a month and day"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return