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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGDRDIH4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPACtwx3es7yPfiWJXxi%2F4cLDFjD9leTpnfNuPQ%2BY7igIhAI2wGd%2BmrMTG2KBYZYqrIBGxeSVtIylfZ%2BElOCog2PToKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz98GKbel0P9mjWpy8q3ANvuYwS1wCSijDlLujYm7wME%2FvpPEQXhdYejPQ4El6SKEwwrQwry4LM9uOjtr%2BhwX6agfUgKzSDEe69b2XvHgJD%2BDCAfir9uumE4Yiixh%2BITU3yemQpkDWgadjezNL27C0DRkP0zXvL4Lo03atl%2BEQ0RZOjE2g50uCLtifAdvP%2BQ6mkamypdPP25j%2FOcwdgdH1EJjJn1VhwbNTdRi4tDPSZwoY%2FIp4Km3Wyj%2B6ZWJfX7Yak79iMXVwGSnGAJgWQkUf8zVdJ8x7wNWlGPniBeteB3IRv5QGX1c25G2Xnm88x%2BSE%2F7lkL5viUeEzveiATib38pijcO5FKx1tlaErmLoMe3FmGFO8ZtjsiIYsyfplRVwEgA3sXZXTinRmez%2FVq4mvuVj9RgVKisTeJq0YSkJHMkDoXWjB%2B8Y0y%2Fc%2FuvvGsLPB6BGNin%2Fejs9NfWG822g%2FjvT9CicsPlBW%2FcFqK7M49Tho0AMdLya2xRmA4unsfD%2B8wk%2BYS7GyXgEfV5ucXFEZ%2Br73k2LGg3hRmaowRcVTfJ48IuL59aRDBQb3V3rGzP2PjYY4WdsR%2BmOMgd42sHLUg1hN%2FCiFZSofYJTzy27C0I2Y5EmbExSarhhpNO9f9LaXvSsT4UEalpUyNqDDmzOnMBjqkAcI1IvjdUzMeTcDZ3FQ3KUkwivvSOW%2Ff0kZyYKsPcy30ENC%2FreuU7Uzn5u6MMgaDWgcMskuqyJBHOM2kxBIqnvP3yjTy08YGqPyJmr83%2F73ztbzVjEWBhnDLB9YhyqpY%2BXi0kBY4jB44MsU69PWgyZVnjEMKmV4bFH0qRLnCSOPZ0PUY0%2BhImxt81nrSCiC8peQ%2BHPM6HiYz0jLtQntdMYB3ldTS&X-Amz-Signature=59036ea68adce8e32a5f4ed764bc03a27e4ab6c19d8e17441647f61a77783189&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGDRDIH4%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPACtwx3es7yPfiWJXxi%2F4cLDFjD9leTpnfNuPQ%2BY7igIhAI2wGd%2BmrMTG2KBYZYqrIBGxeSVtIylfZ%2BElOCog2PToKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz98GKbel0P9mjWpy8q3ANvuYwS1wCSijDlLujYm7wME%2FvpPEQXhdYejPQ4El6SKEwwrQwry4LM9uOjtr%2BhwX6agfUgKzSDEe69b2XvHgJD%2BDCAfir9uumE4Yiixh%2BITU3yemQpkDWgadjezNL27C0DRkP0zXvL4Lo03atl%2BEQ0RZOjE2g50uCLtifAdvP%2BQ6mkamypdPP25j%2FOcwdgdH1EJjJn1VhwbNTdRi4tDPSZwoY%2FIp4Km3Wyj%2B6ZWJfX7Yak79iMXVwGSnGAJgWQkUf8zVdJ8x7wNWlGPniBeteB3IRv5QGX1c25G2Xnm88x%2BSE%2F7lkL5viUeEzveiATib38pijcO5FKx1tlaErmLoMe3FmGFO8ZtjsiIYsyfplRVwEgA3sXZXTinRmez%2FVq4mvuVj9RgVKisTeJq0YSkJHMkDoXWjB%2B8Y0y%2Fc%2FuvvGsLPB6BGNin%2Fejs9NfWG822g%2FjvT9CicsPlBW%2FcFqK7M49Tho0AMdLya2xRmA4unsfD%2B8wk%2BYS7GyXgEfV5ucXFEZ%2Br73k2LGg3hRmaowRcVTfJ48IuL59aRDBQb3V3rGzP2PjYY4WdsR%2BmOMgd42sHLUg1hN%2FCiFZSofYJTzy27C0I2Y5EmbExSarhhpNO9f9LaXvSsT4UEalpUyNqDDmzOnMBjqkAcI1IvjdUzMeTcDZ3FQ3KUkwivvSOW%2Ff0kZyYKsPcy30ENC%2FreuU7Uzn5u6MMgaDWgcMskuqyJBHOM2kxBIqnvP3yjTy08YGqPyJmr83%2F73ztbzVjEWBhnDLB9YhyqpY%2BXi0kBY4jB44MsU69PWgyZVnjEMKmV4bFH0qRLnCSOPZ0PUY0%2BhImxt81nrSCiC8peQ%2BHPM6HiYz0jLtQntdMYB3ldTS&X-Amz-Signature=b0dcd1f7f85a6cb6af392a9d4afca64098d8e31e3cb5e6185a0ec85c18b8eaa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

