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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZQRS74R%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoY%2FUVyNPvlZ7fliE%2BJ15vN6s2FxYAqrrIFuacmyTueQIhAOa%2Bmi5NPCuNyEN3eTvzjB6AGqNvfAdSM%2Fl%2FUWwyvi0vKv8DCHQQABoMNjM3NDIzMTgzODA1IgxdWUCQ9omJMuK61p0q3AOPcJR%2Fu%2BNFWxVOmMBiI%2BadNHSasSzFqxozKQqLTcMS9y3UHRrR4BO37LnbT6ndnGrs1lpCFkNgQ8mBznWlK8jMFgfimKbZYFmHQpoKzJ0vO9aaJhYNyQfOws3ZNpS6zXf1dEVt8E05%2FiyXamGhcOe5ttpp2CpG%2FWihc6HNOvngZqLqiN98KOErYmOvI6QTMlrPUdExM9R%2ByaqNhVQ0NRh0DmEthMcciZIzifKOlyK1hdh64b7wIBa1TAdv5UH4qz6lDYPWuUrMphK5zZoaE0iaDOkHORnSnwIC57KBc0Q7Clcr%2FIqaqW5foG9MZz8Z%2BgIYCMb8KvfLpaVzxxz3FYP6yoft1Z%2BaEExWNBKCYGm3jjQa%2B5ydSEDyrCZFlrlQkoYTvju6SfKjJotAh5cnMiTSAqNu1u%2FPeSyx5WzQbPVp%2BDrLCUUtGzRUGzUCLGOZ1JpCWfvRXgmn4qZw%2B7A4PP82%2BQwLYq4PogjEAVWYnfbz%2FoMjpyIX4bHRoT8fS7FAz3Hm4Xu2KkbP5tx5hnIIN%2FYbuLD1LlE85aUQvLOUaDFIY78m22qA3%2Bd6PoZAzu%2BbFlk2f7i0l1MRguwo9Anys4rLUBgV2cr%2BxVBS2I1QpyS5cAHqBQ%2Fx7Lc%2FhCGp9DCd8dnMBjqkAV2RSq7r%2BBNGy0E2i8LJNSCILI8X%2Fymf%2FRybwr3cpKHl%2Fss6MzvYdlPdaB6GVZAxn1xqpCh38DEd8H%2FIgi8E4pNYFSeLPx0u4fENZQiAoIk36IdieGUMTWAzSbddQoSGwW7btbHt2t9WyHI42bbLXK%2FSDGVa24RroGXhr0Dz293uE63dOQS6RKai1WPEd0yiY4%2BUiSfY8STeFjJ%2Fgf0KwAaRcwnQ&X-Amz-Signature=f4ee1a542a83e3f939e7d68765cdd374ac4924a6d8fb2daec7854a997cdf72a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZQRS74R%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoY%2FUVyNPvlZ7fliE%2BJ15vN6s2FxYAqrrIFuacmyTueQIhAOa%2Bmi5NPCuNyEN3eTvzjB6AGqNvfAdSM%2Fl%2FUWwyvi0vKv8DCHQQABoMNjM3NDIzMTgzODA1IgxdWUCQ9omJMuK61p0q3AOPcJR%2Fu%2BNFWxVOmMBiI%2BadNHSasSzFqxozKQqLTcMS9y3UHRrR4BO37LnbT6ndnGrs1lpCFkNgQ8mBznWlK8jMFgfimKbZYFmHQpoKzJ0vO9aaJhYNyQfOws3ZNpS6zXf1dEVt8E05%2FiyXamGhcOe5ttpp2CpG%2FWihc6HNOvngZqLqiN98KOErYmOvI6QTMlrPUdExM9R%2ByaqNhVQ0NRh0DmEthMcciZIzifKOlyK1hdh64b7wIBa1TAdv5UH4qz6lDYPWuUrMphK5zZoaE0iaDOkHORnSnwIC57KBc0Q7Clcr%2FIqaqW5foG9MZz8Z%2BgIYCMb8KvfLpaVzxxz3FYP6yoft1Z%2BaEExWNBKCYGm3jjQa%2B5ydSEDyrCZFlrlQkoYTvju6SfKjJotAh5cnMiTSAqNu1u%2FPeSyx5WzQbPVp%2BDrLCUUtGzRUGzUCLGOZ1JpCWfvRXgmn4qZw%2B7A4PP82%2BQwLYq4PogjEAVWYnfbz%2FoMjpyIX4bHRoT8fS7FAz3Hm4Xu2KkbP5tx5hnIIN%2FYbuLD1LlE85aUQvLOUaDFIY78m22qA3%2Bd6PoZAzu%2BbFlk2f7i0l1MRguwo9Anys4rLUBgV2cr%2BxVBS2I1QpyS5cAHqBQ%2Fx7Lc%2FhCGp9DCd8dnMBjqkAV2RSq7r%2BBNGy0E2i8LJNSCILI8X%2Fymf%2FRybwr3cpKHl%2Fss6MzvYdlPdaB6GVZAxn1xqpCh38DEd8H%2FIgi8E4pNYFSeLPx0u4fENZQiAoIk36IdieGUMTWAzSbddQoSGwW7btbHt2t9WyHI42bbLXK%2FSDGVa24RroGXhr0Dz293uE63dOQS6RKai1WPEd0yiY4%2BUiSfY8STeFjJ%2Fgf0KwAaRcwnQ&X-Amz-Signature=b397faa4d5ed4e41b349d91f4cb186f002b2a82a1c89f38c78569370d99c0bbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

