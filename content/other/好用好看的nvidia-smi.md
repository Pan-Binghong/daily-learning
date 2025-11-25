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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EMMEEPS%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMkFTmGumTNPd8xMb3gZjX1SrBMLBxkPoDcJz6iz5RCAiBi7qf2Q4Iad4klbtUyFy4oOQ092m2qCL0c5hioh9p9qCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIM4iQCbCUdKqzvfDtqKtwDMpPpri3vzVHJs7wxxri8N560uSwXX2jv%2B6i%2Fp%2F2Uq1WGwtaAPdXPhQx4aHQaBudDoKqGddYFnt8oyQRgUureopXs%2BKgzOEADsCYS9TLqV5XeQtvsqW3YJ7N3inY%2Bh1LSYlTjyFN%2BRB3hTTTEROkoCZhh77nqgi%2FcL%2Bz1xokjDQDOwOfeOxK2MfmmVvrQVvb90Ju%2BR2zOsqhEMDFo%2FyubDMZaMC060AX9puuZJ5zOfVA9n8IoiDvmRpklWXucGfQ5uGM108ux%2BG2EhXevRtm0m4ipGRz1ogES29qMf98LlI2eSjkOJwpMFan1AXttgicBQZFabFTepJ0AR7A41k8%2B3XIFCSTJzO%2BI2iahUGIsSYlOrxMUc3DcFuyb1v7NJGc%2B%2BLYGFWv0RQ2ce9%2FgBjrCZUD%2BkAWCqiSQn2wVEgG3WYK48FUExReBo8ZMG2MCQQYrAyX5iOu6aofK59StJemO7N1HxuYYWuQy9D9l1mfDQs1UyC158AdOUMXVhselC2diNtd1RBsjrgj4AUOGChjjaIBMeiuBDBBhSX82wQI6Zz6j1YWen6DTJxqrGr9USChBHMzlm70Dsly11evBPwiOM0jw5HOXWcmpubhpFCMm2owSFoXQ8xQzlp07D%2FEwqq6UyQY6pgFFkGmOIfnyQugsc14FXyKe%2F9fB9puaxnEBB2weBr5M2b0GVHdt4l%2Ft1DSDOiF24mbK1lHAQb%2FFi0C3PqPugH4MJHGpcsw5GuhkQfjhPANRyHC2pB5kWfLRQ1sNESvUxeMSlj966TWrnbffBuho5qA%2BKJfnLZ0eS9sb7%2BJ0QhGoF9SrPGCaySI1SZUOlZSNWW6qR7zPbdXe473Pbv0qC5aHz%2Bzyz0iW&X-Amz-Signature=371ab6bcab05581ab2d114f1f95e6392220386af54d429c328b4cddfbca829e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EMMEEPS%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMkFTmGumTNPd8xMb3gZjX1SrBMLBxkPoDcJz6iz5RCAiBi7qf2Q4Iad4klbtUyFy4oOQ092m2qCL0c5hioh9p9qCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIM4iQCbCUdKqzvfDtqKtwDMpPpri3vzVHJs7wxxri8N560uSwXX2jv%2B6i%2Fp%2F2Uq1WGwtaAPdXPhQx4aHQaBudDoKqGddYFnt8oyQRgUureopXs%2BKgzOEADsCYS9TLqV5XeQtvsqW3YJ7N3inY%2Bh1LSYlTjyFN%2BRB3hTTTEROkoCZhh77nqgi%2FcL%2Bz1xokjDQDOwOfeOxK2MfmmVvrQVvb90Ju%2BR2zOsqhEMDFo%2FyubDMZaMC060AX9puuZJ5zOfVA9n8IoiDvmRpklWXucGfQ5uGM108ux%2BG2EhXevRtm0m4ipGRz1ogES29qMf98LlI2eSjkOJwpMFan1AXttgicBQZFabFTepJ0AR7A41k8%2B3XIFCSTJzO%2BI2iahUGIsSYlOrxMUc3DcFuyb1v7NJGc%2B%2BLYGFWv0RQ2ce9%2FgBjrCZUD%2BkAWCqiSQn2wVEgG3WYK48FUExReBo8ZMG2MCQQYrAyX5iOu6aofK59StJemO7N1HxuYYWuQy9D9l1mfDQs1UyC158AdOUMXVhselC2diNtd1RBsjrgj4AUOGChjjaIBMeiuBDBBhSX82wQI6Zz6j1YWen6DTJxqrGr9USChBHMzlm70Dsly11evBPwiOM0jw5HOXWcmpubhpFCMm2owSFoXQ8xQzlp07D%2FEwqq6UyQY6pgFFkGmOIfnyQugsc14FXyKe%2F9fB9puaxnEBB2weBr5M2b0GVHdt4l%2Ft1DSDOiF24mbK1lHAQb%2FFi0C3PqPugH4MJHGpcsw5GuhkQfjhPANRyHC2pB5kWfLRQ1sNESvUxeMSlj966TWrnbffBuho5qA%2BKJfnLZ0eS9sb7%2BJ0QhGoF9SrPGCaySI1SZUOlZSNWW6qR7zPbdXe473Pbv0qC5aHz%2Bzyz0iW&X-Amz-Signature=59202d1d3ecf644d57b4dbc7bb500d596cc55e0be866c5bd6028234473ca1432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









