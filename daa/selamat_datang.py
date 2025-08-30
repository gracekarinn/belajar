def count_daa_subsequences(s):
    d_count = 0
    da_count = 0
    daa_count = 0
    
    for char in s:
        if char == 'D':
            d_count += 1
        elif char == 'A':
            daa_count += da_count
            da_count += d_count
    
    return daa_count

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    result = count_daa_subsequences(s)
    print(result)