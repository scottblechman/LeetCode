# LeetCode
## Scott Blechman

![tests](https://github.com/scottblechman/LeetCode/workflows/tests/badge.svg)

### Overview
Solutions are categorized by difficulty (e.g. Easy, Medium, Hard). All solutions are written in Python 3.8+. Not every solution is optimal (optimized solutions are noted, along with the complexities).

Each solution includes:
* Python implementation
* Unit test(s) (verified during CI)
* Implementation notes ("thought process")

### Repository Structure
```
LeetCode
│   README.md
│   LICENSE
│
└───solutions
│   │
│   └───easy
│       │   problem_title_one.py
│       │   problem_title_two.py
│       │   ...
│   
└───tests
│   │
│   └───easy
│       │   problem_title_one_test.py
│       │   problem_title_two_test.py
│       │   ...
│   
└───notes
│   │
│   └───easy
│       │   problem_title_one.md
│       │   problem_title_two.md
│       │   ...
```

### Libraries
* Pytest - unit testing

### Contributing
If you find an error or would like to see a certain test case for a solution, feel free to open an issue. For new test cases, describe the input and expected output in your issue, and put the problem number in the title. Algorithms may change if a proposed test case does not pass; changes will not be merged unless the new solution passes all LeetCode tests.