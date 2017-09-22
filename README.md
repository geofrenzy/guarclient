# GUAR (Global Unmanned Airframe Registry) client library

This library contains a Python package (`uasclient`) for easily integrating GUAR projects into other Python projects (This supports Python 3.)

To install, simply just use `pip` to locally install this directory:
```bash
pip install -e /path/to/guar/client/
```
(Where `/path/to/guar/client/` is the path to this directory.)

Then, inside of a python script:
```python
import guarClient

guarClient.uasLookup("Tail number of airframe")
```
Where `Tail number of airframe` is the tail number you're looking up.
