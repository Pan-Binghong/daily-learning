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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBXWAOTM%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQD0Y8zIPnVVw7ncu5CZ0dqVYW9FdenlKWdyCQChv5QOVwIgAiXHf924pQGULWfETVJqALbXSvEAAzbNNCFFEikTVy0qiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsesgIb%2BQ24WiaHwircA7uFWLfLYgReuPuKe2cZSpH85S%2FxEG2OXUFJetlIyEtb%2B4e83tLnICtlW1Xt8NoE8cBpTm6tIR1PWGpbPcnt5EJ7gKMDo4X3%2BUjGvHR9y1IxxbUKZtYe1%2Ffb3XADm41i5W%2FTnB200c9TTnVAj1lkH4vcBabrZreO%2FjBsTIZzn995BW2a%2FC8oma9HBktC%2FgL8xhI1AmJw5QgfvadUDVqD7Yf%2B2imbfwq1ltEH6HNLwmGoSoTVRY2uwA3anNXsoFEeigGQjK4Y5LbLjk7osWhYbnxWrgDA7SnbsFo6c6lLfQ9nysdninohOdhje7l78lcYktZFA5k6EDqXaSjEnXldVu4yPSb8XlQKpieEDWS25AEy5Uyv41rxQ21QfxaUnapJyq7l0mg3j09GkyWIKvKm%2BXonK4RiSmDLfVHYvtO5mJf4b4j%2F2GjYrwZji9sUKusbEpAmPRZJo1aWyY63Pf2RwwaYtYr7%2F05SVK%2FNIvGbk1Nk%2B1cCz6zbCMqj287NxKVoXjaRt5RqMQ9Z1DIyS92Kw11ZOfTeiYGjHkiqLP5G80YHxQXZ5DbK5PDI60I1h2O%2FlujihcbllvQ%2Bj3qdBVqpxab%2FaFPEVvEYd3j2yNz5LMhnBjMgEGNTIq6mAqHVMK7twM8GOqUBzOr7IZPpQNsvu%2FlB37reFV713uFsfMg60OTZAuPFgItPqx%2FGniEZRPHk5p%2BKXOdcgWzrs67Egu06B9pCicibl9BVbU1qeaN9DcCqKvREbWnz7vhOYLyJP80RG4w1YA4k9Y4IJpwaLnwofjw10b8QmmolUqaXGEvFB5adVC25UkUBA2HKZrpfWahn0UNAcAUGRv7pyyYFKHFGAPHcHRAXHXGwZxnk&X-Amz-Signature=50f2f69435fc8425153c1e4682fcf34fdac3ab87025e03b6308d36101060d073&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBXWAOTM%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQD0Y8zIPnVVw7ncu5CZ0dqVYW9FdenlKWdyCQChv5QOVwIgAiXHf924pQGULWfETVJqALbXSvEAAzbNNCFFEikTVy0qiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsesgIb%2BQ24WiaHwircA7uFWLfLYgReuPuKe2cZSpH85S%2FxEG2OXUFJetlIyEtb%2B4e83tLnICtlW1Xt8NoE8cBpTm6tIR1PWGpbPcnt5EJ7gKMDo4X3%2BUjGvHR9y1IxxbUKZtYe1%2Ffb3XADm41i5W%2FTnB200c9TTnVAj1lkH4vcBabrZreO%2FjBsTIZzn995BW2a%2FC8oma9HBktC%2FgL8xhI1AmJw5QgfvadUDVqD7Yf%2B2imbfwq1ltEH6HNLwmGoSoTVRY2uwA3anNXsoFEeigGQjK4Y5LbLjk7osWhYbnxWrgDA7SnbsFo6c6lLfQ9nysdninohOdhje7l78lcYktZFA5k6EDqXaSjEnXldVu4yPSb8XlQKpieEDWS25AEy5Uyv41rxQ21QfxaUnapJyq7l0mg3j09GkyWIKvKm%2BXonK4RiSmDLfVHYvtO5mJf4b4j%2F2GjYrwZji9sUKusbEpAmPRZJo1aWyY63Pf2RwwaYtYr7%2F05SVK%2FNIvGbk1Nk%2B1cCz6zbCMqj287NxKVoXjaRt5RqMQ9Z1DIyS92Kw11ZOfTeiYGjHkiqLP5G80YHxQXZ5DbK5PDI60I1h2O%2FlujihcbllvQ%2Bj3qdBVqpxab%2FaFPEVvEYd3j2yNz5LMhnBjMgEGNTIq6mAqHVMK7twM8GOqUBzOr7IZPpQNsvu%2FlB37reFV713uFsfMg60OTZAuPFgItPqx%2FGniEZRPHk5p%2BKXOdcgWzrs67Egu06B9pCicibl9BVbU1qeaN9DcCqKvREbWnz7vhOYLyJP80RG4w1YA4k9Y4IJpwaLnwofjw10b8QmmolUqaXGEvFB5adVC25UkUBA2HKZrpfWahn0UNAcAUGRv7pyyYFKHFGAPHcHRAXHXGwZxnk&X-Amz-Signature=4321bfcd59da2ed0393d9221cffe337b8935916b3301126305d651b106b5cb9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBXWAOTM%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQD0Y8zIPnVVw7ncu5CZ0dqVYW9FdenlKWdyCQChv5QOVwIgAiXHf924pQGULWfETVJqALbXSvEAAzbNNCFFEikTVy0qiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsesgIb%2BQ24WiaHwircA7uFWLfLYgReuPuKe2cZSpH85S%2FxEG2OXUFJetlIyEtb%2B4e83tLnICtlW1Xt8NoE8cBpTm6tIR1PWGpbPcnt5EJ7gKMDo4X3%2BUjGvHR9y1IxxbUKZtYe1%2Ffb3XADm41i5W%2FTnB200c9TTnVAj1lkH4vcBabrZreO%2FjBsTIZzn995BW2a%2FC8oma9HBktC%2FgL8xhI1AmJw5QgfvadUDVqD7Yf%2B2imbfwq1ltEH6HNLwmGoSoTVRY2uwA3anNXsoFEeigGQjK4Y5LbLjk7osWhYbnxWrgDA7SnbsFo6c6lLfQ9nysdninohOdhje7l78lcYktZFA5k6EDqXaSjEnXldVu4yPSb8XlQKpieEDWS25AEy5Uyv41rxQ21QfxaUnapJyq7l0mg3j09GkyWIKvKm%2BXonK4RiSmDLfVHYvtO5mJf4b4j%2F2GjYrwZji9sUKusbEpAmPRZJo1aWyY63Pf2RwwaYtYr7%2F05SVK%2FNIvGbk1Nk%2B1cCz6zbCMqj287NxKVoXjaRt5RqMQ9Z1DIyS92Kw11ZOfTeiYGjHkiqLP5G80YHxQXZ5DbK5PDI60I1h2O%2FlujihcbllvQ%2Bj3qdBVqpxab%2FaFPEVvEYd3j2yNz5LMhnBjMgEGNTIq6mAqHVMK7twM8GOqUBzOr7IZPpQNsvu%2FlB37reFV713uFsfMg60OTZAuPFgItPqx%2FGniEZRPHk5p%2BKXOdcgWzrs67Egu06B9pCicibl9BVbU1qeaN9DcCqKvREbWnz7vhOYLyJP80RG4w1YA4k9Y4IJpwaLnwofjw10b8QmmolUqaXGEvFB5adVC25UkUBA2HKZrpfWahn0UNAcAUGRv7pyyYFKHFGAPHcHRAXHXGwZxnk&X-Amz-Signature=b14ea79b3dd80171420b0b12fe80084262bfcab992b2c0ff5447503ad0a9bf57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

