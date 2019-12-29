import asyncio
import math
import random

async def is_prime(n):
    if n < 2:
        return True
    for i in range(2, n):
        # allow event_loop to run other coroutine
        await asyncio.sleep(0)
        if n % i == 0:
            return False
    return True

async def prime_generator(n_prime):
    counter = 0
    n = 0
    while counter < n_prime:
        n += 1
        # wait for is_prime to finish
        prime = await is_prime(n)
        if prime:
            yield n
            counter += 1

async def check_email(limit):
    for i in range(limit):
        if random.random() > 0.8:
            print('1 new email')
        else:
            print('0 new email')
        await asyncio.sleep(2)

async def print_prime(n):
    async for prime in prime_generator(n):
        print('new prime number found:', prime)

def main():
    loop = asyncio.new_event_loop()
    prime = loop.create_task(print_prime(3000))
    email = loop.create_task(check_email(10))
    loop.run_until_complete(asyncio.wait([prime, email]))
    loop.close()

main()