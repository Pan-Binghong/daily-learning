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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOARBQAV%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDn%2FNN0%2FIoKfLnzAJSaQMR1y6FHqDseKxNGnZJK8FUAhAiB4kXPNNaUQ1KTdNq0iGuuHBmjVCAKGfbA0SS2y0%2F0l4iqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShhk8sbtWihm6dOHKtwDhs9FejGGolILfiZu6KpyAQ1e6%2Ft0MAB2ktVEKiJJOXicDoD3%2FuOFyNnMA6kQO%2F2yUCzDIrDS5COp9YRWw%2B2Zhj895gn5b5xHxBw8UmcnianKeed0bfPbuofPmuH%2Bt9l32%2FTZdnh3s34Vsq1vOLbsMjVGKd9Yimgl8HKE2ibEqviEJ7F4v3o2zmltAYEdjQmlo8BUM7zs7NO%2Brhe8BphDsR3QtC2ShJ5KDkqxDgxgMwTtGxYyZ0%2BDWqT1a%2FzYBqHv8gqgSVj9rO9nFyc7EJQP0WCPHlGmPTSHqXk75RByxv5h7hijcPexUERGFOd3L7Y5bAhmvMp%2Br5YLRdKfILmhObYCkwVfnAyASQvasvDclCymZ%2Fn6OfQmm05Wd19fRHLg53esBp39prPIijpXRIXa7V%2BKnRE2HRIdCNdH%2FaZKedHiLx94aXSbGLAf6a7IPnAnHlrBh9owqdR46rR9MlmS7H6Fw9NeLRcBaSBaB74mhePQcyPhurZDIAk%2FoxYwJNuFgp1bFUqH4qvqifcSCZ9b8fVFy1%2BblPkXk8iiebVo66bm0ttpfMhulYUecLXUrENbB6dleTMdhWdEjTcc%2FlnxSf4yY%2FZzQ%2Fh2MDXXocdR2CrFhaVHpfdpWz2Xlbkwz%2Br5yAY6pgEDSsRwKREbvH0wv3QZiv7FyoBcu3t7WAHhCtu3som41D5bRqp6bTXsl55L4JjYrmtYw5x4xfRtIeyYTK0Ic%2B4ye2cCGzt5hI1%2BoJcTuo0wOXuZnZ0rOBQ0sgm7jG1F5pgp57PwWMN6a%2B0z6HTZ0ktb%2FOeRkHtKqpLhwc2Rz7ILB3yufmClPEUjz10z7fyKKE9dFI8HpcBV7sbuglrs33g0Extd54VB&X-Amz-Signature=6f2ec8f16ff18ecc65686ca46fac444b22a01db07e08a8776dcd8faa1f41c7b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOARBQAV%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDn%2FNN0%2FIoKfLnzAJSaQMR1y6FHqDseKxNGnZJK8FUAhAiB4kXPNNaUQ1KTdNq0iGuuHBmjVCAKGfbA0SS2y0%2F0l4iqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMShhk8sbtWihm6dOHKtwDhs9FejGGolILfiZu6KpyAQ1e6%2Ft0MAB2ktVEKiJJOXicDoD3%2FuOFyNnMA6kQO%2F2yUCzDIrDS5COp9YRWw%2B2Zhj895gn5b5xHxBw8UmcnianKeed0bfPbuofPmuH%2Bt9l32%2FTZdnh3s34Vsq1vOLbsMjVGKd9Yimgl8HKE2ibEqviEJ7F4v3o2zmltAYEdjQmlo8BUM7zs7NO%2Brhe8BphDsR3QtC2ShJ5KDkqxDgxgMwTtGxYyZ0%2BDWqT1a%2FzYBqHv8gqgSVj9rO9nFyc7EJQP0WCPHlGmPTSHqXk75RByxv5h7hijcPexUERGFOd3L7Y5bAhmvMp%2Br5YLRdKfILmhObYCkwVfnAyASQvasvDclCymZ%2Fn6OfQmm05Wd19fRHLg53esBp39prPIijpXRIXa7V%2BKnRE2HRIdCNdH%2FaZKedHiLx94aXSbGLAf6a7IPnAnHlrBh9owqdR46rR9MlmS7H6Fw9NeLRcBaSBaB74mhePQcyPhurZDIAk%2FoxYwJNuFgp1bFUqH4qvqifcSCZ9b8fVFy1%2BblPkXk8iiebVo66bm0ttpfMhulYUecLXUrENbB6dleTMdhWdEjTcc%2FlnxSf4yY%2FZzQ%2Fh2MDXXocdR2CrFhaVHpfdpWz2Xlbkwz%2Br5yAY6pgEDSsRwKREbvH0wv3QZiv7FyoBcu3t7WAHhCtu3som41D5bRqp6bTXsl55L4JjYrmtYw5x4xfRtIeyYTK0Ic%2B4ye2cCGzt5hI1%2BoJcTuo0wOXuZnZ0rOBQ0sgm7jG1F5pgp57PwWMN6a%2B0z6HTZ0ktb%2FOeRkHtKqpLhwc2Rz7ILB3yufmClPEUjz10z7fyKKE9dFI8HpcBV7sbuglrs33g0Extd54VB&X-Amz-Signature=96d2b4216387e45eea4110f4daa346e3267d5086701461e3751b9fa4272557dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



