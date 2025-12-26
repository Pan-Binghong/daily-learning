---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP5WE354%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy82qMkcnKF1T5CYlPhQIU%2BKMm%2FxSEsRcqpEGUu6khUAIhAPUHaP9V4eLb772I0sQm5Z6lnJz7S1MTDHEPhpGBrF2FKv8DCEsQABoMNjM3NDIzMTgzODA1IgzD33D27fLjJ563fn8q3ANU0bKIbeqhzkHjxY2rz1qAC276MhabHTSzl%2BqHDUuBwt02ZzwsMuKs7dUBsexAF9aKdD15C22sdjFvwDad%2B3IB1RDj9DkEfP7ngTIMzX0GYdvMlTCZ804tBL1z%2BbX0RV0z1g0Do%2FrDJpgp3Oq3DckT%2FVOWsEiAffJ29MYEhFYehZ64ktaWyy2L7RYwyuKyyO4PPSVsUp7cgWSzauVkG%2FVvRFyv02mB677JUN34Sj0WEnl8%2FrZPrYjcanfvlcVvOCEZct6yjV%2FywJCgChb459XSLto68CibEWGe03wMvgcr5kHfjN7kiA3e8a06y4p7GbiWQU5fvm%2FxOHJp3r%2FqkRwzRgaPKzlr0zRGBddTqxZkyvXAf2UKzyJPpM%2BM0nROoDaAMtxvQeuN%2FF4SG4Fmr5dOvYASFnkKx6781GIW8xRHMstPa6drLst9uFRVMlS%2BxmwPVjOpdAG0dto0Se%2BN10qc8k19hHcxUEPb0VEeuDC774qAChhrvc8xxLTTBdJ%2BSW9t1%2F7aFd%2FGmKa%2FRZoE%2F2XUWhncVAPn%2B9ZWYKiDvTN%2BCl%2FUILVyffsTJFh9gXY%2BUE4lZp9jp0VJR1Vo6ml4LrL8Xg0GWfyzQCJQiSvObTZJTnkhNXT%2BUUNxh6%2FlKjCNz7fKBjqkAZZsmbXPj0Vnc8qNq0%2F7dvsoLF7ZKVaQhfM%2FnQeVMQtQMszzgSmh6TMjs%2Fehc2wjrKH66Q7Vn9VGqTAPcwqhVV99q0qekONMk2KVVexGbuQ%2Bk%2BmhuWm53VDftmMvfbIDtT0j71f5Px6%2Bh5CygJ0FbYOM7vxr1uagrf%2BuD0W%2BZo4nQqZ2ZYu53mcdeGxsePZH%2FOIVxN899EMELufZm1icT8n0Wtny&X-Amz-Signature=1e8f45d63f5f489311ce23232d8eeb3d9a2e11a43af2d8562beecdae0f5039f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP5WE354%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy82qMkcnKF1T5CYlPhQIU%2BKMm%2FxSEsRcqpEGUu6khUAIhAPUHaP9V4eLb772I0sQm5Z6lnJz7S1MTDHEPhpGBrF2FKv8DCEsQABoMNjM3NDIzMTgzODA1IgzD33D27fLjJ563fn8q3ANU0bKIbeqhzkHjxY2rz1qAC276MhabHTSzl%2BqHDUuBwt02ZzwsMuKs7dUBsexAF9aKdD15C22sdjFvwDad%2B3IB1RDj9DkEfP7ngTIMzX0GYdvMlTCZ804tBL1z%2BbX0RV0z1g0Do%2FrDJpgp3Oq3DckT%2FVOWsEiAffJ29MYEhFYehZ64ktaWyy2L7RYwyuKyyO4PPSVsUp7cgWSzauVkG%2FVvRFyv02mB677JUN34Sj0WEnl8%2FrZPrYjcanfvlcVvOCEZct6yjV%2FywJCgChb459XSLto68CibEWGe03wMvgcr5kHfjN7kiA3e8a06y4p7GbiWQU5fvm%2FxOHJp3r%2FqkRwzRgaPKzlr0zRGBddTqxZkyvXAf2UKzyJPpM%2BM0nROoDaAMtxvQeuN%2FF4SG4Fmr5dOvYASFnkKx6781GIW8xRHMstPa6drLst9uFRVMlS%2BxmwPVjOpdAG0dto0Se%2BN10qc8k19hHcxUEPb0VEeuDC774qAChhrvc8xxLTTBdJ%2BSW9t1%2F7aFd%2FGmKa%2FRZoE%2F2XUWhncVAPn%2B9ZWYKiDvTN%2BCl%2FUILVyffsTJFh9gXY%2BUE4lZp9jp0VJR1Vo6ml4LrL8Xg0GWfyzQCJQiSvObTZJTnkhNXT%2BUUNxh6%2FlKjCNz7fKBjqkAZZsmbXPj0Vnc8qNq0%2F7dvsoLF7ZKVaQhfM%2FnQeVMQtQMszzgSmh6TMjs%2Fehc2wjrKH66Q7Vn9VGqTAPcwqhVV99q0qekONMk2KVVexGbuQ%2Bk%2BmhuWm53VDftmMvfbIDtT0j71f5Px6%2Bh5CygJ0FbYOM7vxr1uagrf%2BuD0W%2BZo4nQqZ2ZYu53mcdeGxsePZH%2FOIVxN899EMELufZm1icT8n0Wtny&X-Amz-Signature=78edc9f28f6e2a49d5c51fcd72e47d1b374fc810830e1359c49c2b92d3d07792&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP5WE354%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy82qMkcnKF1T5CYlPhQIU%2BKMm%2FxSEsRcqpEGUu6khUAIhAPUHaP9V4eLb772I0sQm5Z6lnJz7S1MTDHEPhpGBrF2FKv8DCEsQABoMNjM3NDIzMTgzODA1IgzD33D27fLjJ563fn8q3ANU0bKIbeqhzkHjxY2rz1qAC276MhabHTSzl%2BqHDUuBwt02ZzwsMuKs7dUBsexAF9aKdD15C22sdjFvwDad%2B3IB1RDj9DkEfP7ngTIMzX0GYdvMlTCZ804tBL1z%2BbX0RV0z1g0Do%2FrDJpgp3Oq3DckT%2FVOWsEiAffJ29MYEhFYehZ64ktaWyy2L7RYwyuKyyO4PPSVsUp7cgWSzauVkG%2FVvRFyv02mB677JUN34Sj0WEnl8%2FrZPrYjcanfvlcVvOCEZct6yjV%2FywJCgChb459XSLto68CibEWGe03wMvgcr5kHfjN7kiA3e8a06y4p7GbiWQU5fvm%2FxOHJp3r%2FqkRwzRgaPKzlr0zRGBddTqxZkyvXAf2UKzyJPpM%2BM0nROoDaAMtxvQeuN%2FF4SG4Fmr5dOvYASFnkKx6781GIW8xRHMstPa6drLst9uFRVMlS%2BxmwPVjOpdAG0dto0Se%2BN10qc8k19hHcxUEPb0VEeuDC774qAChhrvc8xxLTTBdJ%2BSW9t1%2F7aFd%2FGmKa%2FRZoE%2F2XUWhncVAPn%2B9ZWYKiDvTN%2BCl%2FUILVyffsTJFh9gXY%2BUE4lZp9jp0VJR1Vo6ml4LrL8Xg0GWfyzQCJQiSvObTZJTnkhNXT%2BUUNxh6%2FlKjCNz7fKBjqkAZZsmbXPj0Vnc8qNq0%2F7dvsoLF7ZKVaQhfM%2FnQeVMQtQMszzgSmh6TMjs%2Fehc2wjrKH66Q7Vn9VGqTAPcwqhVV99q0qekONMk2KVVexGbuQ%2Bk%2BmhuWm53VDftmMvfbIDtT0j71f5Px6%2Bh5CygJ0FbYOM7vxr1uagrf%2BuD0W%2BZo4nQqZ2ZYu53mcdeGxsePZH%2FOIVxN899EMELufZm1icT8n0Wtny&X-Amz-Signature=f6ed9b4aa374a25b1cd3163f6c5b8e42cdce6f887d9dfd93a1925a5ae90fc0f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

