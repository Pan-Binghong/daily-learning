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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN5VITE3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgxx6l2V4ylNxegM9HkkKIrNggr2eC8CINzWiIUL2cQAIgd%2FD0tZrPxH%2BXEIr8PjDMUQ08wGgtnyNfjLyoNtNeV44qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYefShLO5pQM%2F3KHircA1tyfRoRJ1scD5q%2BZsHh%2BLupLbhgLRWjxmnal%2B%2B8KayvtbwcHTuEeDQYF7ZhVfVgScMgYf%2FeY9PXHBnco0TnAJOuhLO9H5yeDBDxK84pGlKlRQd1bYmOjwtnuFGqd3GZAVDWo01ht78jj9ly9Ilt1U7MnoIv%2FIxiHtLuM25zqnOSFTr5swT9cfVszzdsBoFSN5JjH58i7caI2GGk8OyxfiH%2FE5ttg2S6OI4iYxlFueUzMt2C9xJzrzvPLt%2F3%2Bqgct6Hdb%2BbLV9PaIwlXlIfpNOb30CH2Fww8829HppMgNVlyHB4CdBszN3SkXChKrJrAdUZaaI%2BxCOTnKjQjLRtRwsYUA%2BmeNayLfpqs0AY5RmfNprJ9uota70OxN1KwTxhJ5%2B8g0gfFbyxV9c8gq%2B3OVd%2Bpc0CWUY738feQJSdtJ%2B1XMqGDdsswIbiHtai3%2BnEIULPxafQfU7AM%2FNsV3yG%2BTLKETaertye%2FG0dHICxk5%2F5xOor%2BixT1ubA0Uv%2BllgsozD7%2FFvda4bPnxDzZNLUdvHs8k4c3l9CBsyoHWmLD9EATEQjRJHUHfjdbe%2Bt6WgPYNQCQ78gvdzqseo3wC6fmAF5HgBLB0CeEj25%2BVSxEJYPcQfJpdAy3DY0dRVppMPDxr8gGOqUB4geiPO%2BMMka%2F64%2FGVX6ERVqZHBQwR1pIr4bilzbd3uLuSrvrv2AgP6m1FZ5NG1%2FeSG0GdErHWnMPLpUJmP3VR%2F1gKt7waZjOsCnYK1p4id8apJNtJU%2BIiejibeeFacHwJJ5YSEgCUnqH7ajF4t5rsSSI0%2BZk0jUu7XjoLme0DgQGWuzkZ7SB5nuUAd0jKHNmNtd%2FkOSa5W2qQuPwmqTnXe7FObSE&X-Amz-Signature=018eda7a8de0105bd4c034b15d5a49f9d5de05e8891278cb7b2a4904b20e51da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN5VITE3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgxx6l2V4ylNxegM9HkkKIrNggr2eC8CINzWiIUL2cQAIgd%2FD0tZrPxH%2BXEIr8PjDMUQ08wGgtnyNfjLyoNtNeV44qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYefShLO5pQM%2F3KHircA1tyfRoRJ1scD5q%2BZsHh%2BLupLbhgLRWjxmnal%2B%2B8KayvtbwcHTuEeDQYF7ZhVfVgScMgYf%2FeY9PXHBnco0TnAJOuhLO9H5yeDBDxK84pGlKlRQd1bYmOjwtnuFGqd3GZAVDWo01ht78jj9ly9Ilt1U7MnoIv%2FIxiHtLuM25zqnOSFTr5swT9cfVszzdsBoFSN5JjH58i7caI2GGk8OyxfiH%2FE5ttg2S6OI4iYxlFueUzMt2C9xJzrzvPLt%2F3%2Bqgct6Hdb%2BbLV9PaIwlXlIfpNOb30CH2Fww8829HppMgNVlyHB4CdBszN3SkXChKrJrAdUZaaI%2BxCOTnKjQjLRtRwsYUA%2BmeNayLfpqs0AY5RmfNprJ9uota70OxN1KwTxhJ5%2B8g0gfFbyxV9c8gq%2B3OVd%2Bpc0CWUY738feQJSdtJ%2B1XMqGDdsswIbiHtai3%2BnEIULPxafQfU7AM%2FNsV3yG%2BTLKETaertye%2FG0dHICxk5%2F5xOor%2BixT1ubA0Uv%2BllgsozD7%2FFvda4bPnxDzZNLUdvHs8k4c3l9CBsyoHWmLD9EATEQjRJHUHfjdbe%2Bt6WgPYNQCQ78gvdzqseo3wC6fmAF5HgBLB0CeEj25%2BVSxEJYPcQfJpdAy3DY0dRVppMPDxr8gGOqUB4geiPO%2BMMka%2F64%2FGVX6ERVqZHBQwR1pIr4bilzbd3uLuSrvrv2AgP6m1FZ5NG1%2FeSG0GdErHWnMPLpUJmP3VR%2F1gKt7waZjOsCnYK1p4id8apJNtJU%2BIiejibeeFacHwJJ5YSEgCUnqH7ajF4t5rsSSI0%2BZk0jUu7XjoLme0DgQGWuzkZ7SB5nuUAd0jKHNmNtd%2FkOSa5W2qQuPwmqTnXe7FObSE&X-Amz-Signature=d941d81610fcc03469c91e62c3d70c0e327de2d173dfa038f0049552f5b2b8d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN5VITE3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgxx6l2V4ylNxegM9HkkKIrNggr2eC8CINzWiIUL2cQAIgd%2FD0tZrPxH%2BXEIr8PjDMUQ08wGgtnyNfjLyoNtNeV44qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYefShLO5pQM%2F3KHircA1tyfRoRJ1scD5q%2BZsHh%2BLupLbhgLRWjxmnal%2B%2B8KayvtbwcHTuEeDQYF7ZhVfVgScMgYf%2FeY9PXHBnco0TnAJOuhLO9H5yeDBDxK84pGlKlRQd1bYmOjwtnuFGqd3GZAVDWo01ht78jj9ly9Ilt1U7MnoIv%2FIxiHtLuM25zqnOSFTr5swT9cfVszzdsBoFSN5JjH58i7caI2GGk8OyxfiH%2FE5ttg2S6OI4iYxlFueUzMt2C9xJzrzvPLt%2F3%2Bqgct6Hdb%2BbLV9PaIwlXlIfpNOb30CH2Fww8829HppMgNVlyHB4CdBszN3SkXChKrJrAdUZaaI%2BxCOTnKjQjLRtRwsYUA%2BmeNayLfpqs0AY5RmfNprJ9uota70OxN1KwTxhJ5%2B8g0gfFbyxV9c8gq%2B3OVd%2Bpc0CWUY738feQJSdtJ%2B1XMqGDdsswIbiHtai3%2BnEIULPxafQfU7AM%2FNsV3yG%2BTLKETaertye%2FG0dHICxk5%2F5xOor%2BixT1ubA0Uv%2BllgsozD7%2FFvda4bPnxDzZNLUdvHs8k4c3l9CBsyoHWmLD9EATEQjRJHUHfjdbe%2Bt6WgPYNQCQ78gvdzqseo3wC6fmAF5HgBLB0CeEj25%2BVSxEJYPcQfJpdAy3DY0dRVppMPDxr8gGOqUB4geiPO%2BMMka%2F64%2FGVX6ERVqZHBQwR1pIr4bilzbd3uLuSrvrv2AgP6m1FZ5NG1%2FeSG0GdErHWnMPLpUJmP3VR%2F1gKt7waZjOsCnYK1p4id8apJNtJU%2BIiejibeeFacHwJJ5YSEgCUnqH7ajF4t5rsSSI0%2BZk0jUu7XjoLme0DgQGWuzkZ7SB5nuUAd0jKHNmNtd%2FkOSa5W2qQuPwmqTnXe7FObSE&X-Amz-Signature=54750a6125614a2780c86f33e4b979c83999d13dd066f6cfb81a8b1d2851b63e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

