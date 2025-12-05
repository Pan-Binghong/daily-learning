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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ2BUVY%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFhh0q9%2B804Wsy%2BL%2B3beTLMWQscVX5DT3dFvZ6l7E68wIhAJpiFr%2BpIFQMraUo1xopgDgaBGOEPpgtucdYS453mICrKv8DCE8QABoMNjM3NDIzMTgzODA1IgzL0fdsMmBTE5MhI9kq3AOJYvzaxMM7M3LTpgf5qG%2BebUovGoMuiP2zMuqrvUd0NolKgUZHg0D212As%2B4TeqH8jrolGL%2FLDtDm0JGu3gxQa07uF%2FDKmGdf3j3IUGb3BF6RheEjM02HHivH1lxzyqrjhUxz4cmn%2FSsLdg4i0Em7owfPcLVnehmMG3nejS%2B9Ni71b%2FSIgq2X%2F8R6uu2g63cf5voxrVn6ANqNfR7AS1uCJg8NqHHM2SyE5GuGi%2F%2BSbnOGP13FzA4WjCnZkTrxgpMEvKphriJ9%2FuHGv1WeqKOCcCZA8gRxL2GMcWBrHFnA9YRz1SOy3LvcLLZ3IzUHK4oi6bHLrQZ%2FnDhkrAdTVGT%2Bl%2B1fnpN32sFQlgbAdyBs2qGVwOKk5hVBHb%2FW2OKzy5qNXtd9L9B28%2FJrg1nHMmgLkSFU%2FMNgo1S8OOBCPp%2BUr%2BtWwTyjkfUF7EJ3%2B0802uqv%2BE%2F%2FhoZmht0wXrdh2GMKqEtEM6iljYYVw%2FWvXfxEVFfBMlZablBIoTMw70csy8k9AD%2Fnkj9IMwSgj1IvylWP05k20JEjlDW5%2Bpffpr7XfRX5c3lLexeMDRDTbx%2FhIJP6%2Fbyn8UmGltpCfTN8bQuvRCBcjCjYiKxLDtLWkhH5tR3LFcAhlbjor5e7U2zDUjMjJBjqkAVRMU7EvyucjTF740BTRpLGcX37ZszLZoPWP4uIhq1UO2gu1WSEW6Qd9kTN8Ntkmbx54y1Ht2gMVQzTcttJ2C3qWfykYxxMgnqpjGu3fEQBXOrKbiaRkkvD%2Bc6HQxx5ZuuLmGEIzT5Pnf0ETWtalpXBXcBsujz2oDYTv6SklFjZaLf%2BSaCMFRvkScsW6uSYc8TvvPz%2B1qWc6pyJ7Ane8D8RkjM03&X-Amz-Signature=77589f77a9b1a37b13fcfdd2d15a683408eae5f42a7bb3c2f080b40146851fc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJ2BUVY%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFhh0q9%2B804Wsy%2BL%2B3beTLMWQscVX5DT3dFvZ6l7E68wIhAJpiFr%2BpIFQMraUo1xopgDgaBGOEPpgtucdYS453mICrKv8DCE8QABoMNjM3NDIzMTgzODA1IgzL0fdsMmBTE5MhI9kq3AOJYvzaxMM7M3LTpgf5qG%2BebUovGoMuiP2zMuqrvUd0NolKgUZHg0D212As%2B4TeqH8jrolGL%2FLDtDm0JGu3gxQa07uF%2FDKmGdf3j3IUGb3BF6RheEjM02HHivH1lxzyqrjhUxz4cmn%2FSsLdg4i0Em7owfPcLVnehmMG3nejS%2B9Ni71b%2FSIgq2X%2F8R6uu2g63cf5voxrVn6ANqNfR7AS1uCJg8NqHHM2SyE5GuGi%2F%2BSbnOGP13FzA4WjCnZkTrxgpMEvKphriJ9%2FuHGv1WeqKOCcCZA8gRxL2GMcWBrHFnA9YRz1SOy3LvcLLZ3IzUHK4oi6bHLrQZ%2FnDhkrAdTVGT%2Bl%2B1fnpN32sFQlgbAdyBs2qGVwOKk5hVBHb%2FW2OKzy5qNXtd9L9B28%2FJrg1nHMmgLkSFU%2FMNgo1S8OOBCPp%2BUr%2BtWwTyjkfUF7EJ3%2B0802uqv%2BE%2F%2FhoZmht0wXrdh2GMKqEtEM6iljYYVw%2FWvXfxEVFfBMlZablBIoTMw70csy8k9AD%2Fnkj9IMwSgj1IvylWP05k20JEjlDW5%2Bpffpr7XfRX5c3lLexeMDRDTbx%2FhIJP6%2Fbyn8UmGltpCfTN8bQuvRCBcjCjYiKxLDtLWkhH5tR3LFcAhlbjor5e7U2zDUjMjJBjqkAVRMU7EvyucjTF740BTRpLGcX37ZszLZoPWP4uIhq1UO2gu1WSEW6Qd9kTN8Ntkmbx54y1Ht2gMVQzTcttJ2C3qWfykYxxMgnqpjGu3fEQBXOrKbiaRkkvD%2Bc6HQxx5ZuuLmGEIzT5Pnf0ETWtalpXBXcBsujz2oDYTv6SklFjZaLf%2BSaCMFRvkScsW6uSYc8TvvPz%2B1qWc6pyJ7Ane8D8RkjM03&X-Amz-Signature=2905b883e1fb5e4cb60754f983bfeaefebe93b5fff72b8e2bf86b881531ef112&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



