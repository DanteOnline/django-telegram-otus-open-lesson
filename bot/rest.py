import httpx


async def get_messages():
    url = 'http://127.0.0.1:8000/api/messages/'
    try:
        async with httpx.AsyncClient(timeout=1) as client:
            response = await client.get(url)

        response.raise_for_status()
        response_json = response.json()
        return response_json
    except httpx.HTTPError as error:
        print(f'Произошла ошибка {error}')
        return ''


async def create_message(text, chat_id):
    url = 'http://127.0.0.1:8000/api/messages/'
    try:
        async with httpx.AsyncClient(timeout=1) as client:
            data = {
                'text': text,
                'chat_id': chat_id,
            }
            response = await client.post(url, data=data)

        response.raise_for_status()
        return response
    except httpx.HTTPError as error:
        print(f'Произошла ошибка {error}')
        return ''
