# Django-AIOHTTP-Async-API-Requests

In this example, AsyncIO and AIOHTTP libraries are used within Django Views to
make asyncronous requests to an example external API (the Pokemon API) to speed
up the data pulling process.

### Use steps:
0. Running on Python 3.7 venv
1. pip install -r requirements.txt
2. python manage.py runserver
3. Navigate to test urls

### Test urls:
- /normalRequests --> regular loading with syncronous requests.get() [slow]
- /aiohttpRequests --> syncronous loading with aiohttp ClientSession() [faster]
- /asyncRequests --> asyncronous loading firing all requests at once with asyncio [fastest]
