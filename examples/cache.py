import tvc
import asyncio

from tvc import Ammunition
from typing import List

TOKEN: str = 'blahblah some token string'

client = tvc.TVCClient(token=TOKEN)


async def main():
    ammunition: List[Ammunition] = client.ammunition

    for ammo in ammunition:
        print(f"Name: {ammo}")

if __name__ == '__main__':
    # Use the pre-cache `start` function to use something like client.armors, client.ammunition, etc.
    # If you're not going to use this property, you don't have to call this.
    # If you are not using this function, see the link example below
    # https://github.com/Hostagen/tarkov-changes.py/blob/master/examples/get_ammunition.py
    client.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
