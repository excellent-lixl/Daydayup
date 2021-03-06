import csv
import pandas as pd
import random
from gmssl import sm3, func

# 1. 创建文件对象
f = open('id.csv','w',encoding='utf-8')
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 3. 构建列表头
csv_writer.writerow(["CARD_ID"])
# 4. 写入csv文件内容
for m in range(100): 
    str = ""
    for i in range(18):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    
    csv_writer.writerow([str])
    
# 5. 关闭文件
f.close()


def data_sm3_toString(strs):
    str_b = bytes(strs, encoding='utf-8')
    result = sm3.sm3_hash(func.bytes_to_list(str_b))
    return result


##这种适用于numpy格式
def data_sm3_toNumpy(strs):
#     str_b = bytes(strs, encoding='utf-8')
    str_b = data.iloc[g,0].tobytes()
    result = sm3.sm3_hash(func.bytes_to_list(str_b))
    return result;
#     print(result)  #50f03b05d10fa07f1169aff1d1e119ae3169107035b1abd24f76009ee05a8e2c

