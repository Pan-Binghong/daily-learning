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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4EZF43M%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICf9JyfyVB5srp1b1%2BuZOmt384E0TfWUh27o3mbDabnjAiEAgCd6caucBKAVbswQIRFY4TZ1gT69VPzdbieB5FyM%2FlEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDFACXAT4PfS0k4Bf%2BSrcA7vDxeyGuGfqNn3xOJRZ4WD%2FMC6qFrpH2wK6MF1%2FLRdSYkc%2B17B0ZR6aFgjgpX4zbp97cMjtuO9Cv2P0aaa5VIiYhw5PkdOBfD3SIYuA1h%2F6EVOoOCIR%2Fk5JWXHO4pZ1QOqNWSWauw%2Bp2xxhjsP8fprVYhmOxcWZ%2BpyYwjjc544jatMFRwUeKxYvUqnxGprRsL2jijwdraB7MFCyRr2BrXzeq2NoCuKqVdVx8NNqu6w8oVKiOUBc1hcpsmcwM5lzgEtWag1yfNc%2B4eKVSPiy6djhDMZflI5grTJcpNkedaMwGiflaxgh9RDw%2FTPTXRFpXk1ZSOvAmxixctMzr5jBOL8bdwDdFiiAmdOqwwaeto%2By%2Fxcx5qqWRrsLz6H8n46PKaY7VsgGy2IuvPJTmzn7355WrviRBvVi%2BMyprCcY%2F2ErQvuc8oOY%2FJ96%2FkfkSCjLXYx93OZoOnAIemQC%2FIYk5nHKHILktN9HcvY%2FrCAgZSCXTZIkCl1dE748kyyLqgBXmtdQQvzTrUjAIiDct%2Bnk712j2yyPCfPa2%2BnDSSSfmOpdAwixcfOW%2BmgcifB4Clyjb7OZ5OsFt7f2ehRyi3CLg1jfZHPqjMQDS8Ls%2B6tmNg6jwAwz3zb8%2B%2F394YBuMKzp5s4GOqUB9EG5g%2FRxVNCCNLffIeD7Y18yHmatNPQDneMwMQqY3hXiuDLPUTB7uvT2LVnfn5h9vxnCIhV7R70OgAJUu40BugiZC4BTap%2F83a0yAPm6SpIH9DKVhKS8KxcQG0QAnv5F1C2HcL3tGk26fWgBlb4I5%2BMXm1wyMQQ4p%2Fcmo3m1GCtyZl3i%2BwPy50NxPRkoX2rlyyWqofr8ELRWG4XsA7IsVrzVzTDB&X-Amz-Signature=0003e85521b4e423d98e738e93c5ca8c6998809b8ea473d61914a59274747769&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4EZF43M%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICf9JyfyVB5srp1b1%2BuZOmt384E0TfWUh27o3mbDabnjAiEAgCd6caucBKAVbswQIRFY4TZ1gT69VPzdbieB5FyM%2FlEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDFACXAT4PfS0k4Bf%2BSrcA7vDxeyGuGfqNn3xOJRZ4WD%2FMC6qFrpH2wK6MF1%2FLRdSYkc%2B17B0ZR6aFgjgpX4zbp97cMjtuO9Cv2P0aaa5VIiYhw5PkdOBfD3SIYuA1h%2F6EVOoOCIR%2Fk5JWXHO4pZ1QOqNWSWauw%2Bp2xxhjsP8fprVYhmOxcWZ%2BpyYwjjc544jatMFRwUeKxYvUqnxGprRsL2jijwdraB7MFCyRr2BrXzeq2NoCuKqVdVx8NNqu6w8oVKiOUBc1hcpsmcwM5lzgEtWag1yfNc%2B4eKVSPiy6djhDMZflI5grTJcpNkedaMwGiflaxgh9RDw%2FTPTXRFpXk1ZSOvAmxixctMzr5jBOL8bdwDdFiiAmdOqwwaeto%2By%2Fxcx5qqWRrsLz6H8n46PKaY7VsgGy2IuvPJTmzn7355WrviRBvVi%2BMyprCcY%2F2ErQvuc8oOY%2FJ96%2FkfkSCjLXYx93OZoOnAIemQC%2FIYk5nHKHILktN9HcvY%2FrCAgZSCXTZIkCl1dE748kyyLqgBXmtdQQvzTrUjAIiDct%2Bnk712j2yyPCfPa2%2BnDSSSfmOpdAwixcfOW%2BmgcifB4Clyjb7OZ5OsFt7f2ehRyi3CLg1jfZHPqjMQDS8Ls%2B6tmNg6jwAwz3zb8%2B%2F394YBuMKzp5s4GOqUB9EG5g%2FRxVNCCNLffIeD7Y18yHmatNPQDneMwMQqY3hXiuDLPUTB7uvT2LVnfn5h9vxnCIhV7R70OgAJUu40BugiZC4BTap%2F83a0yAPm6SpIH9DKVhKS8KxcQG0QAnv5F1C2HcL3tGk26fWgBlb4I5%2BMXm1wyMQQ4p%2Fcmo3m1GCtyZl3i%2BwPy50NxPRkoX2rlyyWqofr8ELRWG4XsA7IsVrzVzTDB&X-Amz-Signature=80b390520ec2dab7bb09f3eb919dcaf181c66d8cd83eae398499341e23fea9c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4EZF43M%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICf9JyfyVB5srp1b1%2BuZOmt384E0TfWUh27o3mbDabnjAiEAgCd6caucBKAVbswQIRFY4TZ1gT69VPzdbieB5FyM%2FlEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDFACXAT4PfS0k4Bf%2BSrcA7vDxeyGuGfqNn3xOJRZ4WD%2FMC6qFrpH2wK6MF1%2FLRdSYkc%2B17B0ZR6aFgjgpX4zbp97cMjtuO9Cv2P0aaa5VIiYhw5PkdOBfD3SIYuA1h%2F6EVOoOCIR%2Fk5JWXHO4pZ1QOqNWSWauw%2Bp2xxhjsP8fprVYhmOxcWZ%2BpyYwjjc544jatMFRwUeKxYvUqnxGprRsL2jijwdraB7MFCyRr2BrXzeq2NoCuKqVdVx8NNqu6w8oVKiOUBc1hcpsmcwM5lzgEtWag1yfNc%2B4eKVSPiy6djhDMZflI5grTJcpNkedaMwGiflaxgh9RDw%2FTPTXRFpXk1ZSOvAmxixctMzr5jBOL8bdwDdFiiAmdOqwwaeto%2By%2Fxcx5qqWRrsLz6H8n46PKaY7VsgGy2IuvPJTmzn7355WrviRBvVi%2BMyprCcY%2F2ErQvuc8oOY%2FJ96%2FkfkSCjLXYx93OZoOnAIemQC%2FIYk5nHKHILktN9HcvY%2FrCAgZSCXTZIkCl1dE748kyyLqgBXmtdQQvzTrUjAIiDct%2Bnk712j2yyPCfPa2%2BnDSSSfmOpdAwixcfOW%2BmgcifB4Clyjb7OZ5OsFt7f2ehRyi3CLg1jfZHPqjMQDS8Ls%2B6tmNg6jwAwz3zb8%2B%2F394YBuMKzp5s4GOqUB9EG5g%2FRxVNCCNLffIeD7Y18yHmatNPQDneMwMQqY3hXiuDLPUTB7uvT2LVnfn5h9vxnCIhV7R70OgAJUu40BugiZC4BTap%2F83a0yAPm6SpIH9DKVhKS8KxcQG0QAnv5F1C2HcL3tGk26fWgBlb4I5%2BMXm1wyMQQ4p%2Fcmo3m1GCtyZl3i%2BwPy50NxPRkoX2rlyyWqofr8ELRWG4XsA7IsVrzVzTDB&X-Amz-Signature=b20bea4dba751a79b29a8c2f62ec35f7e856ec78953734fb5d9a481b94d2aa71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

