import os.path
import tornado.web
import sass

from src import route

# Route configured to compile and send SCSS stylesheets
# TODO: support for indented SASS
class SassHandler(route.BaseRoute):
    def initialize(self, path):
        self.path = path
    def get(self, path: str):
        path = os.path.join(self.path, path + ".scss")
        if "_" in path or not os.path.isfile(path):
            self.not_found()
        else:
            self.write(sass.compile(filename=path))
            self.set_header("Content-Type", "text/css")