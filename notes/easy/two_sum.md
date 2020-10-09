# [1. Two Sum](https://leetcode.com/problems/two-sum/)
| Submission Detail  | Value |
| ------------- | ------------- |
| Status  | Accepted  |
| Test Cases Passed  | 29 / 29  |
| Runtime  | 1080 ms (29th percentile) |
| Memory Usage  | 12.8 MB (66th percentile)  |

## Implementation Notes
For the initial solution, the approach was to iterate over the indices of the list, checking if the values match the target. For each element in the list, a nested iterator would compare it to the other elements. I was able to use the assumptions to guide the approach. For example, knowing that a two-length list could exist means that we can check if the list has two elements, then just return indices 0 and 1. Also, knowing that the approach might try to match the same index to itself, I added a clause to the condition to not return if x and y were the same.

However, this approach isn't optimal (it is O(n^2)), and didn't pass all cases due to the time limit. To improve this, I took a different approach: go through each element in the list, and check if the difference between the target and the element also exists, then return both indices. This simplifies the complexity to O(n) and passes all test cases under the time limit.

Since the test cases have passed, the next step will be to improve the runtime and memory usage of the solution, since they are low compared to other python submissions.