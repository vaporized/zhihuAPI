import os

from zhihuAPI.account import ZhihuAccount


def machine_backup_complete(cookie_path, url_token, save_path):
    machine = ZhihuAccount(cookie_path)
    machine.save_all_pages_json("Miscellaneous", "Profile", url_token, save_path)
    for item in ['Followers', 'Followees', "FollowingQuestions", "FollowingTopics", "FollowingColumns",
                 "FollowingFavlists", "Questions", "Answers", "Pins", "Articles", "Columns", "Favlists", "Activities"]:
        print('Processing', item)
        machine.save_all_pages_json('Members', item, url_token, save_path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--cookie', '-c', help="path to exported cookies json",
                        default='/Users/vapor/Downloads/export.json')
    parser.add_argument('--url_token', '-u', help='url token of the user to backup', nargs='+', type=str, required=True)
    parser.add_argument('--save_path', '-p', help='path to save output json and htmls',
                        default=os.path.dirname(os.path.abspath(__file__)))
    args = parser.parse_args()
    for u in args.url_token:
        machine_backup_complete(args.cookie, u, args.save_path)
