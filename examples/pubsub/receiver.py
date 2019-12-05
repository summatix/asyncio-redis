#!/usr/bin/env python
import asyncio
import logging
import asyncio_redis

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Enable logging
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().setLevel(logging.INFO)

    def run():
        # Create a new redis connection (this will also auto reconnect)
        connection = await asyncio_redis.Connection.create('localhost', 6379)

        try:
            # Subscribe to a channel.
            subscriber = await connection.start_subscribe()
            await subscriber.subscribe([ 'our-channel' ])

            # Print published values in a while/true loop.
            while True:
                reply = await subscriber.next_published()
                print('Received: ', repr(reply.value), 'on channel', reply.channel)

        finally:
            connection.close()

    loop.run_until_complete(run())
