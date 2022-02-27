import subprocess
import urllib.parse
import time
import json
from insta.config import command, index, url_base, after, in_current_batch

while True:
    after_value = f',"after":"{after}"' if after else ''
    variables = f'{{"id": "910217080", "include_reel": true, "fetch_mutual": true, "first": 50{after_value}}}'
    get_params = {
        'query_hash' : 'c76146de99bb02f6415203be841dd25a',
        'variables' : variables
    }
    ws_url = url_base+urllib.parse.urlencode(get_params)
    result = subprocess.run(command.format(url=ws_url, index=index), shell=True, capture_output=True)
    if result.returncode != 0:
        print("Error")
    with open(f'json/followers_{index}.json', "r") as f:
        data = json.load(f)
    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
    index+=1
    all_followers = data['data']['user']['edge_followed_by']['count']
    in_current_batch += len(data['data']['user']['edge_followed_by']['edges'])
    print(f"sucsef {in_current_batch}/{all_followers}")

    time.sleep(1 if index % 10 != 0 else 3)

    if data['data']['user']['edge_followed_by']['page_info']['has_next_page'] == False:
        break


print('the end')