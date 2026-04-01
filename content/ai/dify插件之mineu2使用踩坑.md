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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU2HOTN2%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAFO8YpxbZg8MF5kwarzjAj7d9L7D1L4mQMjOhm0VKxBAiATv88cRQnhRpXkuhZTb2fJeyUqvXQ85xuYSveDrDW%2BqCr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMx3W%2B1ihUpfj1GRiwKtwDHQjF%2BcdMFIZJ25gXhT%2FdcHe4zB%2B%2FwAGE2cF%2Bdzn6J1X0LoM35ThnLDJT7m82LPf%2BEPPhF7PFL1EdK81vVJd1t%2FxhDLQGaz3alE6eP0IUvGh%2BMo85%2FxXqszoKXgJpXS1oE%2F3GLbZSsn3QXy1AxXptMgDTbad0nQIIPihyQbZDhMJhrfi9z7LsrnXlP%2BVf8xFtf%2Fr6jow3VbikhnWd5FAQR44DQwvyuQpep6iapgyGkdrhevSlNClXj5TeLnveL%2BFm2OQycVZ8C86i3muB%2B3BNfLbLKnrYgjMVKRWJ3V3SBkbaaJIqauCzXNHLlB%2F91G04sm7iR0ETskMOSeZrF3N1Xqg6Y%2Ffg019pM6kcNgxm%2FfFH%2FFpKQ%2BkrWvqGdTtRs1tu5VpFLxnxXpR3Kezu7kBDjoQg40Q1FzpNAACWo4GVJwbnxqKPyhBo2bWr4hfvtPXrRj0vCK%2F4Fu1Rsrv1ucnKiPGzQO%2F7ja86ktjHrEhkKuCOXyZizMJ1wH3RyRMCdFA%2BTmRPXnE7jYe%2BxnEydPgnEEZvIe%2BQWlw6wgef4GVR7aKjSpbAso0ioLHjdD7ldhA50c%2Bvnor0HDT9%2F4w254cZx2JrT40LfyBPnud0l%2FTu5SH53M92wbRt%2FyLPCrAwyKKyzgY6pgGvyIihYy6N7n5T7968r%2BB0Uy7SBt7UTxqea7nVQFPhS%2BVqRrZyTjI83MsB5PoyGca16dfw3CMv8uGHoiCNl5uHiwUlCM8IsLbtO2NoDM6mY1xdsohdGkT0drnZf7sx%2BMZcK3vFfFp46A%2BhSqiro34%2BZss%2FxeUO%2Bb%2F9%2BkmjBThy9UeztY0rEWBRVgRMhTMM3OPteJ5fBzbzdtHXthWHObRnmaGWNUQS&X-Amz-Signature=e19d2a4e2222dbfb1a2e67d37f694000f92212ddbbce760559ae7c3d4b2ccb8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU2HOTN2%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAFO8YpxbZg8MF5kwarzjAj7d9L7D1L4mQMjOhm0VKxBAiATv88cRQnhRpXkuhZTb2fJeyUqvXQ85xuYSveDrDW%2BqCr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMx3W%2B1ihUpfj1GRiwKtwDHQjF%2BcdMFIZJ25gXhT%2FdcHe4zB%2B%2FwAGE2cF%2Bdzn6J1X0LoM35ThnLDJT7m82LPf%2BEPPhF7PFL1EdK81vVJd1t%2FxhDLQGaz3alE6eP0IUvGh%2BMo85%2FxXqszoKXgJpXS1oE%2F3GLbZSsn3QXy1AxXptMgDTbad0nQIIPihyQbZDhMJhrfi9z7LsrnXlP%2BVf8xFtf%2Fr6jow3VbikhnWd5FAQR44DQwvyuQpep6iapgyGkdrhevSlNClXj5TeLnveL%2BFm2OQycVZ8C86i3muB%2B3BNfLbLKnrYgjMVKRWJ3V3SBkbaaJIqauCzXNHLlB%2F91G04sm7iR0ETskMOSeZrF3N1Xqg6Y%2Ffg019pM6kcNgxm%2FfFH%2FFpKQ%2BkrWvqGdTtRs1tu5VpFLxnxXpR3Kezu7kBDjoQg40Q1FzpNAACWo4GVJwbnxqKPyhBo2bWr4hfvtPXrRj0vCK%2F4Fu1Rsrv1ucnKiPGzQO%2F7ja86ktjHrEhkKuCOXyZizMJ1wH3RyRMCdFA%2BTmRPXnE7jYe%2BxnEydPgnEEZvIe%2BQWlw6wgef4GVR7aKjSpbAso0ioLHjdD7ldhA50c%2Bvnor0HDT9%2F4w254cZx2JrT40LfyBPnud0l%2FTu5SH53M92wbRt%2FyLPCrAwyKKyzgY6pgGvyIihYy6N7n5T7968r%2BB0Uy7SBt7UTxqea7nVQFPhS%2BVqRrZyTjI83MsB5PoyGca16dfw3CMv8uGHoiCNl5uHiwUlCM8IsLbtO2NoDM6mY1xdsohdGkT0drnZf7sx%2BMZcK3vFfFp46A%2BhSqiro34%2BZss%2FxeUO%2Bb%2F9%2BkmjBThy9UeztY0rEWBRVgRMhTMM3OPteJ5fBzbzdtHXthWHObRnmaGWNUQS&X-Amz-Signature=d044ea64c41ca2e8fa86546a56e835bf121bb34a5450c0b4e00f7d614658f0d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



