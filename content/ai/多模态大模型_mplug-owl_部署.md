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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GFWHA3O%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqRPn%2BnPznXkdkZjLKh6lbIZKT3kpuNaixR8CX4JNXqwIhANsIoU5jGWLfwZf2zRgLkLrIVUbC1wy%2F%2BFAdKv4TBXZ9Kv8DCHwQABoMNjM3NDIzMTgzODA1IgzRiM6nA7J%2B%2FK2ze0Eq3ANe%2F9ru6ZPoUR%2FWfFmU3rc5amBLPVHySStUTwN7%2B6k52xOgtNMBj2Itblt3%2Fbnl9XtZa39WGuOthi46rkvI79A6QesOCXLJspVaY5gqcP1ldkdTiNqQ%2FVF8Xt3HXME%2FPgEYRB4BMVY0phmrwMYnthcGxaTmQdnEKNUw4DIYd0GL6jecHCOvo3ohjInI2u2uWCTEjKJZ9nTJX6rWyPuoQIlW5iQtoFu2DDwX74WzTgbWbXe6diGKZ2kySZ4g6XunDM8rgQQlMCByrnbD3RNNur5IfN5hBWo8Ah3Alnnpff3pDR0hZ7QUcOc09VXpWS931lAizr3bZ6R%2B6nuX8IlCJ%2Fr4QncMUw4KH1dlKDcfnMaj1Vqm2Gv1RCigww0uIJ1PkDcFL05mXCzkm%2FPt%2FeNpF8rKZodevudWy3Oh4%2BoMWOQ1WpDIpVpTowRwct3uph6rPkJpyrKfptJFsUJLm64REvqFCAQuq31r86Ryat2De73gBVK%2FGASNpOiJn4ZdDqxILqhyAcI4aJ%2F1YBeI74RROVz1KKPAYZlVIjkbIScl5sFw5Ca5eFDOqR5Grnp3OlwdXYde3uUoWrxgy9KxZxjLqvky%2F8cgwOp29ayKwvnWavXldCwlprdrzeDC3lxoKTDfoevLBjqkAat2f07KUppkkoLamNNFakmmdcl%2FG%2BNSZkjfUq9yddjyCFPsQIqIot9kUUL76%2FJXYNm%2FMAJ%2FCNBwK04FEISa5qpSASBalfeUCA730o07lO1v%2Bd8fIdLQcJLVtPkjsIbs9IqR2A3D%2BybczNES0itNTjnhyAsbY5lyPhSebPN5fqvH%2BDNvRuWdcPTdRF6iC1MQrG6qqM%2FM8Wp6%2FaoHeCG9XhhX82Br&X-Amz-Signature=7f4e54dfc023078e45f3890ddbe54504ffa9c427219f8ab06d48d5d3807ea2c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GFWHA3O%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqRPn%2BnPznXkdkZjLKh6lbIZKT3kpuNaixR8CX4JNXqwIhANsIoU5jGWLfwZf2zRgLkLrIVUbC1wy%2F%2BFAdKv4TBXZ9Kv8DCHwQABoMNjM3NDIzMTgzODA1IgzRiM6nA7J%2B%2FK2ze0Eq3ANe%2F9ru6ZPoUR%2FWfFmU3rc5amBLPVHySStUTwN7%2B6k52xOgtNMBj2Itblt3%2Fbnl9XtZa39WGuOthi46rkvI79A6QesOCXLJspVaY5gqcP1ldkdTiNqQ%2FVF8Xt3HXME%2FPgEYRB4BMVY0phmrwMYnthcGxaTmQdnEKNUw4DIYd0GL6jecHCOvo3ohjInI2u2uWCTEjKJZ9nTJX6rWyPuoQIlW5iQtoFu2DDwX74WzTgbWbXe6diGKZ2kySZ4g6XunDM8rgQQlMCByrnbD3RNNur5IfN5hBWo8Ah3Alnnpff3pDR0hZ7QUcOc09VXpWS931lAizr3bZ6R%2B6nuX8IlCJ%2Fr4QncMUw4KH1dlKDcfnMaj1Vqm2Gv1RCigww0uIJ1PkDcFL05mXCzkm%2FPt%2FeNpF8rKZodevudWy3Oh4%2BoMWOQ1WpDIpVpTowRwct3uph6rPkJpyrKfptJFsUJLm64REvqFCAQuq31r86Ryat2De73gBVK%2FGASNpOiJn4ZdDqxILqhyAcI4aJ%2F1YBeI74RROVz1KKPAYZlVIjkbIScl5sFw5Ca5eFDOqR5Grnp3OlwdXYde3uUoWrxgy9KxZxjLqvky%2F8cgwOp29ayKwvnWavXldCwlprdrzeDC3lxoKTDfoevLBjqkAat2f07KUppkkoLamNNFakmmdcl%2FG%2BNSZkjfUq9yddjyCFPsQIqIot9kUUL76%2FJXYNm%2FMAJ%2FCNBwK04FEISa5qpSASBalfeUCA730o07lO1v%2Bd8fIdLQcJLVtPkjsIbs9IqR2A3D%2BybczNES0itNTjnhyAsbY5lyPhSebPN5fqvH%2BDNvRuWdcPTdRF6iC1MQrG6qqM%2FM8Wp6%2FaoHeCG9XhhX82Br&X-Amz-Signature=cd3bf550191d238c3ff146efb575e730a3424f08f3e4c98080c6bab1d3bdc16a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

