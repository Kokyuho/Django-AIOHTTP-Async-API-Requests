import asyncio
import time

import aiohttp
import requests
from django.shortcuts import render


# Test urls overview
def index(request):

    urls = [
        '/normalRequests',
        '/aiohttpRequests',
        '/asyncRequests'
    ]

    descriptions = [
        'regular loading with syncronous requests.get() [slow]',
        'syncronous loading with aiohttp ClientSession() [faster]',
        'asyncronous loading firing all requests at once with asyncio [fastest]'
    ]

    zipped = list(zip(urls, descriptions))

    return render(
        request,
        "index.html",
        {"zipped": zipped},
    )


# Test view regular loading with syncronous requests.get() [slow]
def test_normal_requests(request):

    starting_time = time.time()

    pokemon_data = []

    for num in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        res = requests.get(url)
        pokemon = res.json()
        pokemon_data.append(pokemon["name"])

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "test.html",
        {"data": pokemon_data, "count": count, "time": total_time},
    )


# Test view syncronous loading with aiohttp ClientSession() [faster]
async def test_aiohttp_requests(request):

    starting_time = time.time()

    pokemon_data = []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            async with session.get(pokemon_url) as res:
                pokemon = await res.json()
                pokemon_data.append(pokemon["name"])

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "test.html",
        {"data": pokemon_data, "count": count, "time": total_time},
    )


# Get pokemon helper function
async def get_pokemon(session, url):
    async with session.get(url) as res:
        pokemon_data = await res.json()
        return pokemon_data


# Test view asyncronous loading firing all requests at once with asyncio [fastest]
async def test_async_requests(request):

    starting_time = time.time()

    actions = []
    pokemon_data = []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(asyncio.ensure_future(get_pokemon(session, url)))

        pokemon_res = await asyncio.gather(*actions)
        for data in pokemon_res:
            pokemon_data.append(data)

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "test.html",
        {"data": pokemon_data, "count": count, "time": total_time},
    )
