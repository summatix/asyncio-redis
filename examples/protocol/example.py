#!/usr/bin/env python
"""
Simple example that sets a key, and retrieves it again.
"""
import asyncio
from asyncio_redis import RedisProtocol

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    def run():
        # Create connection
        transport, protocol = await loop.create_connection(RedisProtocol, 'localhost', 6379)

        # Set a key
        await protocol.set('key', 'value')

        # Retrieve a key
        result = await protocol.get('key')

        # Print result
        print ('Succeeded', result == 'value')

        transport.close()

    loop.run_until_complete(run())
