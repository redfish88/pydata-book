#coding=utf8
import json
from collections import Counter
from pandas import DataFrame,Series
import pandas as pd;import numpy as np
path = "usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)]
print records[0]['tz']
#time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]

#获取时区出现的次数
def get_counts(sqquence):
    counts = {}
    for x in time_zones:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
counts = get_counts(time_zones)
print counts
#按照次数对时区进行排序
print counts.iteritems()
print counts.items()
sort_pairs = sorted(counts.iteritems(),key = lambda b:b[1], reverse=True)
print  sort_pairs[:10]
sort_pairs2 = sorted(counts.items(),key = lambda b:b[1], reverse=True)
print sort_pairs2[:10]

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs
#书中字典排序方法
print top_counts(counts)
counts = Counter(time_zones)
print counts.most_common(10)

frame = DataFrame(records)

print frame['tz'][:10]
tz_counts = frame['tz'].value_counts()
print tz_counts[:10]


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print tz_counts[:10]
tz_counts[:10].plot(kind='barh', rot=0)
results = Series([x.split()[0] for x in frame.a.dropna()])
print results[:5]
print results.value_counts()[:10]
print frame.tz













