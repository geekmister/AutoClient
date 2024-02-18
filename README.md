# cd-auto-test-client

Auto test client of Calculbility Document. 

## Test case write description for yaml file

Contains four parts:

1. test_infos
2. test_pres
3. test_steps
4. test_checks

### test_infos

This part is described abstract information of test case, must would write by the format, see the sample:

```yaml
test_infos:
  - id: test001
    check: 检查登录流程是否正常
    pre: 未登录
```

1. id: Custom by user with format that appointed.
2. check: Description for the test case goal.
3. pre: Description for the test case before execute.

### test_pres

This part is described operation steps before test case execute, must would write bt the format, see the sample:

```yaml
test_pres:
  - operation_type: driver
    operation_action: open_url
    value: https://keepwork.com/
    info: 打开网站
  - operation_type: others
    operation_action: wait
    value: 5000 (the value‘s unit is millisecond)
    info: 等待5s
  - operation_type: others
    operation_action: find
    value: xpath string or other locate way
    info: 查找“登录”按钮是否存在？
```

1. operation_type: operation_type's value is described operation type that contains:
   1) driver: About operation for webdriver;
   2) others: Some operation type is not sort easy like wait and find for structure clear, so these operation type sort to others and divide by operation_action.
   3) element: About operation for find element;
   4) mouse: About operation for mouse;
   5) keyboard: About operation for keyboard;
2. operate_action

