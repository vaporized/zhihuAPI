import json
import os
import re
import time

import requests

from zhihuAPI.action import APIURLACTION
from zhihuAPI.get import APIURLGET


def fix_api_url(url, cat, item):
    if cat == 'Members' and item in ['FollowingQuestions', 'Answers',
                                     'Questions', 'Articles', 'Columns', 'FollowingColumns']:
        return re.sub('zhihu.com/', 'zhihu.com/api/v4/', url)
    else:
        return url


def fix_html_url(url, item):
    if item == 'Questions':
        return re.sub('questions', 'question', url)
    elif item == 'Answers':
        return re.sub('answers', 'answer', url)
    else:
        return url


class ZhihuAPIError(Exception):
    pass


class ZhihuAccount:
    def __init__(self, path):
        with open(path) as f:
            cookies_tmp = json.load(f)
        self.cookies = {item['name']: item['value'] for item in cookies_tmp if item['domain'] == '.zhihu.com'}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36'}

    def get_url_json(self, url, _params=None):
        if _params is None:
            _params = {}
        resp = requests.get(url, cookies=self.cookies, headers=self.headers, params=_params)
        if resp.status_code != requests.codes.ok:
            print("Status code:", resp.status_code, "for", url)
            raise ZhihuAPIError
        else:
            try:
                result = json.loads(resp.text)
                return result
            except json.JSONDecodeError:
                print('Cannot decode JSON for', url)
                raise ZhihuAPIError

    def get_page_json(self, cat, item, _id, _params=None):
        if _params is None:
            _params = {}
        return self.get_url_json(APIURLGET[cat][item].format(_id), _params)

    def get_all_pages_json(self, cat, item, _id, _params=None):
        if _params is None:
            _params = {}
        current = self.get_page_json(cat, item, _id, _params)
        if not current:
            return {}
        if 'paging' not in current:
            return current
        else:
            data_list = current['data']
            while not current['paging']['is_end']:
                current = self.get_url_json(fix_api_url(current['paging']['next'], cat, item), _params)
                data_list += current['data']
            return data_list

    def save_all_pages_json(self, cat, item, _id, save_dir, time_stamp=False):
        save_path = os.path.join(save_dir, 'JSON', cat, item)
        if time_stamp:
            save_filename = str(_id) + str(int(time.time())) + '.json'
        else:
            save_filename = str(_id) + '.json'
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        res = self.get_all_pages_json(cat, item, _id)
        with open(os.path.join(save_path, save_filename), 'w+') as f:
            json.dump(res, f, indent=4, ensure_ascii=False)

    def get_html(self, url):
        resp = requests.get(url, cookies=self.cookies, headers=self.headers)
        if resp.status_code != requests.codes.ok:
            print("Status code:", resp.status_code, "for", url)
            raise ZhihuAPIError
        else:
            return re.sub("<script.*?</script>", '', resp.text)

    def save_html(self, url, item, save_dir, author=None):
        if author:
            save_path = os.path.join(save_dir, 'HTML', author, item)
        else:
            save_path = os.path.join(save_dir, 'HTML', item)
        save_filename = url.split('/')[-1] + '.html'
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        content = self.get_html(fix_html_url(url, item))
        with open(os.path.join(save_path, save_filename), 'w+') as f:
            f.write(content)

    def save_all_html(self, item, user_id, save_dir, author=None):
        info_list = self.get_all_pages_json('Members', item, user_id)
        for dic in info_list:
            self.save_html(dic['url'], item, save_dir, author)

    def action(self, cat, item, _id, _data=None, _params=None):
        if _data is None:
            _data = {}
        if _params is None:
            _params = {}
        api_info = APIURLACTION[cat][item]
        url = api_info['url'].format(_id)
        func_dic = {'post': requests.post, 'put': requests.put, 'delete': requests.delete}
        func = func_dic[api_info['method']]
        if 'data' in api_info:
            predefined_payload = {**api_info['data']}
        else:
            predefined_payload = {}
        if 'required_keys' in api_info:
            for key in api_info['required_keys']:
                assert key in _data
        payload = {**predefined_payload, **_data}
        if 'form_data' in api_info and api_info['form_data']:
            resp = func(url, data=payload, cookies=self.cookies, headers=self.headers, params=_params)
        else:
            resp = func(url, json=payload, cookies=self.cookies, headers=self.headers, params=_params)
        if 200 <= resp.status_code < 300:
            try:
                result = json.loads(resp.text)
                return result
            except json.JSONDecodeError:
                print('Cannot decode JSON for', url)
                return resp.text
        else:
            print("Status code:", resp.status_code, "for", url)
            print(resp.text)
            raise ZhihuAPIError
