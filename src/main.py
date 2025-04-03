<<<<<<< Updated upstream
from src.heroes_generator import HeroesGenerator
from src.tournamnet import Fight



def main():
    generator = HeroesGenerator()
    heroes = generator.get_heroes(2)


    fight = Fight()
    fight.tournament(heroes)

main()
=======
import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK


from src.heroes_generator import HeroesGenerator
from src.tournamnet import Fight

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def hello(websocket):
    while True:
        try:
            message = await websocket.recv()
        except ConnectionClosedOK:
            break
        print(message)

async def main():
    generator = HeroesGenerator()
    heroes = generator.get_heroes(2)
    fight = Fight()
    fight.tournament(heroes)

    async with serve(hello, "localhost", 8765) as server:
        await server.serve_forever()


asyncio.run(main())
>>>>>>> Stashed changes
