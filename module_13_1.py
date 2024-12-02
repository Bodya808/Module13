import asyncio


async def delay(power, message):
    await asyncio.sleep(5 / power)
    print(message)


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(5):
        task = asyncio.create_task(delay(power, f'Силач {name} поднял {i + 1} шар.'))
        await task

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = []

    names = ['Pasha', 'Denis', 'Apollon']
    powers = [3, 4, 5]

    for name, power in zip(names, powers):
        tasks.append(start_strongman(name, power))

    await asyncio.gather(*tasks)


asyncio.run(start_tournament())
