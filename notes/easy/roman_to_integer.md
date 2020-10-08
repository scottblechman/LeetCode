# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
| Submission Detail  | Value |
| ------------- | ------------- |
| Status  | Accepted  |
| Test Cases Passed  | 3999 / 3999  |
| Runtime  | 36 ms (98th percentile) |
| Memory Usage  | 12.8 MB (100th percentile)  |

## Implementation Notes
The optimal solution to this problem was fairly straightforward, and effectively the same as the brute-force solution. Some assumptions were made, such as the validity of the string, but others weren't as relevant in the solution, such as the length of the string.

The algorithm ends up being a simple parser, with one and sometimes two-character tokens affecting the final value. Some basic handling of two-character tokens and their respective values is added, but otherwise the algorithm mainly matches the current character to an integer value sequentially.
