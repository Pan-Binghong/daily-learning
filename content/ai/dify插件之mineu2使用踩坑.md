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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466262JFGIO%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDaH7hOfo1YNBkWWZSLpxyYmdHs38oU7tWmHP1hcZd9PAiEAtGj3gJacOZlCLFGoE6CiYoVgh3x3idKkY3kyWf8fr4QqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkqfk5NVwdGFecr0ircAwoveniv2SfsWXjjEc50p7qalSEd1AF1RRDaBAyIHReHSpsaVtpx4fnsWsAJVaRt11iUeL3BYyQZ%2BVrg9KXCukrZzN%2BF8KBcSxcY3kcmePAW7s5K%2FjLKbD%2BGg2i11wyOSzgTfMg%2B%2FCxPdsgcRKQgpuQcvF8RuEKfzg4Qmo%2BVtaL%2BOQpv9xovy%2FKkBP%2FimQatqGqoFL7VQ%2B9iTks2TZJzOHj4g5hYf%2FfbDYIuUNw51SLtfybWF7%2BlkVT8MhDND9vTCIv1fV7Zu0r7QvDD0ikUmXo5qalGm6gt0EL4zGSUXPyVUfsgp87YHg%2FxDqjoKv%2FEHBFT%2FxLD3cRascvHLc5bfyCBbZumDAkFOJFJP1JNvgRs4c%2BbF8PZ7LVVAra%2FeAzzjnTobgOzpI4bvhzjsnakBptyQ8TW%2FAuEQrboNV95lZ0Igiusssbx6DI0rtRi6qgHTEwLndrJ0p73Z6vcMCp39MTjVQulqBsMk1xCGyvTKCcmKmxp8Oc1WdOmlhtaTHdcWPhNdtTVfnsP6JHJR1ORQ8E9B2%2BP29kM5pumXVBAQ6Ck89hPKd015P5HRp2KfHFRkPkoB3F9008F7J4FPLaIr7ODgYXcusfqwSR9XSdSm0%2BSwPs5GqXzCkTS3sx7MMPI8MsGOqUBsb7XspjmMjD18fb%2B3a1wWQTIIUbPd8PpRO7FcuNV7q0R0kmL04W8o0Zfmbr8QnLyVl3saN6MuurhzzbSgKUCJtZzsVDK2IIi7SOynH7TvUejqxjOnyXsypD3mUBSsKk7HZ36xDykmD7bq728XYTvI0e3QXAFP%2Bp6D7blzYTBwtdjb1ErvohAzKVGSlnT6txfYxItTfcnq%2BReUBa3M3JOELKxW%2FjF&X-Amz-Signature=252658b245df83c5f8f9807ed60f1c3d4a09241055561bf6bf90b6c295c98dbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466262JFGIO%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDaH7hOfo1YNBkWWZSLpxyYmdHs38oU7tWmHP1hcZd9PAiEAtGj3gJacOZlCLFGoE6CiYoVgh3x3idKkY3kyWf8fr4QqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkqfk5NVwdGFecr0ircAwoveniv2SfsWXjjEc50p7qalSEd1AF1RRDaBAyIHReHSpsaVtpx4fnsWsAJVaRt11iUeL3BYyQZ%2BVrg9KXCukrZzN%2BF8KBcSxcY3kcmePAW7s5K%2FjLKbD%2BGg2i11wyOSzgTfMg%2B%2FCxPdsgcRKQgpuQcvF8RuEKfzg4Qmo%2BVtaL%2BOQpv9xovy%2FKkBP%2FimQatqGqoFL7VQ%2B9iTks2TZJzOHj4g5hYf%2FfbDYIuUNw51SLtfybWF7%2BlkVT8MhDND9vTCIv1fV7Zu0r7QvDD0ikUmXo5qalGm6gt0EL4zGSUXPyVUfsgp87YHg%2FxDqjoKv%2FEHBFT%2FxLD3cRascvHLc5bfyCBbZumDAkFOJFJP1JNvgRs4c%2BbF8PZ7LVVAra%2FeAzzjnTobgOzpI4bvhzjsnakBptyQ8TW%2FAuEQrboNV95lZ0Igiusssbx6DI0rtRi6qgHTEwLndrJ0p73Z6vcMCp39MTjVQulqBsMk1xCGyvTKCcmKmxp8Oc1WdOmlhtaTHdcWPhNdtTVfnsP6JHJR1ORQ8E9B2%2BP29kM5pumXVBAQ6Ck89hPKd015P5HRp2KfHFRkPkoB3F9008F7J4FPLaIr7ODgYXcusfqwSR9XSdSm0%2BSwPs5GqXzCkTS3sx7MMPI8MsGOqUBsb7XspjmMjD18fb%2B3a1wWQTIIUbPd8PpRO7FcuNV7q0R0kmL04W8o0Zfmbr8QnLyVl3saN6MuurhzzbSgKUCJtZzsVDK2IIi7SOynH7TvUejqxjOnyXsypD3mUBSsKk7HZ36xDykmD7bq728XYTvI0e3QXAFP%2Bp6D7blzYTBwtdjb1ErvohAzKVGSlnT6txfYxItTfcnq%2BReUBa3M3JOELKxW%2FjF&X-Amz-Signature=241f42fa443df56ab909ce88baa024ceee385b6bcb51237178edd12d7dced2c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



