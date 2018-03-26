.. image:: https://travis-ci.org/scotchka/LRU.svg?branch=master
  :target: https://travis-ci.org/scotchka/LRU
.. image:: https://coveralls.io/repos/github/scotchka/LRU/badge.svg?branch=master
  :target: https://coveralls.io/github/scotchka/LRU?branch=master


Least Recently Used (LRU) cache
-------------------------------

.. code:: python

  >>> from lru import LRU
  >>> cache = LRU(maxsize=3)
  >>> cache['a'] = 1
  >>> cache['b'] = 2
  >>> cache['c'] = 3
  >>> cache['a']
  1
  >>> cache['d'] = 4
  >>> cache
  {'a': 1, 'c': 3, 'd': 4}
