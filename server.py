import tornado
from tornado.web import Application
from tornado import ioloop

from apis_handler import CreateTask, GetUsersList, GetWorkItem, GetUser


class MyServer(Application):
    def __init__(self):
        handler = self.GetHandler()
        Application.__init__(self, handler)

    def GetHandler(self):
        handler = [
            (r'/create-task', CreateTask),
            (r'/get-users-list', GetUsersList),
            (r'/workitem', GetWorkItem),
            (r'/get-user', GetUser)
        ]

        return handler

    def start_server(self):
        self.listen(8089)
        print("Port running at 8089")
        tornado.ioloop.IOLoop.current().start()

