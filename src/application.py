import tornado.web

from src import route, loader, sassnado

class Application(tornado.web.Application):
    def __init__(self, template_path, static_path, sass_path, handlers):
        # register default handlers for static files and SASS styles while we're at it
        handlers.append(( r"/static/(.+)", tornado.web.StaticFileHandler, {"path": static_path} ))
        handlers.append(( r"/style/(.+).css", sassnado.SassHandler, {"path": sass_path} ))
        handlers.append(( r"/(.*)", route.NotFoundRoute ))
        super().__init__(handlers)
        # initialize custom template loader
        self.settings["template_loader"] = loader.ViewLoader(template_path)