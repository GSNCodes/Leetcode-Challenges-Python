Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The '.' character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. 
For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. 
Its third and fourth level revision number are both 0.


Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both 01 and 001 represent the same number 1
Example 5:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"
 

Note:

Version strings are composed of numeric strings separated by dots '.' and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.

#My Solution
# O(n) Time and O(n) Space where n is the number of levels in the version
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')
            
        if v1_list[-1] == 0:
            while int(v1_list[-1]) == 0:
                v1_list.pop()
        if v2_list[-1] == 0:
            while int(v2_list[-1]) == 0:
                v2_list.pop()
        
        v1_list = list(map(str, list(map(int, v1_list))))
        v2_list = list(map(str, list(map(int, v2_list))))
        
        if len(v1_list)<len(v2_list):
            for i in range(len(v2_list)-len(v1_list)):
                v1_list.append('0')
                
        elif len(v1_list)>len(v2_list):
            for i in range(len(v1_list)-len(v2_list)):
                v2_list.append('0')
                
        v1 = int(''.join(v1_list))
        v2 = int(''.join(v2_list))
        
        if v1<v2:
            return -1
        elif v1>v2:
            return 1
        else:
            return 0


# Better Solution
# O(n) Time and O(n) Space where n is the max number of levels in the either version
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)
        
        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            print(i1, i2)
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        # the versions are equal
        return 0 