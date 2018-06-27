# zhihuAPI
[Zhihu](https://www.zhihu.com) APIs for Python 3.5+

Introduction
--------------
Zhihu API is a Python package that provides 100+ operations in one line on [Zhihu](https://www.zhihu.com) with its web APIs. 


Installation
--------------
You can install the package via
```bash
pip install git+https://github.com/vaporized/zhihuAPI
```
Or, you can simply download the code and run scripts in its directory.

Documentation
---------------
The documentation of all APIs implemented is [here](http://zhihuapi.readthedocs.io/en/latest/).

Quick Example
---------------
The following code snippet shows the titles of the **the first page** of the following questions of a certain user. (To get the 
full data, use `get_all_pages_json` instead, and there is no need of accessing the `'data'` key.) (This page is not of full 
length because the other six questions are deleted.)
```python
from zhihuAPI.account import ZhihuAccount
machine = ZhihuAccount('~/Downloads/export.json')
for item in machine.get_page_json('Members','FollowingQuestions','vapor-vx')['data']:
    print(item['title'])
    
# Returns
有什么东西你摸过一次后就再也不敢摸了？
你在清洗车轮的时候发现过什么奇怪的东西？
如何以“没想到你还活着”为开头写一个故事？
如何以“一看关注列表，发现这个问题并没有那么简单”为题写作？
```

Example Scripts
-----------------
Some direct applications of the package for common tasks are provided in `examples/`. New scripts may be added upon requests. 
The scripts emphasize readability and simplicity, so they do not have additional features and are not ready for large scale 
use. You need to implement your own logic in this case.

Here is an example of running one of the scripts, querying the status of an account.
```bash
python -m examples.machine_status -u vapor-vx
# Returns
由于严重违反知乎社区管理规定，该账号已于 2018-01-20 18:47:01 被停用。 原因是 politics RIP[蜡烛]
```

Requesting Features
--------------------
If you need some feature that is unavailable in the package, please post an issue and I will add it if it is achievable via calling APIs alone.

Notice
-----------
From June 12th, 2018, Zhihu blocked all access (including API access) to banned accounts(停用，非禁言/限制). Therefore backing up / querying status of those accounts is no longer possible. Please perform backups of your accounts frequently before its lifespan ends.

