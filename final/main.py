CODE = "ABCD"  # 登錄活動代碼
ID = "A123456789"  # 身分證字號
next_date = "2020/12/21"  # 開放登錄日期
next_time = "15:00:00"  # 開放登錄時間

try:
    from PIL import Image
except ImportError:
    import Image

import datetime
import json
import sys
import threading
import time

import cv2
import numpy as np
import pytesseract
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings() # 關閉 requests 警告

if (len(sys.argv) == 2): # 讀取執行參數
    CODE = sys.argv[1]
url_captcha = r"https://example.com/api/security/captcha" # 驗證碼圖檔網址
url_SignActivity = r"https://example.com/api/Activity/SignActivity" # 登錄網址
se = requests.Session()
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 數字
count = 0


def submit(): # 登錄函數
    try:
        global CODE, ID, url_captcha, url_SignActivity, se, digits, count
        t1 = time.time()
        count += 1 # 嘗試登錄次數
        l = list() # 存放驗證碼
        while (len(l) != 6): # 檢查驗證碼是否為 6 位數，若不是則不斷取得新驗證碼
            req = se.get(url_captcha, stream=True, verify=False).raw # 取得驗證碼圖檔
            captcha = np.asarray(bytearray(req.read()), dtype=np.uint8) # 將圖檔轉成 np
            image = cv2.imdecode(captcha, cv2.IMREAD_GRAYSCALE) # 影像轉灰階
            cv2.dilate(image, (5, 5), image) # 影像膨脹
            s = pytesseract.image_to_string(image, config='--psm 7') # 文字辨識（文字類型設定無效）
            l = list(s) # 將辨識結果存入串列
            l.pop(-1)
            l.pop(-1)
            print(f'list1={l}') # 印出原始辨識結果串列
            for i in l:
                if i not in digits: # 由於文字類型設定無效，因此手動判斷是否為數字，若不是則移除
                    l.remove(i)
                    print(f'remove({i}), list1={l}') # 印出刪除掉的非數字及新 
                    break
        s = "".join(l) # 將 6 位數的驗證碼轉成字串
        print(f"s={s}") # 印出最終辨識結果字串
        header = { # 設定 request header
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "https://example.com",
            "Referer": "https://example.com/Activity/Register?Code=" + CODE,
            "Captcha": s
        }
        json_data = {"Content": {"Code": CODE, "ID": ID}, "Header": {"ApplicationName": "EWEB2", "UserID": None}} # 設定 request data
        jsonData = json.dumps(json_data)
        req = se.post(url=url_SignActivity, headers=header, data=jsonData, verify=False)
        t2 = time.time()
        print(f"{count}. {t2 - t1} sec") # 印出花費時間
        print(req.text) # 印出登錄結果
        if (req.json()["Result"] == False or req.json()["ResultCode"] == "09") and count < 10: # 重新嘗試登錄
            return 1
    except Exception as e:
        print(e)
        return 2
    return 0

def start(): # 呼叫登錄函數避免無窮遞迴
    t1 = time.time()

    req = submit()
    while req == 1:
        req = submit()
    if req == 2:
        print("登錄錯誤")
    
    t2 = time.time()
    print(f"total {t2 - t1} sec") # 印出總耗時

now_time = datetime.datetime.now()
next_datetime = datetime.datetime.strptime(f"{next_date} {next_time}", "%Y/%m/%d %H:%M:%S")
timer_start_time = (next_datetime - now_time).total_seconds()
timer = threading.Timer(timer_start_time, start) # 建立登錄倒數
timer.start()
while (timer_start_time >= 1):  # 印出登錄倒數時間
    now_time = datetime.datetime.now()
    timer_start_time = (next_datetime - now_time).total_seconds()
    print(f"{(int)(timer_start_time / 60)}分{timer_start_time % 60:.3f}秒")
    time.sleep(1)
