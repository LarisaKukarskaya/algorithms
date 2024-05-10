def length_substring(a):
    max_a = ''
    cnt = 0
    max_cnt = 0
    beginning, end = 0, len(a) - 1
    
    while beginning <= end:
        if a[beginning] not in max_a:
            max_a += a[beginning]
            cnt += 1
        else:
            index = max_a.index(a[beginning])
            max_a = max_a[max_a.index(a[beginning]) + 1:] + a[beginning]
            cnt = len(max_a)
        if cnt > max_cnt:
            max_cnt = cnt

        beginning += 1

    return max_cnt    

print(length_substring(input()))
