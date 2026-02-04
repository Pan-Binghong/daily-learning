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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZY27XYK%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIAKL7hsRGeqTVefXuxv4jlcBmOCNOqgmnlxacvyxgr%2F%2FAiEA%2BwpbceQ0WKAVkzUK5L9cYV8egdA7PahfxB5UiZyydKEq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDEZnNbQpbGAo2P7oGCrcA6oSxlyCuJ3BEyHJ39BwYcBxpS2dyftHafD2kC2HB%2ByrG3RLOoRcY0tM%2Bp2TD%2BoKNfhCyPRGtntVfpL3PVWbze7dFmRlvuFTuFPzwq0n34dK%2Bekhv%2BJ3iLdzZ8sS%2Bsw3DzOWbmzbdn1A74ScHmt8DVQzYeT3Ym9NCop4bp%2FlMrX9gVLCTH%2Bi7ig2pbEVwxVTjNL4iM8QrYgGttnA1jFlLHiGsRWUvKKY5XNwWFRcBpWcCoD5BYHvnx33ozzXpcIMcfIdHzqetv4qxIxVV96bZNSlbJyh%2FwdoJaYS%2FDjsDJXfRecgDIFOZOp4HkA2MZQrO10BvoUtGR2IL79NF1ncdRiLiQLTKe%2BOWD4EtmhNumpOtuj7ULPfEs9lAGql8San3r4a0PrJAHABvLlwYS3KuU3HS3TGPEO8YYmyjzbavl4lMi5rtPJAQ9kUEMhRS3GmdJrLcs%2BpddJXUXgJaOlEPFYP9e%2FcGDE2ofnlXtGBsX68ULYfu8lq3Q4q7ZumOBt03TUVP6JsfNZ%2FGNPJLzyP2TooNxE0iyH7klAZBgkBPqAS5L1MdbvzI8fp0USfvK9AtYz3xBao7%2BbyFK%2FNFCmcT%2FwwysDupJwU%2Bq4H2VczusHN2I92r%2FNbUUgqI6xoMJfpiswGOqUBfAPx3Bsa%2FpemETj5byYEnBkcbBARTWo8Sit3zNyjw3Tt9HRLZt8MgPKpgD%2FaX6Zrec7NDWoxzanehGfnkKfux283586HX1ppYZHpSx4klDMCe%2B5dqd3wL5sHRSbMHOpc1bpqlhP7ip0Ly3zCZCwo%2FNeQDNzoiUmS4oJKQ2PwHu6uDepSy6WXOiGEc8QTOqa25PsURWTFiFYDbaKNLFha6WwSaN8f&X-Amz-Signature=1f6ae1331fa804d55d6da513c347f33d982cb5dcffdf1506ff03b38b25e01818&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



