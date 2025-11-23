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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC6O5RWY%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCID8sgu1jfE4haRX79%2BJ2qOEKXPklS4a72wtauSnYNIftAiEAtp%2BvQpj0ar%2Bn8EjrynmJcJY%2Fsjd5%2F0z8epI9SPTmj%2Fkq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCsSmWAjOPg0qmWMWCrcA1MiK9zn%2BFST3YQ8RY%2B38wDGZ9wT6cnL%2Fm27DLNnMQLouzPw%2FPk8w2YRem%2BouBJRc2BwOJjrH2wfO8soCbXkLjp839r3W6B8cl8PpGNz%2BT7DkGdHg7breVGb3HgFej5ECO2GA3BVJ4mvzzXJpoJqD76XZiVm%2FYYpPl2T7Eag%2FxY%2BlhPpeBawLWmZLECVQwHf%2B4HyIfsCNRQS27QU2wNV0O964i9Yx1mGUs%2BE6iObjP9C5ciNblQJBf7ekKKZV3P30PHJlg%2BtBv6R78w5qTcr%2BRp%2Fx7qUjEtrkrEfzfeIX%2FP5u7b0tx22EKU2ApTJVEBqlDFN5WkdB2HZcQbONRlk9KQjHE8GMrSPYV136CC3upmFj0HtuRpPWAe6b94N3u%2BNHv1YbadQfevuaC%2Blku2LNqCWdNEuYqAZecnW16kQTpFFpmJDwMjGb6QIRp8%2B0DSlR56AuIAMkyEzKQiyb6I2nUTlxQuWP9x4XPphFL1V8MhT3V2IjwN0rI5ghVZiBJZwJcvIWJFPVrDh6%2FHf2%2BE%2F%2BXGRQ1aVvAf598R2ISUSZtfnLqR551T8XcghrJCM8nNJSUdiDYHFHQ0jU0OHLmeR8kBodhuJ7cxWhsvwtBENlYFT8DT%2Bdic4Vv8%2FXxbNMI2xickGOqUBC889%2FUo%2FGThIs4wlW%2BAz4Cy5SrIPe%2B3Z7x%2BmDHSYBotLqjWrdiM%2B1Q%2FCX1%2FPVsy2Nf%2FCvYmv7SFIpZTIJ0XUrwn9kNdEXwmvYhpqCsnGnYS8dvN54l67yGKnitJRmmP10DFbDjImKnHQ1%2BSH9WfKnbaFjsYrmZizNmy%2BpvN6r88UuE6fQb0YXksx4l3s7aO2nDaS7vbz2qhXcUjhUNLjAgOW7Cum&X-Amz-Signature=f5cf286fb3d5d7c5c6be19a0c093867798f5f95dc235038e0a26cecd90d31dbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC6O5RWY%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCID8sgu1jfE4haRX79%2BJ2qOEKXPklS4a72wtauSnYNIftAiEAtp%2BvQpj0ar%2Bn8EjrynmJcJY%2Fsjd5%2F0z8epI9SPTmj%2Fkq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCsSmWAjOPg0qmWMWCrcA1MiK9zn%2BFST3YQ8RY%2B38wDGZ9wT6cnL%2Fm27DLNnMQLouzPw%2FPk8w2YRem%2BouBJRc2BwOJjrH2wfO8soCbXkLjp839r3W6B8cl8PpGNz%2BT7DkGdHg7breVGb3HgFej5ECO2GA3BVJ4mvzzXJpoJqD76XZiVm%2FYYpPl2T7Eag%2FxY%2BlhPpeBawLWmZLECVQwHf%2B4HyIfsCNRQS27QU2wNV0O964i9Yx1mGUs%2BE6iObjP9C5ciNblQJBf7ekKKZV3P30PHJlg%2BtBv6R78w5qTcr%2BRp%2Fx7qUjEtrkrEfzfeIX%2FP5u7b0tx22EKU2ApTJVEBqlDFN5WkdB2HZcQbONRlk9KQjHE8GMrSPYV136CC3upmFj0HtuRpPWAe6b94N3u%2BNHv1YbadQfevuaC%2Blku2LNqCWdNEuYqAZecnW16kQTpFFpmJDwMjGb6QIRp8%2B0DSlR56AuIAMkyEzKQiyb6I2nUTlxQuWP9x4XPphFL1V8MhT3V2IjwN0rI5ghVZiBJZwJcvIWJFPVrDh6%2FHf2%2BE%2F%2BXGRQ1aVvAf598R2ISUSZtfnLqR551T8XcghrJCM8nNJSUdiDYHFHQ0jU0OHLmeR8kBodhuJ7cxWhsvwtBENlYFT8DT%2Bdic4Vv8%2FXxbNMI2xickGOqUBC889%2FUo%2FGThIs4wlW%2BAz4Cy5SrIPe%2B3Z7x%2BmDHSYBotLqjWrdiM%2B1Q%2FCX1%2FPVsy2Nf%2FCvYmv7SFIpZTIJ0XUrwn9kNdEXwmvYhpqCsnGnYS8dvN54l67yGKnitJRmmP10DFbDjImKnHQ1%2BSH9WfKnbaFjsYrmZizNmy%2BpvN6r88UuE6fQb0YXksx4l3s7aO2nDaS7vbz2qhXcUjhUNLjAgOW7Cum&X-Amz-Signature=48fba1028bc141a4e5531510cc39754f7121b659565160d9540efad22cdc41cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC6O5RWY%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCID8sgu1jfE4haRX79%2BJ2qOEKXPklS4a72wtauSnYNIftAiEAtp%2BvQpj0ar%2Bn8EjrynmJcJY%2Fsjd5%2F0z8epI9SPTmj%2Fkq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDCsSmWAjOPg0qmWMWCrcA1MiK9zn%2BFST3YQ8RY%2B38wDGZ9wT6cnL%2Fm27DLNnMQLouzPw%2FPk8w2YRem%2BouBJRc2BwOJjrH2wfO8soCbXkLjp839r3W6B8cl8PpGNz%2BT7DkGdHg7breVGb3HgFej5ECO2GA3BVJ4mvzzXJpoJqD76XZiVm%2FYYpPl2T7Eag%2FxY%2BlhPpeBawLWmZLECVQwHf%2B4HyIfsCNRQS27QU2wNV0O964i9Yx1mGUs%2BE6iObjP9C5ciNblQJBf7ekKKZV3P30PHJlg%2BtBv6R78w5qTcr%2BRp%2Fx7qUjEtrkrEfzfeIX%2FP5u7b0tx22EKU2ApTJVEBqlDFN5WkdB2HZcQbONRlk9KQjHE8GMrSPYV136CC3upmFj0HtuRpPWAe6b94N3u%2BNHv1YbadQfevuaC%2Blku2LNqCWdNEuYqAZecnW16kQTpFFpmJDwMjGb6QIRp8%2B0DSlR56AuIAMkyEzKQiyb6I2nUTlxQuWP9x4XPphFL1V8MhT3V2IjwN0rI5ghVZiBJZwJcvIWJFPVrDh6%2FHf2%2BE%2F%2BXGRQ1aVvAf598R2ISUSZtfnLqR551T8XcghrJCM8nNJSUdiDYHFHQ0jU0OHLmeR8kBodhuJ7cxWhsvwtBENlYFT8DT%2Bdic4Vv8%2FXxbNMI2xickGOqUBC889%2FUo%2FGThIs4wlW%2BAz4Cy5SrIPe%2B3Z7x%2BmDHSYBotLqjWrdiM%2B1Q%2FCX1%2FPVsy2Nf%2FCvYmv7SFIpZTIJ0XUrwn9kNdEXwmvYhpqCsnGnYS8dvN54l67yGKnitJRmmP10DFbDjImKnHQ1%2BSH9WfKnbaFjsYrmZizNmy%2BpvN6r88UuE6fQb0YXksx4l3s7aO2nDaS7vbz2qhXcUjhUNLjAgOW7Cum&X-Amz-Signature=0defc2dbf46cccda21766309e6b8e2bb05c8f0957ba2c94c6bf2daa90d6ac9fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

