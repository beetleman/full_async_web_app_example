async def test_index(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    assert await resp.json() == {'error': None, 'message': 'hello'}
