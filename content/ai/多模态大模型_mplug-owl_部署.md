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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWLBBA4L%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIA6AxqBIiQK%2B%2BB8x3Jo6JAO5vWb83xn4%2BYUlKIvelKDTAiEAvf1eB%2FyXSqAPicyPXa%2BEs1F6S9XLVeU9HkIPvdUa5UEq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKx47TnwggivcW3nDyrcA%2FccBTeYBBcmoCKtY368Mqx4fdo%2FWI17ANcmXhvMs5QSETdubuUWZ3rpn7RmiWnmG7WfpKwrh%2B0WQeLfdiiOlep%2FkN%2FCXpUHE8rN26kac3PG%2FlgDqIyzjw2GcAbGDtEisvuomgwglf7CHWimv%2BSsd%2BfpTxLQz9A7p7yotXeZR7a0CmrVFB5tqCfj9pTcvo3QJDDvwqjbhERVvgMk1nFTaFH9if4EH%2BJH3Ymqi5h%2B%2BGbhL3cPOmX2%2F0loqYOw9extlk%2FPtEottVg%2FJa6OR6P5yzy%2BoBAB8Z1MxAmLre950sDSREmPbJx3KtcXOrG9w%2FjuLffhP8zNgfo%2BR0Allaem1cwk%2BkEc0uXo%2F1EUQ3xXHwXkfSa6eKet2jR6WIZ03KPoGNxN8i0t88TYVK5MsXPR7t9X8rjw7zCurnjqTNnK7m8ZCy%2B3Qa5SP0UWpUKRsih9D6PEW9JlXqagakqFKBITt8vQ4ZwDBAgFDej%2FfP5mJvT%2BWIZQNtY778XffGlIo9wZLp4RS44xPquZcKhZjlKsTcofRCLQV4KLK%2Fz3FLCeIazvFEt0X1075Ky5gWKNjKtZXAPX9b8YZH7Vqy0V4kShEOreUUab2%2BHv%2FxXkYfEz9khLYAWepXTk1wrs4punML3x1MgGOqUBhVyjIp9%2BlOhS1tFAO0SLZjU1gEF%2Bp320RdN8XgQJVce0RtYgCjyu5BeEnbWLnFBEW7mg8wClqiAEwoe42aUQN5Ik%2Bnj1FV4A%2FQoXMrVE%2BiAvMtPPgKO%2BG8M48bB5yDcKZJgYSfDHIYg9Zl04ruPi%2FSaVh12eqKqD%2FTyLXpoW30EzV6smqpoqeOsdCYjM4sNXz0pt58MZwV4D02ESKOdCJw8tpXFp&X-Amz-Signature=517ccb62b4375863a72dbd3456932e8e131d44ad09dc88720769d84ae0ed6f33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWLBBA4L%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIA6AxqBIiQK%2B%2BB8x3Jo6JAO5vWb83xn4%2BYUlKIvelKDTAiEAvf1eB%2FyXSqAPicyPXa%2BEs1F6S9XLVeU9HkIPvdUa5UEq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKx47TnwggivcW3nDyrcA%2FccBTeYBBcmoCKtY368Mqx4fdo%2FWI17ANcmXhvMs5QSETdubuUWZ3rpn7RmiWnmG7WfpKwrh%2B0WQeLfdiiOlep%2FkN%2FCXpUHE8rN26kac3PG%2FlgDqIyzjw2GcAbGDtEisvuomgwglf7CHWimv%2BSsd%2BfpTxLQz9A7p7yotXeZR7a0CmrVFB5tqCfj9pTcvo3QJDDvwqjbhERVvgMk1nFTaFH9if4EH%2BJH3Ymqi5h%2B%2BGbhL3cPOmX2%2F0loqYOw9extlk%2FPtEottVg%2FJa6OR6P5yzy%2BoBAB8Z1MxAmLre950sDSREmPbJx3KtcXOrG9w%2FjuLffhP8zNgfo%2BR0Allaem1cwk%2BkEc0uXo%2F1EUQ3xXHwXkfSa6eKet2jR6WIZ03KPoGNxN8i0t88TYVK5MsXPR7t9X8rjw7zCurnjqTNnK7m8ZCy%2B3Qa5SP0UWpUKRsih9D6PEW9JlXqagakqFKBITt8vQ4ZwDBAgFDej%2FfP5mJvT%2BWIZQNtY778XffGlIo9wZLp4RS44xPquZcKhZjlKsTcofRCLQV4KLK%2Fz3FLCeIazvFEt0X1075Ky5gWKNjKtZXAPX9b8YZH7Vqy0V4kShEOreUUab2%2BHv%2FxXkYfEz9khLYAWepXTk1wrs4punML3x1MgGOqUBhVyjIp9%2BlOhS1tFAO0SLZjU1gEF%2Bp320RdN8XgQJVce0RtYgCjyu5BeEnbWLnFBEW7mg8wClqiAEwoe42aUQN5Ik%2Bnj1FV4A%2FQoXMrVE%2BiAvMtPPgKO%2BG8M48bB5yDcKZJgYSfDHIYg9Zl04ruPi%2FSaVh12eqKqD%2FTyLXpoW30EzV6smqpoqeOsdCYjM4sNXz0pt58MZwV4D02ESKOdCJw8tpXFp&X-Amz-Signature=db58c006ccc68451ee94cdd6c77697e41cd4f6b188e49c8f3d656416b42524fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

