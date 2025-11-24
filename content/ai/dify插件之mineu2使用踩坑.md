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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCQVZDVV%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsV6D8uCo7fuVlIns9HML1X2u0rhvqFfuoOjxNWwzrWAiEA4ESoh3WT8JybeuHkuW1iQtIn6ikAImAgVHd3VwvdWcwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPs%2FJjNP8umdNmj4FCrcA%2FH%2FhD%2BuhAOCpvnin%2BJrj5IrqM1CgdigmJeacaBgC5332tRzJvwHs1KP37ESQeC63i48WHVNzXibkuHcc6%2BUZpUvWPGrwknAOp1EnKocFlzTeam0ZWKihbt3%2Fam3ZMEhTuTIyJ1eY%2F8yYhlzZ1NBgUSIy1UgU1thIYvQRM%2B7FHpKU7zX9IQH4wZOUJDUafX9BL7UqKqW64F%2F2Mk5pdPrk9Xrq4oXtsvt5AJ7sL7GE7LlwruMkRegoxR5XVb5aZ%2Ff%2B6l4VfvJwwzVGddtwuxj58v3rWo5LjS%2Fst78df1zsNp8%2BP4%2B7uP7hAqgq7KDcFaJsgV6ttslIwAMWNsptq2VyPlfoT%2BpKrsFSnYdDUha0ylKZ7r2gkEx5A%2FnGkbmnRC06joKL75XEiUKB2%2FTS4dyfZ3WOtfR9mWQIhe2uc12NZVJzPedlv5Mv9zmLsuBzdFkMZOnR7Lf%2F7T%2B8RwTnF9CHl%2BSMyz2V7EDrMgcFG%2BVYEXma9CfiEBvSWpkySMsUUwhejhUnCon%2BHVINqaZv4sklTVTRf8n%2BoWt%2BgdbatwRFxq67JUzxpgH1ebDxZAH5gHFxM14%2FEaiNe7zh3arzFERX0rohbUWCS1jpQx8Vuj01yA%2BRm49Wir3EEGgxyToMMPcjskGOqUBfiqJ4NvUbHr9iT392Ffa1maKbVI0uAkn84HcFPFTjHyhGm6eMVZQ1KzAlLFFnpB0vmoHvaZUJkMVIolJ0XULH4r%2FkD8PP2CxkrqfuC9IVThmgQNSAKi16Sgm32drNc0g258jgco%2B9xb0SkxmGOkQa7TZknUMSMItn0CyCec1NHC96f%2Fvfqk1MSH3MI6ho8MPpqvyRdzjt9Uy%2FtCkJR0sEw3%2Fv6AF&X-Amz-Signature=70ef20d388e8315817806cb912c3b343750f8ee0278e2f04aae99d2caaac6123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCQVZDVV%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsV6D8uCo7fuVlIns9HML1X2u0rhvqFfuoOjxNWwzrWAiEA4ESoh3WT8JybeuHkuW1iQtIn6ikAImAgVHd3VwvdWcwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPs%2FJjNP8umdNmj4FCrcA%2FH%2FhD%2BuhAOCpvnin%2BJrj5IrqM1CgdigmJeacaBgC5332tRzJvwHs1KP37ESQeC63i48WHVNzXibkuHcc6%2BUZpUvWPGrwknAOp1EnKocFlzTeam0ZWKihbt3%2Fam3ZMEhTuTIyJ1eY%2F8yYhlzZ1NBgUSIy1UgU1thIYvQRM%2B7FHpKU7zX9IQH4wZOUJDUafX9BL7UqKqW64F%2F2Mk5pdPrk9Xrq4oXtsvt5AJ7sL7GE7LlwruMkRegoxR5XVb5aZ%2Ff%2B6l4VfvJwwzVGddtwuxj58v3rWo5LjS%2Fst78df1zsNp8%2BP4%2B7uP7hAqgq7KDcFaJsgV6ttslIwAMWNsptq2VyPlfoT%2BpKrsFSnYdDUha0ylKZ7r2gkEx5A%2FnGkbmnRC06joKL75XEiUKB2%2FTS4dyfZ3WOtfR9mWQIhe2uc12NZVJzPedlv5Mv9zmLsuBzdFkMZOnR7Lf%2F7T%2B8RwTnF9CHl%2BSMyz2V7EDrMgcFG%2BVYEXma9CfiEBvSWpkySMsUUwhejhUnCon%2BHVINqaZv4sklTVTRf8n%2BoWt%2BgdbatwRFxq67JUzxpgH1ebDxZAH5gHFxM14%2FEaiNe7zh3arzFERX0rohbUWCS1jpQx8Vuj01yA%2BRm49Wir3EEGgxyToMMPcjskGOqUBfiqJ4NvUbHr9iT392Ffa1maKbVI0uAkn84HcFPFTjHyhGm6eMVZQ1KzAlLFFnpB0vmoHvaZUJkMVIolJ0XULH4r%2FkD8PP2CxkrqfuC9IVThmgQNSAKi16Sgm32drNc0g258jgco%2B9xb0SkxmGOkQa7TZknUMSMItn0CyCec1NHC96f%2Fvfqk1MSH3MI6ho8MPpqvyRdzjt9Uy%2FtCkJR0sEw3%2Fv6AF&X-Amz-Signature=bd2353a0282722b1743410a06f31a2e085dd76e6646a24131a0ce633c9ee65f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



