#!/bin/bash
sleep 5
export PYTHONPATH='/usr/lib/python35.zip:/usr/lib/python3.5:/usr/lib/python3.5/plat-arm-linux-gnueabihf:/usr/lib/python3.5/lib-dynload:/home/pi/.local/lib/python3.5/site-packages:/usr/local/lib/python3.5/dist-packages:/usr/lib/python3/dist-packages' 


/usr/bin/python3 /home/pi/robot/smallmove.py
/usr/bin/python3 /home/pi/robot/bluebot.py
