#include <iostream>
#include <vector>

using namespace std;
/**
 * The Problem
 * Given two arrays, write a function to compute their intersection.
 *
 * Example:
 * Input: nums1 = [1,2,2,1], nums2 = [2,2]
 * Output: [2]
 *
 * A bit help to get the best solution.
 * When designing your solution think on a case like this:
 * nums1 = [4,8,1,1]
 * nums2 = [7,6,2]
 * 
 * Output = []
 *
 * **/

vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    vector<int> res;
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());

    if (nums1.size() == 0 || nums2.size() == 0)
        return res;
    int x = 0;
    int y = 0;
    bool flag = true;
    int current = INT_MIN;

    while (flag)
    {
        if (x == nums1.size() or y == nums2.size())
            return res;
        else
        {
            if (nums1[x] == nums2[y] and nums1[x] != current)
            {
                res.insert(res.begin(), nums1[x]);
                current = nums1[x];
            }

            else if (nums1[x] < nums2[y])
                x += 1;
            else
                y += 1;
        }
    }
    return res;
}

int main()
{
    int arr[] = { 1, 2, 1 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    vector<int> nums1(arr, arr + n);

    int arr2[] = { 7, 8, 5, 7, 4 }; 
    int n2 = sizeof(arr2) / sizeof(arr2[0]); 
    vector<int> nums2(arr2, arr2 + n2);

    vector<int> result = intersection(nums1, nums2);

    // Expect result to be empty
    cout << "Size of vector result for [1,2,1] and [7,8,5,7,4]: " << result.size() << endl;

    // Inser 1 in 2nd vector
    nums2.insert(nums2.begin(), 1);
    result = intersection(nums1, nums2);

    // Expect result to be [1]
    std::vector<int>::iterator it = result.begin();
    while(it != result.end()) {
        cout << "Result after adding 1 to second array: " << *it << endl;
        it += 1;
    }

    return 0;
}
