import time

def strftime(value):
    try:
        num = int(value)
        size = len(str(num))
        if(size == 10):
            num = num
        elif(size == 13):
            num /= 1000
        else:
            return None
        e = time.localtime(num)
        return time.strftime('%Y-%m-%d %H:%M:%S',e)        
    except ValueError:
        return None

def humanstamp(value, key = None):
    if(value is None):
        return None
    if (isinstance(value, list)):
        bufs = []
        for el in value:
            bufs.append(humanstamp(el, None))
        return bufs
    elif(isinstance(value, dict)):
        objs = {}
        for (ek, ev) in value.items():
            values = humanstamp(ev, ek)
            key_ts = '%s_ts' % ek
            ext = values.get(key_ts, None) if(isinstance(values, dict)) else None
            if(ext is None):
                objs[ek] = values
                continue
            objs[ek] = ev
            if(len(ext) > 0):
                objs[key_ts] = ext
        return objs
    elif(key is not None):
        ext = strftime(value)
        return {('%s_ts' % key): '' if(ext is None) else ext}
    else:
        pass
    return None


# if (__name__ == "__main__"):
#     obj = {'errCode': 0, 'errMsg': 'success', 'data': [
#         {'a': 1649825172000, 'b': 'hello'},
#         {'a': 1649825172, 'b': 'hello'},
#         {'a': {'x': 1649825172000}, 'b': 'hello'},
#     ]}
#     target = humanstamp(obj, None)
#     print(target)