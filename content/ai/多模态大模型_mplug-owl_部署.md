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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZADH622%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3WYBWJM4aOYNjBFH7CYr4dmtbE7C6tanowr8GulDqQIhAPgjLvFBn2%2FOoPDiPCGuwQwTcMoPOByLHnciciyKRIptKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxapubftkBCxTyjgm4q3AOVNOo0eVuuwIKu9pmNWAoFf0qRHn8kGFScIF2IH6iVuWqBNc6fhgx51NDQT8Zsr5GawFGG%2B4TbUfO1zR7jLQCngtSGpBTB4yGG4cqCxGPd8NP6kCpqny1NLIpcC6tCZRnpMy%2FAzHRcHJNR0RSmKFdUT6kxIUTmRCoJzwkIfbF%2Flqj4cvOSsXQMnW8nqCcfHZu%2F99n48mG1QZRWsVw9RD9m%2BfsZbncgGYzoS52jST4tz7%2F7rpKJGNbOH%2FL1BOyiLE3B1%2FLZ%2B7PXP6i6Y46RJR1P%2BHH02ltrVJxUAHvypHfdsJB2%2BG5hSvmd270r32WqMUdmmeisneNTH2nypx%2F9xSj0Da4aj0J0j2dbcGPbpSdIy9FaW7WtC5nkhlvU3DBLJWdzOGoRewy8jEBKug%2BczMM2HO%2BZHOV1fD2%2By01h4m1xjZBmAIJGPVTswULjb8gxZv7Xd4rroDMpi9ZAJF6fUqKN5KKGdQ7qr%2BUiqHuPYfvOoT10zwPsjCO1VzheCHdpeYg5VVqs%2FptfNfCxN8nUCu7Iu%2FBl5QWo%2BHvbglslJPfJ0yasTC3VtJrTiBnlMvtnwj77vGhcew%2B9B97luGlTPgsea3YG56DX3ASTsor4pMerz2jhKviULu2mORtR4DDXtYHPBjqkAeu2EsWtAG%2FI%2BpDGIgjovVPCYyW4ACPDCAS6BtrH2XHmZ73eSUK%2F7p%2BZdJ8t4yrfyqMB5f7%2FFeME%2BK8aduXrbxwXLgL6aRgNLwaah5HdNZhqMQAJw4tI%2FocQ%2FYcMgpDlwICX3SFU9ozVIIGshzVn%2BE2Ea%2B4XJZmurwO%2BAFU%2BwPPtBTMAQWP8Bh0LJegn6f0YnUoU3akIyoOhewCqbdqA224yhN7D&X-Amz-Signature=77606edb38013b4e0772a83fb98287dac17e0337cdd9585b3242d3631306222b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZADH622%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCC3WYBWJM4aOYNjBFH7CYr4dmtbE7C6tanowr8GulDqQIhAPgjLvFBn2%2FOoPDiPCGuwQwTcMoPOByLHnciciyKRIptKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxapubftkBCxTyjgm4q3AOVNOo0eVuuwIKu9pmNWAoFf0qRHn8kGFScIF2IH6iVuWqBNc6fhgx51NDQT8Zsr5GawFGG%2B4TbUfO1zR7jLQCngtSGpBTB4yGG4cqCxGPd8NP6kCpqny1NLIpcC6tCZRnpMy%2FAzHRcHJNR0RSmKFdUT6kxIUTmRCoJzwkIfbF%2Flqj4cvOSsXQMnW8nqCcfHZu%2F99n48mG1QZRWsVw9RD9m%2BfsZbncgGYzoS52jST4tz7%2F7rpKJGNbOH%2FL1BOyiLE3B1%2FLZ%2B7PXP6i6Y46RJR1P%2BHH02ltrVJxUAHvypHfdsJB2%2BG5hSvmd270r32WqMUdmmeisneNTH2nypx%2F9xSj0Da4aj0J0j2dbcGPbpSdIy9FaW7WtC5nkhlvU3DBLJWdzOGoRewy8jEBKug%2BczMM2HO%2BZHOV1fD2%2By01h4m1xjZBmAIJGPVTswULjb8gxZv7Xd4rroDMpi9ZAJF6fUqKN5KKGdQ7qr%2BUiqHuPYfvOoT10zwPsjCO1VzheCHdpeYg5VVqs%2FptfNfCxN8nUCu7Iu%2FBl5QWo%2BHvbglslJPfJ0yasTC3VtJrTiBnlMvtnwj77vGhcew%2B9B97luGlTPgsea3YG56DX3ASTsor4pMerz2jhKviULu2mORtR4DDXtYHPBjqkAeu2EsWtAG%2FI%2BpDGIgjovVPCYyW4ACPDCAS6BtrH2XHmZ73eSUK%2F7p%2BZdJ8t4yrfyqMB5f7%2FFeME%2BK8aduXrbxwXLgL6aRgNLwaah5HdNZhqMQAJw4tI%2FocQ%2FYcMgpDlwICX3SFU9ozVIIGshzVn%2BE2Ea%2B4XJZmurwO%2BAFU%2BwPPtBTMAQWP8Bh0LJegn6f0YnUoU3akIyoOhewCqbdqA224yhN7D&X-Amz-Signature=3fd5c2a1b898b6bde1ae79dfdc5f373eb55e0f43bd576e411c82688bfa8e022c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

