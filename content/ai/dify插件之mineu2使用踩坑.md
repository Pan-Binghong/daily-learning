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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3O2NQIR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSExaEsTWTCySQR2oN3sinjsNUdSLPCFccotvEYxsu0AiEA6kPqQ59KPoVWiU3sQlbkWNUcGzKH3buogskq3SaXOlcqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnsbQXHtAgRvtr3USrcA96Wcu6von2g8jG3SJL9v7OviZ5rAnE24ozOKsGJY3o6HNMqHSFxBYQRQOMZCz%2FE48tKHL0NApDrzYgZu7pvYKQQYKfkUIf3ujm4iGxio%2F3YWKjlEl8I0iWTIwDkfZGIwTfi%2BzHw9Y4cr1LY78mgAeFKmSyyDbssXK4IuAfyiTo1swSBl42XkTJCT27k5bHF8WbIRNj75CpID%2Ffjaiynk6anBajFy7goGRnZht1V1wPpaOg3xC4iFFsXgrdmBLUbuDAL2p97Q%2BJlR9J%2Fi5Ofh4m8rYu%2FhDtf%2Fbash3zg73nNiUit3Ps6ALUZpyQPqAmGHVkdEhZwiFm%2FMbPeyP1z5bZaIoPQH8a0dMW%2B7AllNerb4TbdVsdfgsk1SS7%2F0LXXu%2FuRWpn73m6pJwnu9LhoroKMsQoh1VSEx2Q1vVdnGn5BEF0n7kefBcfCn3FjzMEGRhPK5FOrL2FWGweTn1o%2BChZ%2BDh24so6XZDrrPVQ8EapO8QdgPTN5SnWREk3aYwH%2BUfuoJM1poN7TyUwOv0YqnIbBDH4R7RSZkkPL3RyarA6ix6qyJwrtMck%2B0lvAQDHHau7aeubjz1g3QgJNghiRGxEoN%2BXKfKYH4xoqntlI96a67Za3X0mF%2F3ne1MwpMIS1tcgGOqUBAiIllZ%2BTeawoqLolWlnH8JRT7tDN8xLfmUiha99ekjUWT8TpJtHWvfY5q2lw8xmJKmFnXbk1Itjxzlzjm9saAmuk5rtcTvsiQFwz8LdpABttYoG8B4j%2FLikWKUBhldw%2FpLqyhISsC4du9yOjeCnWsrz9cb6OCZeWAE7gfoj0MWU4%2F97Ujtu8i2wxx8z8KGM990SKewMrT0%2FmNpIW%2F4fgo2dwXmlj&X-Amz-Signature=e4f95c89f884dc6cb090d3a3e5fa1d7d81505e9ad528be80efd006e6aef257b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3O2NQIR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSExaEsTWTCySQR2oN3sinjsNUdSLPCFccotvEYxsu0AiEA6kPqQ59KPoVWiU3sQlbkWNUcGzKH3buogskq3SaXOlcqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEnsbQXHtAgRvtr3USrcA96Wcu6von2g8jG3SJL9v7OviZ5rAnE24ozOKsGJY3o6HNMqHSFxBYQRQOMZCz%2FE48tKHL0NApDrzYgZu7pvYKQQYKfkUIf3ujm4iGxio%2F3YWKjlEl8I0iWTIwDkfZGIwTfi%2BzHw9Y4cr1LY78mgAeFKmSyyDbssXK4IuAfyiTo1swSBl42XkTJCT27k5bHF8WbIRNj75CpID%2Ffjaiynk6anBajFy7goGRnZht1V1wPpaOg3xC4iFFsXgrdmBLUbuDAL2p97Q%2BJlR9J%2Fi5Ofh4m8rYu%2FhDtf%2Fbash3zg73nNiUit3Ps6ALUZpyQPqAmGHVkdEhZwiFm%2FMbPeyP1z5bZaIoPQH8a0dMW%2B7AllNerb4TbdVsdfgsk1SS7%2F0LXXu%2FuRWpn73m6pJwnu9LhoroKMsQoh1VSEx2Q1vVdnGn5BEF0n7kefBcfCn3FjzMEGRhPK5FOrL2FWGweTn1o%2BChZ%2BDh24so6XZDrrPVQ8EapO8QdgPTN5SnWREk3aYwH%2BUfuoJM1poN7TyUwOv0YqnIbBDH4R7RSZkkPL3RyarA6ix6qyJwrtMck%2B0lvAQDHHau7aeubjz1g3QgJNghiRGxEoN%2BXKfKYH4xoqntlI96a67Za3X0mF%2F3ne1MwpMIS1tcgGOqUBAiIllZ%2BTeawoqLolWlnH8JRT7tDN8xLfmUiha99ekjUWT8TpJtHWvfY5q2lw8xmJKmFnXbk1Itjxzlzjm9saAmuk5rtcTvsiQFwz8LdpABttYoG8B4j%2FLikWKUBhldw%2FpLqyhISsC4du9yOjeCnWsrz9cb6OCZeWAE7gfoj0MWU4%2F97Ujtu8i2wxx8z8KGM990SKewMrT0%2FmNpIW%2F4fgo2dwXmlj&X-Amz-Signature=d7a18114754c2e87868b5ddc60ef9767e9667a4d983a54cc87e124395b96c82a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



