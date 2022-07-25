tarkov-changes.py
=======================

.. image:: https://img.shields.io/pypi/v/tarkov-changes.py?color=ffd242&logo=pypi&logoColor=ffffff&style=for-the-badge
    :alt: PyPI
    :target: https://pypi.org/project/tarkov-changes.py/
.. image:: https://img.shields.io/github/v/release/Hostagen/tarkov-changes.py?include_prereleases&logo=github&style=for-the-badge
    :alt: GitHub release (latest by date including pre-releases)
    :target: https://github.com/Hostagen/tarkov-changes.py/releases

A Wrapper for the `Tarkov Changes <https://tarkov-changes.com/changes>`_ API.

Quick Examples
---------------

Basic use with use client
'''''''''''''''''''''''''''

.. code:: py

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
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()


Simple to use without client declaration
'''''''''''''''''''''''''''''''''''''''''

.. code:: py

    import asyncio

    from tvc import Ammunition, TVCClient
    from typing import List

    TOKEN: str = 'blahblah some token string'


    async def main():

        async with TVCClient(TOKEN) as api:
            ammunition: List[Ammunition] = await api.fetch_ammunition('7.62x39mm BP gzh')

            if not ammunition:
                # fetch result can be return empty list.
                # If the list of ammunition what responded to is empty.
                print('Can not found ammunition!')
                return

            for ammo in ammunition:
                print(f"Name: {ammo}")

            # Returns all entries if you do not insert a query into the fetch function argument.
            ammunition: List[Ammunition] = await api.fetch_ammunition()

            for ammo in ammunition:
                print(f"Name: {ammo}")

        # When you exit the `async with` syntax, aiohttp.ClientSession is automatically and securely terminated.
        # When you use the `async with` with again, a new aiohttp.ClientSession is created again.

        async with TVCClient(TOKEN) as api:
            ...

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()

View more examples
---------------------------------------------------------
`Click here! <https://github.com/Hostagen/tarkov-changes.py/tree/master/examples>`_
