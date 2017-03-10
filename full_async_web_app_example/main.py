import asyncio
from .app import create

loop = asyncio.get_event_loop()
app = create(loop=loop)
