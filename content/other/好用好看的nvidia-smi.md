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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMO3MNID%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIEUG%2BTta0nquLwjEFgKSYvBvU7VF4EvkPA6pFs2yykC9AiBaFro4PVsysQLFyPD0%2FN%2BFu66k%2FGzl2Vi%2F48nuTWmO3Sr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMXoUitC1O7JtIQk0cKtwDKIWrn%2FcW%2BytSTzd97qqIS0%2B6JRB7gFKh0vUgH7oKyBxyMAptLdzazVwm7y7aQzCB5VnjqTYvAJ2ij0Gm3OPO%2FAnJ7ov3ocSSo58UyYm3A6xlQy%2BOcU1LA7zewLZjzxSXM0j9nUjah67SKwFYF5IrGJMEhKfkaiaEGssSU6ac1sT5MR6tW28AHhkwW1hzFfWATEydh2G1hcvFbLh3kbP1hciabaLSrq0XKOfbWuQoZj0yl9HDCol75CWO6xcb0Ekfp%2BKVnF58EBPrKrJm9F2v77Ey%2F4yh6U%2B2QKGPzl9wy6fGzI%2F9jEdpwJ4c97IH7sqQYe1qbReL4hq3bLYT8RWzxUmZT%2FVRw3cDK1J0m7gW94ibmRap4Y6POKIzlf1ZE3%2FIcaitDhZBvPeFOQu%2F0HHummZ2lgFto7QKpaufQ0spPXxl2p0Ih%2BkW61or5QhZwmgINWCMT0TN2ymhtiK9VzvDuNgVx8sfdq2%2BizQgjMXdPjkw4dxHW6Fa0n%2FNSNICGYSQLKdyONgJeftsoeQNFxvhCiVgUvwhGiiFcX5JXSwAFQRx43RbdtG1Rt6paqP5M0SFtYQMYZF00FpUL9CZ4K5VkbRJSCvb6LGOouvGsiHRlSNOPkl5aXRf8S2LaOsw4LDaywY6pgHyhLI4%2Fl95xKgsqAXDC1i6feHpyIxot0e2tu7k2y4a3FkjH%2FA8UUE%2BXB7%2BIXS%2BMOJn%2FfWU4P1idwqflQu0XvKv9QHQKg3Mf%2BpGnDgU03%2FflHnO4AOI0QlPqMceWIWL5WkLL38dBfJIruBAkzrpXrOObKoq9KhWN%2B6f0%2Bn9jEkL%2FNk6ii4C%2FZAunBT1GFvW%2FzS8qZEeRuW%2BQQuxzC%2B8PeH2k0IE5ws9&X-Amz-Signature=fa25ae20435229c08df2a93cde1ee149aace3685fdc86bd9fef34301a1711c57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMO3MNID%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIEUG%2BTta0nquLwjEFgKSYvBvU7VF4EvkPA6pFs2yykC9AiBaFro4PVsysQLFyPD0%2FN%2BFu66k%2FGzl2Vi%2F48nuTWmO3Sr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMXoUitC1O7JtIQk0cKtwDKIWrn%2FcW%2BytSTzd97qqIS0%2B6JRB7gFKh0vUgH7oKyBxyMAptLdzazVwm7y7aQzCB5VnjqTYvAJ2ij0Gm3OPO%2FAnJ7ov3ocSSo58UyYm3A6xlQy%2BOcU1LA7zewLZjzxSXM0j9nUjah67SKwFYF5IrGJMEhKfkaiaEGssSU6ac1sT5MR6tW28AHhkwW1hzFfWATEydh2G1hcvFbLh3kbP1hciabaLSrq0XKOfbWuQoZj0yl9HDCol75CWO6xcb0Ekfp%2BKVnF58EBPrKrJm9F2v77Ey%2F4yh6U%2B2QKGPzl9wy6fGzI%2F9jEdpwJ4c97IH7sqQYe1qbReL4hq3bLYT8RWzxUmZT%2FVRw3cDK1J0m7gW94ibmRap4Y6POKIzlf1ZE3%2FIcaitDhZBvPeFOQu%2F0HHummZ2lgFto7QKpaufQ0spPXxl2p0Ih%2BkW61or5QhZwmgINWCMT0TN2ymhtiK9VzvDuNgVx8sfdq2%2BizQgjMXdPjkw4dxHW6Fa0n%2FNSNICGYSQLKdyONgJeftsoeQNFxvhCiVgUvwhGiiFcX5JXSwAFQRx43RbdtG1Rt6paqP5M0SFtYQMYZF00FpUL9CZ4K5VkbRJSCvb6LGOouvGsiHRlSNOPkl5aXRf8S2LaOsw4LDaywY6pgHyhLI4%2Fl95xKgsqAXDC1i6feHpyIxot0e2tu7k2y4a3FkjH%2FA8UUE%2BXB7%2BIXS%2BMOJn%2FfWU4P1idwqflQu0XvKv9QHQKg3Mf%2BpGnDgU03%2FflHnO4AOI0QlPqMceWIWL5WkLL38dBfJIruBAkzrpXrOObKoq9KhWN%2B6f0%2Bn9jEkL%2FNk6ii4C%2FZAunBT1GFvW%2FzS8qZEeRuW%2BQQuxzC%2B8PeH2k0IE5ws9&X-Amz-Signature=fe10332fa351f76bc4f73a078a5e1de34796a2b74b47c82e2807148792270aa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









