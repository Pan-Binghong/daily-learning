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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXFMNQNB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvpmzqwxg3xScXmVzFzYxF4TvbG4OL9Z6634rjaDrqqwIgNB8sJVm%2FViwtCMiLsXZBf0wXpQvfmt37u9yJUhgNOz4q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNQd%2FP5z%2FtcfhlQgkyrcAx3q8NymL599K0IJEjD9FiViZb%2BWEIty0TFtLX0qUzanSgr30Hj6mYllH4n7EpRxD3lvHssZuaDclwf6c8Eysa4mBCz5mmwVYx6Co2lrfnupyksV8rrObOnLq5E9aQC%2Bl62ZD7iE75dmItP3N%2Bs6A0cthiR4ZEDvHSePESSsJEYIcsyOngWYmAt%2BFhfUxVKoaGIzTJozZ40EQIgz1sc7LTxQK8ER4oB%2BkQcWVVrOerQ9mKvtf9aYIrU7pcXRkGbA1hc3YV7pvloXtMZbLAG7%2BlcXFgPjG%2BTao3Ts5gQMlfX%2BpUS3zbN8CfkdZpu4mqGYPX96qLbwftm9YyzH68HTwF%2FexsiLyLQ38Cq498VCl3tvWsLZuNquR0BCkuosHUCCt8lPSASErme4bM7XaehQWMmgyvBTAwKdVeUB0uT6SGqLcfCuzFgkELn04xXS5i6qfB4fMEks0fNRWe11GUuEF74O5I7xYPXVM4VZMiFv%2BbhZNmfd8vnjRMYOfZ9yxTknEBQ%2FzTeQTndYk7eKektnv%2BwNK5adCh4o3NKVvmcgCsnCuqsosbC6LrPh6cskcgkFLpSTUpOdPCTua%2BKrb6pEWZv%2BLI%2B9sFpmg09I77iFq6eMWaa8XcGrd5YqybCCMLeBscsGOqUB8GhbpFv3orIv55tVYHKWp%2BroWoWYc8fdOS1rjJAirtxaf3rclh7MynRf5hM6PyZC6swrkbcIsfp2dS0zFabJhvYn9roTpDC6xLALMhNtaapPoUL6Ml7VuwDslggDNhJ3vOC7bo7RG%2FgTGSbnQcybM3w%2FokP49UyF4HSdZsBBz%2FKvp%2BOzbbLsYALX8bQ%2ByiliJl0ZAWgNGhx2kNDI%2FH8e90uVu16i&X-Amz-Signature=c2d9d4ff14fa0859c48d147f49cb2a20929c458cd2e42fb537728528f09566e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXFMNQNB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDvpmzqwxg3xScXmVzFzYxF4TvbG4OL9Z6634rjaDrqqwIgNB8sJVm%2FViwtCMiLsXZBf0wXpQvfmt37u9yJUhgNOz4q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNQd%2FP5z%2FtcfhlQgkyrcAx3q8NymL599K0IJEjD9FiViZb%2BWEIty0TFtLX0qUzanSgr30Hj6mYllH4n7EpRxD3lvHssZuaDclwf6c8Eysa4mBCz5mmwVYx6Co2lrfnupyksV8rrObOnLq5E9aQC%2Bl62ZD7iE75dmItP3N%2Bs6A0cthiR4ZEDvHSePESSsJEYIcsyOngWYmAt%2BFhfUxVKoaGIzTJozZ40EQIgz1sc7LTxQK8ER4oB%2BkQcWVVrOerQ9mKvtf9aYIrU7pcXRkGbA1hc3YV7pvloXtMZbLAG7%2BlcXFgPjG%2BTao3Ts5gQMlfX%2BpUS3zbN8CfkdZpu4mqGYPX96qLbwftm9YyzH68HTwF%2FexsiLyLQ38Cq498VCl3tvWsLZuNquR0BCkuosHUCCt8lPSASErme4bM7XaehQWMmgyvBTAwKdVeUB0uT6SGqLcfCuzFgkELn04xXS5i6qfB4fMEks0fNRWe11GUuEF74O5I7xYPXVM4VZMiFv%2BbhZNmfd8vnjRMYOfZ9yxTknEBQ%2FzTeQTndYk7eKektnv%2BwNK5adCh4o3NKVvmcgCsnCuqsosbC6LrPh6cskcgkFLpSTUpOdPCTua%2BKrb6pEWZv%2BLI%2B9sFpmg09I77iFq6eMWaa8XcGrd5YqybCCMLeBscsGOqUB8GhbpFv3orIv55tVYHKWp%2BroWoWYc8fdOS1rjJAirtxaf3rclh7MynRf5hM6PyZC6swrkbcIsfp2dS0zFabJhvYn9roTpDC6xLALMhNtaapPoUL6Ml7VuwDslggDNhJ3vOC7bo7RG%2FgTGSbnQcybM3w%2FokP49UyF4HSdZsBBz%2FKvp%2BOzbbLsYALX8bQ%2ByiliJl0ZAWgNGhx2kNDI%2FH8e90uVu16i&X-Amz-Signature=dc1af36210e96c4dffbc52cbe00def70a335925868a86de34ffcd5661034842b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

