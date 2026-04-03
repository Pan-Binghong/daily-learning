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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DAPDMNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgPjxsgMdutC6tWFUmviXs%2BWcQdLqkPGMkblrfgWd1kgIhAI1SLYMkyewQN4rwHZF3cCorurWC5UlD3bET6PecIyiQKv8DCH8QABoMNjM3NDIzMTgzODA1Igw%2F8KB3FAOKKI2XicYq3APg2kep8%2FcY4I6xAfy1wGgkUVt%2FOg0NIIrZZskbZYkGGBq%2BNz3jwza%2Bj5cbKdUd0YX3T2pucRTPKnEW7PKInD%2Fb%2FZCvJDeqp%2F%2Fqw3cEZFmoCmtCknOUEAlYHlSnuCf4gv%2BfR0cU4XX1UR8wLV6OwJhfISJEH0c6UmNgu1kI0OMqgouH3Q%2FiV%2B76FYBunJWHuLJq3Uhv1xfnUHmio2dOq40If0zshxmcs2pSvlkUdZB2S1rqI8auwEYVuYTHjn2iXrCMXn1x%2BPqeLKTqnUsWzHsI5t78Ze7lWxSBLFO2WM89JcTB7w0m7Dza42tCewKnZw7YvmkQGL5ov1atIJPs9dTjT115Rr6s%2BPAjv2ti2sNVE648lwx2GeLVxJg3vCZ19J68OV1qJmNhyrAmRfUwJXEFkK0JtyuwV%2Fc70JlW7LCmCCbtaQhVEVZ8oqMJdjrvG2mOm1OsaBnVPRg8zoxQDlQWoFcgumtrtVLtWSJP4RYcfGv8J%2Bo0Ce6jfz6QLfbcXcDcVIxFpEE51oaDKsLyg5FYqz29fJJTaskI4Bo6LyOOPZo%2FMDivmwRsQ39brb%2Fpkybu4u5U%2FuBIQbcnA0lyJVUik%2BPKTxALDzobJi0YKAlJmuHy%2Ft0aPlguTWk3FjDcrr3OBjqkAf9uk75Kbb9lkfsV1D5eZQenFrIjxJ5TW3nFfLRt6d%2FNSpeqyez7ug3d8Mn2MttBchznoH7pjBqsuOrdlqGRAFdpBIKx11jgE4mpXejUNOaI50lgLzDxuYXR4KXcvnx8hjDzZNU5cv8jlRnwN0xV2mVaVum7Z5Ij0ZMkNXev8mUs9vvmU1jYoFw6%2FUEuOFd8T%2Bnqwbtiy37qQWHRztp3ZHQbuYnl&X-Amz-Signature=fe77e5b4fa2b6a51b341ab3c898807da8ade031db27d892c4f13f2395b286c6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DAPDMNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgPjxsgMdutC6tWFUmviXs%2BWcQdLqkPGMkblrfgWd1kgIhAI1SLYMkyewQN4rwHZF3cCorurWC5UlD3bET6PecIyiQKv8DCH8QABoMNjM3NDIzMTgzODA1Igw%2F8KB3FAOKKI2XicYq3APg2kep8%2FcY4I6xAfy1wGgkUVt%2FOg0NIIrZZskbZYkGGBq%2BNz3jwza%2Bj5cbKdUd0YX3T2pucRTPKnEW7PKInD%2Fb%2FZCvJDeqp%2F%2Fqw3cEZFmoCmtCknOUEAlYHlSnuCf4gv%2BfR0cU4XX1UR8wLV6OwJhfISJEH0c6UmNgu1kI0OMqgouH3Q%2FiV%2B76FYBunJWHuLJq3Uhv1xfnUHmio2dOq40If0zshxmcs2pSvlkUdZB2S1rqI8auwEYVuYTHjn2iXrCMXn1x%2BPqeLKTqnUsWzHsI5t78Ze7lWxSBLFO2WM89JcTB7w0m7Dza42tCewKnZw7YvmkQGL5ov1atIJPs9dTjT115Rr6s%2BPAjv2ti2sNVE648lwx2GeLVxJg3vCZ19J68OV1qJmNhyrAmRfUwJXEFkK0JtyuwV%2Fc70JlW7LCmCCbtaQhVEVZ8oqMJdjrvG2mOm1OsaBnVPRg8zoxQDlQWoFcgumtrtVLtWSJP4RYcfGv8J%2Bo0Ce6jfz6QLfbcXcDcVIxFpEE51oaDKsLyg5FYqz29fJJTaskI4Bo6LyOOPZo%2FMDivmwRsQ39brb%2Fpkybu4u5U%2FuBIQbcnA0lyJVUik%2BPKTxALDzobJi0YKAlJmuHy%2Ft0aPlguTWk3FjDcrr3OBjqkAf9uk75Kbb9lkfsV1D5eZQenFrIjxJ5TW3nFfLRt6d%2FNSpeqyez7ug3d8Mn2MttBchznoH7pjBqsuOrdlqGRAFdpBIKx11jgE4mpXejUNOaI50lgLzDxuYXR4KXcvnx8hjDzZNU5cv8jlRnwN0xV2mVaVum7Z5Ij0ZMkNXev8mUs9vvmU1jYoFw6%2FUEuOFd8T%2Bnqwbtiy37qQWHRztp3ZHQbuYnl&X-Amz-Signature=c479566ecd21d3034ebf0ae6a08d0f75c21b5e23968ebd19589c877677d49988&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



