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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4SKIDCA%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDnp3ZrnrPWv0ECjEwp%2Fgc7mmNnj8rLhc0Zfs6fZVhzAgIhAL4tW1TzjU4ozh6NiTLV4HURCMm34HbNSuecrOnUBWS7KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9vwUw0F3V85BHvmkq3AOPMtc%2FcWrn4clWTITPJPn%2BGHTzV8bHpZKTlaUT9EO7HuY7iRyoKkPAKgm8vMsh%2BKjF0p33DAGdktfDpayvRIpoK97wmctngLa1AVqC9739JUd%2ByBdwG0EdaF6MRxWLCYZrRMNhJ8MzECGWC98ReOe9b43yhDzRDpnxnIrwnRN7zPhDjlN2eP1Uc0JcQm1VZgS1wxxWv6F7NKoG5sLslfWqEJPWjnKbkGnLlvKDylBMu%2BIy4%2FFKPu0m3JBN89J2VVKu6tGWY7Af4mMUtv71wXv2CU2yKcM7DkfBIAlXnVhAQ%2FbSLz48kaVYHrZb6oDetZ%2Bih%2B4KY%2BC%2FM6XVNd9o%2B5z%2F0nYb2PYbVCkcF0VVRJre5DQsmlbuSpkyibRJj3Se5G6mJQ8OELIgH7HFExLxdydDeDuU3YWzglnfHXxGFGjkSF1ntR9KQGuOWaluzdgnRrafW579X%2BOxY3BhIXv6DMS1rRMp%2F44PQcMkOEUTkGhc01x6RJnn47J0Xb8XuKsssezy63MddrFTMqpHDM4yXTmrrvUDImYRrXGS6u6wK6CZo0ykzbaEEg6mYNh8gNdJKCQLazBiwEcViyD44YDaXSpAeUCEAs4pxauZwd28ReUYE4CuxzNjUhKdTZM80TCe3pDPBjqkAS%2BIzLZSmhpAY%2FZp%2B3Y0ON7M%2FMf5QcRdEOjjuUVTv%2BCcGpw2OGSEfTszSp2WqOTGhrzpYZU3PB88nr5YJvd5Z%2Bf422hnS57ibEgK1NRTcAPcnh7tLqYL0XHzTXiCbN%2BZCllaacVrOHrne4epsOoeORUpBHHoCjjvJmX6VlzXUmneL92gvdWKkfFTDFuyFV%2Fl3Al3eIq5d16tajYFDyfCcKfNM9du&X-Amz-Signature=55058d41233abb4423b35f555b3a38c4652325a22b7139f0d2505f291e9721ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4SKIDCA%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDnp3ZrnrPWv0ECjEwp%2Fgc7mmNnj8rLhc0Zfs6fZVhzAgIhAL4tW1TzjU4ozh6NiTLV4HURCMm34HbNSuecrOnUBWS7KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9vwUw0F3V85BHvmkq3AOPMtc%2FcWrn4clWTITPJPn%2BGHTzV8bHpZKTlaUT9EO7HuY7iRyoKkPAKgm8vMsh%2BKjF0p33DAGdktfDpayvRIpoK97wmctngLa1AVqC9739JUd%2ByBdwG0EdaF6MRxWLCYZrRMNhJ8MzECGWC98ReOe9b43yhDzRDpnxnIrwnRN7zPhDjlN2eP1Uc0JcQm1VZgS1wxxWv6F7NKoG5sLslfWqEJPWjnKbkGnLlvKDylBMu%2BIy4%2FFKPu0m3JBN89J2VVKu6tGWY7Af4mMUtv71wXv2CU2yKcM7DkfBIAlXnVhAQ%2FbSLz48kaVYHrZb6oDetZ%2Bih%2B4KY%2BC%2FM6XVNd9o%2B5z%2F0nYb2PYbVCkcF0VVRJre5DQsmlbuSpkyibRJj3Se5G6mJQ8OELIgH7HFExLxdydDeDuU3YWzglnfHXxGFGjkSF1ntR9KQGuOWaluzdgnRrafW579X%2BOxY3BhIXv6DMS1rRMp%2F44PQcMkOEUTkGhc01x6RJnn47J0Xb8XuKsssezy63MddrFTMqpHDM4yXTmrrvUDImYRrXGS6u6wK6CZo0ykzbaEEg6mYNh8gNdJKCQLazBiwEcViyD44YDaXSpAeUCEAs4pxauZwd28ReUYE4CuxzNjUhKdTZM80TCe3pDPBjqkAS%2BIzLZSmhpAY%2FZp%2B3Y0ON7M%2FMf5QcRdEOjjuUVTv%2BCcGpw2OGSEfTszSp2WqOTGhrzpYZU3PB88nr5YJvd5Z%2Bf422hnS57ibEgK1NRTcAPcnh7tLqYL0XHzTXiCbN%2BZCllaacVrOHrne4epsOoeORUpBHHoCjjvJmX6VlzXUmneL92gvdWKkfFTDFuyFV%2Fl3Al3eIq5d16tajYFDyfCcKfNM9du&X-Amz-Signature=2851659ba8088d6caeabd58387396348c1f4f85ac177413825f65643b2440b28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4SKIDCA%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDnp3ZrnrPWv0ECjEwp%2Fgc7mmNnj8rLhc0Zfs6fZVhzAgIhAL4tW1TzjU4ozh6NiTLV4HURCMm34HbNSuecrOnUBWS7KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9vwUw0F3V85BHvmkq3AOPMtc%2FcWrn4clWTITPJPn%2BGHTzV8bHpZKTlaUT9EO7HuY7iRyoKkPAKgm8vMsh%2BKjF0p33DAGdktfDpayvRIpoK97wmctngLa1AVqC9739JUd%2ByBdwG0EdaF6MRxWLCYZrRMNhJ8MzECGWC98ReOe9b43yhDzRDpnxnIrwnRN7zPhDjlN2eP1Uc0JcQm1VZgS1wxxWv6F7NKoG5sLslfWqEJPWjnKbkGnLlvKDylBMu%2BIy4%2FFKPu0m3JBN89J2VVKu6tGWY7Af4mMUtv71wXv2CU2yKcM7DkfBIAlXnVhAQ%2FbSLz48kaVYHrZb6oDetZ%2Bih%2B4KY%2BC%2FM6XVNd9o%2B5z%2F0nYb2PYbVCkcF0VVRJre5DQsmlbuSpkyibRJj3Se5G6mJQ8OELIgH7HFExLxdydDeDuU3YWzglnfHXxGFGjkSF1ntR9KQGuOWaluzdgnRrafW579X%2BOxY3BhIXv6DMS1rRMp%2F44PQcMkOEUTkGhc01x6RJnn47J0Xb8XuKsssezy63MddrFTMqpHDM4yXTmrrvUDImYRrXGS6u6wK6CZo0ykzbaEEg6mYNh8gNdJKCQLazBiwEcViyD44YDaXSpAeUCEAs4pxauZwd28ReUYE4CuxzNjUhKdTZM80TCe3pDPBjqkAS%2BIzLZSmhpAY%2FZp%2B3Y0ON7M%2FMf5QcRdEOjjuUVTv%2BCcGpw2OGSEfTszSp2WqOTGhrzpYZU3PB88nr5YJvd5Z%2Bf422hnS57ibEgK1NRTcAPcnh7tLqYL0XHzTXiCbN%2BZCllaacVrOHrne4epsOoeORUpBHHoCjjvJmX6VlzXUmneL92gvdWKkfFTDFuyFV%2Fl3Al3eIq5d16tajYFDyfCcKfNM9du&X-Amz-Signature=e54b39c131f60202d0f1ce9c8e1ba162a1623ff885ca67ece5f1fae63dbc8b40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

