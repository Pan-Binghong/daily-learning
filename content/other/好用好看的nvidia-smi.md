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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBGJMOG%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIHTteb%2ByVRyOg8VHwDYynukjaU%2BvyOIXCml20OA5qG0hAiEAtKGXDKorafRdP49G5y400AORLjyN42%2BtMrSFD7ZNO8QqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5d1CbeYUwqRhW1zCrcAzx7aGJWBMasvNcGSua59wPC5I%2B%2BzTM9eg0vbgAzOCEmNZijnbehSysnTUn3aH36n%2FYz5twilUdfUfh6R68lJiL8T4EIPrDTt6MuAGPaQF5UZhW1AaQV9Ay6phFAwjb6%2F%2B91deu2qYzKc%2BU%2F1%2BNK%2Bk7eknb4KCMH%2BwDD1NzWAibU%2F1JEtYVRecpqD4qIJKK8pDGh%2FW5gztiI0oulEaxums5qiTuhGsUn2CsFAkcscijXSvgQTt5RbAqPT6bzeYdJpUDGRdpg8aCiD4ulU9btFVDr6Gx3tj3vhYxRst%2BQRdxjvH71cZOiTAgzK79GoiiF0QjjdzKT9CADB2xUwCnlq4834cuUvRNaqo0PXssdUz8caIk89GVh0%2ByGBcZRH%2FaCrnEFjbQrK5qPmq%2BIyEsQnDeTJ4m2CKRaxdNqE%2BLNhQnsjfjh8q6pGjRd9ldWWi%2Fy7SGH0nf5iia2bR9VLgG070ByVhzX8YluVKS1JVkOch5GVAJXnyAyAGxyKt1Pzqy6GmUHn88YtcCTl22VrOmwJbU5u7PFEoRduIln93pbhqkikkm4%2FF8hYy8u4lTQ6vlKhUK6UyhLsdnoA9H4N08XHDaYJNtnJn%2B%2FKk7YzJGCl9D9MynghhfOcJt4N8JJMP2DjMsGOqUBllCrJzrkwq4lxm8To2YmZA%2BfeG8rXkfmRrM2Rkw%2Fk2xZ0uqvZs2iFcKK1Q4E7JZ%2BXhlajsVlJc1xXItgmTUUO%2BBOEaQhvV1w0tiC1i2%2FFLyhiQ9GeCRXLm2v1ctgjTOPdHuWUChnIclbj4C0a8MTsRIYZEQORXXphu0zCIRQyiQglErYS7D%2FMSqu6SOXjBIouQnjG%2Fix8XJP1FNgYjbNbKizFe2H&X-Amz-Signature=87a2f0211a0b7a3c35b9f1ae41be2331a40e531c16ffe2dc733079527aa6e047&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBBGJMOG%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIHTteb%2ByVRyOg8VHwDYynukjaU%2BvyOIXCml20OA5qG0hAiEAtKGXDKorafRdP49G5y400AORLjyN42%2BtMrSFD7ZNO8QqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5d1CbeYUwqRhW1zCrcAzx7aGJWBMasvNcGSua59wPC5I%2B%2BzTM9eg0vbgAzOCEmNZijnbehSysnTUn3aH36n%2FYz5twilUdfUfh6R68lJiL8T4EIPrDTt6MuAGPaQF5UZhW1AaQV9Ay6phFAwjb6%2F%2B91deu2qYzKc%2BU%2F1%2BNK%2Bk7eknb4KCMH%2BwDD1NzWAibU%2F1JEtYVRecpqD4qIJKK8pDGh%2FW5gztiI0oulEaxums5qiTuhGsUn2CsFAkcscijXSvgQTt5RbAqPT6bzeYdJpUDGRdpg8aCiD4ulU9btFVDr6Gx3tj3vhYxRst%2BQRdxjvH71cZOiTAgzK79GoiiF0QjjdzKT9CADB2xUwCnlq4834cuUvRNaqo0PXssdUz8caIk89GVh0%2ByGBcZRH%2FaCrnEFjbQrK5qPmq%2BIyEsQnDeTJ4m2CKRaxdNqE%2BLNhQnsjfjh8q6pGjRd9ldWWi%2Fy7SGH0nf5iia2bR9VLgG070ByVhzX8YluVKS1JVkOch5GVAJXnyAyAGxyKt1Pzqy6GmUHn88YtcCTl22VrOmwJbU5u7PFEoRduIln93pbhqkikkm4%2FF8hYy8u4lTQ6vlKhUK6UyhLsdnoA9H4N08XHDaYJNtnJn%2B%2FKk7YzJGCl9D9MynghhfOcJt4N8JJMP2DjMsGOqUBllCrJzrkwq4lxm8To2YmZA%2BfeG8rXkfmRrM2Rkw%2Fk2xZ0uqvZs2iFcKK1Q4E7JZ%2BXhlajsVlJc1xXItgmTUUO%2BBOEaQhvV1w0tiC1i2%2FFLyhiQ9GeCRXLm2v1ctgjTOPdHuWUChnIclbj4C0a8MTsRIYZEQORXXphu0zCIRQyiQglErYS7D%2FMSqu6SOXjBIouQnjG%2Fix8XJP1FNgYjbNbKizFe2H&X-Amz-Signature=8ef10abf56fe4a7255defa0752cf159a9aabde4063371baee2d78d52c9680fe8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









