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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AAOVU7A%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHrn6ek9%2Fkmd5SkXITUJ2NjzQnFvYUjpquypU3%2B4YfbAiEA7RQ%2FLOIbPz%2BS%2BzPWgACBNHqEobxeRm2fdodDC4jbsAAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMWSt38Tu6sa7Fzo%2FSrcA1lGSo4woUts8OHA%2BawEPzAnT5chjfuvXZzwMrfzUNNKvqA8b0iuNA611jyOr0ZeMIsOLL1xCL4c8NkS%2FSpLM21VnkRmI0UYpdYG3n%2B27CdpfDTIo0Xyr8xCCgLLb%2F89OyaxZrV7ImZXw6Kal4hdLOkhWgF8tEqwn8PFXYMwZY7RejM2phCvMIngzrtjsu%2BFXVadBcuDT%2BpdwkEtzho0b85UNChGHK4dn3Q0InnYXU%2BAR4K%2BSJs%2Bj%2BX7QVr2cOoi9ydwcUUhZCkQ4aNhU4ySJkL1gZB5NCJ2TxEcFpLXFA9PmPMdGumr94pDQu0RTGwPA%2FIqeiYcmGnKJipZ%2BVANEXq%2FJ0tfa4TVy4xdKfNTC5KpmVxvifyVQGW0kfmqxR37YToCkPF7gm2PqTs2o1uFZ6JNa7BJ5OGeEZpdlSvF9PRPFnwC2cS4sV%2FsK4DIPGRriK9lgpcsAJkIglSot1wwxhptpWD3lthi6rs0cJJbScDSr8ZyhSXYSJldmCv3AexbvGjHOmWACLgbOtKt1VRXUYxj%2Fw6L%2FItGcLLhOYyWblQ%2FcyBDt7VW4bomgQ4VNblhWFzTlqOa2z97fCMA%2FsyLj7jW%2FcdWWGn6uscfLjYnD%2FGw3nwqtd1rFh17ht%2BvMOjjgs4GOqUBxg2WfaGeSOMKYtIpnvOnszmu3DpP5ct%2BU2RQvW%2BT%2Boayty6i807kJofiGt%2Fdfw7Gc%2BPC1jIe3fcahRdZGEymZlyuvP4%2FtbpvegYPno5WipjuMetq1wj%2BAZF4NvDPHJxr2MyZs%2F7tfk%2BhU%2BkonnTE2J0qXfTgzLTiTAIYCiYI%2BwS1n5CkHr1niPoTk6egftydLJrjQln8DP4eLkyVSNtlbGEdbP5L&X-Amz-Signature=090ecb98d0f9ce57c7de1e2382bfefca455f394abde21d649ff86ac4cbba6567&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AAOVU7A%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHrn6ek9%2Fkmd5SkXITUJ2NjzQnFvYUjpquypU3%2B4YfbAiEA7RQ%2FLOIbPz%2BS%2BzPWgACBNHqEobxeRm2fdodDC4jbsAAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMWSt38Tu6sa7Fzo%2FSrcA1lGSo4woUts8OHA%2BawEPzAnT5chjfuvXZzwMrfzUNNKvqA8b0iuNA611jyOr0ZeMIsOLL1xCL4c8NkS%2FSpLM21VnkRmI0UYpdYG3n%2B27CdpfDTIo0Xyr8xCCgLLb%2F89OyaxZrV7ImZXw6Kal4hdLOkhWgF8tEqwn8PFXYMwZY7RejM2phCvMIngzrtjsu%2BFXVadBcuDT%2BpdwkEtzho0b85UNChGHK4dn3Q0InnYXU%2BAR4K%2BSJs%2Bj%2BX7QVr2cOoi9ydwcUUhZCkQ4aNhU4ySJkL1gZB5NCJ2TxEcFpLXFA9PmPMdGumr94pDQu0RTGwPA%2FIqeiYcmGnKJipZ%2BVANEXq%2FJ0tfa4TVy4xdKfNTC5KpmVxvifyVQGW0kfmqxR37YToCkPF7gm2PqTs2o1uFZ6JNa7BJ5OGeEZpdlSvF9PRPFnwC2cS4sV%2FsK4DIPGRriK9lgpcsAJkIglSot1wwxhptpWD3lthi6rs0cJJbScDSr8ZyhSXYSJldmCv3AexbvGjHOmWACLgbOtKt1VRXUYxj%2Fw6L%2FItGcLLhOYyWblQ%2FcyBDt7VW4bomgQ4VNblhWFzTlqOa2z97fCMA%2FsyLj7jW%2FcdWWGn6uscfLjYnD%2FGw3nwqtd1rFh17ht%2BvMOjjgs4GOqUBxg2WfaGeSOMKYtIpnvOnszmu3DpP5ct%2BU2RQvW%2BT%2Boayty6i807kJofiGt%2Fdfw7Gc%2BPC1jIe3fcahRdZGEymZlyuvP4%2FtbpvegYPno5WipjuMetq1wj%2BAZF4NvDPHJxr2MyZs%2F7tfk%2BhU%2BkonnTE2J0qXfTgzLTiTAIYCiYI%2BwS1n5CkHr1niPoTk6egftydLJrjQln8DP4eLkyVSNtlbGEdbP5L&X-Amz-Signature=136aa5bf92d67ac65e8ccffe7d48611d63cb3cb50b6a3217b05ee2a4c7165dd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AAOVU7A%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFHrn6ek9%2Fkmd5SkXITUJ2NjzQnFvYUjpquypU3%2B4YfbAiEA7RQ%2FLOIbPz%2BS%2BzPWgACBNHqEobxeRm2fdodDC4jbsAAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMWSt38Tu6sa7Fzo%2FSrcA1lGSo4woUts8OHA%2BawEPzAnT5chjfuvXZzwMrfzUNNKvqA8b0iuNA611jyOr0ZeMIsOLL1xCL4c8NkS%2FSpLM21VnkRmI0UYpdYG3n%2B27CdpfDTIo0Xyr8xCCgLLb%2F89OyaxZrV7ImZXw6Kal4hdLOkhWgF8tEqwn8PFXYMwZY7RejM2phCvMIngzrtjsu%2BFXVadBcuDT%2BpdwkEtzho0b85UNChGHK4dn3Q0InnYXU%2BAR4K%2BSJs%2Bj%2BX7QVr2cOoi9ydwcUUhZCkQ4aNhU4ySJkL1gZB5NCJ2TxEcFpLXFA9PmPMdGumr94pDQu0RTGwPA%2FIqeiYcmGnKJipZ%2BVANEXq%2FJ0tfa4TVy4xdKfNTC5KpmVxvifyVQGW0kfmqxR37YToCkPF7gm2PqTs2o1uFZ6JNa7BJ5OGeEZpdlSvF9PRPFnwC2cS4sV%2FsK4DIPGRriK9lgpcsAJkIglSot1wwxhptpWD3lthi6rs0cJJbScDSr8ZyhSXYSJldmCv3AexbvGjHOmWACLgbOtKt1VRXUYxj%2Fw6L%2FItGcLLhOYyWblQ%2FcyBDt7VW4bomgQ4VNblhWFzTlqOa2z97fCMA%2FsyLj7jW%2FcdWWGn6uscfLjYnD%2FGw3nwqtd1rFh17ht%2BvMOjjgs4GOqUBxg2WfaGeSOMKYtIpnvOnszmu3DpP5ct%2BU2RQvW%2BT%2Boayty6i807kJofiGt%2Fdfw7Gc%2BPC1jIe3fcahRdZGEymZlyuvP4%2FtbpvegYPno5WipjuMetq1wj%2BAZF4NvDPHJxr2MyZs%2F7tfk%2BhU%2BkonnTE2J0qXfTgzLTiTAIYCiYI%2BwS1n5CkHr1niPoTk6egftydLJrjQln8DP4eLkyVSNtlbGEdbP5L&X-Amz-Signature=0fe8148fd5a73c9eebed5147bd6782d2c7cee1053346371770c7648705e72153&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

