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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2TOWY6T%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAe9858p4odEjtEFeDkYu9qUemPt4ihTt3vfVLp8XrtlAiEAgu%2FXUpnxtPvuWCnwkXDJtFLyVK1Sr3kFbO21TWaPOTAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDMJHQwB7zQ%2FAu8XSCircA6vEp12JmE06Flc86WRHs6FUKxw401j%2F5Sgo9MbVKMZM8SL1EqkfQIvdSczpyqZnefyujZx%2FtJqhxZuaohZBa3YZtwG8CUEwDzOgxpCNYsTuNzXWsGrXQDJb56olwixEZh1YYg65zREqnvZ3fpR6SSJdQUQmO%2FRwf%2FSIJ6gPLLBE%2BJIHIx%2FVmG9O55LRfbLmWYrJOgDy3ceA3mlCnY5sHj%2BTTRZZw8I6NwmO23gIUYarmiixkN8A8KsKi0KqRw5Xuu%2BDr2RgH5C1LCKLShrWZkZnoouR1HaUK7pNDlFlB2yJc%2BuuqjditEfmpGu4HOR4GrZmFsVKNyn%2BgOuK73Qk2bkpr3ee5%2FGOlEmAfd5YSArwg2S%2BnilfvxgVafEFxE1dz63LQnGughALyH0eFObw6sQYwCYqy1gQdAXxnOnR%2FOosE5B%2F8j0tT%2FcOAHgVPBEMAWtEWJHCh1oN72k80tx72Z13xclGyZxa6UbRvzp40arIs0o38%2F%2B%2FbmQktjE%2BoKyAU6vS%2BfeZIY5oSjsA710lZNwtY2TbVJ7kGKhQV76xqgVbU%2BtAnF4AWGZR3%2Fie0neK8%2FNe%2BPWxrFPL99IWcRiUUCJVuOXo7JsaaZEKXIM6tQ4vgnQJoTc2NGE5Y%2F%2F0MN%2FrwcoGOqUBpwTnWs%2BrE8oZlKSRVUKq4zdRnoUlrvJ6ns9Sx7MWZg0o9VsaWR4AASPR4PBzQrVUO8zlc2FC13nt5jKY5PA9iB3qToIvxcUWLYaGqH%2FBByXcNp%2Fb0mFn0QttFYtS1iok6n9hM8QAnPmD17iZpy0OlWj4jI%2BUX3hRxLW%2FXZyA3vp7OrBpBqk9Eb%2BJKroCisscr5MklVwDGc9yMPuuHZC9FEAj5Iqs&X-Amz-Signature=4f5c899bde6f545d5e0982b7fa208d6b33dbce2f988c56d7d6028db6bc112a4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2TOWY6T%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAe9858p4odEjtEFeDkYu9qUemPt4ihTt3vfVLp8XrtlAiEAgu%2FXUpnxtPvuWCnwkXDJtFLyVK1Sr3kFbO21TWaPOTAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDMJHQwB7zQ%2FAu8XSCircA6vEp12JmE06Flc86WRHs6FUKxw401j%2F5Sgo9MbVKMZM8SL1EqkfQIvdSczpyqZnefyujZx%2FtJqhxZuaohZBa3YZtwG8CUEwDzOgxpCNYsTuNzXWsGrXQDJb56olwixEZh1YYg65zREqnvZ3fpR6SSJdQUQmO%2FRwf%2FSIJ6gPLLBE%2BJIHIx%2FVmG9O55LRfbLmWYrJOgDy3ceA3mlCnY5sHj%2BTTRZZw8I6NwmO23gIUYarmiixkN8A8KsKi0KqRw5Xuu%2BDr2RgH5C1LCKLShrWZkZnoouR1HaUK7pNDlFlB2yJc%2BuuqjditEfmpGu4HOR4GrZmFsVKNyn%2BgOuK73Qk2bkpr3ee5%2FGOlEmAfd5YSArwg2S%2BnilfvxgVafEFxE1dz63LQnGughALyH0eFObw6sQYwCYqy1gQdAXxnOnR%2FOosE5B%2F8j0tT%2FcOAHgVPBEMAWtEWJHCh1oN72k80tx72Z13xclGyZxa6UbRvzp40arIs0o38%2F%2B%2FbmQktjE%2BoKyAU6vS%2BfeZIY5oSjsA710lZNwtY2TbVJ7kGKhQV76xqgVbU%2BtAnF4AWGZR3%2Fie0neK8%2FNe%2BPWxrFPL99IWcRiUUCJVuOXo7JsaaZEKXIM6tQ4vgnQJoTc2NGE5Y%2F%2F0MN%2FrwcoGOqUBpwTnWs%2BrE8oZlKSRVUKq4zdRnoUlrvJ6ns9Sx7MWZg0o9VsaWR4AASPR4PBzQrVUO8zlc2FC13nt5jKY5PA9iB3qToIvxcUWLYaGqH%2FBByXcNp%2Fb0mFn0QttFYtS1iok6n9hM8QAnPmD17iZpy0OlWj4jI%2BUX3hRxLW%2FXZyA3vp7OrBpBqk9Eb%2BJKroCisscr5MklVwDGc9yMPuuHZC9FEAj5Iqs&X-Amz-Signature=fc39d292ea705ba4b16faf9078d270e656044a4e848c3e55d85cb0d5f1807186&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2TOWY6T%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAe9858p4odEjtEFeDkYu9qUemPt4ihTt3vfVLp8XrtlAiEAgu%2FXUpnxtPvuWCnwkXDJtFLyVK1Sr3kFbO21TWaPOTAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDMJHQwB7zQ%2FAu8XSCircA6vEp12JmE06Flc86WRHs6FUKxw401j%2F5Sgo9MbVKMZM8SL1EqkfQIvdSczpyqZnefyujZx%2FtJqhxZuaohZBa3YZtwG8CUEwDzOgxpCNYsTuNzXWsGrXQDJb56olwixEZh1YYg65zREqnvZ3fpR6SSJdQUQmO%2FRwf%2FSIJ6gPLLBE%2BJIHIx%2FVmG9O55LRfbLmWYrJOgDy3ceA3mlCnY5sHj%2BTTRZZw8I6NwmO23gIUYarmiixkN8A8KsKi0KqRw5Xuu%2BDr2RgH5C1LCKLShrWZkZnoouR1HaUK7pNDlFlB2yJc%2BuuqjditEfmpGu4HOR4GrZmFsVKNyn%2BgOuK73Qk2bkpr3ee5%2FGOlEmAfd5YSArwg2S%2BnilfvxgVafEFxE1dz63LQnGughALyH0eFObw6sQYwCYqy1gQdAXxnOnR%2FOosE5B%2F8j0tT%2FcOAHgVPBEMAWtEWJHCh1oN72k80tx72Z13xclGyZxa6UbRvzp40arIs0o38%2F%2B%2FbmQktjE%2BoKyAU6vS%2BfeZIY5oSjsA710lZNwtY2TbVJ7kGKhQV76xqgVbU%2BtAnF4AWGZR3%2Fie0neK8%2FNe%2BPWxrFPL99IWcRiUUCJVuOXo7JsaaZEKXIM6tQ4vgnQJoTc2NGE5Y%2F%2F0MN%2FrwcoGOqUBpwTnWs%2BrE8oZlKSRVUKq4zdRnoUlrvJ6ns9Sx7MWZg0o9VsaWR4AASPR4PBzQrVUO8zlc2FC13nt5jKY5PA9iB3qToIvxcUWLYaGqH%2FBByXcNp%2Fb0mFn0QttFYtS1iok6n9hM8QAnPmD17iZpy0OlWj4jI%2BUX3hRxLW%2FXZyA3vp7OrBpBqk9Eb%2BJKroCisscr5MklVwDGc9yMPuuHZC9FEAj5Iqs&X-Amz-Signature=ff038416e67a0afe8d612af7436ba665e0e35954eb6666c06dab336171a714ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

