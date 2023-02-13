Pelican Mini Wiki: A Plugin for Pelican
====================================================

[![Build Status](https://img.shields.io/github/actions/workflow/status/hreikin/pelican-mini-wiki/build-and-publish-on-tagged-release.yml?branch=main)](https://github.com/hreikin/pelican-mini-wiki/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-mini-wiki)](https://pypi.org/project/pelican-mini-wiki/)
[![License](https://img.shields.io/pypi/l/pelican-mini-wiki?color=blue)](https://github.com/hreikin/pelican-mini-wiki/blob/main/LICENSE.md)

Pelican Mini Wiki allows you to add a minimal wiki to any Pelican theme and website.

> **NOTE:** still under development, will not currently work or be useful.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-mini-wiki

Usage
-----

Instructions coming soon. Configuration settings are available below.

```python
# pelicanconf.py

...
# REQUIRED SETTINGS
MINI_WIKI = True            # Enables the plugin.
MINI_WIKI_PATH  ='wiki'     # Path to wiki files, relative to `content/` directory.
# RECOMMENDED SETTINGS
PAGE_PATHS = ['pages', MINI_WIKI_PATH]      # Sets paths to look in for `pages` type content.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'   # Strips the file extension from the `path` variable.
PAGE_URL = '{path_no_ext}/'                 # Replaces the stripped file extension for the URL with a forward slash.
PAGE_SAVE_AS = '{path_no_ext}.html'         # Replaces the stripped file extension for saving.
...

```

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues](https://github.com/hreikin/pelican-mini-wiki/issues).

To start contributing to this plugin, review the [Contributing to Pelican](https://docs.getpelican.com/en/latest/contribute.html) documentation, beginning with the **Contributing Code** section.

License
-------

This project is licensed under the MIT license.
