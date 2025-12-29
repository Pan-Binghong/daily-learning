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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSKGL56X%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBp5MjHyCHtdYVDuDA2sn9%2BAeLKjHjzGzVgKV0sSRXRwIhAJKRHMWenZgG5JtoFrXrmGChuzBTKpy06tOlJYWK7LoWKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJcg2tRfJk4LS8DWsq3APetaaHbwAGtGzs1t6T%2B5e%2Bzof3eu0mfrYl75zqyLVMf8O19Rozb4xOa8fKite1uo%2FsyNMmL%2FjiC7wU%2F4%2FuPGPXDzDueWTzwtqSy39skGWLgfCIx1xsJKN1Q3N%2Bsyodkj3IU%2FQlJdQZ6IgWnbUX6WJWplfQjL6Xifh53I8qpg1ogAwGZK8CnwmB2wXwM%2FCOiFycvAla%2ByePujDNECPFtMMah56XPbKvHtJy9dQWaqFqtmFbj7wwhRjI%2FYjExOq5Tz9R9O7UxvzRfH57RBkAwa1RuXhrA0TpSosr5pstGd4m67JxwU5wVdiAa3qYEUaniS0wRUSLRENzG6X6DAIJlqyUtvbmy6KQYCngMS525AoCI3uwf3TOMsOmwwJI%2F7Gc9tbLJk7d%2BaUwgMmyoaTFa%2F697x6Sfkm%2B1WzrCEjvTz83u7Ql6Ji%2FMgOg9lzUC7n98CYYm9gckJvbe7R%2BQqmRVcNn78KitsZaN3F8T1WKWrwM3myD9snSS2r0sZQvvJ%2B8tICiZVNXN2mQlNHYdu%2BRjEYV56rcGUXdVXFh%2FmTSLu02pquV0KJ0u9R1pvxuqmHBTuieZi0S3zKneLx3M%2BYjuEj09I7EdqEjiO1HDb5RMvZv38Mv%2FTEv%2BGvBWQSjqzDXmsfKBjqkAeadPSCewWQqkxiT0w3iBlnMAUubrRkQMKizcaeb%2F9%2Bf02vdhn36W8geCM8miXFXHTZxD%2FQGOeP8INAQ3vHPBoxAo0AZImK2SCoJCB9JbHUMc8q8egnl8ADQJipboIjl8gf3yTeEh3XFMEwGZ%2BwQdoPHWAIZcL4TbTc8UajEFo6zNTaFCREDUgHwP7gPMgdgenKt5wHRoyJOCPWRWMN4b4d8KVoB&X-Amz-Signature=9928cf1653cb67674059becb6bef2d4b1af7e25dfca94f591dbffe869f44befc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSKGL56X%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBp5MjHyCHtdYVDuDA2sn9%2BAeLKjHjzGzVgKV0sSRXRwIhAJKRHMWenZgG5JtoFrXrmGChuzBTKpy06tOlJYWK7LoWKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJcg2tRfJk4LS8DWsq3APetaaHbwAGtGzs1t6T%2B5e%2Bzof3eu0mfrYl75zqyLVMf8O19Rozb4xOa8fKite1uo%2FsyNMmL%2FjiC7wU%2F4%2FuPGPXDzDueWTzwtqSy39skGWLgfCIx1xsJKN1Q3N%2Bsyodkj3IU%2FQlJdQZ6IgWnbUX6WJWplfQjL6Xifh53I8qpg1ogAwGZK8CnwmB2wXwM%2FCOiFycvAla%2ByePujDNECPFtMMah56XPbKvHtJy9dQWaqFqtmFbj7wwhRjI%2FYjExOq5Tz9R9O7UxvzRfH57RBkAwa1RuXhrA0TpSosr5pstGd4m67JxwU5wVdiAa3qYEUaniS0wRUSLRENzG6X6DAIJlqyUtvbmy6KQYCngMS525AoCI3uwf3TOMsOmwwJI%2F7Gc9tbLJk7d%2BaUwgMmyoaTFa%2F697x6Sfkm%2B1WzrCEjvTz83u7Ql6Ji%2FMgOg9lzUC7n98CYYm9gckJvbe7R%2BQqmRVcNn78KitsZaN3F8T1WKWrwM3myD9snSS2r0sZQvvJ%2B8tICiZVNXN2mQlNHYdu%2BRjEYV56rcGUXdVXFh%2FmTSLu02pquV0KJ0u9R1pvxuqmHBTuieZi0S3zKneLx3M%2BYjuEj09I7EdqEjiO1HDb5RMvZv38Mv%2FTEv%2BGvBWQSjqzDXmsfKBjqkAeadPSCewWQqkxiT0w3iBlnMAUubrRkQMKizcaeb%2F9%2Bf02vdhn36W8geCM8miXFXHTZxD%2FQGOeP8INAQ3vHPBoxAo0AZImK2SCoJCB9JbHUMc8q8egnl8ADQJipboIjl8gf3yTeEh3XFMEwGZ%2BwQdoPHWAIZcL4TbTc8UajEFo6zNTaFCREDUgHwP7gPMgdgenKt5wHRoyJOCPWRWMN4b4d8KVoB&X-Amz-Signature=30f48414d7a36402ce41c9b09489d4fba18c64e11ba6f9f6854bd9da911dc784&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

