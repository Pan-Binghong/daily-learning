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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAWYA37%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj7tnNCb4dVipoLWFrM9HrMvvrJRu7bJxvf3Z1JWK5NAIhAKNp7%2B7BQ%2FHNfO%2Bq1eVAtF9Gf%2F6nOn5lKVqBn%2Fs3qml6KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYVxouLCxPudXB6XEq3APfAKh57lEzm9n2px%2BIkjhppsKsdhWEyT1v14F4FwRimRrMfyOIUPcxYw2TqaAyukFhgJ1tMSaP0qfYL2tmEF37MwXH9Vi0U434bs3FpjStgQ%2FE3cm%2BnUilVpZTOdN333XHzgpzf0MZxx35ePa7QlrwixQ3bwYefHzcIZOw5mM0fEsuH60n78DXairYwFIeSxmK3JR%2Blevw3G%2F8fwMZoXfpao%2FpcHc4MW9O21jfp6ujAAOvThZd3Rs1MId%2Bh0sstfDAHz8ZSXMXYX46cEvzFCwH13ABl9wR3dPQ99nYIDj66JVXsI5BCX%2FLvBJLJdc%2B1oYdpsFEi4ap2Ch4JLs4NhFV3%2B0QG7qvFHVMgIvhXZhq0GWxNAV5MOAAnmQTFjOAfaFo9yskpSJ%2BcpAKIjtAHbkyPFPfxCNXCvrtQMZ1trhE5o6uOmj%2FsgtUdqmyBjWgw1kV%2FB05kEXn1wl5fZeRGQ4%2FkROl87IikS0omJqf1dfAZW2knVUx4jifyQ7uy%2BU60nOlYyH9cWWeFRfJfdU8bNdBOdYyLci3ylxu2Z7ferTJHJtq95gyCqJLmxIGGLEc4VGLe2G7IWw40xcB9vRTpAAwbLvZyzzfhkbUF4J45%2FhGSbA3jH%2FyB9ZGdSYF1DCG8a%2FIBjqkAS0oKrB%2ForaKksJJaEtDI4zXjOj2Bgytfo2NBBhImtjht8uapw151CGi7RA2vT7QfzbhFHJPSBo36lUSpKz86IA41wYVwtkszit27Z7Eb9o1jxMIlHQO%2F9akgmH25a8t0IDZ%2FlZP5i7ogwStg%2BcQ9CjruRtXoP1Rbb3Q7WXQ7OMfHIpbaVBK9XOAU87D0lT8wPfq0RIjYT1QWail555rBJ2KL7An&X-Amz-Signature=330606d2044b63aa9f11a3fee1180e3fd0c244f70fb91aa15a26ea4b8a32cab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAWYA37%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj7tnNCb4dVipoLWFrM9HrMvvrJRu7bJxvf3Z1JWK5NAIhAKNp7%2B7BQ%2FHNfO%2Bq1eVAtF9Gf%2F6nOn5lKVqBn%2Fs3qml6KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYVxouLCxPudXB6XEq3APfAKh57lEzm9n2px%2BIkjhppsKsdhWEyT1v14F4FwRimRrMfyOIUPcxYw2TqaAyukFhgJ1tMSaP0qfYL2tmEF37MwXH9Vi0U434bs3FpjStgQ%2FE3cm%2BnUilVpZTOdN333XHzgpzf0MZxx35ePa7QlrwixQ3bwYefHzcIZOw5mM0fEsuH60n78DXairYwFIeSxmK3JR%2Blevw3G%2F8fwMZoXfpao%2FpcHc4MW9O21jfp6ujAAOvThZd3Rs1MId%2Bh0sstfDAHz8ZSXMXYX46cEvzFCwH13ABl9wR3dPQ99nYIDj66JVXsI5BCX%2FLvBJLJdc%2B1oYdpsFEi4ap2Ch4JLs4NhFV3%2B0QG7qvFHVMgIvhXZhq0GWxNAV5MOAAnmQTFjOAfaFo9yskpSJ%2BcpAKIjtAHbkyPFPfxCNXCvrtQMZ1trhE5o6uOmj%2FsgtUdqmyBjWgw1kV%2FB05kEXn1wl5fZeRGQ4%2FkROl87IikS0omJqf1dfAZW2knVUx4jifyQ7uy%2BU60nOlYyH9cWWeFRfJfdU8bNdBOdYyLci3ylxu2Z7ferTJHJtq95gyCqJLmxIGGLEc4VGLe2G7IWw40xcB9vRTpAAwbLvZyzzfhkbUF4J45%2FhGSbA3jH%2FyB9ZGdSYF1DCG8a%2FIBjqkAS0oKrB%2ForaKksJJaEtDI4zXjOj2Bgytfo2NBBhImtjht8uapw151CGi7RA2vT7QfzbhFHJPSBo36lUSpKz86IA41wYVwtkszit27Z7Eb9o1jxMIlHQO%2F9akgmH25a8t0IDZ%2FlZP5i7ogwStg%2BcQ9CjruRtXoP1Rbb3Q7WXQ7OMfHIpbaVBK9XOAU87D0lT8wPfq0RIjYT1QWail555rBJ2KL7An&X-Amz-Signature=7f952a69e6660777ba67c861452d94752fe0ed326d32f0656820ceb9162c38f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAWYA37%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj7tnNCb4dVipoLWFrM9HrMvvrJRu7bJxvf3Z1JWK5NAIhAKNp7%2B7BQ%2FHNfO%2Bq1eVAtF9Gf%2F6nOn5lKVqBn%2Fs3qml6KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYVxouLCxPudXB6XEq3APfAKh57lEzm9n2px%2BIkjhppsKsdhWEyT1v14F4FwRimRrMfyOIUPcxYw2TqaAyukFhgJ1tMSaP0qfYL2tmEF37MwXH9Vi0U434bs3FpjStgQ%2FE3cm%2BnUilVpZTOdN333XHzgpzf0MZxx35ePa7QlrwixQ3bwYefHzcIZOw5mM0fEsuH60n78DXairYwFIeSxmK3JR%2Blevw3G%2F8fwMZoXfpao%2FpcHc4MW9O21jfp6ujAAOvThZd3Rs1MId%2Bh0sstfDAHz8ZSXMXYX46cEvzFCwH13ABl9wR3dPQ99nYIDj66JVXsI5BCX%2FLvBJLJdc%2B1oYdpsFEi4ap2Ch4JLs4NhFV3%2B0QG7qvFHVMgIvhXZhq0GWxNAV5MOAAnmQTFjOAfaFo9yskpSJ%2BcpAKIjtAHbkyPFPfxCNXCvrtQMZ1trhE5o6uOmj%2FsgtUdqmyBjWgw1kV%2FB05kEXn1wl5fZeRGQ4%2FkROl87IikS0omJqf1dfAZW2knVUx4jifyQ7uy%2BU60nOlYyH9cWWeFRfJfdU8bNdBOdYyLci3ylxu2Z7ferTJHJtq95gyCqJLmxIGGLEc4VGLe2G7IWw40xcB9vRTpAAwbLvZyzzfhkbUF4J45%2FhGSbA3jH%2FyB9ZGdSYF1DCG8a%2FIBjqkAS0oKrB%2ForaKksJJaEtDI4zXjOj2Bgytfo2NBBhImtjht8uapw151CGi7RA2vT7QfzbhFHJPSBo36lUSpKz86IA41wYVwtkszit27Z7Eb9o1jxMIlHQO%2F9akgmH25a8t0IDZ%2FlZP5i7ogwStg%2BcQ9CjruRtXoP1Rbb3Q7WXQ7OMfHIpbaVBK9XOAU87D0lT8wPfq0RIjYT1QWail555rBJ2KL7An&X-Amz-Signature=0e627494fd47d557e1eeeb4109703eb2b541e630cd398d5918d5a4cfd42d2e5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

