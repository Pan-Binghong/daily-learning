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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHJMHH5R%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBpkizXWVKGLu5h%2Bm7WZOF%2FRrjb4E5uzkcspzoeoits2AiAbOFMt5vkgBKm%2F8qK4Rk3a6k%2FQYU%2FZGXMa5eK0l2DhxSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMPEEqMNUqxtRQljJ4KtwDQ9fA%2F1EBXp1zRzYIg%2B9u8aTqXz0MlqVV1mQoQVj9DO%2Bbo8f6nHn1aB%2BK3Uwu93KwkoBRBIQDmTexZVK268YRiyuQL61dW4%2FUUkf8yI7pldt%2BvmNv9kjzz7frOJYMlYERxRZfV%2BcoDuAD0dd4bfsLhovd8pwuVnlrDQzfdYmlZ3kN9i8403EHGwGOCqX4920DJyNMjG6tb2L0RS0Y5567jnlWweNwSM49P6wewVlnsLWbbJZrVohbrutt3%2FW5paTJ4tvlTgJRte5g9ND1LIPl4UPh0D02yOSJD3afJfSy7id7SPrmoUgvyftIj6hVUbomNcKvK31IMYa%2BCNgHOA8m0VLk1XeU%2F3Furqp9VuKqzHs21WdOuT8ksJjDoQ6T3hCuMCgQ0aaOF8Dv9Xwr4KFgjVf8ruP41LFzkfx3IgGjXgWWQ4akim6LZvjJigAIu2K1ZbKsmkh8UssYaFx9q0tn%2BMqJbzgJ8vmufImUjDFfNWwOMTkGja8qpWGFGe8wLGRZuzTnYZ990zyieMsstTq8SG1yOshm%2B2Z8BtUqfpR4EVeju6DMX36FDxzrfjDxAGIZ4SZ1QjIGwcAZ8fHdLQqF9auBmI%2B%2FTqDzk50m%2BDysuPVtpWrQw%2FnS8nBOjZIwxv64zQY6pgHRpVGhRnLDaNn3UNIsp%2BMlO%2FP4%2FpFk5LkUvB%2FzKVeZq7GNAiBUS7PiewGZH2mLXuGp3Bxk%2FkA1OOTFCoe%2BwuuiCsIixnGasAT%2B3vv96v5KSBf8x8A45m%2BRwEBxRQbN2Iyr5f7kBRJIU5p1oed1%2B4Uk92jNaezR96NjErg3UWhm3oxYJloNdN1j0lx%2FYH61xOzgOJ7tL0rvIGuAf%2FP6m%2Fu5KvusT2Hu&X-Amz-Signature=231cd6fe52712854945280ca54ff04d769f26330feb6a4f0255c32e1dff19023&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHJMHH5R%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBpkizXWVKGLu5h%2Bm7WZOF%2FRrjb4E5uzkcspzoeoits2AiAbOFMt5vkgBKm%2F8qK4Rk3a6k%2FQYU%2FZGXMa5eK0l2DhxSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMPEEqMNUqxtRQljJ4KtwDQ9fA%2F1EBXp1zRzYIg%2B9u8aTqXz0MlqVV1mQoQVj9DO%2Bbo8f6nHn1aB%2BK3Uwu93KwkoBRBIQDmTexZVK268YRiyuQL61dW4%2FUUkf8yI7pldt%2BvmNv9kjzz7frOJYMlYERxRZfV%2BcoDuAD0dd4bfsLhovd8pwuVnlrDQzfdYmlZ3kN9i8403EHGwGOCqX4920DJyNMjG6tb2L0RS0Y5567jnlWweNwSM49P6wewVlnsLWbbJZrVohbrutt3%2FW5paTJ4tvlTgJRte5g9ND1LIPl4UPh0D02yOSJD3afJfSy7id7SPrmoUgvyftIj6hVUbomNcKvK31IMYa%2BCNgHOA8m0VLk1XeU%2F3Furqp9VuKqzHs21WdOuT8ksJjDoQ6T3hCuMCgQ0aaOF8Dv9Xwr4KFgjVf8ruP41LFzkfx3IgGjXgWWQ4akim6LZvjJigAIu2K1ZbKsmkh8UssYaFx9q0tn%2BMqJbzgJ8vmufImUjDFfNWwOMTkGja8qpWGFGe8wLGRZuzTnYZ990zyieMsstTq8SG1yOshm%2B2Z8BtUqfpR4EVeju6DMX36FDxzrfjDxAGIZ4SZ1QjIGwcAZ8fHdLQqF9auBmI%2B%2FTqDzk50m%2BDysuPVtpWrQw%2FnS8nBOjZIwxv64zQY6pgHRpVGhRnLDaNn3UNIsp%2BMlO%2FP4%2FpFk5LkUvB%2FzKVeZq7GNAiBUS7PiewGZH2mLXuGp3Bxk%2FkA1OOTFCoe%2BwuuiCsIixnGasAT%2B3vv96v5KSBf8x8A45m%2BRwEBxRQbN2Iyr5f7kBRJIU5p1oed1%2B4Uk92jNaezR96NjErg3UWhm3oxYJloNdN1j0lx%2FYH61xOzgOJ7tL0rvIGuAf%2FP6m%2Fu5KvusT2Hu&X-Amz-Signature=4f0f691f55f8430f07f39be66c29bd9916ea07f970b9b0478819e477ccd3408a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

