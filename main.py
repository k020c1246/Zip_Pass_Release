import zipfile
import random
 
file_path = 'sueyoshi_num6.zip'
size = 6
chars = '0123456789'
count = 0
 
with zipfile.ZipFile(file_path , 'r') as zf:
    for i in range(1000000):
        # パスワードはバイト型で有る必要がある
        pwd = bytes(''.join(random.choices(chars,k=size)),'UTF-8')
        try:
            zf.extractall(path='.', pwd=pwd)
            print('success : password  : {}'.format(pwd))
            break
        except Exception as e:
            count +=1
 
