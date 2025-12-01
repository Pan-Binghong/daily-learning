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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI6YNMAV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCOg%2BWMKRy7OTm%2BXvyfqqrxMinw%2Bt4zo0sYnJCVS7bkoAIgDjogoTP3iQpL8UWZKKgNpvAxTehlDXpqOy95BOeGLMgqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNikJNCwrfrwB299jircA9IYVqMI8WJ3UwdeEuDzyhSK%2FNHmV1GZhiIIjpyXKUye%2BNFzFi8v863o30RcZ7A9BJEHEz0Xb7i27rYWmeFm%2FVTiqTJiZIApkPX9kDtxCV13sP3xX5LKc3CcPbIci3fJT%2F69x0bWefnOT%2BCEL4sjuQV3bYaMzVIKrQI3NxDaLo2MRyGjlbedCuwrnGOLrlFRMXl89xTf4CV1%2F2O4CsJEQOpkuF3dJo3s7ytCvyiCJwYGn%2BduVwwhU4hSBQREg9wK1tWSStvG2wQNYphfmZFsl0NLuk4t%2FbTd9%2BvfCiZuEMuJuMdRf5gKJdTT4ivhVMCeF03BhdKvjihjip4j1OGnk8U7rteYZj0Tf6pRPYzR2dor58jQOn8T5Xrwi9ckWM9OI0EkfKDAglILflffi8y8X0wnIKHAKxe3Jumm6jCmxTWbv1Xe4s4jAHoutAD%2Bbfz5NFEhQPDNwDvjz2I52NmowfqfYv889p8It9HRw74mlwkON%2FeYnEaidDpuhdDFDvAD4lfp8%2BnjLCYxAO9IaGaO6WDjPsJzTmPgWu9unUDx9cO0sFCItRHgC%2Fj6JvbyBSkTqGHcNS4dVbYvTGs0YrFwj1t1eEzVOIuCftcomkCyn2LXrFDw7NifgDphlbr1MKmFs8kGOqUBvyN7mXimYf2CvLeLdd1EPgAJyVZJsCONr8GPnrMGMnsUy%2FnbQqoozbvaxQEBc%2BUpbJLJTZN%2Fq%2BuCRoZtO%2FMwgt1AWyvcWBosTOcJ9%2FNHYmaBmLZh8%2Fy7%2BJp0brMIXRu33%2F5Y8k5LSXfIgkwqU5jUbMU9wl8rkfup8JYWe7SMjz%2BeIe4DCpgqUSCLobealA%2BXY2iRlDZrpxsA6QrUJMKen1gf12Fs&X-Amz-Signature=e2be5501ce362142da442c8afbc101e1bda28668040b51987786bb22c7c48aaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI6YNMAV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCOg%2BWMKRy7OTm%2BXvyfqqrxMinw%2Bt4zo0sYnJCVS7bkoAIgDjogoTP3iQpL8UWZKKgNpvAxTehlDXpqOy95BOeGLMgqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNikJNCwrfrwB299jircA9IYVqMI8WJ3UwdeEuDzyhSK%2FNHmV1GZhiIIjpyXKUye%2BNFzFi8v863o30RcZ7A9BJEHEz0Xb7i27rYWmeFm%2FVTiqTJiZIApkPX9kDtxCV13sP3xX5LKc3CcPbIci3fJT%2F69x0bWefnOT%2BCEL4sjuQV3bYaMzVIKrQI3NxDaLo2MRyGjlbedCuwrnGOLrlFRMXl89xTf4CV1%2F2O4CsJEQOpkuF3dJo3s7ytCvyiCJwYGn%2BduVwwhU4hSBQREg9wK1tWSStvG2wQNYphfmZFsl0NLuk4t%2FbTd9%2BvfCiZuEMuJuMdRf5gKJdTT4ivhVMCeF03BhdKvjihjip4j1OGnk8U7rteYZj0Tf6pRPYzR2dor58jQOn8T5Xrwi9ckWM9OI0EkfKDAglILflffi8y8X0wnIKHAKxe3Jumm6jCmxTWbv1Xe4s4jAHoutAD%2Bbfz5NFEhQPDNwDvjz2I52NmowfqfYv889p8It9HRw74mlwkON%2FeYnEaidDpuhdDFDvAD4lfp8%2BnjLCYxAO9IaGaO6WDjPsJzTmPgWu9unUDx9cO0sFCItRHgC%2Fj6JvbyBSkTqGHcNS4dVbYvTGs0YrFwj1t1eEzVOIuCftcomkCyn2LXrFDw7NifgDphlbr1MKmFs8kGOqUBvyN7mXimYf2CvLeLdd1EPgAJyVZJsCONr8GPnrMGMnsUy%2FnbQqoozbvaxQEBc%2BUpbJLJTZN%2Fq%2BuCRoZtO%2FMwgt1AWyvcWBosTOcJ9%2FNHYmaBmLZh8%2Fy7%2BJp0brMIXRu33%2F5Y8k5LSXfIgkwqU5jUbMU9wl8rkfup8JYWe7SMjz%2BeIe4DCpgqUSCLobealA%2BXY2iRlDZrpxsA6QrUJMKen1gf12Fs&X-Amz-Signature=5fcea1d56baa54b78f4109edd5adf8b262bd19e5063544826f0e41d893f80ffe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI6YNMAV%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQCOg%2BWMKRy7OTm%2BXvyfqqrxMinw%2Bt4zo0sYnJCVS7bkoAIgDjogoTP3iQpL8UWZKKgNpvAxTehlDXpqOy95BOeGLMgqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNikJNCwrfrwB299jircA9IYVqMI8WJ3UwdeEuDzyhSK%2FNHmV1GZhiIIjpyXKUye%2BNFzFi8v863o30RcZ7A9BJEHEz0Xb7i27rYWmeFm%2FVTiqTJiZIApkPX9kDtxCV13sP3xX5LKc3CcPbIci3fJT%2F69x0bWefnOT%2BCEL4sjuQV3bYaMzVIKrQI3NxDaLo2MRyGjlbedCuwrnGOLrlFRMXl89xTf4CV1%2F2O4CsJEQOpkuF3dJo3s7ytCvyiCJwYGn%2BduVwwhU4hSBQREg9wK1tWSStvG2wQNYphfmZFsl0NLuk4t%2FbTd9%2BvfCiZuEMuJuMdRf5gKJdTT4ivhVMCeF03BhdKvjihjip4j1OGnk8U7rteYZj0Tf6pRPYzR2dor58jQOn8T5Xrwi9ckWM9OI0EkfKDAglILflffi8y8X0wnIKHAKxe3Jumm6jCmxTWbv1Xe4s4jAHoutAD%2Bbfz5NFEhQPDNwDvjz2I52NmowfqfYv889p8It9HRw74mlwkON%2FeYnEaidDpuhdDFDvAD4lfp8%2BnjLCYxAO9IaGaO6WDjPsJzTmPgWu9unUDx9cO0sFCItRHgC%2Fj6JvbyBSkTqGHcNS4dVbYvTGs0YrFwj1t1eEzVOIuCftcomkCyn2LXrFDw7NifgDphlbr1MKmFs8kGOqUBvyN7mXimYf2CvLeLdd1EPgAJyVZJsCONr8GPnrMGMnsUy%2FnbQqoozbvaxQEBc%2BUpbJLJTZN%2Fq%2BuCRoZtO%2FMwgt1AWyvcWBosTOcJ9%2FNHYmaBmLZh8%2Fy7%2BJp0brMIXRu33%2F5Y8k5LSXfIgkwqU5jUbMU9wl8rkfup8JYWe7SMjz%2BeIe4DCpgqUSCLobealA%2BXY2iRlDZrpxsA6QrUJMKen1gf12Fs&X-Amz-Signature=e4023177dcf8dabe7a5bc9f401f30a54897203889f831bd1923af5384372225c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

