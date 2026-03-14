---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJRIYUG%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkwBbRZnbrnNNvLQ1yUW%2B74jrDqADspXroOKZhjGGo4gIgakIQsrO8DiPJqJzftWeA2FBbn0xcFZHxn397KNnJD8oqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC90lRPn%2FMi1EKEPiCrcA2rz2gNaahUGjz6tZ%2FoDhBbakLYBRlsyCVG0pTMKJJE4TWbpDMXvQLl%2FN%2B547wQlliWAjohh%2F1hEI%2FR%2BPIT%2BOoT1d9fyV8xcfODkc3DDNyYXp4V64leKCVlmr8GIpMqcLOB81WE4hz8esRJl9cpVYuff1tw6RxKlxt6Q%2BQlNCSBIXVY0nW7u%2B5bUHrdk1mO937qXPA1MMnYUhTXw5Jd1q0VSqcyFjRLybVxpBpKfBE5UpW85FRxOeFRw9FaBHhBlKDCuY6zhoNrZZFS6h0%2BPxIcYojLc9Ojrby7I%2F%2FCyQR08KWdF5l9mN6obObq1YvRXwru4Hn8Usm1e4JnyeJuz4cg1AHaRFdo1%2FJqKemWHbF4IzDdtPecekF6bi8tNL4b7ZKuTY8wYUjpohYql0s3G%2BhSeU2ad2Ha%2BOrSvy%2F5O%2FgEOeANvVv9DgEblTeGcCBwlvoUe1scNGkIHxIKjFKXPQi69R0yYcqgc7fG96asjYKxJqHEuMZgACNKsUvXAYfGo4jhcuUdKQoNP08JchKKie3Z%2Bp1jVmhFn3Q8gP4ewonJelW3KmuQQQU9puLDiEAOrn2Kis%2B4DbZXNrB6dbWYIFUF7A6YRrORwn4UWeEWO%2Fut1o5bjso51zqSesJBAMPiB080GOqUB2B4tsQeT%2FaMm%2BepCt2tcylnfW33Gc4HYXwuy4Oo1A3Yk%2BaQ%2BDMNOL0A0ws1hmbVmTZrLhEPOletzkMxMzYTZdStfpwKmhufA2IdhSa3LO%2BJX7pwxzYEx3oMHou7tlZDJbvgj6Rg3Tue%2BDAXfOi3wU9ag4%2BCdC0YZ84574tkKmm%2FypAsvCLDNG%2BhXzIRsBY7RiXOogEMyo3PU9TbwO5NmW9GGkhgH&X-Amz-Signature=5a4b54b34d26b2b6bd0c96b634fae25488df1908406281e7a5d2b1a0af9dd3c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJRIYUG%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkwBbRZnbrnNNvLQ1yUW%2B74jrDqADspXroOKZhjGGo4gIgakIQsrO8DiPJqJzftWeA2FBbn0xcFZHxn397KNnJD8oqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC90lRPn%2FMi1EKEPiCrcA2rz2gNaahUGjz6tZ%2FoDhBbakLYBRlsyCVG0pTMKJJE4TWbpDMXvQLl%2FN%2B547wQlliWAjohh%2F1hEI%2FR%2BPIT%2BOoT1d9fyV8xcfODkc3DDNyYXp4V64leKCVlmr8GIpMqcLOB81WE4hz8esRJl9cpVYuff1tw6RxKlxt6Q%2BQlNCSBIXVY0nW7u%2B5bUHrdk1mO937qXPA1MMnYUhTXw5Jd1q0VSqcyFjRLybVxpBpKfBE5UpW85FRxOeFRw9FaBHhBlKDCuY6zhoNrZZFS6h0%2BPxIcYojLc9Ojrby7I%2F%2FCyQR08KWdF5l9mN6obObq1YvRXwru4Hn8Usm1e4JnyeJuz4cg1AHaRFdo1%2FJqKemWHbF4IzDdtPecekF6bi8tNL4b7ZKuTY8wYUjpohYql0s3G%2BhSeU2ad2Ha%2BOrSvy%2F5O%2FgEOeANvVv9DgEblTeGcCBwlvoUe1scNGkIHxIKjFKXPQi69R0yYcqgc7fG96asjYKxJqHEuMZgACNKsUvXAYfGo4jhcuUdKQoNP08JchKKie3Z%2Bp1jVmhFn3Q8gP4ewonJelW3KmuQQQU9puLDiEAOrn2Kis%2B4DbZXNrB6dbWYIFUF7A6YRrORwn4UWeEWO%2Fut1o5bjso51zqSesJBAMPiB080GOqUB2B4tsQeT%2FaMm%2BepCt2tcylnfW33Gc4HYXwuy4Oo1A3Yk%2BaQ%2BDMNOL0A0ws1hmbVmTZrLhEPOletzkMxMzYTZdStfpwKmhufA2IdhSa3LO%2BJX7pwxzYEx3oMHou7tlZDJbvgj6Rg3Tue%2BDAXfOi3wU9ag4%2BCdC0YZ84574tkKmm%2FypAsvCLDNG%2BhXzIRsBY7RiXOogEMyo3PU9TbwO5NmW9GGkhgH&X-Amz-Signature=aca85ab9c9e4117d7de6802f9af7a147c1fcf238d74aac8bb4a72b1c0dbb2c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



