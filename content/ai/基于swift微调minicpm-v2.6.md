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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZPSZTWT%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb2pvru%2FsnWuKOeBsLy760%2FRBplUx0F9FGUpwEyCGcwIgIXkrNirasRG3XiOqb0F5XCdmwCOd%2Fk9bJCUJm3PgWo0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBIXVKRmSHSWImHaASrcA0%2FrjgIDafRJT82W8IxxD4N4X7ZEDTK1cZqnozzfsJgxRPRkdmknuxb4Rqy%2BvSgWoyaPRuO9YB%2F3C9WGPZT7%2BYDRNyNOf4VB45mzxrcctd8PhF3J2GkDFH5pGdlVZvh9%2FCLezOD8Iry0gPjOyoXkXYEt9LZRPSk0R8N%2B3Np5Lxw%2BNvpD4rhOV8cG9XKF7GTgNMG8ZJHLSU1Als3fD6TNwjzOv08lx1bLe7Y0DJcCUKJW9kTknGP7j1CK%2FsFDyqYG6b6Vx7T1muXB%2FuB68zcYNry6aZoL9v7%2BDxGJLp%2BLon0W28q3l7TgvHBMOMYe8Tq2pRobW9Csjq7qYR9ONCPpKT1KfipjhvOkpHVMOQcoZf91txkbiJcO2v4RdAwQV3xhA3INMTsKpw%2Br8PhKp828Abs1u8W34p8gT46CSCfkjNHa8x%2Fjl1gGNcCsrQcJmRa27p%2B2LiB3j1FwZ%2BYxuKXz%2BHrZH%2FilD2RrvCl1CXkQTMDpzIVS5tEys9N44UUYhjZ5jFXdX%2BcnctpPKFYQCU3dtMSDnvIZzL1LIEHDSBUKMrjG3JpxHU0AIp5tKpI1WSTzFqjBokQYLfTD3uMcGkMJ8bjZS532f5xzy%2FJfmThO3IRiclICfeq08OJOmXSTMKai68sGOqUBHaYbVxAaruBUseKLluy%2FbPSIY2nQcGGx5DHCHfZOTdS2uwd2KmDWQLQzLriTCjc8qDZ9xFUtNbEL67CQUluto5ARLW7MTsDylLZzpmnPTpGJuY%2Bu%2BpsNcpzV16sHnZhEPXD%2Ba9hmIe71j9%2BhgStRVtR1l1a1fmSpf2oeRPQ7m2yigxbeTTO3OXJQamiMOBRDGKXzQlE36k6MyHcx%2BJS3ySNPI49B&X-Amz-Signature=5cd755e5af35165aba9eff57c7e53fd6ab5c0b8c889f62c0fa0a5570bf411123&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZPSZTWT%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb2pvru%2FsnWuKOeBsLy760%2FRBplUx0F9FGUpwEyCGcwIgIXkrNirasRG3XiOqb0F5XCdmwCOd%2Fk9bJCUJm3PgWo0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBIXVKRmSHSWImHaASrcA0%2FrjgIDafRJT82W8IxxD4N4X7ZEDTK1cZqnozzfsJgxRPRkdmknuxb4Rqy%2BvSgWoyaPRuO9YB%2F3C9WGPZT7%2BYDRNyNOf4VB45mzxrcctd8PhF3J2GkDFH5pGdlVZvh9%2FCLezOD8Iry0gPjOyoXkXYEt9LZRPSk0R8N%2B3Np5Lxw%2BNvpD4rhOV8cG9XKF7GTgNMG8ZJHLSU1Als3fD6TNwjzOv08lx1bLe7Y0DJcCUKJW9kTknGP7j1CK%2FsFDyqYG6b6Vx7T1muXB%2FuB68zcYNry6aZoL9v7%2BDxGJLp%2BLon0W28q3l7TgvHBMOMYe8Tq2pRobW9Csjq7qYR9ONCPpKT1KfipjhvOkpHVMOQcoZf91txkbiJcO2v4RdAwQV3xhA3INMTsKpw%2Br8PhKp828Abs1u8W34p8gT46CSCfkjNHa8x%2Fjl1gGNcCsrQcJmRa27p%2B2LiB3j1FwZ%2BYxuKXz%2BHrZH%2FilD2RrvCl1CXkQTMDpzIVS5tEys9N44UUYhjZ5jFXdX%2BcnctpPKFYQCU3dtMSDnvIZzL1LIEHDSBUKMrjG3JpxHU0AIp5tKpI1WSTzFqjBokQYLfTD3uMcGkMJ8bjZS532f5xzy%2FJfmThO3IRiclICfeq08OJOmXSTMKai68sGOqUBHaYbVxAaruBUseKLluy%2FbPSIY2nQcGGx5DHCHfZOTdS2uwd2KmDWQLQzLriTCjc8qDZ9xFUtNbEL67CQUluto5ARLW7MTsDylLZzpmnPTpGJuY%2Bu%2BpsNcpzV16sHnZhEPXD%2Ba9hmIe71j9%2BhgStRVtR1l1a1fmSpf2oeRPQ7m2yigxbeTTO3OXJQamiMOBRDGKXzQlE36k6MyHcx%2BJS3ySNPI49B&X-Amz-Signature=fb606561b67a0b035269d4f9fdbd6b5bbc2149b874b268ae4e719b5d54099ffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZPSZTWT%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyb2pvru%2FsnWuKOeBsLy760%2FRBplUx0F9FGUpwEyCGcwIgIXkrNirasRG3XiOqb0F5XCdmwCOd%2Fk9bJCUJm3PgWo0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDBIXVKRmSHSWImHaASrcA0%2FrjgIDafRJT82W8IxxD4N4X7ZEDTK1cZqnozzfsJgxRPRkdmknuxb4Rqy%2BvSgWoyaPRuO9YB%2F3C9WGPZT7%2BYDRNyNOf4VB45mzxrcctd8PhF3J2GkDFH5pGdlVZvh9%2FCLezOD8Iry0gPjOyoXkXYEt9LZRPSk0R8N%2B3Np5Lxw%2BNvpD4rhOV8cG9XKF7GTgNMG8ZJHLSU1Als3fD6TNwjzOv08lx1bLe7Y0DJcCUKJW9kTknGP7j1CK%2FsFDyqYG6b6Vx7T1muXB%2FuB68zcYNry6aZoL9v7%2BDxGJLp%2BLon0W28q3l7TgvHBMOMYe8Tq2pRobW9Csjq7qYR9ONCPpKT1KfipjhvOkpHVMOQcoZf91txkbiJcO2v4RdAwQV3xhA3INMTsKpw%2Br8PhKp828Abs1u8W34p8gT46CSCfkjNHa8x%2Fjl1gGNcCsrQcJmRa27p%2B2LiB3j1FwZ%2BYxuKXz%2BHrZH%2FilD2RrvCl1CXkQTMDpzIVS5tEys9N44UUYhjZ5jFXdX%2BcnctpPKFYQCU3dtMSDnvIZzL1LIEHDSBUKMrjG3JpxHU0AIp5tKpI1WSTzFqjBokQYLfTD3uMcGkMJ8bjZS532f5xzy%2FJfmThO3IRiclICfeq08OJOmXSTMKai68sGOqUBHaYbVxAaruBUseKLluy%2FbPSIY2nQcGGx5DHCHfZOTdS2uwd2KmDWQLQzLriTCjc8qDZ9xFUtNbEL67CQUluto5ARLW7MTsDylLZzpmnPTpGJuY%2Bu%2BpsNcpzV16sHnZhEPXD%2Ba9hmIe71j9%2BhgStRVtR1l1a1fmSpf2oeRPQ7m2yigxbeTTO3OXJQamiMOBRDGKXzQlE36k6MyHcx%2BJS3ySNPI49B&X-Amz-Signature=b01061d6596e8bf403580c66c931cf9be74e84f69476cfc46d633cb13ad67eee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

