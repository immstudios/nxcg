NXCG
====
This library combines power of PIL (or Pillow), PyCairo and Pango and focuses on
2d graphics for broadcast applications.

## Installation

### Requirements

- PIL
- PyCairo
- PangoCairo
- NumPy

```bash
apt-get install python-cairo python-gtk2 python-imaging python-numpy
```

## Basic usage

Hello world
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nxcg import *

cg = CG(1920, 1080)
cg.text("Hello World!", pos=(100,100), color="#cc0000", font="Sans 36")
cg.save("hello.png")
```

## Documentation

Code is quite self-documenting see `nxcg/core.py` for build-ins
and `plugins/test_plugin.py` to see how to write your own plug-ins :-)

See NXTV sources for more advanced usage tips and underlying libraries documentation:

 - http://www.pygtk.org/pygtk2reference/class-pangolayout.html
 - https://developer.gnome.org/pygtk/stable/pango-markup-language.html

### Notes
 - Loading non-png glyphs is quite slow.
   For real-time or near real time graphics use PNG or cache images in advance.

