---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIN7TUJR%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBO5xjvuLtKVIQb7vamOxFEnNg%2FKFQelL6p2rcPikfSMAiAalKTzVE1D9RN4HKDCl5OXFoMxDt9ZIQLzdfKjT3vr9Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMRUybt3PmltpspuLIKtwDWrbQ1NY%2Fqg8j7igkzr2wCU7Gf0rmd4XbRFuBgAc61QuMZQHZrbv%2Bf8UOIL6npc%2Bpefo6hIzcwEHVYmJrBfowIoEfRkKdd1ks1TfkoDO7dYOk6Onfy1rX2G6AjusnukhWoVfCUeEkkSRzflDoz4pJbYq1qhvgZt4hZZMwuIsQ6TnUR4uS%2BiEYVgl1%2FIQIBBqcvttVCZ7JkDR%2Bff0W%2B5o9MUGCsAQ%2F1leX%2BjHN72fXuGFaV7H4O3aPGtOpggyRPmUAu%2B6LWP7Vh7hwFoI5jJnj%2BReaMrlGiuVSHUvNeN2D11hfinGZYdswQgg2w0x3%2B%2FSE3cjPC0swYcJ3ygwSim8rv5OBjoxRcu7CiZ3x%2FkHllGIf5hF69GE%2F2MQ76e%2BhmAPyVrtuXLkHiUof%2F8sP3DN5WLjtgSVu49M%2BbANCdcs7UNcXkyBmyjJpTvwOYvoL2efh8I65OO%2BrGQYJgwh0%2ByDg9FrXIXz1cNRs2UDe783n2fjB%2FSn%2BM6an6XMUulVo0j6n6bfIihe3Ym8y0k3PTfcFVNg5vbRvf79r%2BLgZveGcnX5UtCGYji5uegNzb19HD5ne%2BIo1qGMv7T7b6fQxTbCe9JmqfvFEdssMcbaGcEj60ulF%2F0PZcAFkd6zfZegw%2Fq%2F4yQY6pgFCGarve%2BXwDsunGLvHHIbO%2ByA7FMqoORUTYXO%2Bt%2Bd8bU0FGhK5CchUokhUDIeu9Qtnlb2gWIV5xwnixRCcTfC3lgOC%2B776pG78POAng9G3K4PVdC3L8%2B%2BCufRJPPPGmaosPdlNPjYtHl6VtzPZCNdX9df128mrvP1obNy35aaa2ta8cOjYgfhWHo8GDnQrfiD3LF4UlMT7757DfiJl9%2BHcJZlGjtbJ&X-Amz-Signature=dcda9c1ff50a8e38fdf89e3b442ab336a0c6ad6d227436fbef7878042d3a6f16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIN7TUJR%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIBO5xjvuLtKVIQb7vamOxFEnNg%2FKFQelL6p2rcPikfSMAiAalKTzVE1D9RN4HKDCl5OXFoMxDt9ZIQLzdfKjT3vr9Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMRUybt3PmltpspuLIKtwDWrbQ1NY%2Fqg8j7igkzr2wCU7Gf0rmd4XbRFuBgAc61QuMZQHZrbv%2Bf8UOIL6npc%2Bpefo6hIzcwEHVYmJrBfowIoEfRkKdd1ks1TfkoDO7dYOk6Onfy1rX2G6AjusnukhWoVfCUeEkkSRzflDoz4pJbYq1qhvgZt4hZZMwuIsQ6TnUR4uS%2BiEYVgl1%2FIQIBBqcvttVCZ7JkDR%2Bff0W%2B5o9MUGCsAQ%2F1leX%2BjHN72fXuGFaV7H4O3aPGtOpggyRPmUAu%2B6LWP7Vh7hwFoI5jJnj%2BReaMrlGiuVSHUvNeN2D11hfinGZYdswQgg2w0x3%2B%2FSE3cjPC0swYcJ3ygwSim8rv5OBjoxRcu7CiZ3x%2FkHllGIf5hF69GE%2F2MQ76e%2BhmAPyVrtuXLkHiUof%2F8sP3DN5WLjtgSVu49M%2BbANCdcs7UNcXkyBmyjJpTvwOYvoL2efh8I65OO%2BrGQYJgwh0%2ByDg9FrXIXz1cNRs2UDe783n2fjB%2FSn%2BM6an6XMUulVo0j6n6bfIihe3Ym8y0k3PTfcFVNg5vbRvf79r%2BLgZveGcnX5UtCGYji5uegNzb19HD5ne%2BIo1qGMv7T7b6fQxTbCe9JmqfvFEdssMcbaGcEj60ulF%2F0PZcAFkd6zfZegw%2Fq%2F4yQY6pgFCGarve%2BXwDsunGLvHHIbO%2ByA7FMqoORUTYXO%2Bt%2Bd8bU0FGhK5CchUokhUDIeu9Qtnlb2gWIV5xwnixRCcTfC3lgOC%2B776pG78POAng9G3K4PVdC3L8%2B%2BCufRJPPPGmaosPdlNPjYtHl6VtzPZCNdX9df128mrvP1obNy35aaa2ta8cOjYgfhWHo8GDnQrfiD3LF4UlMT7757DfiJl9%2BHcJZlGjtbJ&X-Amz-Signature=43cf95a5f7f0de5e4c5a2823ba9789de841d64db00611113ef28a532ee63faa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



