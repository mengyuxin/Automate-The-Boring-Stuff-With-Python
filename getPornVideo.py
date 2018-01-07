#! python3
# -*- coding:utf-8 -*-

import re
import os
import time
import urllib
import random
import requests

try:
    #html_Z = requests.get('http://www.qydh7.com/')
    html_Z = requests.get('http://www.qyl066.com/')
    name_url = re.findall('com</a><a href="(.*?)" target="_parent', html_Z.text, re.S)
    name_url = ''.join(name_url)
    print(name_url)
    #html = requests.get(name_url)
    html = requests.get("http://www.qyl066.com/43616/%E5%B9%BF%E5%B7%9E%E9%85%92%E5%BA%97%E5%A4%A7%E6%88%98%E6%80%A7%E6%84%9F%E9%BB%91%E4%B8%9D%E5%A4%A7%E5%AD%A6%E7%BE%8E%E5%A5%B3-%E5%8F%A3%E6%B4%BB%E8%B6%85%E6%A3%92%E5%90%83%E7%B4%AF%E4%BA%86%E4%B8%BB%E5%8A%A8%E5%9D%90%E5%9C%A8%E9%B8%A1%E5%B7%B4%E4%B8%8A%E6%89%AD%E5%8A%A8/")
except requests.exceptions.ConnectionError as e:
    html_Z = requests.get('http://www.qydh7.com/')
    name_url = re.findall('com</a><a href="(.*?)" target="_parent', html_Z.text, re.S)
    html = requests.get(name_url)
except requests.exceptions.InvalidSchema as e:
    print('Connection failed.')
    time.sleep(100)
    pass
finally:
    # print(html.text)
    av_flag = re.findall('<ul(.*?)</ul>', html.text, re.S)[5]
    av_flag = re.findall('<li><a href="/(.*?)/">', av_flag, re.S)
    # print(av_flag)
    filename = 0
    for echa in av_flag:
        url_echa = random.choice(av_flag)
        flag = ''.join(url_echa)
        av_url = name_url + '/' + flag
        # print(av_url)
        html2 = requests.get(av_url)
        # print(av_url)
        av_flag2 = re.findall('<ul class="videos">(.*?)</ul>', html2.text, re.S)
        # print(av_flag2)
        for echa1 in av_flag2:
            av_flag3 = re.findall('<li id= "video-(.*?)">', echa1, re.S)
            # title = re.findall('title="(.*?)"', echa1, re.S)
            url = random.choice(av_flag3)
            taobao_flag = ''.join(url)
            # print(tabbao_flag)
            av_qyule8 = name_url + "/embed/" + taobao_flag
            # print(av_qyule8)
            html8 = requests.get(av_qyule8)
            # print(av_qyule8)
            av_flag8 = re.findall('<source src="(.*?)" type="video/mp4" label=', html8.text, re.S)[0]
            print(av_flag8)

            mv = requests.get(av_flag8, stream=True)
            fp = open('mv//' + 'mv' + str(filename) + '.mp4', 'wb')
            fp.write(mv.contenct)
            print('Downloading')
            fp.close
            filename +=1
            
            
