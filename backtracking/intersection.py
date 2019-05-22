def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if(len(nums1) == 0 or len(nums2) == 0):
        return []

    findings = set()
    result = []

    for num in nums1:
        if(num not in findings):
            findings.add(num)

    for num in nums2:
        if(num in findings):
            result.append(num)
            findings.remove(num)

    return result

nums1 = [1,2,1,2,2,2,5]
nums2 = [4,5,6,7,1,1,1,1]

res = intersection(nums1, nums2)
print res
