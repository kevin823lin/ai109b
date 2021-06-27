# 期末專案

> 本程式完全是原創作品，沒有修改自任何來源，也沒有剪貼自其他程式作品。

## 信用卡活動自動登錄程式

* 此程式為本人於 2020 年底練習文字辨識時所撰寫，僅作為研究用途，並未實際用於搶登錄名額領取回饋

* 該銀行登錄流程已更改，因撰寫目標僅為練習文字辨識，因此不再進行更改

### 撰寫過程

1. 透過 Fiddler 擷取登錄過程中的請求

1. 模擬發送驗證碼請求

1. 辨識驗證碼文字

1. 模擬發送登錄請求

### 遇到的問題

1. pytesseract.image_to_string() 應該要能設定欲辨識的文字類型

    實際測試發現不管設定什麼，總是有機會辨識出非我設定的類型，因此我自行判斷辨識結果並進行篩選

2. 登錄流程更改

    由於不打算將此程式實際用於搶登錄名額領取回饋，因此不對新版登錄流程進行更新

[main.py](./main.py)

* 文字辨識及處理的片段

    ```python
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
    ```

* 執行結果

    ```text
    PS D:\檔案\課程\1092\人工智慧\ai109b\final> python .\main.py
    list1=['5', '6', '3', '9', '5', '9']
    s=563959
    1. 0.4544994831085205 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['2', '9', '7', '5', '2', '8']
    s=297528
    2. 0.30276942253112793 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['9', '2', '4', '6', '5', '7']
    s=924657
    3. 0.31070995330810547 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['0', '3', '7', '2', '3', '3']
    s=037233
    4. 0.33886051177978516 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['5', '6', '4', '9', '2', '3']
    s=564923
    5. 0.3040609359741211 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['2', '4', '1', '6', '2', '7']
    s=241627
    6. 0.3157203197479248 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['4', '6', '4', '8', '7', '5']
    s=464875
    7. 0.29799532890319824 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['8', '2', '8', '8', '5', '5']
    s=828855
    8. 0.32407450675964355 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['2', '4', '4', '5', '2', '5']
    s=244525
    9. 0.30234813690185547 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    list1=['2', '8', '3', '4', '0', '9', '"']
    remove("), list1=['2', '8', '3', '4', '0', '9']
    s=283409
    10. 0.3243532180786133 sec
    {"Result":false,"Header":null,"ResultCode":"C3","ResultMessage":"驗證金鑰未產生","Error":null}
    total 3.2764296531677246 sec
    ```

## 參考資料

* <https://stackoverflow.com/questions/50531745/unable-to-load-image>

* <https://shengyu7697.github.io/python-opencv-erode-dilate/>
