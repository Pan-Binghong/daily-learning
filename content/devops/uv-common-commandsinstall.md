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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T4Q2QDT%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF07n31yvXU2KYDba7KA8zPk6bzy%2FklrOIvB%2FnyYEnWOAiEAxfz9ejiUys5ElEdG0I6MlmY3El88oxvtvdsRt12Qvnwq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO2O%2BfvK%2FYO7AW%2BPjyrcA0oVXDgPP0QldcQrLBfh%2F4ZLX1RaUpV8hW3j6IVeE7iZVGkpy0Mk45LjYLRMgOyhWVDq9ho0gwnlJ0u9%2F0XiWyAlp4At2u5taVDpkMbkVSjjXPzr65Onx5QUJKQTgFK1B5ZHZ7YxinE8a4AoCPUxaFE%2F%2FAhuUiHRnRSdLDMiH4Q7FWvU1Osqh2Jdox9TTaWMI%2FsIiYGJkNBv2n5NThgex9Hzwo3T9MKMTxAUdty6cN5GK8rRcUQlCugsJZj8ZpOeRn%2FgGG91CEMkXfekq%2FIsSfXJ9SO6NG1mlt7we0dtRKaR4aJDxzVpV39hqo0WwGKW6ge1Y87krSAgVfEYbqC93ZcFYJNBMEKE8c97jC2lvLjPHXC3dACxvIKjX%2FKW13ALFOsnbDo9UcW%2BJTVa12HW4Ptoydq3c%2BPXqUbQVsrvTQiU6RR1c63MMEqk0Fg7IvLXiQ50uD334rp7kvnDjGByUOd6Iij2A3VRHio58ZnfYl25Nownpfdi33kdM49oKLfJmVcrBArnHU1BOb9XgzYUg7VyZObDLhCpGsXmFs%2BrALvxD1EAkmsjI9kFIZlrMVp4cWvvZ2jkvQMMsDdxwhEXsewdvwmx1zxPWcB3zQog%2BUjo2sWQR5%2FQuh5iZk8RMKes%2Fc0GOqUBSvlaSbpbS5KnnpKb3j7Drpnr0J6XCtrv1S6jBYu4f5Aq46ZhenvY0DkDtk7kEyNzl8X7MmNo5yX9Wko5QoNKTvWd8pWfgGngQAp0YcNDVnQuh79waPWd6UQyf%2BKyvRi%2BBN4TDky3FcA5CO3INTkib2MsRwYdkLaeB7wjYqaDdF1TTaO7AAfqIn0EHPzjXS8bTrngqXtTYY6TxmKAWyZG4lmApj1B&X-Amz-Signature=03196ca6e1c70ab6c5231012c460c03502390f89c576a583ffdc95e8231a4857&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T4Q2QDT%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF07n31yvXU2KYDba7KA8zPk6bzy%2FklrOIvB%2FnyYEnWOAiEAxfz9ejiUys5ElEdG0I6MlmY3El88oxvtvdsRt12Qvnwq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO2O%2BfvK%2FYO7AW%2BPjyrcA0oVXDgPP0QldcQrLBfh%2F4ZLX1RaUpV8hW3j6IVeE7iZVGkpy0Mk45LjYLRMgOyhWVDq9ho0gwnlJ0u9%2F0XiWyAlp4At2u5taVDpkMbkVSjjXPzr65Onx5QUJKQTgFK1B5ZHZ7YxinE8a4AoCPUxaFE%2F%2FAhuUiHRnRSdLDMiH4Q7FWvU1Osqh2Jdox9TTaWMI%2FsIiYGJkNBv2n5NThgex9Hzwo3T9MKMTxAUdty6cN5GK8rRcUQlCugsJZj8ZpOeRn%2FgGG91CEMkXfekq%2FIsSfXJ9SO6NG1mlt7we0dtRKaR4aJDxzVpV39hqo0WwGKW6ge1Y87krSAgVfEYbqC93ZcFYJNBMEKE8c97jC2lvLjPHXC3dACxvIKjX%2FKW13ALFOsnbDo9UcW%2BJTVa12HW4Ptoydq3c%2BPXqUbQVsrvTQiU6RR1c63MMEqk0Fg7IvLXiQ50uD334rp7kvnDjGByUOd6Iij2A3VRHio58ZnfYl25Nownpfdi33kdM49oKLfJmVcrBArnHU1BOb9XgzYUg7VyZObDLhCpGsXmFs%2BrALvxD1EAkmsjI9kFIZlrMVp4cWvvZ2jkvQMMsDdxwhEXsewdvwmx1zxPWcB3zQog%2BUjo2sWQR5%2FQuh5iZk8RMKes%2Fc0GOqUBSvlaSbpbS5KnnpKb3j7Drpnr0J6XCtrv1S6jBYu4f5Aq46ZhenvY0DkDtk7kEyNzl8X7MmNo5yX9Wko5QoNKTvWd8pWfgGngQAp0YcNDVnQuh79waPWd6UQyf%2BKyvRi%2BBN4TDky3FcA5CO3INTkib2MsRwYdkLaeB7wjYqaDdF1TTaO7AAfqIn0EHPzjXS8bTrngqXtTYY6TxmKAWyZG4lmApj1B&X-Amz-Signature=917456ebb07f939effe035909aded8829702faad1d3cd542a16532bdd48064a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T4Q2QDT%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF07n31yvXU2KYDba7KA8zPk6bzy%2FklrOIvB%2FnyYEnWOAiEAxfz9ejiUys5ElEdG0I6MlmY3El88oxvtvdsRt12Qvnwq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO2O%2BfvK%2FYO7AW%2BPjyrcA0oVXDgPP0QldcQrLBfh%2F4ZLX1RaUpV8hW3j6IVeE7iZVGkpy0Mk45LjYLRMgOyhWVDq9ho0gwnlJ0u9%2F0XiWyAlp4At2u5taVDpkMbkVSjjXPzr65Onx5QUJKQTgFK1B5ZHZ7YxinE8a4AoCPUxaFE%2F%2FAhuUiHRnRSdLDMiH4Q7FWvU1Osqh2Jdox9TTaWMI%2FsIiYGJkNBv2n5NThgex9Hzwo3T9MKMTxAUdty6cN5GK8rRcUQlCugsJZj8ZpOeRn%2FgGG91CEMkXfekq%2FIsSfXJ9SO6NG1mlt7we0dtRKaR4aJDxzVpV39hqo0WwGKW6ge1Y87krSAgVfEYbqC93ZcFYJNBMEKE8c97jC2lvLjPHXC3dACxvIKjX%2FKW13ALFOsnbDo9UcW%2BJTVa12HW4Ptoydq3c%2BPXqUbQVsrvTQiU6RR1c63MMEqk0Fg7IvLXiQ50uD334rp7kvnDjGByUOd6Iij2A3VRHio58ZnfYl25Nownpfdi33kdM49oKLfJmVcrBArnHU1BOb9XgzYUg7VyZObDLhCpGsXmFs%2BrALvxD1EAkmsjI9kFIZlrMVp4cWvvZ2jkvQMMsDdxwhEXsewdvwmx1zxPWcB3zQog%2BUjo2sWQR5%2FQuh5iZk8RMKes%2Fc0GOqUBSvlaSbpbS5KnnpKb3j7Drpnr0J6XCtrv1S6jBYu4f5Aq46ZhenvY0DkDtk7kEyNzl8X7MmNo5yX9Wko5QoNKTvWd8pWfgGngQAp0YcNDVnQuh79waPWd6UQyf%2BKyvRi%2BBN4TDky3FcA5CO3INTkib2MsRwYdkLaeB7wjYqaDdF1TTaO7AAfqIn0EHPzjXS8bTrngqXtTYY6TxmKAWyZG4lmApj1B&X-Amz-Signature=112c1838c82c31a031871b205e23aa84d413b53dc9d749311d7390b8ddcd4d0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

