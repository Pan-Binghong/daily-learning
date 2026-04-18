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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB3HVTDK%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDk7N3jTSPljz5qsAWTK%2FOyDDcEs8Xmem8q2YUldA41LAIgBRoASsssbnPHXjOCkWwSgm96%2FrTaazye%2F%2FDRc5egtw0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDUpz9%2F9vO7CggrVSrcA5XHuJIz1w1RYfENLOkQUGQKD%2BcFRQ5VGcJs8MSv2TenaGtHhv4kWjCoOBcFpdOc73qB3v8KMHiQvRJOunhe9H56CBJARJlbu59ZwzNBHsd0dn5qetffcrDDus1kzmaDq9h4pXCCGGheCVnbZP06eM81JHe5X2egIHTnPNvlJMgoFzJAeLI93CKpeNvFqc%2BsSgkKDyjNQGz5Gzk%2BsFGPi%2FQGD%2FduujA6G672SiwEdOlquBcacTudmPn%2FNG4zVVZmupOQP3l2piOrrZUdYfSgLjFheOwIGXqgjJcT3HZ459lFhmlLNXGnp5NQKGVP2jfubpVHaYRR3lnlpIuvsnHtfmr5SFmf%2F7oVvj1FfiQAqgqFFddJsfvjs7CSVnav0Ivgo3sLVpg1SrigXNpRmGtG0MyD74BEB%2B1kj93f%2BuQrts94f8b9sdLhexlXbfLv4kuDR5W67gNOJYP35bvwUhFuZySA6PYDwUij%2FsKNCySzNg5sIrnsWa9WWUxKU60qkFfTLPJDVyl4i9sQ32%2BYI7EgEj%2FLsS%2FIewQn5QMoOfUzbzIVN%2FknJaoikfJdytHI4CjlA8dk%2BVT5ckWx2tdlaS6NggHnzdw1jy2bsSQaTmQ67L%2Fg%2BW4okPcNt7xdEzhgMOOui88GOqUBXkggeI%2B2x4iUSC0h2BVSTI3mOjQ%2B307RjTP2JxhuSGJItGt1PP52hDuoAMik6qQhXt76CzkAq1Kq5LdAxVqOFQaGOV5mCXEu%2FAzei6dq8k81ctHBRQ83gcst%2FgLfaW2110LElUDT%2FkUVURLowxUX3M0onjt2UV1GR0oVj4E3znPR5mGlcN26tDlgA7SEFZ7nvJHwRmF3lhp%2FGKXQ9Sw6G0%2BLPpyP&X-Amz-Signature=238d3e31d1b765ad5659b0f71823faad490825a42ee5956389ea20d94bf31e5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB3HVTDK%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDk7N3jTSPljz5qsAWTK%2FOyDDcEs8Xmem8q2YUldA41LAIgBRoASsssbnPHXjOCkWwSgm96%2FrTaazye%2F%2FDRc5egtw0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPDUpz9%2F9vO7CggrVSrcA5XHuJIz1w1RYfENLOkQUGQKD%2BcFRQ5VGcJs8MSv2TenaGtHhv4kWjCoOBcFpdOc73qB3v8KMHiQvRJOunhe9H56CBJARJlbu59ZwzNBHsd0dn5qetffcrDDus1kzmaDq9h4pXCCGGheCVnbZP06eM81JHe5X2egIHTnPNvlJMgoFzJAeLI93CKpeNvFqc%2BsSgkKDyjNQGz5Gzk%2BsFGPi%2FQGD%2FduujA6G672SiwEdOlquBcacTudmPn%2FNG4zVVZmupOQP3l2piOrrZUdYfSgLjFheOwIGXqgjJcT3HZ459lFhmlLNXGnp5NQKGVP2jfubpVHaYRR3lnlpIuvsnHtfmr5SFmf%2F7oVvj1FfiQAqgqFFddJsfvjs7CSVnav0Ivgo3sLVpg1SrigXNpRmGtG0MyD74BEB%2B1kj93f%2BuQrts94f8b9sdLhexlXbfLv4kuDR5W67gNOJYP35bvwUhFuZySA6PYDwUij%2FsKNCySzNg5sIrnsWa9WWUxKU60qkFfTLPJDVyl4i9sQ32%2BYI7EgEj%2FLsS%2FIewQn5QMoOfUzbzIVN%2FknJaoikfJdytHI4CjlA8dk%2BVT5ckWx2tdlaS6NggHnzdw1jy2bsSQaTmQ67L%2Fg%2BW4okPcNt7xdEzhgMOOui88GOqUBXkggeI%2B2x4iUSC0h2BVSTI3mOjQ%2B307RjTP2JxhuSGJItGt1PP52hDuoAMik6qQhXt76CzkAq1Kq5LdAxVqOFQaGOV5mCXEu%2FAzei6dq8k81ctHBRQ83gcst%2FgLfaW2110LElUDT%2FkUVURLowxUX3M0onjt2UV1GR0oVj4E3znPR5mGlcN26tDlgA7SEFZ7nvJHwRmF3lhp%2FGKXQ9Sw6G0%2BLPpyP&X-Amz-Signature=a941c28bb7d1fa81f03f9d699a0161878102195a8148ab085db4bbd5765d14db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

