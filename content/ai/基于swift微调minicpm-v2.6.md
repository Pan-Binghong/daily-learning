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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNU4CJY%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCICOiA0a2dv5LCNosYFja0Y6xDGGdJGnPKtwUqUvVp240AiEAodmbED%2FOEat%2Bgd5qNJ72f57y6nKri7iYCnWqksbr0WgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4pWJ9VfTqlhwrTRircA%2BZnXL1zdqZcQF%2BI%2BeCV%2BlAKkqBokdpHcTXPlEgsfsW5VdFAw3aamRHrkenPvVEwgbZsY2itjMkS8SuBXIAZCe3WAQm6Fy%2BjEkj%2B2DIMVOEjnNxu29IVHHZO7aktKwyDz5Rb568LNa6V5ajRpaemFNvFQPBuu8kSd3k5w5LiDdN9UBbg8sMYV6Gi4mYJkx5%2BL2AyntJtynGZFYcp42eX5rtcZun9mGkFTeQTp6eFbdtAT4sdojNQarSXWmWlnjAr531J4eDfS3N2s2%2BSAGpDH0GNY9rh2L5L6DWX6DxaVOBPZ2NgcUl7F5FRnfOMpwCbg07vuS%2FDxsiF3tLr%2BRyAzD39svgZ%2BTmb1EZ%2BwbZ0FEYv6J%2FeXxyMG2DAJTXfOG9Z7kUvHs11cwyHcIPh4ZwyakJMbGAcI77XkSkxQCFBxZIxtJ0RBtqzndNK3cdSPpv0F2sH1e6c68DnmSbWC%2FEUKzSZ1N7ejlTo5bovZ5U269t%2BpvFhkr50eR1OaQ%2Fcc77v4e1y%2BqnLbrzWjm5jPSzMpjCK5eGSJBzA%2Fm4u%2BZs6CK1cqqz1ju2YIN9zpKY1fEGSA0A29DfEY1tAt4ai1mK4fPdMJyTU2bdLsxnvM%2FqDXVQOhvcQ1IS%2BZytiilTiMIW29MwGOqUBqzDLJ5UjCiIyvwHBpWFweB2P4UAbWajO6INOzR54FmYJ7Q7iiKNBX616mLCGvXnsBpaLKAVkOK4MWDM71GbHKtdiii0P9Cb423aPrLRSBKe05DY3H2nB8S%2BO63U7BgiL6ktm04XWbfwFoPVdcc4FZ5b0Y0PtUg6RTX5G4IxVec8Wc%2FoI0QVHxlCzcuOg3PU664yLwYkWue0sZNZM%2B2DvWuENDGz0&X-Amz-Signature=47413427cbd02db5482a3fe03263e3671c887ee4911554badb7e2a19d2a391eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNU4CJY%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCICOiA0a2dv5LCNosYFja0Y6xDGGdJGnPKtwUqUvVp240AiEAodmbED%2FOEat%2Bgd5qNJ72f57y6nKri7iYCnWqksbr0WgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4pWJ9VfTqlhwrTRircA%2BZnXL1zdqZcQF%2BI%2BeCV%2BlAKkqBokdpHcTXPlEgsfsW5VdFAw3aamRHrkenPvVEwgbZsY2itjMkS8SuBXIAZCe3WAQm6Fy%2BjEkj%2B2DIMVOEjnNxu29IVHHZO7aktKwyDz5Rb568LNa6V5ajRpaemFNvFQPBuu8kSd3k5w5LiDdN9UBbg8sMYV6Gi4mYJkx5%2BL2AyntJtynGZFYcp42eX5rtcZun9mGkFTeQTp6eFbdtAT4sdojNQarSXWmWlnjAr531J4eDfS3N2s2%2BSAGpDH0GNY9rh2L5L6DWX6DxaVOBPZ2NgcUl7F5FRnfOMpwCbg07vuS%2FDxsiF3tLr%2BRyAzD39svgZ%2BTmb1EZ%2BwbZ0FEYv6J%2FeXxyMG2DAJTXfOG9Z7kUvHs11cwyHcIPh4ZwyakJMbGAcI77XkSkxQCFBxZIxtJ0RBtqzndNK3cdSPpv0F2sH1e6c68DnmSbWC%2FEUKzSZ1N7ejlTo5bovZ5U269t%2BpvFhkr50eR1OaQ%2Fcc77v4e1y%2BqnLbrzWjm5jPSzMpjCK5eGSJBzA%2Fm4u%2BZs6CK1cqqz1ju2YIN9zpKY1fEGSA0A29DfEY1tAt4ai1mK4fPdMJyTU2bdLsxnvM%2FqDXVQOhvcQ1IS%2BZytiilTiMIW29MwGOqUBqzDLJ5UjCiIyvwHBpWFweB2P4UAbWajO6INOzR54FmYJ7Q7iiKNBX616mLCGvXnsBpaLKAVkOK4MWDM71GbHKtdiii0P9Cb423aPrLRSBKe05DY3H2nB8S%2BO63U7BgiL6ktm04XWbfwFoPVdcc4FZ5b0Y0PtUg6RTX5G4IxVec8Wc%2FoI0QVHxlCzcuOg3PU664yLwYkWue0sZNZM%2B2DvWuENDGz0&X-Amz-Signature=8cc62b9c3b73cd4a8c6ebe2cdcf630ba9f0bf7222ab3543fabce597837fc23ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YNU4CJY%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCICOiA0a2dv5LCNosYFja0Y6xDGGdJGnPKtwUqUvVp240AiEAodmbED%2FOEat%2Bgd5qNJ72f57y6nKri7iYCnWqksbr0WgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4pWJ9VfTqlhwrTRircA%2BZnXL1zdqZcQF%2BI%2BeCV%2BlAKkqBokdpHcTXPlEgsfsW5VdFAw3aamRHrkenPvVEwgbZsY2itjMkS8SuBXIAZCe3WAQm6Fy%2BjEkj%2B2DIMVOEjnNxu29IVHHZO7aktKwyDz5Rb568LNa6V5ajRpaemFNvFQPBuu8kSd3k5w5LiDdN9UBbg8sMYV6Gi4mYJkx5%2BL2AyntJtynGZFYcp42eX5rtcZun9mGkFTeQTp6eFbdtAT4sdojNQarSXWmWlnjAr531J4eDfS3N2s2%2BSAGpDH0GNY9rh2L5L6DWX6DxaVOBPZ2NgcUl7F5FRnfOMpwCbg07vuS%2FDxsiF3tLr%2BRyAzD39svgZ%2BTmb1EZ%2BwbZ0FEYv6J%2FeXxyMG2DAJTXfOG9Z7kUvHs11cwyHcIPh4ZwyakJMbGAcI77XkSkxQCFBxZIxtJ0RBtqzndNK3cdSPpv0F2sH1e6c68DnmSbWC%2FEUKzSZ1N7ejlTo5bovZ5U269t%2BpvFhkr50eR1OaQ%2Fcc77v4e1y%2BqnLbrzWjm5jPSzMpjCK5eGSJBzA%2Fm4u%2BZs6CK1cqqz1ju2YIN9zpKY1fEGSA0A29DfEY1tAt4ai1mK4fPdMJyTU2bdLsxnvM%2FqDXVQOhvcQ1IS%2BZytiilTiMIW29MwGOqUBqzDLJ5UjCiIyvwHBpWFweB2P4UAbWajO6INOzR54FmYJ7Q7iiKNBX616mLCGvXnsBpaLKAVkOK4MWDM71GbHKtdiii0P9Cb423aPrLRSBKe05DY3H2nB8S%2BO63U7BgiL6ktm04XWbfwFoPVdcc4FZ5b0Y0PtUg6RTX5G4IxVec8Wc%2FoI0QVHxlCzcuOg3PU664yLwYkWue0sZNZM%2B2DvWuENDGz0&X-Amz-Signature=c8fa10d0dcfefece29b4b9e81965d5a34686aa1540fd126522b1f5ea6de5bf4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

