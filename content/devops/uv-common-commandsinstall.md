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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q66O5IA%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmEiwFVwAkeuoQ%2FgThYuprbULlDgAJCR3bD4oXLwFRmAiEA9qDPOmsQS%2FBr5tWzSS3HVZki3X0uecjaUHSTGwEfMnQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDEDih6WHEpSgQqq08CrcA3h8Jz6BgUKrPnYTUOTQ%2FSnjGFdBruTlk2MKdOADmuSiGLU7Ydc8r16jlUwOZPPSIxcuZyn8zeQ4rcRkm1PqAvJCfYP0iwl9Rx%2F%2Be5K9vEh8WZb8iIh0Kr1WcNqmNlQ4MkZSRLg61R4UX9vf470eWR0gvC308IHD5ilzeXSkoCpavBVCmRIp9DIh%2FFLLzfcWm2Um6%2BvmWRPvjnd4OfGbV6iPYFbAklgsu0SMN5Fz8YLCc%2FvZqNdUVLK%2Fmi876U%2Fw8MGybIrARzBgEVZgR%2FERb5YNiRMFBYOHnvaWQINEWN%2Fz5mJo8xOll4R8KsADxjP9yX5zM6xGkeXlQaM3ZeZoNcBvlfYAZoKdiuUM1pwTrSRGt%2FwMVIWzbSg7tfeFLDlSttM2cmuIgDn6EccVD1pcbQcCERLiTxtiHMyPR%2BvT1tKeHmZBOGE8TnbKqxUV4%2BgiY8u%2FDoIKugmqW7I3EhKZEz6WjBr3xZITOrJ6lFUmP3q7bTzSPpGAGOIzrRP0XRqDo3qze%2FbpwbroWQcNtcUfFIaFwOm4rA5FsYy8Ou8M%2FOY%2FWJdSqoI%2BtejcTLKoMVT81YUPManohDBgEs423MvTC%2FcHC8S2Bd91v8j5kQyYKXEFD0GABMjp2noSvh6MMPSE1ssGOqUBN%2Fi38pA04Ipye%2FR3P62FP5RnCjZEQWyqTeRWLG6x5MYN3hHNgJ3O6zxWQPYAbPnjs9upe%2B2nMx7KWwETSerKxMvR9gb0eCB2PTEhOu52lnuU0oye2G3YadbUFg0Zg5TUt8hkVlHOMmmK3SIAK5PfTl1SrapoBTcZWb2wgf8moJAAZNtoUlDu5xMbflEu2KCnGrvvUA5vObpfwC%2BeXFV7vPKA0MzU&X-Amz-Signature=9bbcf998536e62cc3b50335f423d5b5a37ef06bda9ef7fbbe4e5893aabd1e811&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q66O5IA%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmEiwFVwAkeuoQ%2FgThYuprbULlDgAJCR3bD4oXLwFRmAiEA9qDPOmsQS%2FBr5tWzSS3HVZki3X0uecjaUHSTGwEfMnQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDEDih6WHEpSgQqq08CrcA3h8Jz6BgUKrPnYTUOTQ%2FSnjGFdBruTlk2MKdOADmuSiGLU7Ydc8r16jlUwOZPPSIxcuZyn8zeQ4rcRkm1PqAvJCfYP0iwl9Rx%2F%2Be5K9vEh8WZb8iIh0Kr1WcNqmNlQ4MkZSRLg61R4UX9vf470eWR0gvC308IHD5ilzeXSkoCpavBVCmRIp9DIh%2FFLLzfcWm2Um6%2BvmWRPvjnd4OfGbV6iPYFbAklgsu0SMN5Fz8YLCc%2FvZqNdUVLK%2Fmi876U%2Fw8MGybIrARzBgEVZgR%2FERb5YNiRMFBYOHnvaWQINEWN%2Fz5mJo8xOll4R8KsADxjP9yX5zM6xGkeXlQaM3ZeZoNcBvlfYAZoKdiuUM1pwTrSRGt%2FwMVIWzbSg7tfeFLDlSttM2cmuIgDn6EccVD1pcbQcCERLiTxtiHMyPR%2BvT1tKeHmZBOGE8TnbKqxUV4%2BgiY8u%2FDoIKugmqW7I3EhKZEz6WjBr3xZITOrJ6lFUmP3q7bTzSPpGAGOIzrRP0XRqDo3qze%2FbpwbroWQcNtcUfFIaFwOm4rA5FsYy8Ou8M%2FOY%2FWJdSqoI%2BtejcTLKoMVT81YUPManohDBgEs423MvTC%2FcHC8S2Bd91v8j5kQyYKXEFD0GABMjp2noSvh6MMPSE1ssGOqUBN%2Fi38pA04Ipye%2FR3P62FP5RnCjZEQWyqTeRWLG6x5MYN3hHNgJ3O6zxWQPYAbPnjs9upe%2B2nMx7KWwETSerKxMvR9gb0eCB2PTEhOu52lnuU0oye2G3YadbUFg0Zg5TUt8hkVlHOMmmK3SIAK5PfTl1SrapoBTcZWb2wgf8moJAAZNtoUlDu5xMbflEu2KCnGrvvUA5vObpfwC%2BeXFV7vPKA0MzU&X-Amz-Signature=1a6c9271164e93b57e11d4d916fb3c7cce8486ad840e4318378791c4c879c022&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q66O5IA%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmEiwFVwAkeuoQ%2FgThYuprbULlDgAJCR3bD4oXLwFRmAiEA9qDPOmsQS%2FBr5tWzSS3HVZki3X0uecjaUHSTGwEfMnQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDEDih6WHEpSgQqq08CrcA3h8Jz6BgUKrPnYTUOTQ%2FSnjGFdBruTlk2MKdOADmuSiGLU7Ydc8r16jlUwOZPPSIxcuZyn8zeQ4rcRkm1PqAvJCfYP0iwl9Rx%2F%2Be5K9vEh8WZb8iIh0Kr1WcNqmNlQ4MkZSRLg61R4UX9vf470eWR0gvC308IHD5ilzeXSkoCpavBVCmRIp9DIh%2FFLLzfcWm2Um6%2BvmWRPvjnd4OfGbV6iPYFbAklgsu0SMN5Fz8YLCc%2FvZqNdUVLK%2Fmi876U%2Fw8MGybIrARzBgEVZgR%2FERb5YNiRMFBYOHnvaWQINEWN%2Fz5mJo8xOll4R8KsADxjP9yX5zM6xGkeXlQaM3ZeZoNcBvlfYAZoKdiuUM1pwTrSRGt%2FwMVIWzbSg7tfeFLDlSttM2cmuIgDn6EccVD1pcbQcCERLiTxtiHMyPR%2BvT1tKeHmZBOGE8TnbKqxUV4%2BgiY8u%2FDoIKugmqW7I3EhKZEz6WjBr3xZITOrJ6lFUmP3q7bTzSPpGAGOIzrRP0XRqDo3qze%2FbpwbroWQcNtcUfFIaFwOm4rA5FsYy8Ou8M%2FOY%2FWJdSqoI%2BtejcTLKoMVT81YUPManohDBgEs423MvTC%2FcHC8S2Bd91v8j5kQyYKXEFD0GABMjp2noSvh6MMPSE1ssGOqUBN%2Fi38pA04Ipye%2FR3P62FP5RnCjZEQWyqTeRWLG6x5MYN3hHNgJ3O6zxWQPYAbPnjs9upe%2B2nMx7KWwETSerKxMvR9gb0eCB2PTEhOu52lnuU0oye2G3YadbUFg0Zg5TUt8hkVlHOMmmK3SIAK5PfTl1SrapoBTcZWb2wgf8moJAAZNtoUlDu5xMbflEu2KCnGrvvUA5vObpfwC%2BeXFV7vPKA0MzU&X-Amz-Signature=a0d0f6f44cfe5288ea9195b8640b9a2031a0b3032d11e83e2f10739abcd17d3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

