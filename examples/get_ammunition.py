import tvc
import asyncio

from tvc import Ammunition
from typing import List

TOKEN: str = 'blahblah some token string'

client = tvc.TVCClient(token=TOKEN)


async def main():
    ammunition: List[Ammunition] = await client.fetch_ammunition('7.62x39mm BP gzh')

    if not ammunition:
        # fetch result can be return empty list.
        # If the list of ammunition what responded to is empty.
        print('Can not found ammunition!')
        return

    for ammo in ammunition:
        print(f"Name: {ammo}")

    # Returns all entries if you do not insert a query into the fetch function argument.
    ammunition: List[Ammunition] = await client.fetch_ammunition()

    for ammo in ammunition:
        print(f"Name: {ammo}")

if __name__ == '__main__':
    client.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
