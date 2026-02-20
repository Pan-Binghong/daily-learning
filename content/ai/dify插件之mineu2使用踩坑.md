---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S326NZVB%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtlsVZqJnXaZalS0PkZG2HdtqvutCzrzgee9FUlnV3cwIhAI5mKzDrYAaTPLtmVKz2d2kfZelhGUsl%2FmeUBM9SH0eXKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkDJS%2Fbk7gf%2FTeZKUq3AN1NIrNu74Sf6YRxif6ZWecgI%2BLdpc%2FIdwUHJ7p9mPr%2BaYX2qumvZivYOnVMumBMEA6uSdSRDhJZ%2Byjf%2Fl29MDGfu0VRESCQODZOJvWCzTSacuhpjrDNmFYSDL3hyyFMh0vENOgYENKe9nkBOWxzOdwcg%2FgOaHmx%2FcWoWo2oyumZ%2BPcucoeulpzG2lpMqx93TlYw7b2kCx4aZtGSEsqvTdCb2gICc6GQxZeeXBPdRdkUa%2FnW80rnmLtUUd0p69C4%2BBP2m8bg9hEnPLyIsCtyAgW5K%2FOoPy5GRB0BMa%2F4hBpNOS1fl5dCAlg7qmWqg4OVTc%2BGiX0ENBbqxFKEmfEggiQTDee2HKuhJxfJCdOyXkS8CT56pvePCiWqWU19PRDViSkkVmk8IbtILHCFsqwKZ3jOQmGikqI90YSAMw2iEKKNABHeDosOrWL16wysX%2BAm2RhT8hz9crAxQwxzA0P6EAA6P%2BDh6SQY1jdab89a1au15pwlSe4ZReYX%2Bb6OzgumSaX5dATwUQgjtCvcI%2BoZaP0DM6bRgKxsT15F8kSKpqMVNYiP%2B2aOSLpC3V0lBwL4ZorbkIn8vX0zIgYl8%2F%2FtUrvrpbs6L%2BFCl2cXC4K6dzyzOgCWgjg3ELMQ1hWCTCbkN%2FMBjqkAb6LsNqKCUGKGb3ZTFEQ5B72ASK3Cel6GA8pe87p9EMvWIeS%2B00iopX0nxwY7lzZnEh%2BjTIfESGMTSCBanlNtD519cr6x7s8xlJ%2BJQm28MaDJiuDc6QE4gG9plJSTjpT%2FfIXG9qP0zhLSp%2FxgE96kdG5cUYXDS6zhub5XUB9CJR1gRdQmZO8ZxuSs%2BzmtX10FmC7WM%2FGE%2F2rhYK6VyeHuolWWlg6&X-Amz-Signature=7cb00cd71c153f7b5e12237757772eefb3abcdea85f671e341388682d28459c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S326NZVB%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtlsVZqJnXaZalS0PkZG2HdtqvutCzrzgee9FUlnV3cwIhAI5mKzDrYAaTPLtmVKz2d2kfZelhGUsl%2FmeUBM9SH0eXKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkDJS%2Fbk7gf%2FTeZKUq3AN1NIrNu74Sf6YRxif6ZWecgI%2BLdpc%2FIdwUHJ7p9mPr%2BaYX2qumvZivYOnVMumBMEA6uSdSRDhJZ%2Byjf%2Fl29MDGfu0VRESCQODZOJvWCzTSacuhpjrDNmFYSDL3hyyFMh0vENOgYENKe9nkBOWxzOdwcg%2FgOaHmx%2FcWoWo2oyumZ%2BPcucoeulpzG2lpMqx93TlYw7b2kCx4aZtGSEsqvTdCb2gICc6GQxZeeXBPdRdkUa%2FnW80rnmLtUUd0p69C4%2BBP2m8bg9hEnPLyIsCtyAgW5K%2FOoPy5GRB0BMa%2F4hBpNOS1fl5dCAlg7qmWqg4OVTc%2BGiX0ENBbqxFKEmfEggiQTDee2HKuhJxfJCdOyXkS8CT56pvePCiWqWU19PRDViSkkVmk8IbtILHCFsqwKZ3jOQmGikqI90YSAMw2iEKKNABHeDosOrWL16wysX%2BAm2RhT8hz9crAxQwxzA0P6EAA6P%2BDh6SQY1jdab89a1au15pwlSe4ZReYX%2Bb6OzgumSaX5dATwUQgjtCvcI%2BoZaP0DM6bRgKxsT15F8kSKpqMVNYiP%2B2aOSLpC3V0lBwL4ZorbkIn8vX0zIgYl8%2F%2FtUrvrpbs6L%2BFCl2cXC4K6dzyzOgCWgjg3ELMQ1hWCTCbkN%2FMBjqkAb6LsNqKCUGKGb3ZTFEQ5B72ASK3Cel6GA8pe87p9EMvWIeS%2B00iopX0nxwY7lzZnEh%2BjTIfESGMTSCBanlNtD519cr6x7s8xlJ%2BJQm28MaDJiuDc6QE4gG9plJSTjpT%2FfIXG9qP0zhLSp%2FxgE96kdG5cUYXDS6zhub5XUB9CJR1gRdQmZO8ZxuSs%2BzmtX10FmC7WM%2FGE%2F2rhYK6VyeHuolWWlg6&X-Amz-Signature=1a2ff45d5ab2a2b6c73a7800d0bbd2476d9223ac2bc07ca4f5b3d6168e7c2e8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



