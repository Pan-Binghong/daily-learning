---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNPHGDFC%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn995nEBfYt2%2FFiBHknAzU%2FNZl3X3wivVghDKqHgkexQIgeU0juXCB%2Fb7pSehLLrDSpFXoXjXtdcQCrxCPQBUtxPAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8OZtbzw08PHQycnyrcA83yQ7E8%2Fw9iCLJAZ%2BGkh3HiEp5lIoR8SLkz0EeNdjPszohmBnrxcAtN4dlGmgmlgyd%2BKhKoaocdpnTQfxSgUZpbV0HYlGYcghHcrl0W50G8GcpV4M1o9aBDXudWVdiSlt0TJ3%2BQDN%2FDibf14ll4FLmYr8wZNtFZS63d0w9BcHjlkmbb0P1GKIYWxb9DAb%2BRXfS4ScnIRwQGIl1FrZMmvZ79Nc%2FnnKrsnuF7mVmFPwkSLqE%2FWK%2F9mhXxFZV4Dtns22jywJmAGnWDzsf%2FHeqDk%2FL3uAKdnhZ8%2Baav9%2FOaJrTyH%2BgtoxNxe1xqrzGf%2BA4HUbWcXPPTMERuMf7g8HGKf1w8nWkqTUKAoowTzmkOrwry5oQ2RPAlVfjKpHLpF7hYPwf9R6Qmpfh1lRMaDcQaMpcGb9dsoQpz1yKKOR1eb%2FXKJLFr30zI3O2dxqbwx6PJce6WdYuusvbAydAcHnSOukw0xzsTIpZ%2Fj1Wz4X3FX8KOY55pR8WK%2FTVMYaNj0isvhrtsleEXMO2Hl%2FULis3SxNbWl1JPlfwzJZ4JyR159qY1eK7m6exr3tvPbZjhVyYd1y94XH94%2B6we1crToClNS1Tj2VczKAIKlIsIpj%2FfHAh3LnVmxQzUbuDOkli0MNDXjs4GOqUBChgL3aaUxmlX5h8%2B7P5vlWCDATHsickyum%2B4ACNdVTLg68aAelHzO6sG0vvOoy5ExS6bQsXXfTLcUwwdsRe3S0uxpXA63XHduEjp7h2PivfjXuBYM3Iik%2B6ExzgzC%2F364hRZQi0ST%2BZz3TQmTAUX0ov3SUr%2FMl6g90iXwe89h4nERbe%2BJAhTCKSneKCVh1bVD%2B7L0hjOOD6GKz5PG%2Bn3Tg4reQCP&X-Amz-Signature=6eafe0623871904a945c0723c69ddcbe02f4a56fddc876c82a283e146c19d601&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



