.. zhihuAPI documentation master file, created by
   sphinx-quickstart on Wed May  2 03:13:12 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

zhihuAPI Documentation
====================================

Introduction
------------------------------------
zhihuAPI provides a python implementation of APIs from https://www.zhihu.com .

The aim of this project is to make a large collection of APIs, instead of building a smart crawler. Therefore
APIs are called in a general framework and only minimal working interface is available. You can add your own
wrappers for specific functionalities and implement strategies for large scale crawling, but they are out of the
scope of this package.


Authorization
------------------------------------
Unfortunately an automated login is not implemented (login with username and password). This is because Zhihu frequently
changes their login code, and makes the required request values increasingly difficult to generate. If there is a stable
and relatively easy way to simulate login, please inform me.

To make API calls, you need a working Zhihu account. Currently zhihuAPI reads from an exported json file for cookies.
The required file format is:

.. code:: javascript

   [
      {
         "domain":".zhihu.com",
         "name":"zap",
         "value":"xxxxx",
         ...
      },
      ...
   ]

One way to obtain this file is to use the "cookie inspector" extension for Chrome, when you visit Zhihu, open the
developer tools, cookies tab (usually the last one), right click and export all cookies. Afterwards, the instance
can be created with:

.. code:: python

   from zhihuAPI.account import ZhihuAccount
   machine = ZhihuAccount('path/to/cookie.json')


API Documentation and Examples
------------------------------------

.. toctree::
   :maxdepth: 2

   account.rst
   fetch_info.rst
   action.rst
   examples.rst

