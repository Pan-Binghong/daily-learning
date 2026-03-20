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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IBP5PQZ%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIGTGxQ5O3w8NtrcQ3WxHXPY3IvfGzTmMhuNkD9hqPnhMAiBYCsB8Hb%2FyJHaH6RFMbbImzA1egSbGwCC9UdELMbY53ir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMjIHFV5VnJmDvHBjIKtwD0e8ErP%2FPkrCSps%2FdF0jqBE02KExc5pScKRgMnE0Dc3BPFPDn5xYZB%2FTGZW9YpiEyo4UbD079NvndA3Z%2BHTN%2BALLiNjyYhGsYo9tmggSwoER2IM0SC1fsere7ssai2AgyKaeU%2BPO3RkYXeg%2Bpaujnqp31A8Kow7Rz488vO%2BtjhC7QxG%2FUc%2BLWijHTRBnjITnr4GWAnEBBhEbLcHgLGiFiupRhYt04PEykLpIBh8nwtEtxqH6ysWh9pe%2B7wmNaTGW0CqenqijBN3uMH5SZr2NXmEdE1p6KQXrOYFrkDiegoKUNNuxPZrvJoicxrN5o0%2Bro9zg3CmrYUYc18FyoxIjMnwaZ336caKx3nmWy6nXkYNGFK9Ac4In%2BAwDKXu1KTd5xBA%2BLhoiRu%2BKLOyP4YPojoyrGYPHNyJlMGVmgz1u3sJ8AgLDNXrZFUEGDYTCa5N3DpzN0eABsZmGwMZQ%2FC2BlW2LE4kEcA%2FcNyt6GrTzByvxRrwQ%2BUA3fk7b%2Fdtypi5U2xc6g8RXc%2FfIAs9AZA2PNuTzk4sCz17zANEkBTeJjgYBha32V6yTJDmjz7smAi%2FEZ8j2HHoUEfrxRJqZUpE5p8gTy0DLOCP3%2FKs2bPM0P%2B0ffQUdgrCmunhkEhB4wgLnyzQY6pgH7ZYW5hkbV%2B7%2BMmcwxu%2FT1NjDVm%2Fs2PX1BoROseTe107fdEXlmAMRM%2BWWhsAnsCEWCK9%2Fqsl8C9Q3LEB6bzVj6h2e2Xt%2FhDkEEokpSZT%2FQ4dcy3LPlIgBPFNY48sD%2BhjLlkx4%2FvkPcavzcBn2Wib0ImBD4c34Z4%2Fh12MoyLQ35LDgWpLoTberiRbfK3ukXynlBaV2g%2FFyRGXmERg8tfGjRm55dti5H&X-Amz-Signature=c4dbb4ab60da97c3eb480efb8d575e1830f1b4ee2720bc16fdd80d61e90b71c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IBP5PQZ%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIGTGxQ5O3w8NtrcQ3WxHXPY3IvfGzTmMhuNkD9hqPnhMAiBYCsB8Hb%2FyJHaH6RFMbbImzA1egSbGwCC9UdELMbY53ir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMjIHFV5VnJmDvHBjIKtwD0e8ErP%2FPkrCSps%2FdF0jqBE02KExc5pScKRgMnE0Dc3BPFPDn5xYZB%2FTGZW9YpiEyo4UbD079NvndA3Z%2BHTN%2BALLiNjyYhGsYo9tmggSwoER2IM0SC1fsere7ssai2AgyKaeU%2BPO3RkYXeg%2Bpaujnqp31A8Kow7Rz488vO%2BtjhC7QxG%2FUc%2BLWijHTRBnjITnr4GWAnEBBhEbLcHgLGiFiupRhYt04PEykLpIBh8nwtEtxqH6ysWh9pe%2B7wmNaTGW0CqenqijBN3uMH5SZr2NXmEdE1p6KQXrOYFrkDiegoKUNNuxPZrvJoicxrN5o0%2Bro9zg3CmrYUYc18FyoxIjMnwaZ336caKx3nmWy6nXkYNGFK9Ac4In%2BAwDKXu1KTd5xBA%2BLhoiRu%2BKLOyP4YPojoyrGYPHNyJlMGVmgz1u3sJ8AgLDNXrZFUEGDYTCa5N3DpzN0eABsZmGwMZQ%2FC2BlW2LE4kEcA%2FcNyt6GrTzByvxRrwQ%2BUA3fk7b%2Fdtypi5U2xc6g8RXc%2FfIAs9AZA2PNuTzk4sCz17zANEkBTeJjgYBha32V6yTJDmjz7smAi%2FEZ8j2HHoUEfrxRJqZUpE5p8gTy0DLOCP3%2FKs2bPM0P%2B0ffQUdgrCmunhkEhB4wgLnyzQY6pgH7ZYW5hkbV%2B7%2BMmcwxu%2FT1NjDVm%2Fs2PX1BoROseTe107fdEXlmAMRM%2BWWhsAnsCEWCK9%2Fqsl8C9Q3LEB6bzVj6h2e2Xt%2FhDkEEokpSZT%2FQ4dcy3LPlIgBPFNY48sD%2BhjLlkx4%2FvkPcavzcBn2Wib0ImBD4c34Z4%2Fh12MoyLQ35LDgWpLoTberiRbfK3ukXynlBaV2g%2FFyRGXmERg8tfGjRm55dti5H&X-Amz-Signature=73c66dccef4c83d1c026e134e2ef4914c5847eca545c155ff3bd92e96ce2ae1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



