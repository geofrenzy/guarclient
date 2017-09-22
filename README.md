# GUAR (Global Unmanned Airframe Registry) client library

This library contains a Python package (`uasclient`) for easily integrating GUAR projects into other Python projects (This supports Python 3.)

To install, simply just use `pip` to install from Github:
```bash
pip install git+git://github.com/geofrenzy/guarclient.git
```

Then, inside of a python script:
```python
import guarclient

guarclient.lookupuas("Tail number of airframe")
```
Where `Tail number of airframe` is the tail number you're looking up.

For an example project, please see the [Jupyter notebook](https://github.com/geofrenzy/guarclient-notebook) demonstrating the use of this package.
