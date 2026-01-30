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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPVYJMHV%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKkRAb9PoKtTOLcSU%2BI8I3Wu5SIDfak6atrizJ4WqbvAiEAoxm9vFM9759iO%2FDg1zwt6JzL%2FGH9nZzHq0K%2BGcX543wqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImywjfx%2FfloLsg0nCrcA0NexiYYycloWagEy0lLrEqujKoV0IsXaMpGaX9m%2B%2BWZe1PknXLSAWAhQcUh8K8o2MqoYtbDM%2FIdfYu02DOKzNYEBqyx0KOHAkSIOBCQ7VZXRmfFXzZqfNjgUioSe1jhloxTu2R5kjlXwqbzHHsfURupAFbeJwBDAoGmSmwylbO8TadRx2ervNK58qIAo9QIU0wIxm4tf9ySwXzTpKY5gNqdXKPMVUjnxseRWHoWCroyd2OUJ2RPI9VBKMuCzMZ9kZnURekjkhAtamZdBjipzK9rOZ%2FMlkJYkfHROH06Fvd3Z0jXJH4MUHK5PdQs0GheuzwdtXH5SO6TI4lzFx8RoUYhK5sJYUO9fJV12UAkO9DQaNGKFxCuPQBxcrwJR%2B2i7C7uJnHJ18UQ6syiIBAvHsRwMP3dYgcOsYccsuZyJntvRNrv74i6K2sH1o5IxWKRvBFrElvZKJYJFyteUv8wa0zFQ6uTdyDrMH65q%2B3MZrOnz0HZ%2F%2FiFJtK9Lo%2BmqImzHuEa0DuPjUyhvIB8n6dsyX50e3HbMKqDToxQyMZ9UCpyCKo2vn0G36Jr91MsfSSAhKnYEgoSQy1qzCMgcN0JcWnhc%2FUDGuO9uDUQ8FKYmMF8WUM39NVteHfGsNA8MP%2FI8MsGOqUB2BoNZR9w8zCk6Bcpq4ifevO6dIUwy%2BrGau9%2FhEh6pXrWd6meII2BA48jsuoZh8DrFQgBsUicvX72Vg%2FN5SG%2B%2B4sTME8NhOQXPt0DpWvzHUKDYyyZ40GB8ckhcJQL2IhiQr3n5F2UVCL2C1CBq6eqhtfzfRmWPvHydrua4Yzek7aUmWMIBNCKdJR7BPb7VHtWmLK6TgrnzQnjuP0eeBxMQBx9ZSaK&X-Amz-Signature=4302a3c26a0d1a7059d5474310b6ae67221f9e8ed370cda6c47e0e53b7b0aad7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPVYJMHV%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKkRAb9PoKtTOLcSU%2BI8I3Wu5SIDfak6atrizJ4WqbvAiEAoxm9vFM9759iO%2FDg1zwt6JzL%2FGH9nZzHq0K%2BGcX543wqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImywjfx%2FfloLsg0nCrcA0NexiYYycloWagEy0lLrEqujKoV0IsXaMpGaX9m%2B%2BWZe1PknXLSAWAhQcUh8K8o2MqoYtbDM%2FIdfYu02DOKzNYEBqyx0KOHAkSIOBCQ7VZXRmfFXzZqfNjgUioSe1jhloxTu2R5kjlXwqbzHHsfURupAFbeJwBDAoGmSmwylbO8TadRx2ervNK58qIAo9QIU0wIxm4tf9ySwXzTpKY5gNqdXKPMVUjnxseRWHoWCroyd2OUJ2RPI9VBKMuCzMZ9kZnURekjkhAtamZdBjipzK9rOZ%2FMlkJYkfHROH06Fvd3Z0jXJH4MUHK5PdQs0GheuzwdtXH5SO6TI4lzFx8RoUYhK5sJYUO9fJV12UAkO9DQaNGKFxCuPQBxcrwJR%2B2i7C7uJnHJ18UQ6syiIBAvHsRwMP3dYgcOsYccsuZyJntvRNrv74i6K2sH1o5IxWKRvBFrElvZKJYJFyteUv8wa0zFQ6uTdyDrMH65q%2B3MZrOnz0HZ%2F%2FiFJtK9Lo%2BmqImzHuEa0DuPjUyhvIB8n6dsyX50e3HbMKqDToxQyMZ9UCpyCKo2vn0G36Jr91MsfSSAhKnYEgoSQy1qzCMgcN0JcWnhc%2FUDGuO9uDUQ8FKYmMF8WUM39NVteHfGsNA8MP%2FI8MsGOqUB2BoNZR9w8zCk6Bcpq4ifevO6dIUwy%2BrGau9%2FhEh6pXrWd6meII2BA48jsuoZh8DrFQgBsUicvX72Vg%2FN5SG%2B%2B4sTME8NhOQXPt0DpWvzHUKDYyyZ40GB8ckhcJQL2IhiQr3n5F2UVCL2C1CBq6eqhtfzfRmWPvHydrua4Yzek7aUmWMIBNCKdJR7BPb7VHtWmLK6TgrnzQnjuP0eeBxMQBx9ZSaK&X-Amz-Signature=5ebca3f7579d82c0f0fbaf32822ce22ed226385b03dac2041c282155591d86e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPVYJMHV%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKkRAb9PoKtTOLcSU%2BI8I3Wu5SIDfak6atrizJ4WqbvAiEAoxm9vFM9759iO%2FDg1zwt6JzL%2FGH9nZzHq0K%2BGcX543wqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDImywjfx%2FfloLsg0nCrcA0NexiYYycloWagEy0lLrEqujKoV0IsXaMpGaX9m%2B%2BWZe1PknXLSAWAhQcUh8K8o2MqoYtbDM%2FIdfYu02DOKzNYEBqyx0KOHAkSIOBCQ7VZXRmfFXzZqfNjgUioSe1jhloxTu2R5kjlXwqbzHHsfURupAFbeJwBDAoGmSmwylbO8TadRx2ervNK58qIAo9QIU0wIxm4tf9ySwXzTpKY5gNqdXKPMVUjnxseRWHoWCroyd2OUJ2RPI9VBKMuCzMZ9kZnURekjkhAtamZdBjipzK9rOZ%2FMlkJYkfHROH06Fvd3Z0jXJH4MUHK5PdQs0GheuzwdtXH5SO6TI4lzFx8RoUYhK5sJYUO9fJV12UAkO9DQaNGKFxCuPQBxcrwJR%2B2i7C7uJnHJ18UQ6syiIBAvHsRwMP3dYgcOsYccsuZyJntvRNrv74i6K2sH1o5IxWKRvBFrElvZKJYJFyteUv8wa0zFQ6uTdyDrMH65q%2B3MZrOnz0HZ%2F%2FiFJtK9Lo%2BmqImzHuEa0DuPjUyhvIB8n6dsyX50e3HbMKqDToxQyMZ9UCpyCKo2vn0G36Jr91MsfSSAhKnYEgoSQy1qzCMgcN0JcWnhc%2FUDGuO9uDUQ8FKYmMF8WUM39NVteHfGsNA8MP%2FI8MsGOqUB2BoNZR9w8zCk6Bcpq4ifevO6dIUwy%2BrGau9%2FhEh6pXrWd6meII2BA48jsuoZh8DrFQgBsUicvX72Vg%2FN5SG%2B%2B4sTME8NhOQXPt0DpWvzHUKDYyyZ40GB8ckhcJQL2IhiQr3n5F2UVCL2C1CBq6eqhtfzfRmWPvHydrua4Yzek7aUmWMIBNCKdJR7BPb7VHtWmLK6TgrnzQnjuP0eeBxMQBx9ZSaK&X-Amz-Signature=908e3704c062076c089d697ca66d7afb7eed9d8250d47c290fa6e9edeb82642e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

