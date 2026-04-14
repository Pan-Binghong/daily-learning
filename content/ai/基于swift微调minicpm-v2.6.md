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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCUQYIRV%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkrES1p34IZQBou7BCMiMbTPZjTIxfd5cGOVd2nPzrRgIgNlQkXHD0uRW%2FAAXTh3O8jqiqjiH6d0cK6bX6uBgplcsqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ20BqrX%2FpIP9iI8sCrcA%2BhEWOUTks%2BWRjudZAf1GLZKMMH2VPLh2c4%2BAc8SYn%2FtqCplnjLDtIjo3TwkNq%2BaGUiVuapJwCLBOzJHqAwygU89CtNpeyuYamxh%2FP9g4ChLtIMR%2B21TLSfqitG9HpST9HkJXICp%2BCWBVURnRkBK4SMiNp%2Bh2qkuvtPI7q%2FlFhSlblSXhrjL4RdBM3qn3It8hUGJ%2BQRJOeftc6kAGqz%2BupdmfJS0AapKUg2OQrfgZTpqEgGvGOwuT%2FKIIibKDhh996Sw5tTywwAQhBTcm8702zZCYlQUtGTzoAGN3A%2BlQbBQ9jjtx2299ZNpV1kwXBkB5z%2F5emWSNsMzBIkT4hiRLlvmWLCFXVDfQS2AAgGYHPU6LsstzLh9E%2FE2hGnh8W49ju%2BmMPzE%2FGopP6n%2BU0tcOkNckMhh7IrpbnHIps94j2wdAGt6j2kjaUBc%2FKfjaX8Z5GCCkB8NIh%2BiXhkXw%2BF25KsKMMkMw8X4lanHWYT8Pq3u1IbQQJ2S0NR2Q7qN6Ed8iGWMyRd7uV03J46jpX6AjG3F%2BtaJKhF6rDNy7N3Dn%2FK3HXzzCIjII84f%2F70r4CVX1QiOXpQgG8Qiz58kRbkvRe%2B%2B37fxK0rerOJhCsD6R5s5en2IirmknDFmUKRMMP3w9s4GOqUBm0WeCXKxKNfowl6ZuZSIRh2JX%2FCybnQuoKRUzTb5WvuHBcNDlNfeQYr3doLg5tu4XLbuKLRvJurhn1cvOHPT9VZ9yU1BrIpDnX461ALGjHNsn2X7k8G3UFjCqrSdESf%2BupgB%2FFJL%2B67JkRneHMMKVXzgBJ1tsB72CQWXZ5oTzaqoaeTNLOWxk0lzepulLlovbmMm25dhnFDWn3DE0DZI3GB4iwYY&X-Amz-Signature=ca226fd039db9bada18371ff50e8f9065d4050e1f7f31bbf39290064566b3c77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCUQYIRV%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkrES1p34IZQBou7BCMiMbTPZjTIxfd5cGOVd2nPzrRgIgNlQkXHD0uRW%2FAAXTh3O8jqiqjiH6d0cK6bX6uBgplcsqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ20BqrX%2FpIP9iI8sCrcA%2BhEWOUTks%2BWRjudZAf1GLZKMMH2VPLh2c4%2BAc8SYn%2FtqCplnjLDtIjo3TwkNq%2BaGUiVuapJwCLBOzJHqAwygU89CtNpeyuYamxh%2FP9g4ChLtIMR%2B21TLSfqitG9HpST9HkJXICp%2BCWBVURnRkBK4SMiNp%2Bh2qkuvtPI7q%2FlFhSlblSXhrjL4RdBM3qn3It8hUGJ%2BQRJOeftc6kAGqz%2BupdmfJS0AapKUg2OQrfgZTpqEgGvGOwuT%2FKIIibKDhh996Sw5tTywwAQhBTcm8702zZCYlQUtGTzoAGN3A%2BlQbBQ9jjtx2299ZNpV1kwXBkB5z%2F5emWSNsMzBIkT4hiRLlvmWLCFXVDfQS2AAgGYHPU6LsstzLh9E%2FE2hGnh8W49ju%2BmMPzE%2FGopP6n%2BU0tcOkNckMhh7IrpbnHIps94j2wdAGt6j2kjaUBc%2FKfjaX8Z5GCCkB8NIh%2BiXhkXw%2BF25KsKMMkMw8X4lanHWYT8Pq3u1IbQQJ2S0NR2Q7qN6Ed8iGWMyRd7uV03J46jpX6AjG3F%2BtaJKhF6rDNy7N3Dn%2FK3HXzzCIjII84f%2F70r4CVX1QiOXpQgG8Qiz58kRbkvRe%2B%2B37fxK0rerOJhCsD6R5s5en2IirmknDFmUKRMMP3w9s4GOqUBm0WeCXKxKNfowl6ZuZSIRh2JX%2FCybnQuoKRUzTb5WvuHBcNDlNfeQYr3doLg5tu4XLbuKLRvJurhn1cvOHPT9VZ9yU1BrIpDnX461ALGjHNsn2X7k8G3UFjCqrSdESf%2BupgB%2FFJL%2B67JkRneHMMKVXzgBJ1tsB72CQWXZ5oTzaqoaeTNLOWxk0lzepulLlovbmMm25dhnFDWn3DE0DZI3GB4iwYY&X-Amz-Signature=c3a56f20e20fe33c6097e7d4f4f28a2124b02b7582a78fe8ed1ba29b885f0cf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCUQYIRV%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkrES1p34IZQBou7BCMiMbTPZjTIxfd5cGOVd2nPzrRgIgNlQkXHD0uRW%2FAAXTh3O8jqiqjiH6d0cK6bX6uBgplcsqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ20BqrX%2FpIP9iI8sCrcA%2BhEWOUTks%2BWRjudZAf1GLZKMMH2VPLh2c4%2BAc8SYn%2FtqCplnjLDtIjo3TwkNq%2BaGUiVuapJwCLBOzJHqAwygU89CtNpeyuYamxh%2FP9g4ChLtIMR%2B21TLSfqitG9HpST9HkJXICp%2BCWBVURnRkBK4SMiNp%2Bh2qkuvtPI7q%2FlFhSlblSXhrjL4RdBM3qn3It8hUGJ%2BQRJOeftc6kAGqz%2BupdmfJS0AapKUg2OQrfgZTpqEgGvGOwuT%2FKIIibKDhh996Sw5tTywwAQhBTcm8702zZCYlQUtGTzoAGN3A%2BlQbBQ9jjtx2299ZNpV1kwXBkB5z%2F5emWSNsMzBIkT4hiRLlvmWLCFXVDfQS2AAgGYHPU6LsstzLh9E%2FE2hGnh8W49ju%2BmMPzE%2FGopP6n%2BU0tcOkNckMhh7IrpbnHIps94j2wdAGt6j2kjaUBc%2FKfjaX8Z5GCCkB8NIh%2BiXhkXw%2BF25KsKMMkMw8X4lanHWYT8Pq3u1IbQQJ2S0NR2Q7qN6Ed8iGWMyRd7uV03J46jpX6AjG3F%2BtaJKhF6rDNy7N3Dn%2FK3HXzzCIjII84f%2F70r4CVX1QiOXpQgG8Qiz58kRbkvRe%2B%2B37fxK0rerOJhCsD6R5s5en2IirmknDFmUKRMMP3w9s4GOqUBm0WeCXKxKNfowl6ZuZSIRh2JX%2FCybnQuoKRUzTb5WvuHBcNDlNfeQYr3doLg5tu4XLbuKLRvJurhn1cvOHPT9VZ9yU1BrIpDnX461ALGjHNsn2X7k8G3UFjCqrSdESf%2BupgB%2FFJL%2B67JkRneHMMKVXzgBJ1tsB72CQWXZ5oTzaqoaeTNLOWxk0lzepulLlovbmMm25dhnFDWn3DE0DZI3GB4iwYY&X-Amz-Signature=02affc5a08a7a3a444799107756e1adaa9ec55b801a6289615dffeabc5c236c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

