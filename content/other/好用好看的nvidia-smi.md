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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GYNSE3O%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFNj%2BRo5wvXxiTBaNXz6s1R0%2FE5At5%2B0UILKquX4Lt5AiEAxuoInarNMGbt9a5TcJ9llTqjXMhEjUZ%2Bsk8FaifDT%2FMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfQv%2BBk17o7k13%2FFSrcA0YnM6sdtwKSL2OCuFobEKHIrDmMsG1GsQqGrEyUnn%2BZal63b99FsoG9UH51g9lHmt7BHdZuChmoiP6MJVDV8ODUEcLy9z2r%2FzmSwxhmtdC%2BK%2BsIuDj3ZfIGsDEkeQCBtF36JAko4cJJt5yE2gr%2BaKL4hBuKZhK6uHE%2Fo1%2Bd7yf6zx%2BauxLiqbtACu5awC3%2BjiwUerM9OyMU%2FYNdSPvF4%2BgOpzZI3AKK2aPRhmyZcNoYDa2wilJCZsC5eZKEZeDBcPz72ntUPZGxF%2BL5D9t5VYj3mA%2F5r4dxL21n8LDjYXDFYWkLuXWznHkQhYK1TQHwiymHRKIyQrEQxiSVPe%2BhJo%2FCdKhaSiehM9zQVh7mHmzHfIzc75VC%2Bao%2BIZiFayIY2Fvs3xASr1kUSPrXLOz%2BKX08KPJOI854UJWEoAdBhiOgko8tR1btjwK%2Bjj4hpfHStBZzRPpNBNFUA7Q6uLR7fkn5kcshFbgsCQ3pYjbJ%2FFRfDFsZidQBURaxUmxDUPKi0Z%2Bebj%2B%2F3eiCjy5%2FyjJb%2FtTZWuie5o9zc39EPF7Lvmt3DhXsrZ43t1rtW3L9YAdkvhcUJMKdK8MJ5kP%2BwrfU6Z4BhuefRAzL12SmZMgCWPshN8S4JEs2n4qC1a81MOjEgcsGOqUBXMaMIeKFS%2BG4kwtYbv2h8tst%2BaWBpwFLp%2BV7Xn4dOeczYKPVeym3OR2SBJeQSDtvoT0ALfpnes%2Fkl8IkbTV1JnUVRv0SOF4XdpHDyAfZb%2FLKww04PDDAymIR1WyXmdDoMvBOBp6fT1lv5T67a%2Bxf8uDe880l6Gk0xR%2B7Pe8Rce8RtWa%2F5fT%2BabNwQnr7NU66PvnskUa00vGbChh3UaYhXj%2Fl5J1S&X-Amz-Signature=2efb147a14253f65553715d8601c6e739e6a729e42279491db61fa5211d20c8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GYNSE3O%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHFNj%2BRo5wvXxiTBaNXz6s1R0%2FE5At5%2B0UILKquX4Lt5AiEAxuoInarNMGbt9a5TcJ9llTqjXMhEjUZ%2Bsk8FaifDT%2FMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEfQv%2BBk17o7k13%2FFSrcA0YnM6sdtwKSL2OCuFobEKHIrDmMsG1GsQqGrEyUnn%2BZal63b99FsoG9UH51g9lHmt7BHdZuChmoiP6MJVDV8ODUEcLy9z2r%2FzmSwxhmtdC%2BK%2BsIuDj3ZfIGsDEkeQCBtF36JAko4cJJt5yE2gr%2BaKL4hBuKZhK6uHE%2Fo1%2Bd7yf6zx%2BauxLiqbtACu5awC3%2BjiwUerM9OyMU%2FYNdSPvF4%2BgOpzZI3AKK2aPRhmyZcNoYDa2wilJCZsC5eZKEZeDBcPz72ntUPZGxF%2BL5D9t5VYj3mA%2F5r4dxL21n8LDjYXDFYWkLuXWznHkQhYK1TQHwiymHRKIyQrEQxiSVPe%2BhJo%2FCdKhaSiehM9zQVh7mHmzHfIzc75VC%2Bao%2BIZiFayIY2Fvs3xASr1kUSPrXLOz%2BKX08KPJOI854UJWEoAdBhiOgko8tR1btjwK%2Bjj4hpfHStBZzRPpNBNFUA7Q6uLR7fkn5kcshFbgsCQ3pYjbJ%2FFRfDFsZidQBURaxUmxDUPKi0Z%2Bebj%2B%2F3eiCjy5%2FyjJb%2FtTZWuie5o9zc39EPF7Lvmt3DhXsrZ43t1rtW3L9YAdkvhcUJMKdK8MJ5kP%2BwrfU6Z4BhuefRAzL12SmZMgCWPshN8S4JEs2n4qC1a81MOjEgcsGOqUBXMaMIeKFS%2BG4kwtYbv2h8tst%2BaWBpwFLp%2BV7Xn4dOeczYKPVeym3OR2SBJeQSDtvoT0ALfpnes%2Fkl8IkbTV1JnUVRv0SOF4XdpHDyAfZb%2FLKww04PDDAymIR1WyXmdDoMvBOBp6fT1lv5T67a%2Bxf8uDe880l6Gk0xR%2B7Pe8Rce8RtWa%2F5fT%2BabNwQnr7NU66PvnskUa00vGbChh3UaYhXj%2Fl5J1S&X-Amz-Signature=2c0decc8b1be6fdbb6022fe6f432c26ab12969bb88cc454490f92929dabd67da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









