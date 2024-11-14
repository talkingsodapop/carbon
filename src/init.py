import os
from src import application, config, route

# load config
config_path = os.environ.get("APP_CONFIG", "config.toml")
config.path_root = os.path.dirname(__file__)
if config.try_load_config("config.toml") != True:
    print("WARNING: failed to load config")

# read site branding from config
route.global_template_args["title"] = None
route.global_template_args["description"] = None
route.global_template_args["site_name"] = config.get_config("branding.site_name", "Carbon")
route.global_template_args["site_color"] = config.get_config("branding.site_color", "#90bb60")

# read server info from config
host = config.get_config("server.host", "localhost")
port = config.get_config("server.port", 4567)

# create application server
def create_server(handlers: list) -> application.Application:
    server = application.Application(
        config.get_path("frontend.views", "./frontend/views"),
        config.get_path("frontend.static", "./frontend/static"),
        config.get_path("frontend.sass", "./frontend/sass"),
        handlers
    )
    return server