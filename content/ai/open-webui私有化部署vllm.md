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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UI2V57TJ%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCaT9KUfUd7xy11iTCJOARm2D%2BxKPlroUSrrVhVkwRenQIgdIW4a1zhIuplHFVthDXlLBhnjC%2Bv3C6bhG3%2F55tnas8qiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC612dMuissWjCpTvCrcAwkdau2c7o52mau0pkJs1IMPwHwt9V%2FhBRNIk45jxwAOzdxbt%2ByqBuLO79tfOJCaSE%2B1RUfiMpJaH1pq%2FQw4eDzLm1g61oysttJ3Dh9UMGZEuuqGFcogABLUuY2v4t%2Fbh9gn0wm1UNfH%2F16LouP4gaK9ik9EyWATfEnkVpqji1lA%2Fln2wRo5%2FabaHOWu0slSW%2ByObPmfQSn4zMnq1hMdpF2VDpvtjPEv8PlEbJ0oMRlwUZX%2Fb5FwFOY86EMNDd6D%2Fgc7NicEP%2B0qaxTHDDgGm66RcXpwcduOX0be7z1GVEhNPsIcOsZO0lirPWNCAoBYq0N45yAG1KemryA9Gs2xiIzRpcGIfvotyLEgdbu2wC0RVtXUBeWb1AOgSuXdVxZ7RF67%2BMkLJgo63jtB3LvwPaoUowGNQRtHOrxXlN9FPlM5U1yTk4fJWauDQXWbr%2Bp9zP5%2FNz2kkXvHrAVtkQU6FDgC44hYZHuJOMTSsi5rZA2tAiWHTWkzEPM8w71u712b6Sp64eNeKpsSm8t14pbgzxmGlSrqotvckOL%2BudFZu9UBP2mpg%2FOrd%2F34VhHXMtlhOf52b7PzXVWwhdXEZYB1YC7jXVkMXoJd%2BnVSBVRwcIj4JpILDN1peHxn0mzrMIO%2F3c0GOqUBjHqPo%2FlValpFE4Pw38HfiPNMx5NO3VT963NOHtjgsnXc5G4PsFeaeEjnYMZ2mAh1oNm9x%2B4XhubQYKNm%2FFldCqxkVogQ%2FUPP5Pvug2E7BiMrLD6vfwhfy%2Bk%2BI%2FUgzT%2FcX6J982ZKNyKcNKf6qQrq02HWieCtInDd4Cxpwh9yUtH1jdLkhbofnVgBXF8MwbvpryZYcCA0%2FleypIbYFY7S7J5dUhWY&X-Amz-Signature=e154a7da35ff6cc271c628b438fb399a6871e5d7a8ecc989db9d99b56e5db0d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



