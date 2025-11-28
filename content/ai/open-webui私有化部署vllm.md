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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR7YQDUI%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHKufPOEX2UZx9hxsd%2FerRSkh42XUgVLd552cBtiLpT5AiEA8%2FGSFMZCdFK3b7%2BEnNVHpqvS0bYV02E9GqfejnMnO%2FoqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHR%2BfdWOFiuscCvTvSrcAzPTu%2B7MfO1HXfgacAtiF%2FdnCq2pyqx504JznxiqLyRL%2FYgyuXXs7zfM9yNS%2BuURs1YFtUiKGzCq2%2FhrTtXviqce0aj1%2BIYK%2BYBKVBkUxyNFggOZFNCj3s5rc8GLY5nlBYfAABW0SGJNrYyw5EIRn80qISIj6cuYDcmp3QrHDxKoc30CI5sBETplV5cpBfa3U1muiAP54ztaneuUh%2Bck2EzN96FB5jjlkwjoF98diAePMDMlI6R76iFl204z4Hx1woX44RLWQv3QdGVz1guKbRubW3yJ0V9k4beyDe6Wdh3bh%2FeHbyXOB6Kw61il4V7dyFEH%2BCRgqkrWWj533%2Fqh9cl4seGlepuIwTZV1qtQGRxdECMvnhP%2BDVhcUEj4nlSJbJDY4FVe%2FnDWuyGE8xBiG9WrvvyuFA0fD%2BvBMVNtb3iABSdW8Xb%2Fm9eu5wXgVu%2BUYo2H87eZ704aH5M8t9k5KYikbyykHsqWh%2BjMqyCIsz3%2Fx6hVAg%2B7qFIbNsY%2F96Ng%2Fs2iyPk6DgpgBVrrNOkH6b6gGOzDF39ndPFcwemRMvcR1YQKHEkFUnnVDa6v6d7KOcnJePqu9mLfTUA5f4kZaoOMIWQlZlVbDlmVU3GK%2FI6YbnVrpXXen1Z5YqXZMO%2F4o8kGOqUB9cPq37XlLaOWY025DqpxJMMqgyXTv4V9I0P8Nk9arL4tEEGBiT1AVr4nMjmPXRMS%2BS%2FOOOJV85SgYzIH6nYf%2BdBpnkoO2XhQfdPLj%2B%2FfDaeSeUXRclHHtqrtojmvMpPnFp0GBpSaWvbqwXIpTsfxf0%2BS2%2B7iPMFysu8ybOrfN4nSnj6%2ByPiooQDo%2B%2BGH2nW%2BKBXqjXosb2mS4QKE%2BtHPJXRjw2RG&X-Amz-Signature=8070c52d4fcd282d5a372169c9bae1bb19025eff307941063f8578bead6c8436&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



