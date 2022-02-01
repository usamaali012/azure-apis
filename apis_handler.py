import json
from abc import ABC

import requests
import tornado.escape
from tornado.httputil import HTTPHeaders
from tornado.web import RequestHandler
from tornado.httpclient import HTTPRequest, AsyncHTTPClient

organization = 'fnawaz'
organization_url = 'https://dev.azure.com/fnawaz'
project = 'CHI Development'


# type_ = 'task'
# url = f'{organization_url}/{project}/_apis/wit/workitems/${type_}?api-version=5.1'
types = ['task', 'user story']


class CreateTask(RequestHandler):
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        content_type = self.request.headers['Content-Type']
        pat = self.request.headers['Authorization'].split(' ')[1]

        headers = HTTPHeaders({'Content-Type': content_type})

        type_ = data[0]['type']
        url = f'{organization_url}/{project}/_apis/wit/workitems/${type_}?api-version=5.1'

        req = requests.post(url=url,
                            json=data,
                            headers=headers,
                            auth=('', pat)
                            )

        data = req.json()

        print(data)

        json_object = json.dumps(data, indent=4)
        json_file = open('response.json', 'w')
        json_file.write(json_object)

        # req = HTTPRequest(url=url,
        #                   method='POST',
        #                   headers=headers,
        #                   body=json.dumps(data)
        #                   )
        #
        # http_client = AsyncHTTPClient()
        # response = await http_client.fetch(request=req, raise_error=True)
        # print(response)


class GetUsersList(RequestHandler):
    def get(self):
        content_type = self.request.headers['Content-Type']
        headers = HTTPHeaders({'Content-Type': content_type})
        pat = self.request.headers['Authorization'].split(' ')[1]

        url = f'https://vssps.dev.azure.com/{organization}/_apis/graph/users?api-version=6.0-preview.1'

        req = requests.get(url=url,
                           headers=headers,
                           auth=('', pat)
                           )

        data = req.json()
        print(data)

        json_object = json.dumps(data, indent=4)
        json_file = open('users.json', 'w')
        json_file.write(json_object)


class GetUser(RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        userDescriptor = data['user_descriptor']

        content_type = self.request.headers['Content-Type']
        headers = HTTPHeaders({'Content-Type': content_type})
        pat = self.request.headers['Authorization'].split(' ')[1]

        url = f'https://vssps.dev.azure.com/{organization}/_apis/graph/users/{userDescriptor}?api-version=6.0-preview.1'

        req = requests.get(url=url,
                           headers=headers,
                           auth=('', pat)
                           )

        data = req.json()
        print(data)

        json_object = json.dumps(data, indent=4)
        json_file = open('one_user.json', 'w')
        json_file.write(json_object)


class GetWorkItem(RequestHandler):
    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        id = data['id']
        content_type = self.request.headers['Content-Type']
        headers = HTTPHeaders({'Content-Type': content_type})
        pat = self.request.headers['Authorization'].split(' ')[1]

        url = f'{organization_url}/{project}/_apis/wit/workitems/{id}?api-version=6.0'

        req = requests.get(url=url,
                           headers=headers,
                           auth=('', pat)
                           )

        data = req.json()
        print(data)

        json_object = json.dumps(data, indent=4)
        json_file = open('workitem.json', 'w')
        json_file.write(json_object)
