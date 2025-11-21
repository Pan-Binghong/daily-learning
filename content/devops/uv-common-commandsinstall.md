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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527ROB5Z%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIDMZxCeXsn0omRB6gEnV7b7r54vFp2Lhdv%2B2KuVxJ%2BENAiEAiE9fe96R%2FxbTiLna5nwTnn4kjeLYB7TVxpjTjfoTr1sq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDE%2FQMq85BMCy6cZGCSrcAzB2LoqrrEq%2Bc3jfz3y1VYeiglfOmPi%2FMiDTZHGN6sEEL1yWlucjBv0PRbLm6AWuabQ4YTQRDvMwWmRYkL%2BsU0Q2z2S0t7qpuZV0yQLtIu3ka7iAoq%2F4Dm2XEkw972XiJkYFd5LbeOca4b3GRiU2AHu4o586rcwt5EmnNoASCVEGEQSlFlLRN3MSRamjGTVUPW8z42CH1Oj98TeCwt5FW%2Fr9o4TypbHRJxiokWb6ei9YwdE5gKvwygJEkO9zfrzJfqhBVOK0JtM7Vzh%2BRJkirKzDP22nhcDxBmcUSxOqo7iFu%2BU5JVpJrNn2MFr%2FGf5J%2BpLuw6tEgc%2BfmyXzKZ%2BQWQySEV1nx9NZLKEl2qkHUr31cLxt3wvCo2hZyKT32CBxAC3rGfvTIESY5HLC8uwV4%2FvPX6APar7wuJYf91%2FGhmco166idHytePD3wMeFzVYt9PAijDSgqK5TEVEjaLkC27hNu2usMOxLqvsk8ogN%2BmdlcKQ6hpE%2BWYbZ%2Bz3dFjW5m92wKx6fqmpMt3SOo7sq8pvFduv%2Bmd7%2F8ji4YYl3EJ6LnO2h2tousiKv0%2FFWt78tqadOTZxClhkK3tadySxnYIRnUN86XvQyP8Rf7eVFfvXNRoVclFY30W1i6RaIMPyf%2F8gGOqUBRyKvphFkiLB3JvNpXbtWCeklgbSqfNboJs9PVrOEzZEg6eXhXevxMibMr9RbvTDG6dv2DRpkpK1uWlQqAjhx1lcDRh4Mo%2BRwX%2FzVS%2BVr8y8wMfJY3kUWPMUXs5hiiQ4FVKHs9m%2B%2F3czTqYXYcp0s4EZcTxuxLaGzuBCQPLUDoymFC3FTR7qVCh3CO58ZaMV6JMtc6EkSt%2Bhx2UKyQk8kodpUhUWz&X-Amz-Signature=1c72e3142a747c78c98d5ce8de0d27f30ac4ff17b08e5cbde133b1649e21bfb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527ROB5Z%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIDMZxCeXsn0omRB6gEnV7b7r54vFp2Lhdv%2B2KuVxJ%2BENAiEAiE9fe96R%2FxbTiLna5nwTnn4kjeLYB7TVxpjTjfoTr1sq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDE%2FQMq85BMCy6cZGCSrcAzB2LoqrrEq%2Bc3jfz3y1VYeiglfOmPi%2FMiDTZHGN6sEEL1yWlucjBv0PRbLm6AWuabQ4YTQRDvMwWmRYkL%2BsU0Q2z2S0t7qpuZV0yQLtIu3ka7iAoq%2F4Dm2XEkw972XiJkYFd5LbeOca4b3GRiU2AHu4o586rcwt5EmnNoASCVEGEQSlFlLRN3MSRamjGTVUPW8z42CH1Oj98TeCwt5FW%2Fr9o4TypbHRJxiokWb6ei9YwdE5gKvwygJEkO9zfrzJfqhBVOK0JtM7Vzh%2BRJkirKzDP22nhcDxBmcUSxOqo7iFu%2BU5JVpJrNn2MFr%2FGf5J%2BpLuw6tEgc%2BfmyXzKZ%2BQWQySEV1nx9NZLKEl2qkHUr31cLxt3wvCo2hZyKT32CBxAC3rGfvTIESY5HLC8uwV4%2FvPX6APar7wuJYf91%2FGhmco166idHytePD3wMeFzVYt9PAijDSgqK5TEVEjaLkC27hNu2usMOxLqvsk8ogN%2BmdlcKQ6hpE%2BWYbZ%2Bz3dFjW5m92wKx6fqmpMt3SOo7sq8pvFduv%2Bmd7%2F8ji4YYl3EJ6LnO2h2tousiKv0%2FFWt78tqadOTZxClhkK3tadySxnYIRnUN86XvQyP8Rf7eVFfvXNRoVclFY30W1i6RaIMPyf%2F8gGOqUBRyKvphFkiLB3JvNpXbtWCeklgbSqfNboJs9PVrOEzZEg6eXhXevxMibMr9RbvTDG6dv2DRpkpK1uWlQqAjhx1lcDRh4Mo%2BRwX%2FzVS%2BVr8y8wMfJY3kUWPMUXs5hiiQ4FVKHs9m%2B%2F3czTqYXYcp0s4EZcTxuxLaGzuBCQPLUDoymFC3FTR7qVCh3CO58ZaMV6JMtc6EkSt%2Bhx2UKyQk8kodpUhUWz&X-Amz-Signature=2c865cebf32212f10c7796968851983fb11e536aaea2663ccd8ad789ad4154fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527ROB5Z%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIDMZxCeXsn0omRB6gEnV7b7r54vFp2Lhdv%2B2KuVxJ%2BENAiEAiE9fe96R%2FxbTiLna5nwTnn4kjeLYB7TVxpjTjfoTr1sq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDE%2FQMq85BMCy6cZGCSrcAzB2LoqrrEq%2Bc3jfz3y1VYeiglfOmPi%2FMiDTZHGN6sEEL1yWlucjBv0PRbLm6AWuabQ4YTQRDvMwWmRYkL%2BsU0Q2z2S0t7qpuZV0yQLtIu3ka7iAoq%2F4Dm2XEkw972XiJkYFd5LbeOca4b3GRiU2AHu4o586rcwt5EmnNoASCVEGEQSlFlLRN3MSRamjGTVUPW8z42CH1Oj98TeCwt5FW%2Fr9o4TypbHRJxiokWb6ei9YwdE5gKvwygJEkO9zfrzJfqhBVOK0JtM7Vzh%2BRJkirKzDP22nhcDxBmcUSxOqo7iFu%2BU5JVpJrNn2MFr%2FGf5J%2BpLuw6tEgc%2BfmyXzKZ%2BQWQySEV1nx9NZLKEl2qkHUr31cLxt3wvCo2hZyKT32CBxAC3rGfvTIESY5HLC8uwV4%2FvPX6APar7wuJYf91%2FGhmco166idHytePD3wMeFzVYt9PAijDSgqK5TEVEjaLkC27hNu2usMOxLqvsk8ogN%2BmdlcKQ6hpE%2BWYbZ%2Bz3dFjW5m92wKx6fqmpMt3SOo7sq8pvFduv%2Bmd7%2F8ji4YYl3EJ6LnO2h2tousiKv0%2FFWt78tqadOTZxClhkK3tadySxnYIRnUN86XvQyP8Rf7eVFfvXNRoVclFY30W1i6RaIMPyf%2F8gGOqUBRyKvphFkiLB3JvNpXbtWCeklgbSqfNboJs9PVrOEzZEg6eXhXevxMibMr9RbvTDG6dv2DRpkpK1uWlQqAjhx1lcDRh4Mo%2BRwX%2FzVS%2BVr8y8wMfJY3kUWPMUXs5hiiQ4FVKHs9m%2B%2F3czTqYXYcp0s4EZcTxuxLaGzuBCQPLUDoymFC3FTR7qVCh3CO58ZaMV6JMtc6EkSt%2Bhx2UKyQk8kodpUhUWz&X-Amz-Signature=e1f3ea7e0a06ad9bc192bdb557f551ba3578e283f85c8b0c293cea6693b4d23e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

