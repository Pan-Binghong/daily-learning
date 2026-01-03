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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33VJ6WK%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIBNPidCAjZm8FL1M7mhWYXxbSMsIuQrlIOHfOKT%2F98AsAiEA8iLP%2BgBZbMOSvPnx23n%2BjkIEeMqKWyNFCV1gpHz6iC0q%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDNJ2x7iN%2Fup0ckQkeyrcA9yKOZlCtobMeF1Rjk957GHTA1pIKrt0ALLpp1nevGj3wcNO7Vays%2BQCj%2BKeZfiYT3SCdQQ9PWB4lPD1F2wteyYPxrHCMSG01qricLHqReYPg%2Fwo1I1aih9nTnEctnzJdk86FREm62PAqn7lLbo2vNo2F0L8SQ7bD4ta4WHLoyQjepgv963MoHG0KZ6fvJwG%2FX2DZOSA9c5pMNOB9dXv%2BL8hW%2Bwv1fLhlDsRpbvXdMGZjszyrHI2yDOOiRV6ysOJR27wc0nXYylIMq4NNfFuMXYjmilG8jc7wwQCBQTdKeedHsdcGe8xW0DJ%2BZWJG2wsO6uuWV7Q5COjUTwuA%2FZCj1QS9EBSFqKtHsdUjCRTuUPsUHHx07vnLzcTd6E8MNyCsVH%2BlV%2FKt%2Fgx7xjAgO2rLJSm%2FbIrekbSNlk4v%2B7R0nMlgR0mDZRqW59TP%2FBH4GOSKzjY4oDv0pNaf2hLACsDiu5PIjm5JU6zomaCjGKOb5RKGiSQRAEQJ62gBDAikUN%2B9HPNhNea1Js9ydZS7V1Mwm5nW7%2F3ex7SJVtnFfmzDz4p7JOS6z%2F10h%2BweY4Cdwm1urVxAFUWS%2Flfef%2FQqdZRfxp2p63igMKDPWz5ZxZ%2Bj%2F%2BpEhRdk9ZwUgweTC4XMMDu4coGOqUB1TEEDLLfWF2jan75MKzV26cxNu0jb45%2F3J9mVsagOXNND%2FqrYjmjYWzBUZtU0xxcYDDLmE21MTHr9d3ldvyvFCgDZkJoQIHNUaBcd6N%2Fs0IMtUwEJS6ODapGvXb1Sm0IZDfy7OubG17TDWV1AR2sbwFz8MC8tJKVssc3jmRutldjpAS%2BVTVf2WgPkcflw4UCYWZaz7H80zRl5E8ZYJII%2Btc%2B0S47&X-Amz-Signature=9862629e2f2120b675cbcf4897c9d84f864871c4f27c7787af3d9c8d778b48e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33VJ6WK%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIBNPidCAjZm8FL1M7mhWYXxbSMsIuQrlIOHfOKT%2F98AsAiEA8iLP%2BgBZbMOSvPnx23n%2BjkIEeMqKWyNFCV1gpHz6iC0q%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDNJ2x7iN%2Fup0ckQkeyrcA9yKOZlCtobMeF1Rjk957GHTA1pIKrt0ALLpp1nevGj3wcNO7Vays%2BQCj%2BKeZfiYT3SCdQQ9PWB4lPD1F2wteyYPxrHCMSG01qricLHqReYPg%2Fwo1I1aih9nTnEctnzJdk86FREm62PAqn7lLbo2vNo2F0L8SQ7bD4ta4WHLoyQjepgv963MoHG0KZ6fvJwG%2FX2DZOSA9c5pMNOB9dXv%2BL8hW%2Bwv1fLhlDsRpbvXdMGZjszyrHI2yDOOiRV6ysOJR27wc0nXYylIMq4NNfFuMXYjmilG8jc7wwQCBQTdKeedHsdcGe8xW0DJ%2BZWJG2wsO6uuWV7Q5COjUTwuA%2FZCj1QS9EBSFqKtHsdUjCRTuUPsUHHx07vnLzcTd6E8MNyCsVH%2BlV%2FKt%2Fgx7xjAgO2rLJSm%2FbIrekbSNlk4v%2B7R0nMlgR0mDZRqW59TP%2FBH4GOSKzjY4oDv0pNaf2hLACsDiu5PIjm5JU6zomaCjGKOb5RKGiSQRAEQJ62gBDAikUN%2B9HPNhNea1Js9ydZS7V1Mwm5nW7%2F3ex7SJVtnFfmzDz4p7JOS6z%2F10h%2BweY4Cdwm1urVxAFUWS%2Flfef%2FQqdZRfxp2p63igMKDPWz5ZxZ%2Bj%2F%2BpEhRdk9ZwUgweTC4XMMDu4coGOqUB1TEEDLLfWF2jan75MKzV26cxNu0jb45%2F3J9mVsagOXNND%2FqrYjmjYWzBUZtU0xxcYDDLmE21MTHr9d3ldvyvFCgDZkJoQIHNUaBcd6N%2Fs0IMtUwEJS6ODapGvXb1Sm0IZDfy7OubG17TDWV1AR2sbwFz8MC8tJKVssc3jmRutldjpAS%2BVTVf2WgPkcflw4UCYWZaz7H80zRl5E8ZYJII%2Btc%2B0S47&X-Amz-Signature=ed280f08af3c494eecb5f4acc800f720f195b720180fe4767657827928577e9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

