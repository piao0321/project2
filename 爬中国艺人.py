# -*- coding: utf-8 -*-
"""
@Time :2022/12/3 16:50
@Author :Lai Xiangyuan
@Email :2936885192@qq.com
@File :爬中国艺人.py
@ID :12003990122
"""
import requests
import json
import os

Download_dir = 'chinese_celeb_imgs'
if not os.path.exists(Download_dir):
    os.mkdir(Download_dir)

header = {
    "Cookie": 'BAIDUID=02B9F693E56D9D9CE810CA622D3D9683:FG=1; BAIDUID_BFESS=02B9F693E56D9D9CE810CA622D3D9683:FG=1; BIDUPSID=02B9F693E56D9D9CE810CA622D3D9683; PSTM=1655813197; ZFY=xiy4lKFh:AlxlmVXCX905Wcw0Z4FODT7ZA4Rs2DDfFHY:C; __bid_n=1837a2c1857df96aaa4207; BAIDU_WISE_UID=wapp_1664202054399_857; BDUSS=W1QTkwwRjVvQXdyVW5yM085ZjI1UmlKU0dLNExCWDZRLWtnR35jWVhQRkVWWGRqRVFBQUFBJCQAAAAAAAAAAAEAAADpZcz4wLLAssCyMzUyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETIT2NEyE9jL; BDUSS_BFESS=W1QTkwwRjVvQXdyVW5yM085ZjI1UmlKU0dLNExCWDZRLWtnR35jWVhQRkVWWGRqRVFBQUFBJCQAAAAAAAAAAAEAAADpZcz4wLLAssCyMzUyOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAETIT2NEyE9jL; channel=bing; BD_UPN=12314753; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1669538693; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1669574124; COOKIE_SESSION=2072_3_7_6_1_16_1_0_4_7_1_3_0_52_0_0_1669437767_1669574181_1669576348|7#65_3_1669574177|2; newlogin=1; BD_HOME=1; BA_HECTOR=al24802g80ag0k00a4al8kh51hom2sg1g; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; PSINO=7; delPer=0; H_PS_PSSID=37856_36550_37519_37828_37840_37766_37823_36807_37759_26350_37790_37882; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; RT="z=1&dm=baidu.com&si=jc2c8fmbyg&ss=lb7oqnkc&sl=3&tt=1td&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=3w3&ul=4bc&hd=4dn"; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; ab_sr=1.0.1_MjY0MTdjOWNhMzZlYWJhNGE3MGVhZTI0MTVmOGNkZGRiYjA0MTVjMGNiMjZmZTY5YjQ0NTIxMTI4ZDg5ODM3YjlkZDBjOGZjYWQyMjhhYjg4MWQwOWUzYWU2Njc4ODhkNTNlNmY1Zjc0MDkwOGM1NzU5OGFmNTQ0MDM1ZDAzMjcyY2Y5MjkzMGZjZGU3YzE2YzM3ZjdjZTE0ZjBhNzAxNg==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; sugstore=1; H_PS_645EC=61e3D6xZYq42Z+WfZT7GtZ/n/TpiCfhU1SlXrwOThl8N9D1BOOPAKI7yKkbhJSpNAivq; baikeVisitId=b238e2b2-ace4-4cff-8172-4a8d025b7315',
    "Referer": "https://cn.bing.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
pn_i = 0
while True:
    pn = str(pn_i)
    pn_i += 100
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=500&format=json&ie=utf-8&oe=utf-8&query=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=" + pn + "&rn=100&_=1580457480665"

    res = requests.get(url, headers=header)
    json_str = json.loads(res.text)
    figs = json_str['data'][0]['result']

    for i in figs:
        name = i['ename']
        img_url = i['pic_4n_78']
        img_res = requests.get(img_url)
        if img_res.status_code == 200:
            ext_str_splits = img_res.headers['Content-Type'].split('/')
            ext = ext_str_splits[len(ext_str_splits) - 1]
            fname = name + "." + ext
            open(os.path.join(Download_dir, fname), 'wb').write(img_res.content)
            print(name, img_url, "saved")
