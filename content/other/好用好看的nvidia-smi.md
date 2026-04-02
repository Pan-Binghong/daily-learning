---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGIL3ZL%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZ%2FGgzdutgh2FNHAXqV18e%2Fklsvnhqp9FcjL2rnDgzBQIgAzblDSmEDup3BAOCC%2BCCK%2Be7sGceFTsgTgMYfAZO%2FdMq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDBb9Zwt8KVn1Ntl0RircA8rB2ZfCAWlj%2FmTqSwDtIKc11zaFSVMsdMDAcuWoAHEprAPHdVr6oZMTBtKdWuDj6u9Xm75ONqYzAFB1iH6QH4mDrzAFSIzvWo9SjqizwHXIHwjDfbqKBk%2B7LPGXTsUCRknoK%2B%2FcjO8r9CWm2G%2BzD16fFh%2BODTJxdfYkeihHv8U9ihBFjjtA28q2HNuWYvdkJdoYYYr90BGX8MF7AqzUAs%2B%2F%2BOnN9hlRw%2BB%2Fcsqg15zvk54DP4TLnRytTQyJv7N9FCEeao%2FCoYf7vwxp24lGQ2kOcCz2Cmg0CAc2AVbsCjyAuo2rkGX%2FD1AkFfJLPERagvvgTjDD03GJvRK%2BmWpo3qlAUGx%2FV6i5kxj5ldOfC2zh833L4ikET6ynFHOTVOR0sZuQKWJaFaaug3dtVsxB87Ny9ICOZC9dUyRYVDyv9bzFQs3hvMGhnd6OhARduj147BCXuzfS1Yks%2FwnL1tq5BUNx%2BfP96a59A%2BVvn6TgZgBndG64qnWOsf7CmYYg3R%2B9gda0qaGhJz5MVXsB0SJ1gsXgfVgyfUlpG5aJP06MoK%2Bdk5shjxpbEOtNO07dIzwfwLqIzhILjEuL9OZ%2FKqfOxjit42qSYL5ggS%2BpPj%2F380fy0iWG8rZbZopClYk5MImvt84GOqUBan79orWrd216%2BMsAakkg8pdoXc7Cixc6TrykLYQkIl9PMEY1G6FXkL3rjG2uL%2BfHSZko9O9lgJLA9qxjdfts4PpHtaBRjGt94AUVys0KL8baEAi3YXjOm%2F%2BwAYXhQeKHUAezSHXhqrG1d0uZOYTFQ%2Ft7ew90MUnUQHDXyKMlpZ2pMhbPOpCk2PGPRwLcABraJqxvK8%2Fsqqrvt7AW0in0sRZtqDCs&X-Amz-Signature=1a8c027f44795dec8b24ce29fe3826f18f6cf57a88ff49440f2904acd6e3e960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VGIL3ZL%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZ%2FGgzdutgh2FNHAXqV18e%2Fklsvnhqp9FcjL2rnDgzBQIgAzblDSmEDup3BAOCC%2BCCK%2Be7sGceFTsgTgMYfAZO%2FdMq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDBb9Zwt8KVn1Ntl0RircA8rB2ZfCAWlj%2FmTqSwDtIKc11zaFSVMsdMDAcuWoAHEprAPHdVr6oZMTBtKdWuDj6u9Xm75ONqYzAFB1iH6QH4mDrzAFSIzvWo9SjqizwHXIHwjDfbqKBk%2B7LPGXTsUCRknoK%2B%2FcjO8r9CWm2G%2BzD16fFh%2BODTJxdfYkeihHv8U9ihBFjjtA28q2HNuWYvdkJdoYYYr90BGX8MF7AqzUAs%2B%2F%2BOnN9hlRw%2BB%2Fcsqg15zvk54DP4TLnRytTQyJv7N9FCEeao%2FCoYf7vwxp24lGQ2kOcCz2Cmg0CAc2AVbsCjyAuo2rkGX%2FD1AkFfJLPERagvvgTjDD03GJvRK%2BmWpo3qlAUGx%2FV6i5kxj5ldOfC2zh833L4ikET6ynFHOTVOR0sZuQKWJaFaaug3dtVsxB87Ny9ICOZC9dUyRYVDyv9bzFQs3hvMGhnd6OhARduj147BCXuzfS1Yks%2FwnL1tq5BUNx%2BfP96a59A%2BVvn6TgZgBndG64qnWOsf7CmYYg3R%2B9gda0qaGhJz5MVXsB0SJ1gsXgfVgyfUlpG5aJP06MoK%2Bdk5shjxpbEOtNO07dIzwfwLqIzhILjEuL9OZ%2FKqfOxjit42qSYL5ggS%2BpPj%2F380fy0iWG8rZbZopClYk5MImvt84GOqUBan79orWrd216%2BMsAakkg8pdoXc7Cixc6TrykLYQkIl9PMEY1G6FXkL3rjG2uL%2BfHSZko9O9lgJLA9qxjdfts4PpHtaBRjGt94AUVys0KL8baEAi3YXjOm%2F%2BwAYXhQeKHUAezSHXhqrG1d0uZOYTFQ%2Ft7ew90MUnUQHDXyKMlpZ2pMhbPOpCk2PGPRwLcABraJqxvK8%2Fsqqrvt7AW0in0sRZtqDCs&X-Amz-Signature=df6305c7adf097a1bc300b5b9bae33689afb94f2d74b36dea12138cab0fa1396&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









