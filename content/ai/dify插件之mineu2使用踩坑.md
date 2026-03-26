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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GBU2SWZ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4hHZHbfLFF83QnslgamNjpQ5X15vFyqe5Jlh6e62%2F3wIhAP3SBPCwh10P1wyMddIWBtF%2FBwPyXrVHcBStdVuvC%2BQZKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3hTq6O0siOjuI18kq3AMmjtgOrXcmAJ%2BW9YAiLoR2tIOII1e5xqxN%2BKJPn9XELq7SD0U%2FyIBzw0xq2bXiru3HzvyYsOYu1h5feD4g%2BQeWju%2Bmdw6nUEObwNuu%2FyRgyo1gzbFn0w7ftUAUW9kxkgqMcO9fKYNl5bpzmT7O8RS52jY%2BDiRHr%2FzufoWVJR%2FfafNCqMT%2BSXkvOW8JbduIIofqohT5GHx7QP23ypTxZ3s%2F1ssx0%2Bg0eyzqZoOMA9gie%2FX1Vaj7B5B7hy0MQg0p66HXB8zchZ4g%2BhUnb%2FYaW5fSsFFUhNfY1Is5sAWfWT4Ia4peE1mPDpSaU1cozJjCnm4VlT%2FmYOWV0UDKnOcOwSxpDg%2Fue%2FpkWWDuHPPqF%2FB1mXs7x7S6RB0PauDcGTcDh6bHydgstrQRbSIKUjJmG8IJjKn8cSE1Q5cKnfRui4shBvFPGi7txIlYv60wna3su2OBiirZEZz16E1mr2cArxLKrMe1B1pV5NR0tTSUuSDK2EATbQQzC5D3Uh2T6X29pX33%2Fkom3jC5ziTMC7CROVMljuFyR4OYbJyUXJr5CmcS55Pb%2FerGawLA2LmpIihNEVXwrjxbZd9qniIz09Hlk2x3L7rDKmVHMk9suGaLn1FkQhKDdQE9YEvbVr4b0jCeyZLOBjqkAQMeiDqGh9iZsmOq9y23pnZgzo%2F1OgHKG33kSOuPm5W6TeOZLstOv6G9Fmf%2FMCGxXWDWxef0ddra9tCwLlJiNyFE43xAG%2BjXJc2d1uOQd2QLe5PpWnhSU3sRdh8NyOkmGt%2Bvxy%2BaRkrgFBT8%2FVJBC3R1kRdIJhjfTYwYgGfBZz98MquN%2F7sX0ANVxwfibiU9BfRk2agCaT7%2BlptCNzahBxszfxR1&X-Amz-Signature=22510fe22d9a9bb16c914014e71106708fcdb2851a9700da9b219ad139384f6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GBU2SWZ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4hHZHbfLFF83QnslgamNjpQ5X15vFyqe5Jlh6e62%2F3wIhAP3SBPCwh10P1wyMddIWBtF%2FBwPyXrVHcBStdVuvC%2BQZKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3hTq6O0siOjuI18kq3AMmjtgOrXcmAJ%2BW9YAiLoR2tIOII1e5xqxN%2BKJPn9XELq7SD0U%2FyIBzw0xq2bXiru3HzvyYsOYu1h5feD4g%2BQeWju%2Bmdw6nUEObwNuu%2FyRgyo1gzbFn0w7ftUAUW9kxkgqMcO9fKYNl5bpzmT7O8RS52jY%2BDiRHr%2FzufoWVJR%2FfafNCqMT%2BSXkvOW8JbduIIofqohT5GHx7QP23ypTxZ3s%2F1ssx0%2Bg0eyzqZoOMA9gie%2FX1Vaj7B5B7hy0MQg0p66HXB8zchZ4g%2BhUnb%2FYaW5fSsFFUhNfY1Is5sAWfWT4Ia4peE1mPDpSaU1cozJjCnm4VlT%2FmYOWV0UDKnOcOwSxpDg%2Fue%2FpkWWDuHPPqF%2FB1mXs7x7S6RB0PauDcGTcDh6bHydgstrQRbSIKUjJmG8IJjKn8cSE1Q5cKnfRui4shBvFPGi7txIlYv60wna3su2OBiirZEZz16E1mr2cArxLKrMe1B1pV5NR0tTSUuSDK2EATbQQzC5D3Uh2T6X29pX33%2Fkom3jC5ziTMC7CROVMljuFyR4OYbJyUXJr5CmcS55Pb%2FerGawLA2LmpIihNEVXwrjxbZd9qniIz09Hlk2x3L7rDKmVHMk9suGaLn1FkQhKDdQE9YEvbVr4b0jCeyZLOBjqkAQMeiDqGh9iZsmOq9y23pnZgzo%2F1OgHKG33kSOuPm5W6TeOZLstOv6G9Fmf%2FMCGxXWDWxef0ddra9tCwLlJiNyFE43xAG%2BjXJc2d1uOQd2QLe5PpWnhSU3sRdh8NyOkmGt%2Bvxy%2BaRkrgFBT8%2FVJBC3R1kRdIJhjfTYwYgGfBZz98MquN%2F7sX0ANVxwfibiU9BfRk2agCaT7%2BlptCNzahBxszfxR1&X-Amz-Signature=29dd3d0a00c086b1de32cb1ebe4c8f3f7112c0bc6b9e5c50fe99b043fd41e86e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



