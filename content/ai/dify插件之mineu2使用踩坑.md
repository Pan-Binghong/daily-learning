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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ2X6LV4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRBO5QCAsWdxbA%2F2h1HMiUFVURUhXpiSdaHPaKGq08gAIgay15btkIFNLsIJfV6ZBIW%2Bt2nFDxYO7dFpyoC6lHprcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEFZHAfQeTiTTnbwpSrcA%2B8CY7F9G6X2ZPAl0sp064dYUafK0%2BZXWLpoPAMxeg2ypRo0kYOcZTsA7hcc%2BjYfQFRlj7Ld468Z6AVn7K%2BGGxLwLuZ3DaGzmmOGIfN4JjCxEhMbqukvpa84gwohJ8gtPQyyt1fp%2BGkYFwjZyRzRycFtankWdYit1J4RJMcqEC4zEyE1CM2BaTLr0NoZH3ihRZ4tBST4HgL2Pj%2FuucpKikc9UyYsXjikDTgEfznckv4Xaxa%2F8vAm3Eb1sdKH7nUoUPKG%2FNc33kxoS9y4zSRGZ4%2BmfwNbVbr0NefMslzMAmHeOmLOukFu6hlc7xnBIVU8gWTmIb73yudRmtickt1RBl%2FNW7Pryj2QFwPjNrdDHir6CiH2Cr80B04ZDSIJPF0jm4w0MbPXaMiBEp3KHmYfsimOcLAMOGssaj%2BTGoCgoijBUZ8kd0tEN2ZhC3gxZXJI2%2FDuHh2zlWc60wu8JTkjb8XPx4YLp1aNLxYusukoG%2FA4F40pcY6JrvLTp6b1Rb1x%2BHUVGzWbvGPBVDGHCdnhzwPDK6Hj%2FpfFdEy3UH2Pr9EHa0MJ7cEmiau2IWOZgd9OcbKtYYTp5lycXdFMScSR%2BPZg%2BaeDX%2FG4hcf2F3hclUbkKwTIOkk5S8iKzxyjMOCtvc4GOqUB2JOYUYI1kRQ1juTx3FrKA0u06g3AZDVAqC4nUvhPRtWUJ0VQ2cCp6JbKSArUI1mqsEufivFISnHcHp1rb95YqIEAV%2B3X1M3xDPlbaz04G7OJLmUgiNOJL%2Fi%2B07StOEdUEQZq8zipHxMVmQjSuwvOskE9dfqvATOSp1nHAC0jlnPggcVETOw5jGM%2FDI%2Fz3T5QUW97%2FZDzeZihVge5Ny6TeLFbavoR&X-Amz-Signature=9c025be17088e4af8513a1b482bcc43eb4fd7eebcee02c05cc62c855a7ec4a7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ2X6LV4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRBO5QCAsWdxbA%2F2h1HMiUFVURUhXpiSdaHPaKGq08gAIgay15btkIFNLsIJfV6ZBIW%2Bt2nFDxYO7dFpyoC6lHprcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDEFZHAfQeTiTTnbwpSrcA%2B8CY7F9G6X2ZPAl0sp064dYUafK0%2BZXWLpoPAMxeg2ypRo0kYOcZTsA7hcc%2BjYfQFRlj7Ld468Z6AVn7K%2BGGxLwLuZ3DaGzmmOGIfN4JjCxEhMbqukvpa84gwohJ8gtPQyyt1fp%2BGkYFwjZyRzRycFtankWdYit1J4RJMcqEC4zEyE1CM2BaTLr0NoZH3ihRZ4tBST4HgL2Pj%2FuucpKikc9UyYsXjikDTgEfznckv4Xaxa%2F8vAm3Eb1sdKH7nUoUPKG%2FNc33kxoS9y4zSRGZ4%2BmfwNbVbr0NefMslzMAmHeOmLOukFu6hlc7xnBIVU8gWTmIb73yudRmtickt1RBl%2FNW7Pryj2QFwPjNrdDHir6CiH2Cr80B04ZDSIJPF0jm4w0MbPXaMiBEp3KHmYfsimOcLAMOGssaj%2BTGoCgoijBUZ8kd0tEN2ZhC3gxZXJI2%2FDuHh2zlWc60wu8JTkjb8XPx4YLp1aNLxYusukoG%2FA4F40pcY6JrvLTp6b1Rb1x%2BHUVGzWbvGPBVDGHCdnhzwPDK6Hj%2FpfFdEy3UH2Pr9EHa0MJ7cEmiau2IWOZgd9OcbKtYYTp5lycXdFMScSR%2BPZg%2BaeDX%2FG4hcf2F3hclUbkKwTIOkk5S8iKzxyjMOCtvc4GOqUB2JOYUYI1kRQ1juTx3FrKA0u06g3AZDVAqC4nUvhPRtWUJ0VQ2cCp6JbKSArUI1mqsEufivFISnHcHp1rb95YqIEAV%2B3X1M3xDPlbaz04G7OJLmUgiNOJL%2Fi%2B07StOEdUEQZq8zipHxMVmQjSuwvOskE9dfqvATOSp1nHAC0jlnPggcVETOw5jGM%2FDI%2Fz3T5QUW97%2FZDzeZihVge5Ny6TeLFbavoR&X-Amz-Signature=97aedce9ebddf8a311d106f0191114aa4edf3369a17cd1adedddaf97e8cb0013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



