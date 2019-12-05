#!/usr/bin/env python
import asyncio
import asyncio_redis
import logging


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Enable logging
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().setLevel(logging.INFO)

    def run():
        # Create a new redis connection (this will also auto reconnect)
        connection = await asyncio_redis.Connection.create('localhost', 6379)

        try:
            while True:
                # Get input (always use executor for blocking calls)
                text = await loop.run_in_executor(None, input, 'Enter message: ')

                # Publish value
                try:
                    await connection.publish('our-channel', text)
                    print('Published.')
                except asyncio_redis.Error as e:
                    print('Published failed', repr(e))

        finally:
            connection.close()

    loop.run_until_complete(run())
