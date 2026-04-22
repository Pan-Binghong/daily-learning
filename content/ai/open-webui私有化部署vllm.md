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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXO2UZIP%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHu80xHegZ5E7dLiXwMrN8Fd2Rtjw1b%2FlF4w4UssUK4pAiEAvZqwxhXgNcQe2IpIMcooSs33uoSc%2BQFByjGSedpOLaMq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDD0CJ%2FqM%2FbZ10r5g2ircA190wx7C%2B6upqGvcRmcusDpxbUA71TORcXMSPBKRJnSHWPO0nz8RmolbAwOzT%2FdvJB%2BGEOoPGVD%2Ftav%2BT%2BixDXUukTQCZGZVMXE28WKsFbWl7O4LanM36o9nwZzyvdEw%2FLpTE9QcHDLdLu0bgqIJm2AoUJEQwe8w9XjPKs99vTNVyfRIrDnivfpf4Q4C1ta6EsllbhR5EoJvfu6Y6A%2FgPcK2C%2BiJVpmXF5zIOHOa3xCdL4lDjv01i2QPrPKsD4%2FKp%2BQpBW%2Fq1pUYBvrzwIGjpDKHtsqzvnQXp1LS8fctRdpAgLSzquprJHDHv1bYzlpc%2B2TWiL132Oq%2F4bU%2BLDlLnVOxKW%2FBheWhmWyujMXjaMm344qt8I2ikqv%2FWQkbzRTTCp%2BSI6QYWyTcvB6H8bIsCVvo6HEIJa7xhEG3lYOcv3EnZOXhlpXRI5tPFGOoUE4XQNCk5D68WT2iYsvg%2F2dV%2BYNb0hS0hdSSB5eLXj5fhpGpvv7cQ74pER7Z4DFjapao9%2FD4sYb%2Fnn1Ot3Q60NDQD5vX6u7u1IJDFQNeq3ZID%2B8yGxlgv7APpa71CYRIypZGmVEZfsK2Z4NaUDLNWTzNPXTnmDWDqfdPV3GGtCR5KpY0p9MCkgcebGkEbZ4QMNj6oM8GOqUBTDEk%2BKdelbXFz0Pw%2FsXAmYwE4HJSCuz6jx0VsD8pK5JDd3njocZ0UnlA9jyX4Zn7c0gv5sQcny0moEQimGrNoDveRoHi4FIEZK4D64srDkcO1iwqw2iyCMwMgSSIdET0tc%2BiMUpJl0S%2B85tEPcOPPa1M1dLocw4jTAJsHMTRaTryGG0tF%2Bw6d0h6pLVZMRT%2Bpxlmfe%2FwDDtLePuXcvyMb7vIFuT3&X-Amz-Signature=c42e64067a16302c7326770cb0c3cd8d51ddc7027786f3acfd4703058faa3142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



