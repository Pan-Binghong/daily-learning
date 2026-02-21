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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTOSIGB6%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHH4lOFcoba5AizpQu1VeBEkEAniOX747kulQa%2BieKfkAiEAtEBuSereGNE4TNtSjt02etS37Sq1w80yEuhxzCpgMo4qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFES%2FEkvrac0zAe1rircAy7fmN4y%2B6nYvqDVgVZBNunNANN0t0rcREnNZP3N8R5x5i%2F1Sea7twyijAa5cVUiF7W3qhWpLO0cwz35lsETMkSsuPwnjV7jL9nhYTSoqqsOQ7NVebeDFnY2WoeiwxCtE4NNu9wErnanj6XMYZ8syns6lbrS72qsEaJjxtHI3ny5Uu3SBu0teidQlG7Jg1qA0sMZiJDw%2Be7YypLnQYTDP%2FwLfZZ6yvm35lJ93AfUAgVYQvbQFGhKKYFiuBy7g30zzJWZYnf8poFhEekPdDWga5%2Bs5omUqoNPI7200abrv6nOwyvD0ASqdurnUWxrWoLtLuKAcEvBsMwOuWK82mdgXfWGzW8tcWsKNOoyBDFXU1Q8MtFw0jQTcJ9WlowYE4%2BwP34nEXaxc9gai6k2peM45NzaJ5p6IpB9zhn5ur6%2Bv0lMFyqwUbD0Ykgu4tsdwbIcCrkPni8hVZcWSGB5aLH6OOncdMdNgh37iC4O0ac6B5c%2Fary3boz625Bk9jU7RxteEB7v1oCVvTRvvcVZpBjEaUoiRRK8Vt40RihqiySNRGfQ%2FO2tysQ8dGC47sv1giT1mV8QGRAhtjW9P4U76WUdMvqP9AbnSNLx4fjkPWog%2Bm3F8umfeh9%2F0ZgaIb2zMNO85MwGOqUBa9cdK79wEsfRlXIjUvwh3YizJJsM9HSKCQmHXPZc0tpiAcmzAqkgsFLqiktUWCJ1QouiY9awnNOCTv471ZNvhsmCe4NCNsJzFz7PHJsSAyx2JGG8R3m4tUD4DS6mzH6DI0vXEJPJVDRqboYSisSF5ztSYOzGU9v6A2MgUUKteuUr1vpJaJXs4fanHQMOgYIK0Wz9GJCdfSrsyet%2F2DyYSf4uXWKV&X-Amz-Signature=400c8867c5f1bc00505fdc13d44db1b1e5c9e5101453806363d7f2143626ea74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTOSIGB6%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHH4lOFcoba5AizpQu1VeBEkEAniOX747kulQa%2BieKfkAiEAtEBuSereGNE4TNtSjt02etS37Sq1w80yEuhxzCpgMo4qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFES%2FEkvrac0zAe1rircAy7fmN4y%2B6nYvqDVgVZBNunNANN0t0rcREnNZP3N8R5x5i%2F1Sea7twyijAa5cVUiF7W3qhWpLO0cwz35lsETMkSsuPwnjV7jL9nhYTSoqqsOQ7NVebeDFnY2WoeiwxCtE4NNu9wErnanj6XMYZ8syns6lbrS72qsEaJjxtHI3ny5Uu3SBu0teidQlG7Jg1qA0sMZiJDw%2Be7YypLnQYTDP%2FwLfZZ6yvm35lJ93AfUAgVYQvbQFGhKKYFiuBy7g30zzJWZYnf8poFhEekPdDWga5%2Bs5omUqoNPI7200abrv6nOwyvD0ASqdurnUWxrWoLtLuKAcEvBsMwOuWK82mdgXfWGzW8tcWsKNOoyBDFXU1Q8MtFw0jQTcJ9WlowYE4%2BwP34nEXaxc9gai6k2peM45NzaJ5p6IpB9zhn5ur6%2Bv0lMFyqwUbD0Ykgu4tsdwbIcCrkPni8hVZcWSGB5aLH6OOncdMdNgh37iC4O0ac6B5c%2Fary3boz625Bk9jU7RxteEB7v1oCVvTRvvcVZpBjEaUoiRRK8Vt40RihqiySNRGfQ%2FO2tysQ8dGC47sv1giT1mV8QGRAhtjW9P4U76WUdMvqP9AbnSNLx4fjkPWog%2Bm3F8umfeh9%2F0ZgaIb2zMNO85MwGOqUBa9cdK79wEsfRlXIjUvwh3YizJJsM9HSKCQmHXPZc0tpiAcmzAqkgsFLqiktUWCJ1QouiY9awnNOCTv471ZNvhsmCe4NCNsJzFz7PHJsSAyx2JGG8R3m4tUD4DS6mzH6DI0vXEJPJVDRqboYSisSF5ztSYOzGU9v6A2MgUUKteuUr1vpJaJXs4fanHQMOgYIK0Wz9GJCdfSrsyet%2F2DyYSf4uXWKV&X-Amz-Signature=2c6dbecc873d9baa94e3f211c0ec86c34528cc945431c7127b1d505e4ff3a09b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

