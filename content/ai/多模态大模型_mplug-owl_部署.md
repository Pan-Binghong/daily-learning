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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MMWQRHI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDXRMznBlFeBkMlvEgT3vtN6dHMLMgDCzPr9nUUHDrWGgIhAMORAGBrQEFAqLy7ZXdAw%2BkDo4vOQovUPZxsxD3q4QCAKv8DCAkQABoMNjM3NDIzMTgzODA1IgwqzrAJfujkjuP2I8sq3ANx%2BoN3N1Pungr7bKYMQVUptHtYzZl3W5bqd%2FvVroYFkKxo1ENk2RTVJgZajdwUM9oNmhPVTD%2BZaGpFNmUQMe6BTAck5d%2B58qpX7JiUQeTQStj%2FZ%2BbswwNS5AgVaNJtBOyW9Qwn%2FQjE7%2B6KwyQKCMZvb2pnpLEY98YeJyYbcPsqrEKmikfOxI6Ai8d3ihgyQn7jsnylq8ArIeAaJgmqbH5%2Fp6OwPFnbJhCvgGG0R%2FoWLoxg4VNc3HBRQ4ucmGB6A9gn4sNTJviWsaAKT24yNyCR3V4xLJHD1Gzr%2BEA%2FVEGyVkomIUcRcDMgffi53oYIWkwuLquOIN60jY8%2F%2FmE1qECgrQuEObWFfA4n1yMIUf8tAzv8Pcr5QH8THfrJNJzakB6Zz4HBi5VCOXxzb1jZVEq2gqWhPFskMcfIqjDyqlQTlVZqybqXCNRIaynix74RZo1Bvlvc%2BaR5zkD%2BpAU5VJqyv%2BYZGf%2FLflpgfxm9rLPpZoTbHTvC%2BhKif58jDmWflt7PCeZ5C8xFHcMMjBznAw8%2BWEybr6xWHsukY%2FW8cYOIWF5ga8lkKDm7G9kkSmXppuTtsPF28h1SxUBq0PdwOEh4kQflA%2FllNkxZhWoc579TWQ58khPRFHJsc0DobjCzm8zPBjqkAYqmTcSJUqPAlQZNZY3RNUUyWJR5c5tAUgblE8t%2BvUHF9M7WsTMGXvxr1jkbVaeJgxpYB4DAx75UHTSB8YkOz6JB%2FS%2BDBTQ%2B7UCLrQi3tp9zsCqX8c5b7nNSj06u3hHP5K3E%2F8Ocl8kJAeF2zqPxOkutddwZ4XsD97NY8wAP%2F1%2BX%2BFu6cxDaR0Mm%2B%2BA211oR4tNmDhm1Pph2z8D7guHfmhKDMKsq&X-Amz-Signature=c3cefb07d8ee2605d483de6198ab32050c18b714bc6e141e2229ea2afb49e462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MMWQRHI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDXRMznBlFeBkMlvEgT3vtN6dHMLMgDCzPr9nUUHDrWGgIhAMORAGBrQEFAqLy7ZXdAw%2BkDo4vOQovUPZxsxD3q4QCAKv8DCAkQABoMNjM3NDIzMTgzODA1IgwqzrAJfujkjuP2I8sq3ANx%2BoN3N1Pungr7bKYMQVUptHtYzZl3W5bqd%2FvVroYFkKxo1ENk2RTVJgZajdwUM9oNmhPVTD%2BZaGpFNmUQMe6BTAck5d%2B58qpX7JiUQeTQStj%2FZ%2BbswwNS5AgVaNJtBOyW9Qwn%2FQjE7%2B6KwyQKCMZvb2pnpLEY98YeJyYbcPsqrEKmikfOxI6Ai8d3ihgyQn7jsnylq8ArIeAaJgmqbH5%2Fp6OwPFnbJhCvgGG0R%2FoWLoxg4VNc3HBRQ4ucmGB6A9gn4sNTJviWsaAKT24yNyCR3V4xLJHD1Gzr%2BEA%2FVEGyVkomIUcRcDMgffi53oYIWkwuLquOIN60jY8%2F%2FmE1qECgrQuEObWFfA4n1yMIUf8tAzv8Pcr5QH8THfrJNJzakB6Zz4HBi5VCOXxzb1jZVEq2gqWhPFskMcfIqjDyqlQTlVZqybqXCNRIaynix74RZo1Bvlvc%2BaR5zkD%2BpAU5VJqyv%2BYZGf%2FLflpgfxm9rLPpZoTbHTvC%2BhKif58jDmWflt7PCeZ5C8xFHcMMjBznAw8%2BWEybr6xWHsukY%2FW8cYOIWF5ga8lkKDm7G9kkSmXppuTtsPF28h1SxUBq0PdwOEh4kQflA%2FllNkxZhWoc579TWQ58khPRFHJsc0DobjCzm8zPBjqkAYqmTcSJUqPAlQZNZY3RNUUyWJR5c5tAUgblE8t%2BvUHF9M7WsTMGXvxr1jkbVaeJgxpYB4DAx75UHTSB8YkOz6JB%2FS%2BDBTQ%2B7UCLrQi3tp9zsCqX8c5b7nNSj06u3hHP5K3E%2F8Ocl8kJAeF2zqPxOkutddwZ4XsD97NY8wAP%2F1%2BX%2BFu6cxDaR0Mm%2B%2BA211oR4tNmDhm1Pph2z8D7guHfmhKDMKsq&X-Amz-Signature=3cea9818b0d90f869ef1da2e74d0f31a6f73464862ea264fc5dd834156457e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

