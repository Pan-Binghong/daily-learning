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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ5O6PZ5%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkPA6gt006qkppUMsEN3zDn4FKjVcAzFif6LI03ecTuAiEA7VRNjOPzEiUfJ1fsf4uE%2B2X%2F9C1%2FvhCZyWNItHFtcWEq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDLrOjCanS9llVhdEoyrcAzT6QtmrMYd8Mx%2FVqtQHJf9lA46sVYLx6yZo7rnQjLY9jAyzY0oPGYtRS5JrRKIjeDNeDM%2BNPazq6l%2B32mgxrYx3Y6sUbopQWmMkdZQLbK%2F4cV9WiDbNsJcHe0XHuQFTrgWdT3uM5iNxeNcdUHywj1UGRahQUOpZV861uho5oArZULYacGSI35Q6u97F342cB496MUtbt1XUrIqnreXmeH9ms7HKE2219JkBSgp7eNFMKhif9Db68emli7LNgxDb9DQHdLVVsM6Aig0yIEhuPBo8yJnmN2XR4%2BBHegZKbKZj4eg8l9CuoLh%2BArdwmj3jlK3SHqXFBNH%2Bl2yBSzxu6KxROlIOs5jK8ToDGCj0lv%2FAKLPsoK3XkuL98I1XDrUXj8lSHgItzMLazVsVJ%2FlP72uzSijjkRpoN0y01RahP03iYFV3EI%2BEjPAgE8jmSpOaeS40NKkq1mZQ%2FrlgGbeBiZx99UnFvbC8%2BYnti761PrmncVS2b72agCb9NsSq%2BOhuMk%2BEJon1AggJiVUZd2v43I9Nj%2FdK5Ym0uSel4k6h%2BxSunQXHkW1JYWlGRPVocceCXwPUu4P8n8GVZ4zV2gTIAU%2FBMl588tmELdG2cLjg58ROYY4YAWXW8cKEhZnEMIzPt8oGOqUBYoa1488cIOJLwxyx6dUkzFT4jotj1zo1zejQit0LtFPgwyv8uMlsbHHc%2Buk%2F%2BEpnkJal8Mh7EUO8EJFfNX3XEce3jFfQFQmfHPV6ea1MQ%2BFjFDsjKVrgWTSUo5ALWtQ%2B0Pggjv2sJ4Ly8FclbLJr2JAtwhVt343WpsYpKIgi0NYCRysM24RepTq6yHxjS%2FblN0nlO%2B%2BmQDLq2bkc9gm1vjWK9KN9&X-Amz-Signature=b08d072e1ea4e64da49b6007e07be2e1321c3d40322969afff641032616c7222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ5O6PZ5%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkPA6gt006qkppUMsEN3zDn4FKjVcAzFif6LI03ecTuAiEA7VRNjOPzEiUfJ1fsf4uE%2B2X%2F9C1%2FvhCZyWNItHFtcWEq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDLrOjCanS9llVhdEoyrcAzT6QtmrMYd8Mx%2FVqtQHJf9lA46sVYLx6yZo7rnQjLY9jAyzY0oPGYtRS5JrRKIjeDNeDM%2BNPazq6l%2B32mgxrYx3Y6sUbopQWmMkdZQLbK%2F4cV9WiDbNsJcHe0XHuQFTrgWdT3uM5iNxeNcdUHywj1UGRahQUOpZV861uho5oArZULYacGSI35Q6u97F342cB496MUtbt1XUrIqnreXmeH9ms7HKE2219JkBSgp7eNFMKhif9Db68emli7LNgxDb9DQHdLVVsM6Aig0yIEhuPBo8yJnmN2XR4%2BBHegZKbKZj4eg8l9CuoLh%2BArdwmj3jlK3SHqXFBNH%2Bl2yBSzxu6KxROlIOs5jK8ToDGCj0lv%2FAKLPsoK3XkuL98I1XDrUXj8lSHgItzMLazVsVJ%2FlP72uzSijjkRpoN0y01RahP03iYFV3EI%2BEjPAgE8jmSpOaeS40NKkq1mZQ%2FrlgGbeBiZx99UnFvbC8%2BYnti761PrmncVS2b72agCb9NsSq%2BOhuMk%2BEJon1AggJiVUZd2v43I9Nj%2FdK5Ym0uSel4k6h%2BxSunQXHkW1JYWlGRPVocceCXwPUu4P8n8GVZ4zV2gTIAU%2FBMl588tmELdG2cLjg58ROYY4YAWXW8cKEhZnEMIzPt8oGOqUBYoa1488cIOJLwxyx6dUkzFT4jotj1zo1zejQit0LtFPgwyv8uMlsbHHc%2Buk%2F%2BEpnkJal8Mh7EUO8EJFfNX3XEce3jFfQFQmfHPV6ea1MQ%2BFjFDsjKVrgWTSUo5ALWtQ%2B0Pggjv2sJ4Ly8FclbLJr2JAtwhVt343WpsYpKIgi0NYCRysM24RepTq6yHxjS%2FblN0nlO%2B%2BmQDLq2bkc9gm1vjWK9KN9&X-Amz-Signature=0a9bb4c7ef49aaa5c3daec63f93a90d64af31a9be225137c4da26a4d4bdf54ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

