from zhihuAPI.account import ZhihuAccount


def mourn_machines(cookie_path):
    machine = ZhihuAccount(cookie_path)
    current_url_token = machine.get_page_json('Miscellaneous', 'Me', '')['url_token']
    people = machine.get_all_pages_json('Members', 'Followers', current_url_token)
    for person in people:
        if person['name'] == '[已重置]':
            if machine.get_page_json('Miscellaneous', 'Profile', person['id'], {'include': ['account_status']})[
                'account_status'][0]['name'] == 'hang':
                machine.action('Me', 'SendMessage', '', {'content': 'RIP', 'receiver_hash': person['id']})


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--cookie', '-c', help='path to exported cookies json',
                        default='/Users/vapor/Downloads/export.json')
    args = parser.parse_args()
    mourn_machines(args.cookie)
