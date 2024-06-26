# 0x01. Caching

## Project Overview

This project focuses on learning different caching algorithms, their purpose, and limitations. It involves implementing various cache replacement policies such as FIFO, LIFO, LRU, MRU, and LFU in Python.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a caching system is
- The meanings of FIFO, LIFO, LRU, MRU, and LFU
- The purpose of a caching system
- The limitations of a caching system

## Requirements

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the pycodestyle style (version 2.5).
- All files must be executable.
- File lengths will be tested using `wc`.
- All modules, classes, and functions must have documentation.

### Documentation

- Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
- Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- Functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- Documentation should be a real sentence explaining the purpose.

## Base Class: `BaseCaching`

All classes must inherit from `BaseCaching`.

### `base_caching.py`

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Resources

- [Cache replacement policies - FIFO](https://example.com/fifo)
- [Cache replacement policies - LIFO](https://example.com/lifo)
- [Cache replacement policies - LRU](https://example.com/lru)
- [Cache replacement policies - MRU](https://example.com/mru)
- [Cache replacement policies - LFU](https://example.com/lfu)

## Timeline

- **Project Start**: Jun 25, 2024, 6:00 AM
- **Project End**: Jun 27, 2024, 6:00 AM
- **Checker Release**: Jun 25, 2024, 6:00 PM
- **Auto Review Launch**: Jun 27, 2024, 6:00 AM

## Note

Ensure all your caching classes extend the `BaseCaching` class and implement the `put` and `get` methods appropriately for each caching policy.
