#coding=utf8
import json
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












