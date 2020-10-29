# backend API

## Making a test request


- URL: test/<question_name>
- POST Request
    - solution: *str*
- Response
    - test_results: *list of test_result*

- Types
    - test_result
        - test_name: *str*
        - input_list: *list of input*
        - expected: *str*
        - actual: *str*
    - input
        - input_name: *str*
        - input_value: *str*

