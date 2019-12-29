import asyncio

async def print_numbers_async1(n, prefix):
    for i in range(n):
        print(prefix, i)

async def print_numbers_async2(n, prefix):
    for i in range(n):
        print(prefix, i)
        if i % 5 == 0:
            await asyncio.sleep(0)

loop1 = asyncio.new_event_loop()
count1_1 = loop1.create_task(print_numbers_async1(10, 'c1_1'))
count2_1 = loop1.create_task(print_numbers_async1(10, 'c2_1'))
loop1.run_until_complete(asyncio.wait([count1_1, count2_1]))
loop1.close()

loop2 = asyncio.new_event_loop()
count1_2 = loop2.create_task(print_numbers_async1(10, 'c1_2'))
count2_2 = loop2.create_task(print_numbers_async1(10, 'c2_2'))
loop2.run_until_complete(asyncio.wait([count1_2, count2_2]))
loop2.close()