import csv
'''添加csv文件'''
def load_csv(filepath):
    '''读取csv文件,返回[{列名：值}，.....]'''
    rows = []
    try:
        with open(filepath,'r',encoding = 'utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
            print(f'读取文件有{len(rows)}条记录')
    except FileNotFoundError:
        print(f'错误：找不到{filepath}文件')
    return rows

def get_column(data,col_name,dtype=float):
    '''提取指定列，转成指定类型'''
    values = []
    for row in data:
        try:
            val = dtype(row[col_name])
            values.append(val)
        except (ValueError,KeyError):
            continue
    return values

def get_unique_values(data,col_name):
    '''删除重复的列'''
    return list(set(row[col_name] for row in data))


