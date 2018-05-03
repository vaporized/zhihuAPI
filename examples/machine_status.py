import time

from zhihuAPI.account import ZhihuAccount


def machine_status(cookie_path, url_token):
    machine = ZhihuAccount(cookie_path)
    res = machine.get_page_json('Miscellaneous', 'Profile', url_token,
                                {'include': ['account_status,is_force_renamed']})
    account_status = res['account_status']
    if not account_status:
        print('该账号正常运行')
    elif account_status[0]['name'] == 'hang':
        print('由于严重违反知乎社区管理规定，该账号已于',
              time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(account_status[0]['created_at'])), '被停用。', '原因是',
              account_status[0]['reason'], 'RIP[蜡烛]')
    elif account_status[0]['name'] == 'ban':
        if account_status[0]['expired_at'] == 864000000:
            print('由于严重违反知乎社区管理规定，该账号已于',
                  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(account_status[0]['created_at'])), '被永久禁言。',
                  '原因是', account_status[0]['reason'], 'RIP[蜡烛]')
        else:
            ban_length = account_status[0]['expired_at'] // 86400
            print('由于违反知乎社区管理规定，该账号已于',
                  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(account_status[0]['created_at'])), '被禁言',
                  ban_length, '天。原因是', account_status[0]['reason'])
    elif account_status[0]['name'] == 'lock':
        print('该账号由于发布', account_status[0]['reason'], '，被反作弊系统限制。')
    else:
        print('account_status not understood:', account_status)

    reset = res['is_force_renamed']
    if reset:
        print('由于违反知乎用户信息管理规范，该账号用户名已被重置。（官方称谓：reseted）')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--cookie', '-c', help='path to exported cookies json',
                        default='/Users/vapor/Downloads/export.json')
    parser.add_argument('--url_token', '-u', help='url token of the user to query', required=True)
    args = parser.parse_args()
    machine_status(args.cookie, args.url_token)
