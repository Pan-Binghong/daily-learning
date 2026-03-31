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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S5R72HN%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHqNsQao1vsXdGM9WprxSyg3CxbyKR%2FKoGQNpST6DgfvAiAjcZR9nNIc%2Fu%2B4FtFJJw3WiG6wsbdWWbrbw3jgQ9yw3ir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMudaJJWygpQc%2BRnElKtwDGRxZXSX5b6jtyteN1OnWlcTsuZJ3R8zZYbzJQJGZmbD3z%2F%2FW3wj133DDPL4CZYh%2BW0LahhUDtcZ0ExCNMYjmd1zU8gSyDJCPKZ%2BrybDSBxhSaKF3SgOhV%2B%2BTu0KKwedI5R62MiRit49uPPlgyz30MPTB0u%2F1tQ%2Ff631ScD56ZeTbIGNw6seMQ55Pl4BpG7EVFv4tfO7FV1vZK%2F1W%2BFSdhIBLBU8zN2N%2Fvv8m%2FG%2B%2BsRlSY8eKqtBLtes86u8bcer2ul7fMP0ZwhgYNfeUcupe8IXNsWlyIWm7SpqAa%2FEaqK8igC0CcXi86DWxzC2hw2F1jYLs7GjTLexhzcMkg2EcJnmWLqTYj%2BbrvchyGtnrnLtPMjtQCL7v7RDKiQF1zl47F8A8mDjQqC6d%2B6CMIubiSvwDu41WeuPQQW6E4Aa90WATqaiVo1wT3DA%2BlGJj8ms18O52dMwJrbnvAZwUiUk5R3JSnuctghs28%2BW7OuSUc51YKhwpwMWYS8NVoLSDzwBjzp38zx%2BbFPw3D%2Fk0g62fB0kuzTeJ5z9oK1on1C9MsOQJXiVHbTBofd1X2eFwhWeytTMCgqZYwgVUw4Bo4GeT3vLFSGqy1CGy2P532VbzGB7P4VLBsfATb%2BNoSvMw2e%2BszgY6pgEVlSGIw%2B6rSff6L%2B0LjXtpNUL2A0sH9KLggAEKajN5yHifzNgL3u%2BHNEuXiZHvGEMiakBvat%2Fg%2B2M5YHZiYlvHSLYxT%2FmDinAXEKYi3t5U1LVclPciQUggMiB9z0JOLqYNi1LXjat3xu7%2FW60k1rbHG6s%2BjtiffUKVWSzklqOwiFbo2Qxe7NN2m05m0%2BUk4%2BFxiQTK%2Bxn0MQEB3F5kxYQVDK0yjcRO&X-Amz-Signature=883d9c76b91c1ffcc6c87b92452c289eca8b759eef105be26566bc18c90a7f7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S5R72HN%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHqNsQao1vsXdGM9WprxSyg3CxbyKR%2FKoGQNpST6DgfvAiAjcZR9nNIc%2Fu%2B4FtFJJw3WiG6wsbdWWbrbw3jgQ9yw3ir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMudaJJWygpQc%2BRnElKtwDGRxZXSX5b6jtyteN1OnWlcTsuZJ3R8zZYbzJQJGZmbD3z%2F%2FW3wj133DDPL4CZYh%2BW0LahhUDtcZ0ExCNMYjmd1zU8gSyDJCPKZ%2BrybDSBxhSaKF3SgOhV%2B%2BTu0KKwedI5R62MiRit49uPPlgyz30MPTB0u%2F1tQ%2Ff631ScD56ZeTbIGNw6seMQ55Pl4BpG7EVFv4tfO7FV1vZK%2F1W%2BFSdhIBLBU8zN2N%2Fvv8m%2FG%2B%2BsRlSY8eKqtBLtes86u8bcer2ul7fMP0ZwhgYNfeUcupe8IXNsWlyIWm7SpqAa%2FEaqK8igC0CcXi86DWxzC2hw2F1jYLs7GjTLexhzcMkg2EcJnmWLqTYj%2BbrvchyGtnrnLtPMjtQCL7v7RDKiQF1zl47F8A8mDjQqC6d%2B6CMIubiSvwDu41WeuPQQW6E4Aa90WATqaiVo1wT3DA%2BlGJj8ms18O52dMwJrbnvAZwUiUk5R3JSnuctghs28%2BW7OuSUc51YKhwpwMWYS8NVoLSDzwBjzp38zx%2BbFPw3D%2Fk0g62fB0kuzTeJ5z9oK1on1C9MsOQJXiVHbTBofd1X2eFwhWeytTMCgqZYwgVUw4Bo4GeT3vLFSGqy1CGy2P532VbzGB7P4VLBsfATb%2BNoSvMw2e%2BszgY6pgEVlSGIw%2B6rSff6L%2B0LjXtpNUL2A0sH9KLggAEKajN5yHifzNgL3u%2BHNEuXiZHvGEMiakBvat%2Fg%2B2M5YHZiYlvHSLYxT%2FmDinAXEKYi3t5U1LVclPciQUggMiB9z0JOLqYNi1LXjat3xu7%2FW60k1rbHG6s%2BjtiffUKVWSzklqOwiFbo2Qxe7NN2m05m0%2BUk4%2BFxiQTK%2Bxn0MQEB3F5kxYQVDK0yjcRO&X-Amz-Signature=ab6de3f707fddccc323523d77f473bb5bf5287a1d208aa1cf3b795ef9265242b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



