"""使用 sm.ms api 上传图片并获取 BBCode 链接"""

import os
from functools import reduce

import requests

# smms.app api configuration
headers = {"Authorization": "xxx"}  # smms.app
# 若你电脑端在使用VPN，一般代理proxies需要设置一下
proxies = {"http": None, "https": None}  # 方式1，设置成None
# 方式2，找到你VPN的代理ip和端口，不过不一定有用，方式1更有用一些
# proxies = {
#     "http": "http://your VPN proxy ip:your VPN proxy port",
#     "https": "https://your VPN proxy ip:your VPN proxy port",
# }
smms_api_url = "https://smms.app/api/v2/"

# smms api configuration
# headers = {"Authorization": "jy5oSw3Ug61FVYMMw61wD6Koga72StRT"}  # sm.ms
# smms_api_url = "https://sm.ms/api/v2/"  # sm.ms

# image path, 可修改项
dir_path = r"your image path"

# flag标志, 可修改项
# flag = 0  # 获取已上传图片BBCode,默认取最后三张图片的
flag = 1  # 上传图片并获取其BBCode


def upload(fn, upload="upload"):
    files = {"smfile": open(fn, "rb")}
    url = smms_api_url + upload
    requests.post(url, files=files, headers=headers, proxies=proxies).json()


def getHistory(img_num=-3, history="upload_history"):
    url = smms_api_url + history
    res = requests.get(url, headers=headers, timeout=5, proxies=proxies).json()
    res = res["data"]
    # 影视截图一般上传3张即可
    res = res[img_num:]
    # res = res[:]['filename']

    for res_item in res:
        item_url = res_item["url"]
        #     item_time = res_item['created_at']
        print(f"[img]{item_url}[/img]")  # 图片链接的BBCode形式


def get_img_path(path):
    os.chdir(path)  # 切换到图片路径

    # 获取图片路径下的图片列表
    file_list = reduce(
        lambda x, y: x + y, [files for root, dirs, files in os.walk(dir_path)]
    )

    return file_list


def main(flag):
    # 上传图片并获取其BBCode
    if flag:
        n = 0
        files = get_img_path(dir_path)

        for file in files:
            n += 1
            file = os.path.join(dir_path, file)
            upload(file)
            print(f"Image {n} upload is done!")

        print(f"All {n} images are uploaded! ")
        print("------------------------------------")
        print("The BBCode of uploaded images are: ")

        getHistory(-n)

    else:  # 获取已上传图片BBCode,默认取最后三张图片的
        print("The BBCode of selected images are: ")
        getHistory()


if __name__ == "__main__":
    main(flag)
