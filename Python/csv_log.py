"""
csvファイルを書き込むためのPythonコードです。
ディレクトリの指定とファイル名を日付と時間にするなど
ファイル名に日時時間情報を付けることで実行された際に一意の
名前のファイルができるため、ログの保存に便利です。
"""

import pathlib
import os
import datetime
import csv

# 日時の取得
now = datetime.datetime.now()

# ディレクトリの指定
filename = './output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
# filename = './output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
# filemake = pathlib.Path(filename)

# if os.path.exists(filename) == False:
    # filemake.touch()



# ファイル、1行目（カラム）の作成
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y', 'z'])

x, y, z = 0, 0, 0
while(1):
    #何らかの処理を描く
    x += 1
    y += 2
    z += 3

    # filenameを作成したファイル名に合わせる
    # writer.writerowでlistをcsvに書き込む
    with open(filename, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x, y, z])

    break