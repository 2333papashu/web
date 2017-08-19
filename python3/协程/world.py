import asyncio

connect = asyncio.open_connection("www.baidu.com", 80)
print(connect)