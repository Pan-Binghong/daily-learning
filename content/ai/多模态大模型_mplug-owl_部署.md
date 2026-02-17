---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJV2LTGD%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDTBpbfB6Ioqf7Ri63SKNrXzhRRnY5saSTNtUf%2FQB1G%2BQIhAJr53guynXu6Rg9M5oo1yokvJAzZf%2B9aSpfUXwJPwVZJKv8DCEUQABoMNjM3NDIzMTgzODA1Igy5DaQzEnJGM8lT7NAq3ANH7mtuAL153mA1lRcuTbsbJX3BICWOVPsxc68OO7Xq8%2FGK2c47TCs1ihyU%2FHuFMX2KTPI3%2BGHskL8%2BcSyNqJ%2Bk5NX2SaJN34BUFwMWDNzY7RsCIzdeLzL65JXKuz3ZPb127vdE4ysUedYql27AXpjzDQ87Ej6SFHfhBCsRt4P%2F%2BfKY9Y9dAtaztCqDtbK9y1KFgo9ny2qnDccp65HlbldWgDllnNnKgmpkliejRJxrnrqxPtphPVJnM1LG3xYao36Lqvh51s3G%2FVkwTxTGRDn7NnhnN2CzBbMQ%2BJFWJH30YMmc6iSnjlcGX3RN1P7x22%2FFeOCbeCwY7EEjdX8j8wE1BtWWjG5Xct%2BqwJ8lvJVeoCoN6iEv4nl4gBJ6y5A73HTluZiFCD1qtnMvXE1uQKLv7uk0auNhuvULpZQKnizx22nVHyyZ85sMGgfv791zKcBdYuInRZHcavULlC%2BidaQlkLXE4V3uQpwZR%2BFuUD70gfH0%2BGpZvTBYBm1dU6obulzzgf%2B8lqic75FzPoMCVaH%2Ff9ebjISH5Kfaqz%2Fqdv5BfKdI3UZhprZuba9NRU3mn3tOx%2FQactAxIKkKhBTY7jIPQCycvBiNVIQjGbHFRyh5jaLrTOSvRc0qt7wvkTCiwM%2FMBjqkATUG0efaFY2oeWehXJhFJlsbTSypCWur%2BvbvFZY6kO5%2B5H2Mporh0XIqm2tK6pWZmeFZ8A%2F%2BDrX3nQJaEhMtukSKutGZISQpe2Cfpw64U4Vx9CWXFO0Xx%2BHydjtm4B1IUInEZWgrxhlynUYCo2OG1zpooyljRAolu1mmmATYZEMsESk869xl49MYWaNsymxz82NZEaaXNs%2BiS8Yi5D0ZaLrZnrpm&X-Amz-Signature=c5fc3199e91c62718d0aab6e8bd48d9aae097e86329e3a40b884cdf3af7e7b84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJV2LTGD%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDTBpbfB6Ioqf7Ri63SKNrXzhRRnY5saSTNtUf%2FQB1G%2BQIhAJr53guynXu6Rg9M5oo1yokvJAzZf%2B9aSpfUXwJPwVZJKv8DCEUQABoMNjM3NDIzMTgzODA1Igy5DaQzEnJGM8lT7NAq3ANH7mtuAL153mA1lRcuTbsbJX3BICWOVPsxc68OO7Xq8%2FGK2c47TCs1ihyU%2FHuFMX2KTPI3%2BGHskL8%2BcSyNqJ%2Bk5NX2SaJN34BUFwMWDNzY7RsCIzdeLzL65JXKuz3ZPb127vdE4ysUedYql27AXpjzDQ87Ej6SFHfhBCsRt4P%2F%2BfKY9Y9dAtaztCqDtbK9y1KFgo9ny2qnDccp65HlbldWgDllnNnKgmpkliejRJxrnrqxPtphPVJnM1LG3xYao36Lqvh51s3G%2FVkwTxTGRDn7NnhnN2CzBbMQ%2BJFWJH30YMmc6iSnjlcGX3RN1P7x22%2FFeOCbeCwY7EEjdX8j8wE1BtWWjG5Xct%2BqwJ8lvJVeoCoN6iEv4nl4gBJ6y5A73HTluZiFCD1qtnMvXE1uQKLv7uk0auNhuvULpZQKnizx22nVHyyZ85sMGgfv791zKcBdYuInRZHcavULlC%2BidaQlkLXE4V3uQpwZR%2BFuUD70gfH0%2BGpZvTBYBm1dU6obulzzgf%2B8lqic75FzPoMCVaH%2Ff9ebjISH5Kfaqz%2Fqdv5BfKdI3UZhprZuba9NRU3mn3tOx%2FQactAxIKkKhBTY7jIPQCycvBiNVIQjGbHFRyh5jaLrTOSvRc0qt7wvkTCiwM%2FMBjqkATUG0efaFY2oeWehXJhFJlsbTSypCWur%2BvbvFZY6kO5%2B5H2Mporh0XIqm2tK6pWZmeFZ8A%2F%2BDrX3nQJaEhMtukSKutGZISQpe2Cfpw64U4Vx9CWXFO0Xx%2BHydjtm4B1IUInEZWgrxhlynUYCo2OG1zpooyljRAolu1mmmATYZEMsESk869xl49MYWaNsymxz82NZEaaXNs%2BiS8Yi5D0ZaLrZnrpm&X-Amz-Signature=cc9179f0861ecf3179dc739b85b029acb0ff607126bcaed61be96e21e80b3d02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

