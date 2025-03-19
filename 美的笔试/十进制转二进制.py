def count_set_bits(n):
    """计算整数n的二进制表示中1的个数"""
    count = 0
    while n > 0:
        n &= (n - 1)  # 清除最低位的1
        count += 1
    return count


def solve():
    t = int(input())
    for _ in range(t):
        num = int(input())
        cnt = count_set_bits(num)
        target_count = 2 * cnt
        
        z = 0
        temp_result = 0
        
        # 优化：如果num的set bit 数已经大于target_count/2,那么 z 直接为0
        
        
        temp_result = num
        result_count = count_set_bits(temp_result)
        
        
        if result_count < target_count:
            
            i = 1
            while True:
                
                temp_result = num | i
                result_count = count_set_bits(temp_result)
                if result_count == target_count:
                    z = i
                    break
                i += 1 #测试所有可能的z,直到满足条件

        print(num | z) # 输出结果

solve()