# Web-auto-test-client

Testcase-Executor mode framework for web auto test. 

## Write test case by yaml format description

A test case contains four parts, they are:

1. test_infos
2. test_pres
3. test_steps
4. test_checks

### test_infos

This part is described abstract information of test case, must would write by the under format, see the under sample:

```yaml
test_infos:
  - id: test001
    check: 检查登录流程是否正常
    pre: 未登录
```

1. `id`: Custom by user with format that appointed.
2. `check`: Description for the test case goal.
3. `pre`: Description for the test case before execute.

### test_pres

This part is described operation steps before execute test case, then we can to learn structure of `test_pres` and `test_steps` and 
`test_checks`. See under the sample.

```yaml
test_pres:
  - operation_type: driver
    operation_action: open_url
    value: https://keepwork.com/
    info: 打开网站
  - operation_type: wait
    operation_action: wait
    value: 5000 (the value‘s unit is millisecond)
    info: 等待5s
  - operation_type: element
    operation_action: find
    value: xpath string or other locate way
    info: 查找“登录”按钮是否存在？
```

**operation_type**

Define operation type for the execute-step, it contains five types:

1. `driver`: About some operations of driver, ex: start and stop session or open and close browser; 
2. `browser`: About some special operations of per browser;
3. `wait`: About wait operation of steps;
4. `element`: About some operations of element, ex: find element and file upload;
5. `interaction`: About some interaction operations of browser, ex: get current page title from browser;
6. `interface`: About some operations of input and output device, ex: mouse, keyboard;
7. `double-protocol`: About some operations of double protocol client and browser; 
8. `additional`: About some operations of selenium provided additional;
9. `trouble-removal`: About some operations of selenium provided trouble removal;

**operation_action and other keys**

Define operation action for the execute-step. It is for `operation_type`, that seem like subset of `operation_type`. The
under list gave all of `operation_action` and relation sunset key description. Per subset of `operation_action` are not 
same, that is important point.

I think `opeartion_type` subset need to write as you do!!! 

1. driver
   1. actions todo
2. browser
   1. actions todo
3. wait
   1. actions todo
4. element
   1. actions todo
5. interaction
   1. actions todo
6. interface
   1. actions todo
7. double-protocol
   1. actions todo
8. additional
   1. actions todo
9. trouble-removal
   1. actions todo

### test_steps

Refer to **test_pres** part.

### test_checks

Refer to **test_pres** part.

