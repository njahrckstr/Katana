# @name:    Katana-DorkScanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane-X-tebbaa (AXT)
# Proxy-file V0.1
# find online proxy servers 
# twitter TebbaaX
import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
import sys
import os

B = """
 ____
|  _ \ _ __ _____  ___   _
| |_) | '__/ _ \ \/ / | | |    Katana-ds V1.5
|  __/| | | (_) >  <| |_| |    Proxy Mode
|_|   |_|  \___/_/\_\\__,  |   Coded by Adnane-X-tebbaa (AXT) 
                     |___/
"""
print(B)
print ("")
print(colored('[+] This will find 25 Different working Proxy server Each time :', 'green', 'on_grey')) 
print(colored('[+] Starting...', 'green', 'on_grey'))

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=25 ), show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(colored('[+] Done', 'green', 'on_grey'))

