from zhihuAPI.account import ZhihuAccount


def machine_renewal(cookie_path, url_token):
    machine = ZhihuAccount(cookie_path)
    topics = machine.get_all_pages_json('Members', 'FollowingTopics', url_token)
    questions = machine.get_all_pages_json('Members', 'FollowingQuestions', url_token)
    people = machine.get_all_pages_json('Members', 'Followees', url_token)
    for item in topics:
        machine.action('Topics', 'FollowTopic', item['topic']['id'])
    for item in questions:
        machine.action('Questions', 'FollowQuestion', item['id'])
    for item in people:
        machine.action('Members', 'Follow', item['url_token'])


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--cookie', '-c', help="path to exported cookies json",
                        default='/Users/vapor/Downloads/export.json')
    parser.add_argument('--url_token', '-u', help='your old account url token', required=True)
    args = parser.parse_args()
    machine_renewal(args.cookie, args.url_token)
