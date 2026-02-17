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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUSKY3ON%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCGMgFkJ2mMZcACAHa4zcT2ic78LOc1P%2BNIdbfOS%2FDATQIhAPoUJbj05SIPKSkxcD9kZUZj%2Bu%2BQTy2x8IPnVmEeo9T9Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxYK2KOMg9mT8MXl3Mq3AMqR3DvG%2FECa%2Fl8%2FCoOgx7pYK3Dy9v1AQ7ExO%2BYw7hIS7nPRMK%2FXcOy4Y2PJ1grV3BflCLPvNl6kUGBZgwVQv6qR%2B5CWEOQn19v6Ewbif62zovOgpjTg2UXpvTEcXEYqCbKOkzOdyOI86od4qFo%2FfasFNd41kr%2BU26lBZdqiWTSoqP%2BSNJKg2w%2B4mAw7%2FMMpZ4jY1gn1JFcMyHXw3wdbh2CFJ59HfjJ4e0xST8yZb2sdM7qr9nFpYKW8DYHWibmlf3Wx4M8JxVbapxzeitSVclmX2NkzLvnmSfDN3H%2BCMzWe4Pgh%2FRlq1o%2Fv4B%2FEcvGFAd1HWbeA8BphvBFoQmB2dIW5cawwjZdfeFBMlB%2Bq1ezOO2uCGOMTjtxuAhfzFLNwJODwuGq0gOkkQHXLgbczc01sp7KdTB7FQiFleTCoR5D1JAPPZGi2qwXYlIMzSc0khVG4HBSMKFr25LIcl2%2F6%2F9TGv7NP%2BaLqxB7i%2BrzIe0WE6FiMvUj%2BdhVq%2F3esQC7o64ngg7q98VInTsOY9y%2BesoTlB%2F5%2F2bJsF1faZFQKnLBcXbwR1MpFPL3q5ggUpDz51TbPWq70TJi4d1U2%2Bs68tjU9hNVNT0o4ji01bvjoxgxToOzx6ggoTVx0Jup5DDiv8%2FMBjqkAYArXHtAdYVtMGs0niibiznbY1pTgg31Xt0LVf0REFFeBuIQvbnJbIjyINxHvQEoSj3PgcGBytEnfg6D79RhUVWq7aaWP%2BmP9gtCWKT4qly7i%2FavpuXy7MNc%2Bljqp9qdWFw8RcorG%2Bul56oLlgp3RviGxymNSEO572shYr85mCApLJbxUCgJkCrzf07pzLNDM3knghgd9qvaQiRG9VVRfTAlHe3o&X-Amz-Signature=42b2250260c3c2f63f63df10ed3a595ab431e7272f9b265db84a9f62461944c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUSKY3ON%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCGMgFkJ2mMZcACAHa4zcT2ic78LOc1P%2BNIdbfOS%2FDATQIhAPoUJbj05SIPKSkxcD9kZUZj%2Bu%2BQTy2x8IPnVmEeo9T9Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxYK2KOMg9mT8MXl3Mq3AMqR3DvG%2FECa%2Fl8%2FCoOgx7pYK3Dy9v1AQ7ExO%2BYw7hIS7nPRMK%2FXcOy4Y2PJ1grV3BflCLPvNl6kUGBZgwVQv6qR%2B5CWEOQn19v6Ewbif62zovOgpjTg2UXpvTEcXEYqCbKOkzOdyOI86od4qFo%2FfasFNd41kr%2BU26lBZdqiWTSoqP%2BSNJKg2w%2B4mAw7%2FMMpZ4jY1gn1JFcMyHXw3wdbh2CFJ59HfjJ4e0xST8yZb2sdM7qr9nFpYKW8DYHWibmlf3Wx4M8JxVbapxzeitSVclmX2NkzLvnmSfDN3H%2BCMzWe4Pgh%2FRlq1o%2Fv4B%2FEcvGFAd1HWbeA8BphvBFoQmB2dIW5cawwjZdfeFBMlB%2Bq1ezOO2uCGOMTjtxuAhfzFLNwJODwuGq0gOkkQHXLgbczc01sp7KdTB7FQiFleTCoR5D1JAPPZGi2qwXYlIMzSc0khVG4HBSMKFr25LIcl2%2F6%2F9TGv7NP%2BaLqxB7i%2BrzIe0WE6FiMvUj%2BdhVq%2F3esQC7o64ngg7q98VInTsOY9y%2BesoTlB%2F5%2F2bJsF1faZFQKnLBcXbwR1MpFPL3q5ggUpDz51TbPWq70TJi4d1U2%2Bs68tjU9hNVNT0o4ji01bvjoxgxToOzx6ggoTVx0Jup5DDiv8%2FMBjqkAYArXHtAdYVtMGs0niibiznbY1pTgg31Xt0LVf0REFFeBuIQvbnJbIjyINxHvQEoSj3PgcGBytEnfg6D79RhUVWq7aaWP%2BmP9gtCWKT4qly7i%2FavpuXy7MNc%2Bljqp9qdWFw8RcorG%2Bul56oLlgp3RviGxymNSEO572shYr85mCApLJbxUCgJkCrzf07pzLNDM3knghgd9qvaQiRG9VVRfTAlHe3o&X-Amz-Signature=511b7cf38908049bc13dbe7a7e29eefa6df2c015811fa249c53dafef2c5f3e07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUSKY3ON%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCGMgFkJ2mMZcACAHa4zcT2ic78LOc1P%2BNIdbfOS%2FDATQIhAPoUJbj05SIPKSkxcD9kZUZj%2Bu%2BQTy2x8IPnVmEeo9T9Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxYK2KOMg9mT8MXl3Mq3AMqR3DvG%2FECa%2Fl8%2FCoOgx7pYK3Dy9v1AQ7ExO%2BYw7hIS7nPRMK%2FXcOy4Y2PJ1grV3BflCLPvNl6kUGBZgwVQv6qR%2B5CWEOQn19v6Ewbif62zovOgpjTg2UXpvTEcXEYqCbKOkzOdyOI86od4qFo%2FfasFNd41kr%2BU26lBZdqiWTSoqP%2BSNJKg2w%2B4mAw7%2FMMpZ4jY1gn1JFcMyHXw3wdbh2CFJ59HfjJ4e0xST8yZb2sdM7qr9nFpYKW8DYHWibmlf3Wx4M8JxVbapxzeitSVclmX2NkzLvnmSfDN3H%2BCMzWe4Pgh%2FRlq1o%2Fv4B%2FEcvGFAd1HWbeA8BphvBFoQmB2dIW5cawwjZdfeFBMlB%2Bq1ezOO2uCGOMTjtxuAhfzFLNwJODwuGq0gOkkQHXLgbczc01sp7KdTB7FQiFleTCoR5D1JAPPZGi2qwXYlIMzSc0khVG4HBSMKFr25LIcl2%2F6%2F9TGv7NP%2BaLqxB7i%2BrzIe0WE6FiMvUj%2BdhVq%2F3esQC7o64ngg7q98VInTsOY9y%2BesoTlB%2F5%2F2bJsF1faZFQKnLBcXbwR1MpFPL3q5ggUpDz51TbPWq70TJi4d1U2%2Bs68tjU9hNVNT0o4ji01bvjoxgxToOzx6ggoTVx0Jup5DDiv8%2FMBjqkAYArXHtAdYVtMGs0niibiznbY1pTgg31Xt0LVf0REFFeBuIQvbnJbIjyINxHvQEoSj3PgcGBytEnfg6D79RhUVWq7aaWP%2BmP9gtCWKT4qly7i%2FavpuXy7MNc%2Bljqp9qdWFw8RcorG%2Bul56oLlgp3RviGxymNSEO572shYr85mCApLJbxUCgJkCrzf07pzLNDM3knghgd9qvaQiRG9VVRfTAlHe3o&X-Amz-Signature=bdc31b7d778f418fdcb1fe6248d11dc87c9bdb3e4067c3d231f3f35bf57cbd2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

