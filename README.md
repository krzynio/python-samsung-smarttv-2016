# Samsung Smart TV 2016 remote in Python 3

Samsung Smart TV 2016 remote in Python 3

Usage from command line:

Switch to channel 107
```
$ python sstv2016.py KEY_1 KEY_0 KEY_7 KEY_ENTER
```

In Python:
```python
from sstv2016 import remote
remote('192.168.1.1', ['KEY_1','KEY_0','KEY_7','KEY_ENTER'])
```

Keys list:

http://www.maartenvisscher.nl/samsung-tv-control/javadoc/nl/maartenvisscher/samsungtvcontrol/Keycode.html

