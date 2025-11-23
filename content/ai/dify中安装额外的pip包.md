---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHOKKXBY%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQDjQaX0YE2%2BfnNXCBMKoiR%2B4aBDzfMldUFvaZAd%2FS9ImAIgNxvYNvGTqf73xmm0LofTUUi9R2HMZ3dyXy%2B09WHt2ewq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDDoSj1YunZRlu0eZpSrcA7Xo5v0vCDwVn0pOniw6tkQgur1TU6xGfCCsIm6EBbOaImGNTlSD4YWtWTG0k9YchmG54wZ6B5RCJOl7MFgHh5caHfZdfmHF3zCob1%2FaK53hjYL2wMo8FsWBH0U%2BuR6t0AFfvYPK0w4CQvw9GqkdcOs387EDKtyfj06IDa%2FSNNMODI95NQCleh9x6H5u5ZwE5%2BkZjj3Il41IskRO3GjTSgbrGXDr%2FoVIAw5RzzPQNNkaRRYzXgTQ%2BuvxgoKzFNeW3tB806lyfZYWIi9gnb3ZfVbiS7OwGU6b0t7qhviTtRi0ztNXNRTWgQIugDHBmuHwWN7RuOri8A9Zwl%2F2V2lk%2FCwR2LhmByStDLtSvZ1ylfWXMEkb5LfBFzZPlspCY0TN5ouS9LuBm8OH9FJDlY7MLRaxEaGKbSFEbmQLAi2TxDU3D58sP%2BxWYRqSAHNl94Y0t7i6sXUd9%2F3OzbAENQYEJytqDt9vUMdIQbNlzYgmKYaAraRxIs0dDXp2drDb4FdaXNHhgZbWsic7OkcX6opmrzK1vVcw72p9O%2FecPQxuMuEJca%2B4GPr2r2BasMX3IK8%2FUORfjvSRNnYwf9LrZU5RW1pxgCsFyLAykCaOO6uvrcqhODRLlaWHmYNK5wcNMOuwickGOqUBLuwqPAskU9b%2FwD62OdVuysW2nMW1En2tUQOe8nJvcgRYPauvngm%2F4ljPWm1B8f5XaNQM3iuuh%2FUea4iKCfK3Qo5gkKWOJTOPhiuuX%2Fy5HjAU541y7wTbxvcAU7QwXrPZsxlsgToSA1HUYJ%2B280z7QVYOVFdQ7uw%2FQl4%2Fm8KOOpSsJZyrJh02hA5QpdrclzBujrfI9vGOj0ssPT8SGlvT%2BFGrd75m&X-Amz-Signature=e51d269453b48c10a61a2f5b2f89ee82f7a13eac9a1f39490690ba94de07a1e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

