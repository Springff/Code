nums = [1,2,3,4]
print(nums[-0])
print(nums[-2])
print(nums[-3])
prefix_products = []
prefix_products.append(1)
for i in range(1,len(nums)):
    prefix_products.append(prefix_products[i-1]*nums[i-1])

suffix_products = []
suffix_products.append(1)
for i in range(len(nums)-2,-1,-1):
    suffix_products.append(suffix_products[-1]*nums[i+1])

output = []
for i in range(len(nums)):
    print(prefix_products[i])
    print(suffix_products[-i])
    output.append(prefix_products[i]*suffix_products[-i])
print(output)
        