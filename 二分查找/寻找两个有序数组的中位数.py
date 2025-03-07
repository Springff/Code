# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

# 算法的时间复杂度应该为 O(log (m+n)) 。


## 有空重做
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        k = (len1+len2)
        if k%2==0:
            return (self.findK(nums1,nums2,k//2)+self.findK(nums1,nums2,k//2+1))/2.0
        return self.findK(nums1,nums2,k//2+1)

    def findK(self,nums1,nums2,k):
            if not nums1:
                return nums2[k-1]
            if not nums2:
                return nums1[k-1]
            if k==1:
                return min(nums1[0],nums2[0])
            i = min(len(nums1),k//2)
            j = min(len(nums2),k//2)
            if nums1[i-1]<nums2[j-1]:
                return self.findK(nums1[i:],nums2,k-i)
            else:
                return self.findK(nums1,nums2[j:],k-j)
                
