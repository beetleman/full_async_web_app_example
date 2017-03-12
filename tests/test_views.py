async def test_index_with_user_agent(cli, objects):
    resps = [
        await cli.get('/')
        for i in range(3)
    ]

    for resp in resps:
        assert resp.status == 200
        assert (
            await resp.json()
        ).get('user-agent') == 'Python/3.6 aiohttp/1.3.3'


async def _test_index_without_user_agent(cli):
    resp = await cli.get('/', headers={'User-Agent': ''})
    assert resp.status == 400
    assert (
        await resp.json()
    ).get('user-agent') == 'missing'
