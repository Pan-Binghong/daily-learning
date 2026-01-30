---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYNZQA7D%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtlkvbME1PF3IhqCEE01indqtSzLXpEqQMUP%2BPQ2erQAiEAyrHvTEjfhDNPdxBgk7DgVGlM9eMEApwrkFPY1UlRfsQqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdzq59aaSTi0OpLpyrcA5q14n%2FPJy2XTuxfjJpsLfGBlaUdd0J%2BRiMGVRtjl1mpgweP%2FmSW722v8%2FXpb%2BXrkZZjjycz7%2F963ZKCPzky8oOKCANpxbqDhnOKYVPl%2BdjQ6EkpPawOfFWNUMTQhb2mXf%2BSeYLDidj86i5iOT6MG733GftxJB7XuASDQYC85MpBO0f%2BD27X%2FOjUlQd6yPJWTzObb28zSpWfx90YtQO7l3CcwKTthVP7yUGkP%2FlC43u6zBLTcX9GIkyaoO8Be3aG9Hxd%2BU3qfYp4Tk0KHbLoDCFuB10XhBQ2o3%2FPVrxPjEjPWPRXDx6h6JEH%2BvwZO9Z0Z4Za9KgISTlZoFaEX%2BCg3aodIf%2Bun6ITPjUw%2Bez7qOVgTF%2Bzb5kJmgkgmomTCimmpr0KcG5mucQsR0Mr5rB%2FigfrcbFGOJLAROI0cu1zscsoZaRlY0VpSyBIDcLab7rLKkVA1aQ0pAE5nXh4YpqcodQo5mR0HTS%2BndsEKFCpOMVSwlOa08jLTcHsAz9%2B6R1ziuYPPulVM9j2xrKgomANDCyxKfecPQJhsjBkqVDuDh%2B3MwsPn%2Bec7IOxR8k7ESCJ3y9h%2BSrTU2AMkuJ9MQ%2FmkQLYZ6ssmkCEqyoYvBbxeaOx1kppVNzIOjJLiRxWMLXJ8MsGOqUB6JFpgqnrElvifDeihjP1JTxn33xBIWW5wnd9HfTsfxXCY3lQBptcPETclcp9rvfBauBx%2FEvX08x9TxRuBx5vMHZ%2F6YnZQaOf6wvPofchKfvQWwr5OxuRbzFW9hRc9%2FfIxSBWC6N8UB0HqMNKP%2Bd%2FnCo2ezWHEYLYfTV4lgfDYDVNsU9Q1Wwg2Hu2DDf%2FW8KfCuc%2B%2BPwzvZ5nLjEdCY1skAovuHDL&X-Amz-Signature=c0a109c1fadfb8d0980b7ebe6d2a5131bd5273875dbbe77af305bb37395f47ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYNZQA7D%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFtlkvbME1PF3IhqCEE01indqtSzLXpEqQMUP%2BPQ2erQAiEAyrHvTEjfhDNPdxBgk7DgVGlM9eMEApwrkFPY1UlRfsQqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJdzq59aaSTi0OpLpyrcA5q14n%2FPJy2XTuxfjJpsLfGBlaUdd0J%2BRiMGVRtjl1mpgweP%2FmSW722v8%2FXpb%2BXrkZZjjycz7%2F963ZKCPzky8oOKCANpxbqDhnOKYVPl%2BdjQ6EkpPawOfFWNUMTQhb2mXf%2BSeYLDidj86i5iOT6MG733GftxJB7XuASDQYC85MpBO0f%2BD27X%2FOjUlQd6yPJWTzObb28zSpWfx90YtQO7l3CcwKTthVP7yUGkP%2FlC43u6zBLTcX9GIkyaoO8Be3aG9Hxd%2BU3qfYp4Tk0KHbLoDCFuB10XhBQ2o3%2FPVrxPjEjPWPRXDx6h6JEH%2BvwZO9Z0Z4Za9KgISTlZoFaEX%2BCg3aodIf%2Bun6ITPjUw%2Bez7qOVgTF%2Bzb5kJmgkgmomTCimmpr0KcG5mucQsR0Mr5rB%2FigfrcbFGOJLAROI0cu1zscsoZaRlY0VpSyBIDcLab7rLKkVA1aQ0pAE5nXh4YpqcodQo5mR0HTS%2BndsEKFCpOMVSwlOa08jLTcHsAz9%2B6R1ziuYPPulVM9j2xrKgomANDCyxKfecPQJhsjBkqVDuDh%2B3MwsPn%2Bec7IOxR8k7ESCJ3y9h%2BSrTU2AMkuJ9MQ%2FmkQLYZ6ssmkCEqyoYvBbxeaOx1kppVNzIOjJLiRxWMLXJ8MsGOqUB6JFpgqnrElvifDeihjP1JTxn33xBIWW5wnd9HfTsfxXCY3lQBptcPETclcp9rvfBauBx%2FEvX08x9TxRuBx5vMHZ%2F6YnZQaOf6wvPofchKfvQWwr5OxuRbzFW9hRc9%2FfIxSBWC6N8UB0HqMNKP%2Bd%2FnCo2ezWHEYLYfTV4lgfDYDVNsU9Q1Wwg2Hu2DDf%2FW8KfCuc%2B%2BPwzvZ5nLjEdCY1skAovuHDL&X-Amz-Signature=c057dc8d72b02503052fd6a5691d2a1c28e4cfc47a5e384e5f32261449e8a59f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



