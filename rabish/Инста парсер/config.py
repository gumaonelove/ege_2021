command = """curl '{url}' \
  -H 'authority: www.instagram.com' \
  -H 'accept: */*' \
  -H 'dnt: 1' \
  -H 'x-ig-www-claim: hmac.AR2AsBlbQefE9xDqKbVPFJFlcMd_zz9R1Qdab3dBhoJ6od9H' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36' \
  -H 'x-csrftoken: D9ynhWuB8iAkNmwoVISVtArYQUdZLy91' \
  -H 'x-ig-app-id: 936619743392459' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.instagram.com/gumaonelove/followers/' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8 number,en;q=0.7' \
  -H 'cookie: ig_did=86F5F42B-8BF1-40CC-BA1F-CAF6D1CF3767; mid=X7u4lgAEAAFBmp4wF2Q9xScexigH; ig_nrcb=1; csrftoken=D9ynhWuB8iAkNmwoVISVtArYQUdZLy91; ds_user_id=910217080; sessionid=910217080%3AB6PMxYfVb34noy%3A10; shbid=9849; shbts=1606138013.8720174; rur=PRN; urlgen="{{\"178.207.30.128\": 28840}}:1khBs6:wfGQhmwNftno3TUOBSWIFnkskR0"' \
  --compressed > json/followers_{index}.json"""

index =1
url_base = 'https://www.instagram.com/graphql/query/?'
after = None
in_current_batch = 0