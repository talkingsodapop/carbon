import os.path
import tornado.web

from src import config

global_template_args = {}

# The cooler RequestHandler
class BaseRoute(tornado.web.RequestHandler):
    # Render a template.
    def render(self, template_name: str, **kwargs):
        # merge global template arguments and keyword args
        template_args = {}
        template_args.update(global_template_args)
        template_args.update(kwargs)
        # # get real path to template
        # template_root = config.get_path("frontend.views", "./frontend/views")
        # template_path = os.path.join(template_root, template_name + ".html")
        # renderinate
        super().render(template_name, **template_args)
    # Return the default 404 page.
    def not_found(self):
        self.clear()
        self.set_status(404)
        self.render("errors/404")

# Default route
class NotFoundRoute(BaseRoute):
    def get(self, *a, **ka):
        self.not_found()