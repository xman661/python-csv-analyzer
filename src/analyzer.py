import numpy as np

def basic_stats(values):
    """基本统计指标：count/mean/median/std/min/max/range"""
    arr = np.array(values)
    return   {
              'counts': int(len(arr)),
              'mean': float(np.mean(arr)),
              'median': float(np.median(arr)),
              'std': float(np.std(arr)),
              'max': float(np.max(arr)),
              'min': float(np.min(arr)),
              'range': float(np.max(arr) - np.min(arr))}

def filter_by_condition(data,col_name,threshold,operator='gt'):
    """按条件筛选行：gt(>)/lt(<)/eq(==)"""
    filtered = []
    for row in data:
        val = float(row[col_name])
        if operator == 'gt' and val > threshold:
            filtered.append(row)
        elif  operator == 'lt' and val < threshold:
            filtered.append(row)
        elif operator == 'eq' and val == threshold:
            filtered.append(row)
    return filtered

def group_mean(data,group_col,values_col):
    """按某列分组，计算另一列均值。返回 {组名: 平均值}"""
    groups = {}
    counts = {}
    for row in data:
        key = row[group_col]
        val = float(row[values_col])
        if key not in groups:
            groups[key] = 0
            counts[key] = 0
        groups[key] += val
        counts[key] += 1
    return {k: groups[k] / counts[k] for k in groups}

def missing_rate(data):
    """计算每列缺失率（空值比例）"""
    if not data:
        return {}
    total = len(data)
    col_names = data[0].keys()
    return {col: sum(1 for r in data if r[col].strip() == '') / total for col in col_names}
