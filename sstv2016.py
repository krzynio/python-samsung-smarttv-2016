#!/usr/bin/env python

import asyncio
import websockets
import json
import time
import sys 

def remote(ip_addr, keys_list):
    asyncio.get_event_loop().run_until_complete(_remote(keys_list, ip_addr))

@asyncio.coroutine
def _remote(keys, tv_addr,delay=1):
    websocket = yield from websockets.connect('ws://%s:%d/api/v2/channels/samsung.remote.control' % (tv_addr,8001))
    if type(keys) is str:
        _keys = [keys]
    else:
        _keys = keys

    try:
        while True:
            message = yield from websocket.recv()
            parsed = json.loads(message)
            if (parsed['event'] == 'ms.channel.connect'):  
                k = 0
                for key in _keys:
                    k = k + 1
                    cmd = '{"method":"ms.remote.control","params":{"Cmd":"Click","DataOfCmd":"%s","Option":"false","TypeOfRemote":"SendRemoteKey"}}' % key
                    yield from websocket.send(cmd)
                    if k != len(_keys):
                        time.sleep(delay)                        
                break
        time.sleep(delay)
    finally:
        yield from websocket.close()

if __name__ == "__main__":
    remote(sys.argv[1], sys.argv[2:])
