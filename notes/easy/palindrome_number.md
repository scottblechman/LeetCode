#[9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
| Submission Detail  | Value |
| ------------- | ------------- |
| Status  | Accepted  |
| Test Cases Passed  | 11509 / 11509  |
| Runtime  | 52 ms (87th percentile) |
| Memory Usage  | 12.7 MB (100th percentile)  |

## Implementation Notes
For this problem, an optimal solution was found while implementing a brute-force solution.

Two assumptions were made when studying the problem. The function should return False if and only if one of the following conditions were met:
* The absolute value of the integer was different when read backwards versus forwards;
* The integer was negative

A less-than-zero check was trivial, but a comparison was not. The brute-force approach I selected was to cast the integer to a string (assuming the function had already returned False if the integer was negative), and check if the reverse of said string was equal to the original. This solution produced an optimal space complexity and near-optimal time complexity, so a more optimal solution was not attempted.

The follow-up to this problem, a solution without converting the integer to a string, was not attempted alongside the initial submission. A revision is planned to add the solution.