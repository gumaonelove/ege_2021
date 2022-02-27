import glob
from pprint import pprint
import json

files = glob.glob("json/*.json")
folowers = {}


for f in files:
    with open(f, 'r') as f:
        data = json.load(f)
        for user in data['data']['user']['edge_followed_by']['edges']:
            user_info = user['node']
            folowers[user_info['id']] = {
                'id' : user_info['id'],
                'user_name' : user_info['username'],
                'followed_by_viewer' : user_info['followed_by_viewer'],
                'full_name' : user_info['full_name'],
                'is_private' : user_info['is_private'],
                'is_verified' : user_info['is_verified'],
                'profile_pic_url' : user_info['profile_pic_url']
            }
folowers = list(folowers.values())

with open('followers.json', 'w') as f:
    json.dump(folowers, f)
