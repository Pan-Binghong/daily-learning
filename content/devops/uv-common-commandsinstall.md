---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAW7LW7%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQCDhNtZCgsuwRuwIa77LttkYQreYLctmSiQ5KkAWRRCZwIhANKeTltdwYc94gyIFYX6d%2B%2BADbfuM7Gjw%2FPsf6aUGHG0KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGHNibi%2BYjnquams8q3AN3rHWWubn3%2FvfVBeL1rGZrPXrKYhNuZ%2BK%2Be6t3YhEd7nededAzY0Tbd9fTENTHCtx4emHNSh%2B4iuFb6iaHYqgcitOoxUBIn7KOw04TzTIzQDRny3pTzJRwOnS9Gpeg8tJZ0X3gUVjt60F7pM%2FZzOzHZMSNAJw3LnhrjPUXoXNyqyVgRnBaU4nFNqLCsCzTRB%2B5h3fnS8BJrob9J87VzhFgMs9XtR20uHE2wgJzjaS8Fg98wZIWx93volO2%2BNJhDpc19pA%2BbJSuJt56aaaDQBgmCR8kJOpIhNlTWJc3mEanNj2vEQ3wLZAvDif7NLL4iEqEkEmqK8B5Zcj8Dt4HEdlPXnXtOCXm7zfbvY%2F1HzrYxAWnMtQPj5tq%2F6yV7QVSAC9TN6j5AkMDQ8wTCTrEI%2BPSF3BAg7qykW6uQ3Li%2FKdFCzLb0YZ%2FGhV%2F7qaCyx%2BK9x5A6BsAsEgW7FQVpkkhogeArF1%2FtvUDvpFl6baVFq9%2B8H%2BqgARvbif542cx6hyod44vG3k1bvh6xM19nPkbt5v5p5n39pkljGjAXmRXhuvXY1grLo1yOYkEfYezBep1rV0DhmMSCIhK59avb2VbbGXX%2BOua9HzoZ3drxPkisYbyY8DLJBm%2BuG%2Bp5R6qJzD3tPTMBjqkAY2BeVRwixMVB%2FvRiqSgxYsg9xMJ%2BJazbz7ncXillO2vxw0PiaGfRYoFHe%2BGrIEPd6miGj6tlrExvC%2Bh2OOuMd%2FnoLHSN27Ps6RxLN7BWW4EZQGkiWf3bnmJeV%2FLYMkfQbfkDhCG4VIUWbZ8U%2BylksGxMiSsARn%2BR5001iKLT9CqLhF8n9YzFl4gHFyYm99GjqEi1muLHzb%2FLBEm%2B2A8PTAgPpbl&X-Amz-Signature=a530d50682e7c90766a9c02c47528e9deff1860c4074a15ca8ac9d7de2cb64bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAW7LW7%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQCDhNtZCgsuwRuwIa77LttkYQreYLctmSiQ5KkAWRRCZwIhANKeTltdwYc94gyIFYX6d%2B%2BADbfuM7Gjw%2FPsf6aUGHG0KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGHNibi%2BYjnquams8q3AN3rHWWubn3%2FvfVBeL1rGZrPXrKYhNuZ%2BK%2Be6t3YhEd7nededAzY0Tbd9fTENTHCtx4emHNSh%2B4iuFb6iaHYqgcitOoxUBIn7KOw04TzTIzQDRny3pTzJRwOnS9Gpeg8tJZ0X3gUVjt60F7pM%2FZzOzHZMSNAJw3LnhrjPUXoXNyqyVgRnBaU4nFNqLCsCzTRB%2B5h3fnS8BJrob9J87VzhFgMs9XtR20uHE2wgJzjaS8Fg98wZIWx93volO2%2BNJhDpc19pA%2BbJSuJt56aaaDQBgmCR8kJOpIhNlTWJc3mEanNj2vEQ3wLZAvDif7NLL4iEqEkEmqK8B5Zcj8Dt4HEdlPXnXtOCXm7zfbvY%2F1HzrYxAWnMtQPj5tq%2F6yV7QVSAC9TN6j5AkMDQ8wTCTrEI%2BPSF3BAg7qykW6uQ3Li%2FKdFCzLb0YZ%2FGhV%2F7qaCyx%2BK9x5A6BsAsEgW7FQVpkkhogeArF1%2FtvUDvpFl6baVFq9%2B8H%2BqgARvbif542cx6hyod44vG3k1bvh6xM19nPkbt5v5p5n39pkljGjAXmRXhuvXY1grLo1yOYkEfYezBep1rV0DhmMSCIhK59avb2VbbGXX%2BOua9HzoZ3drxPkisYbyY8DLJBm%2BuG%2Bp5R6qJzD3tPTMBjqkAY2BeVRwixMVB%2FvRiqSgxYsg9xMJ%2BJazbz7ncXillO2vxw0PiaGfRYoFHe%2BGrIEPd6miGj6tlrExvC%2Bh2OOuMd%2FnoLHSN27Ps6RxLN7BWW4EZQGkiWf3bnmJeV%2FLYMkfQbfkDhCG4VIUWbZ8U%2BylksGxMiSsARn%2BR5001iKLT9CqLhF8n9YzFl4gHFyYm99GjqEi1muLHzb%2FLBEm%2B2A8PTAgPpbl&X-Amz-Signature=f44eb95c3c1b95486f2f12a76b4e12dcb9e836ec7bfc910707e7a47395ddb78a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAW7LW7%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQCDhNtZCgsuwRuwIa77LttkYQreYLctmSiQ5KkAWRRCZwIhANKeTltdwYc94gyIFYX6d%2B%2BADbfuM7Gjw%2FPsf6aUGHG0KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGHNibi%2BYjnquams8q3AN3rHWWubn3%2FvfVBeL1rGZrPXrKYhNuZ%2BK%2Be6t3YhEd7nededAzY0Tbd9fTENTHCtx4emHNSh%2B4iuFb6iaHYqgcitOoxUBIn7KOw04TzTIzQDRny3pTzJRwOnS9Gpeg8tJZ0X3gUVjt60F7pM%2FZzOzHZMSNAJw3LnhrjPUXoXNyqyVgRnBaU4nFNqLCsCzTRB%2B5h3fnS8BJrob9J87VzhFgMs9XtR20uHE2wgJzjaS8Fg98wZIWx93volO2%2BNJhDpc19pA%2BbJSuJt56aaaDQBgmCR8kJOpIhNlTWJc3mEanNj2vEQ3wLZAvDif7NLL4iEqEkEmqK8B5Zcj8Dt4HEdlPXnXtOCXm7zfbvY%2F1HzrYxAWnMtQPj5tq%2F6yV7QVSAC9TN6j5AkMDQ8wTCTrEI%2BPSF3BAg7qykW6uQ3Li%2FKdFCzLb0YZ%2FGhV%2F7qaCyx%2BK9x5A6BsAsEgW7FQVpkkhogeArF1%2FtvUDvpFl6baVFq9%2B8H%2BqgARvbif542cx6hyod44vG3k1bvh6xM19nPkbt5v5p5n39pkljGjAXmRXhuvXY1grLo1yOYkEfYezBep1rV0DhmMSCIhK59avb2VbbGXX%2BOua9HzoZ3drxPkisYbyY8DLJBm%2BuG%2Bp5R6qJzD3tPTMBjqkAY2BeVRwixMVB%2FvRiqSgxYsg9xMJ%2BJazbz7ncXillO2vxw0PiaGfRYoFHe%2BGrIEPd6miGj6tlrExvC%2Bh2OOuMd%2FnoLHSN27Ps6RxLN7BWW4EZQGkiWf3bnmJeV%2FLYMkfQbfkDhCG4VIUWbZ8U%2BylksGxMiSsARn%2BR5001iKLT9CqLhF8n9YzFl4gHFyYm99GjqEi1muLHzb%2FLBEm%2B2A8PTAgPpbl&X-Amz-Signature=99ce12337d797f027fd8b63a2702b3f3594710156fca0fd9723a94160f739062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

