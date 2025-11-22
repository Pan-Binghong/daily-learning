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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKPJYZQH%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCUyhaXHLOrEWTb4grnKizgxc3ZbWVuIGTbKVT%2F3%2Bt16wIgUOydLTFIEXcW6zw0yR4juOS561c6%2FfAQThHZ%2B%2FTbj1Yq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDPbmuL638be388vlaircA097%2BYcldaAN%2FkILR5GVoT6k1xsJiuEt2Owl3Q1NADvneMDvxFYX8B%2BR8xbS0qKMYoWWsMJmS8izv9JjvNAzOwzEES6Iw%2BIy6xyZ7nRKHpCek8WuPOnY3PPFiG4hXuOVw0Z7FZ7IFWrORRs6xAEGAPKv%2Bh%2BJ%2BhUoDMGjp2yAEEaoCTbLw7tYZPyHwQcl5q5rFx3p9FpVOIJMGxO7p7K5RE98ohQavDNagNfCzUkiX5D8LUWdHJRlqnTxaqXs6Pp899zGZWJ9j90ygPJSLEniCQVKhex7Kd92mInSnBj%2BwxdwhmWhzDXdljrby0n%2F7FgW3RUemZBRy3e8aIxHuvftGPlKK1FbweQ5PoBUyoWNOmY07%2FycnUCddBSWmK8D7%2B%2FUajZNKAqOdOXrkVG12CdKdoMZbWzpxaahLcsKCVQjAIHEPWOCqevE79bJ3F%2BMZFTH2ikM9nrYoW7GcGByc52lY%2FUbL3Z%2BzA3civZ4C8zF0OguJDyuebLx6WFWBt%2B%2FWMAXSfMgBVaZF%2BWiljWrfhYxZNF%2Bi027ZlCsYDQT8seM1bKqK0RznZwwMLa9jaWSgdzf31DVMtRzEB9%2Bgbfo%2FXdc8MTeuTyo0FIVwo01Ksj8c10ke%2BzUr4MKA7v6nh3ZMLyhhMkGOqUBOzdrwDweIsPvhf92Q%2B%2FWh6HRuOwUnM8PTc3gV00FMlPJfN0AFNcXJplKWWwtR4%2FJ7AxbO0SqrRYa%2BuSYwLMpuNb3gWN3POWIrG%2B1XGwaXxM1nAaj%2BpkcNiNwn6woUQylUIxmbH2YU5iGdDeHngjs8m2LUtWuDs7inpsaRWSjOm85HU%2BT5SWbrtj3t8FcNVguxUxeqVP3zwnvbhMv0yq2AQ5lLUXy&X-Amz-Signature=0684f5ee3501e2016bd605fa3af4e1f8a189f08a3f126849dc3e5fe859700d6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKPJYZQH%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCUyhaXHLOrEWTb4grnKizgxc3ZbWVuIGTbKVT%2F3%2Bt16wIgUOydLTFIEXcW6zw0yR4juOS561c6%2FfAQThHZ%2B%2FTbj1Yq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDPbmuL638be388vlaircA097%2BYcldaAN%2FkILR5GVoT6k1xsJiuEt2Owl3Q1NADvneMDvxFYX8B%2BR8xbS0qKMYoWWsMJmS8izv9JjvNAzOwzEES6Iw%2BIy6xyZ7nRKHpCek8WuPOnY3PPFiG4hXuOVw0Z7FZ7IFWrORRs6xAEGAPKv%2Bh%2BJ%2BhUoDMGjp2yAEEaoCTbLw7tYZPyHwQcl5q5rFx3p9FpVOIJMGxO7p7K5RE98ohQavDNagNfCzUkiX5D8LUWdHJRlqnTxaqXs6Pp899zGZWJ9j90ygPJSLEniCQVKhex7Kd92mInSnBj%2BwxdwhmWhzDXdljrby0n%2F7FgW3RUemZBRy3e8aIxHuvftGPlKK1FbweQ5PoBUyoWNOmY07%2FycnUCddBSWmK8D7%2B%2FUajZNKAqOdOXrkVG12CdKdoMZbWzpxaahLcsKCVQjAIHEPWOCqevE79bJ3F%2BMZFTH2ikM9nrYoW7GcGByc52lY%2FUbL3Z%2BzA3civZ4C8zF0OguJDyuebLx6WFWBt%2B%2FWMAXSfMgBVaZF%2BWiljWrfhYxZNF%2Bi027ZlCsYDQT8seM1bKqK0RznZwwMLa9jaWSgdzf31DVMtRzEB9%2Bgbfo%2FXdc8MTeuTyo0FIVwo01Ksj8c10ke%2BzUr4MKA7v6nh3ZMLyhhMkGOqUBOzdrwDweIsPvhf92Q%2B%2FWh6HRuOwUnM8PTc3gV00FMlPJfN0AFNcXJplKWWwtR4%2FJ7AxbO0SqrRYa%2BuSYwLMpuNb3gWN3POWIrG%2B1XGwaXxM1nAaj%2BpkcNiNwn6woUQylUIxmbH2YU5iGdDeHngjs8m2LUtWuDs7inpsaRWSjOm85HU%2BT5SWbrtj3t8FcNVguxUxeqVP3zwnvbhMv0yq2AQ5lLUXy&X-Amz-Signature=56736a819ce6930d088994e613224c2700a957c5c94996b3f233d6c6c360415c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKPJYZQH%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCUyhaXHLOrEWTb4grnKizgxc3ZbWVuIGTbKVT%2F3%2Bt16wIgUOydLTFIEXcW6zw0yR4juOS561c6%2FfAQThHZ%2B%2FTbj1Yq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDPbmuL638be388vlaircA097%2BYcldaAN%2FkILR5GVoT6k1xsJiuEt2Owl3Q1NADvneMDvxFYX8B%2BR8xbS0qKMYoWWsMJmS8izv9JjvNAzOwzEES6Iw%2BIy6xyZ7nRKHpCek8WuPOnY3PPFiG4hXuOVw0Z7FZ7IFWrORRs6xAEGAPKv%2Bh%2BJ%2BhUoDMGjp2yAEEaoCTbLw7tYZPyHwQcl5q5rFx3p9FpVOIJMGxO7p7K5RE98ohQavDNagNfCzUkiX5D8LUWdHJRlqnTxaqXs6Pp899zGZWJ9j90ygPJSLEniCQVKhex7Kd92mInSnBj%2BwxdwhmWhzDXdljrby0n%2F7FgW3RUemZBRy3e8aIxHuvftGPlKK1FbweQ5PoBUyoWNOmY07%2FycnUCddBSWmK8D7%2B%2FUajZNKAqOdOXrkVG12CdKdoMZbWzpxaahLcsKCVQjAIHEPWOCqevE79bJ3F%2BMZFTH2ikM9nrYoW7GcGByc52lY%2FUbL3Z%2BzA3civZ4C8zF0OguJDyuebLx6WFWBt%2B%2FWMAXSfMgBVaZF%2BWiljWrfhYxZNF%2Bi027ZlCsYDQT8seM1bKqK0RznZwwMLa9jaWSgdzf31DVMtRzEB9%2Bgbfo%2FXdc8MTeuTyo0FIVwo01Ksj8c10ke%2BzUr4MKA7v6nh3ZMLyhhMkGOqUBOzdrwDweIsPvhf92Q%2B%2FWh6HRuOwUnM8PTc3gV00FMlPJfN0AFNcXJplKWWwtR4%2FJ7AxbO0SqrRYa%2BuSYwLMpuNb3gWN3POWIrG%2B1XGwaXxM1nAaj%2BpkcNiNwn6woUQylUIxmbH2YU5iGdDeHngjs8m2LUtWuDs7inpsaRWSjOm85HU%2BT5SWbrtj3t8FcNVguxUxeqVP3zwnvbhMv0yq2AQ5lLUXy&X-Amz-Signature=a716df4b2084aab20d3a22e7191f8a20d2ad11a1ba81288fd39a68487901f999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

