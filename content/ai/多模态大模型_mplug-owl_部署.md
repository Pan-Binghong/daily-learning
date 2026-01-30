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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZBIUX67%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBU%2Bw%2FhdRHecFfVwXtTgkClQYXi4HkkUD4mG2jwD%2BU1eAiAC6VC2R975ecU9UJM%2Bv0jRPFcQOWQToTteeHnRLKdezCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoOpbPwQHzLvX3q6OKtwDcDDazpCKrJmd%2Fxg9qQqmP06wgXHzVs2C%2FapINbULNHBGqJmK%2BuXun7YpCkX9i5auTcIPaWqLY8Q9ZUEX%2FSKEQJeXLDmrG2%2FoTpFfmNjrD0rP9wP3qj31tHS4GKTLycLqfWu8rEVITKDiJUUKh2BZ%2BSL8hHeh48Ii%2BSESu1lBYZ8mdmmBzNKDmW%2BtUrJSpV10HykYWIXFwyPVSH1I%2BQttdofLPM7VnnE60bHJ5HnAhf8hlcOoNirsVPZxfyGExPbXJ6ZScA0%2B%2FAnvnk5x4AqyfRf3RXmLYQPQHA6LYX%2FhfkmfIEHiDzk2pJZtzQmnl1G84ACpztRaeWszSOO3lZmXx8IB8UwTV6Y02m3VVkRQ1S0L9PL4pc08rtvAXUy1UxcsdckNQ%2FkC7eDHTf%2Bu%2BY5aiBkCGg0UX3OURlcgLhHigVfltzm945I7N5qX5BMpgu7HNmipelScN4hqAwOOgcj9C9PB5N7Dq9KneRl%2BnOa6br7u%2Bhr%2F10mzmLH4Pvpm5PUSTtPvfvcgVhnoQLgUZpuuwQ94UFOnxIEqFTSyxRnrIGwH3DdUtqIkWcjXUz1DhzW90SlNlHNGyn1KYKFfloJy413YBO0sIFiNZIX2jJLhxmI6NS9ah82br1hFlTIw5cjwywY6pgHT1Gvx%2FvQNvKf5xNcHZ4eW7ph%2FRe4tgnHastJc7SEzRujE%2F%2F25G1mK1ShrOWDaayh8%2BAfKHYjFNXf6ceAvCCNHqC1I5kgwhOyvlqw2YQwnddu%2Fx9%2FEzyC1zWjNugcOiJI17NwcHX6epJ74LarWI6xZJgKLiovB810iSjg9iI10oBUUDqdl27qb2F7kYQ9%2FpCHDo7AaKCG2bm%2Bh%2Blad1a4iyK0wygLb&X-Amz-Signature=c1c5bc2444e68f9d8f2f3a22905e2d6a5bb7758d04fa972e58baec985232f07a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZBIUX67%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBU%2Bw%2FhdRHecFfVwXtTgkClQYXi4HkkUD4mG2jwD%2BU1eAiAC6VC2R975ecU9UJM%2Bv0jRPFcQOWQToTteeHnRLKdezCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoOpbPwQHzLvX3q6OKtwDcDDazpCKrJmd%2Fxg9qQqmP06wgXHzVs2C%2FapINbULNHBGqJmK%2BuXun7YpCkX9i5auTcIPaWqLY8Q9ZUEX%2FSKEQJeXLDmrG2%2FoTpFfmNjrD0rP9wP3qj31tHS4GKTLycLqfWu8rEVITKDiJUUKh2BZ%2BSL8hHeh48Ii%2BSESu1lBYZ8mdmmBzNKDmW%2BtUrJSpV10HykYWIXFwyPVSH1I%2BQttdofLPM7VnnE60bHJ5HnAhf8hlcOoNirsVPZxfyGExPbXJ6ZScA0%2B%2FAnvnk5x4AqyfRf3RXmLYQPQHA6LYX%2FhfkmfIEHiDzk2pJZtzQmnl1G84ACpztRaeWszSOO3lZmXx8IB8UwTV6Y02m3VVkRQ1S0L9PL4pc08rtvAXUy1UxcsdckNQ%2FkC7eDHTf%2Bu%2BY5aiBkCGg0UX3OURlcgLhHigVfltzm945I7N5qX5BMpgu7HNmipelScN4hqAwOOgcj9C9PB5N7Dq9KneRl%2BnOa6br7u%2Bhr%2F10mzmLH4Pvpm5PUSTtPvfvcgVhnoQLgUZpuuwQ94UFOnxIEqFTSyxRnrIGwH3DdUtqIkWcjXUz1DhzW90SlNlHNGyn1KYKFfloJy413YBO0sIFiNZIX2jJLhxmI6NS9ah82br1hFlTIw5cjwywY6pgHT1Gvx%2FvQNvKf5xNcHZ4eW7ph%2FRe4tgnHastJc7SEzRujE%2F%2F25G1mK1ShrOWDaayh8%2BAfKHYjFNXf6ceAvCCNHqC1I5kgwhOyvlqw2YQwnddu%2Fx9%2FEzyC1zWjNugcOiJI17NwcHX6epJ74LarWI6xZJgKLiovB810iSjg9iI10oBUUDqdl27qb2F7kYQ9%2FpCHDo7AaKCG2bm%2Bh%2Blad1a4iyK0wygLb&X-Amz-Signature=ada34481dfcb624f7355542a637931b23470ad302af2e5a0721bccd7a5bbb99d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

