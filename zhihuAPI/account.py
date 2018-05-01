import json
import re
import os
import requests

from zhihuAPI.get import APIURLGET


def fix_api_url(url, cat, item):
    if cat == 'Members' and item in ["FollowingQuestions", "Answers",
                                     "Questions", "Articles", "Columns", "FollowingColumns"]:
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
        self.cookies = {item['name']: item['value'] for item in cookies_tmp}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36'}

    def get_url_json(self, url):
        resp = requests.get(url, cookies=self.cookies, headers=self.headers)
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

    def get_page_json(self, cat, item, _id):
        return self.get_url_json(APIURLGET[cat][item].format(_id))

    def get_all_pages_json(self, cat, item, _id):
        current = self.get_page_json(cat, item, _id)
        if not current:
            return {}
        if 'paging' not in current:
            return current
        else:
            data_list = current['data']
            while not current['paging']['is_end']:
                current = self.get_url_json(fix_api_url(current['paging']['next'], cat, item))
                data_list += current['data']
            return data_list

    def save_all_pages_json(self, cat, item, _id, save_dir):
        save_path = os.path.join(save_dir, 'JSON', cat, item)
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
