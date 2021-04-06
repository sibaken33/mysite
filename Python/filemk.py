import pathlib
import os

file_path = './text01.txt'

file01 = pathlib.Path(file_path)

# print(file01.exists())
file01.touch()

# ファイルの存在チェック
print(file01.exists())

print(os.path.getsize(file_path))


