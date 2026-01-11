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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVD4QXB2%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDEDuuNycSNywTigK67TOXIg2Qv4KyaRXYQXd2qOVBrYwIhAKKg%2B8CyULtY8hYZ7etGzP247ZD4eRy0a%2BZtNF7vpT3QKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxNs%2B9omj565f4vNkoq3AOfIA1hjZchDNggWPtJ6J7T6gjYyRZFjIuLy9k8LVDiXDLGndXK18LBupIPVgYEfNKT%2FGmK76UFgY22TUSr%2Bqr9oTlcerTCoOplVeADUm%2B8t99vfWOptrrSVs5p%2BydgWR2Rn%2BeJ%2FUSOUkSVpdKZ6OpUe4MSYd%2Bnvi5US1SdrW6nyAMC4nhf%2BaPpgEd6kkxyqEWYfOPaHm13FxCF%2Fek%2BDu0qOSp%2FYtD5HXZqYy21Nb5wYJQO3NUfME6lENwUpbMtWZdBP86ft2khUlsPBg6IhKHkt6saEXc65Zjg01zNPRMy3%2F3fE3kIqgDjOek8QFLn%2FBbd60hAzEFCCo5Ytej1C911W89FSh3nwz1%2F0Rsor6H1uw9KjZiDgMonHNDWHBnpVqCV4p55i%2FQsC0zl%2BPse76YitkVupASBP66AirbC17BIKUzVaLbJSTpfxaHL%2FylRP9ATnujlih59RcrjHJDxqEFMZo4%2FbFT%2BUrNKl6Si1SZ287A9V3c0o81i0lO2ugbgTklNSr%2BdeLBx0S3699nI4mWNjLCsYDyvDQcaEBLeq9835to8Bfc6%2FzvP7R8D%2Bg9SIynydr1rFfPX8%2F6k7drWyE21qgME2mBA0HD4xo63UYCSSqOmXebQdgB2cNRFljDP%2FYvLBjqkAVTcxOY50O3OCcDqEfet5nffmcwwy7s7btTJMHj1eoB3eHOGGAUPfOI7nI4JIehgLcjuCYbzKZz2cnQS3FJ0ECVy%2FeTY7H7ZDo4JSM9HD2KieKVyIltT5TAWNfcnQ79r6w40qbNo2zzOQZhaJaDzMLvGWVcT7%2B%2Bvt%2FVnurnr%2BM6U9d8Q2ky4wfYE%2BRJ%2BYxlMbiXyWziTVWDYoUmFvHv3wJdm5FVe&X-Amz-Signature=687412b9559ec5694ddb2bbb06759eecde35a70071b365d7d485280e18525367&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



