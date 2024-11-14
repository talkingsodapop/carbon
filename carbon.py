import asyncio
from src import config, application, route, init

class HelloRoute(route.BaseRoute):
    def get(self):
        self.render("test")

async def main():
    server = init.create_server([
        (r"/", HelloRoute)
    ])
    server.listen(init.port, init.host)
    await asyncio.Event().wait()
if __name__ == "__main__":
    asyncio.run(main())