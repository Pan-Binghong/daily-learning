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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PFN6YI%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIF7nh7f8zTgowQm1en9D4aWT6G7Hn%2FVs1oiPDtBFpDPsAiEA3K5dC5wdw68oZrJEtL296zYzoZu2pSTEu6ZCI4PLKnMqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTb8xt8YvOVL%2BDVGircA9zKGC75BvJazqDkPWTTVc%2B7GSOL11J6RdhobV5%2BYTbkyjDB66xgJd6mnX0QBUPvoXWPovxkbtzwTFsjOv4Kd4IpwzFZc0FMhEuN%2FNodkie3bRWmg%2FtWM4BZ4AG%2FRqdkLC6TS8UGpf91c5pl7yLsI%2BNiS%2BHc8J%2BY3q5GDUqQeBOU5R8jS0%2FQ0%2BoZYu3oMVKC5V9vbcTHJBxhHHP4EjaDsT72oWV%2BHPlRoVxIc%2BtHzV2RLyUf%2FqTzhh0ykkcUJuziqatw7dX4ws5T1s7elB3qxyDr6gi5iCHKiHD9Z4SrgBYIjUC4AUk9RCGYAAIkTp7ksz1FZqD%2BerUu9ZgkPZsfdi7uq%2Fdnn3U4CMWdGAQ85VzXEYEpG9fq2%2BTzhJg%2B0mp6S2BLZVpNmLBVfBLsUVPb4hTml%2B%2F4Oxwq70nBz6Opz3mB6qlR4CHp8khw1tb441KJBl6g%2BEx%2FtTMdj0KVkbiOzMwxoROfk3mqiUHSJO7TgudKrnwqLYvlq5B7Hada7HWXQSho5ph%2FsV7ZAZtI8ieOiBx865Q4kXHcohj%2BrnRsHIPIowMnMeH2JCpoOZAN4PKiOdQBL20%2FPwzT%2BcLMen5I%2FSC2cl8fNV7P%2FwabFEKxKhuXOTXeKSPoIjm8P4AZMOO5hs8GOqUBWv69eXMVp6LjmQfetM1%2F5aTyBDO4ybXOAv5z5qzToekt63Ks2%2BdneqTXzm7oDO8B8Q2GSh%2BF4gs8wqq%2F7RR%2BB1laDi9PzQqYcnGj25NOxGCC4PKvR3%2FfMB%2FYeoTj2u0qlZqxITx0FimCD16DtZX9sVujZoFDzZbZbYSw1mS9mmVOlL6IIHdwTplKYDYyu781kz1rqDOmdyMFWcH0pCnNxQW8HCEr&X-Amz-Signature=a7e1c686c840088292fa24c5fe9958fa37f208be3a9a066dbf6a9dfb0aec4daa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PFN6YI%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIF7nh7f8zTgowQm1en9D4aWT6G7Hn%2FVs1oiPDtBFpDPsAiEA3K5dC5wdw68oZrJEtL296zYzoZu2pSTEu6ZCI4PLKnMqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTb8xt8YvOVL%2BDVGircA9zKGC75BvJazqDkPWTTVc%2B7GSOL11J6RdhobV5%2BYTbkyjDB66xgJd6mnX0QBUPvoXWPovxkbtzwTFsjOv4Kd4IpwzFZc0FMhEuN%2FNodkie3bRWmg%2FtWM4BZ4AG%2FRqdkLC6TS8UGpf91c5pl7yLsI%2BNiS%2BHc8J%2BY3q5GDUqQeBOU5R8jS0%2FQ0%2BoZYu3oMVKC5V9vbcTHJBxhHHP4EjaDsT72oWV%2BHPlRoVxIc%2BtHzV2RLyUf%2FqTzhh0ykkcUJuziqatw7dX4ws5T1s7elB3qxyDr6gi5iCHKiHD9Z4SrgBYIjUC4AUk9RCGYAAIkTp7ksz1FZqD%2BerUu9ZgkPZsfdi7uq%2Fdnn3U4CMWdGAQ85VzXEYEpG9fq2%2BTzhJg%2B0mp6S2BLZVpNmLBVfBLsUVPb4hTml%2B%2F4Oxwq70nBz6Opz3mB6qlR4CHp8khw1tb441KJBl6g%2BEx%2FtTMdj0KVkbiOzMwxoROfk3mqiUHSJO7TgudKrnwqLYvlq5B7Hada7HWXQSho5ph%2FsV7ZAZtI8ieOiBx865Q4kXHcohj%2BrnRsHIPIowMnMeH2JCpoOZAN4PKiOdQBL20%2FPwzT%2BcLMen5I%2FSC2cl8fNV7P%2FwabFEKxKhuXOTXeKSPoIjm8P4AZMOO5hs8GOqUBWv69eXMVp6LjmQfetM1%2F5aTyBDO4ybXOAv5z5qzToekt63Ks2%2BdneqTXzm7oDO8B8Q2GSh%2BF4gs8wqq%2F7RR%2BB1laDi9PzQqYcnGj25NOxGCC4PKvR3%2FfMB%2FYeoTj2u0qlZqxITx0FimCD16DtZX9sVujZoFDzZbZbYSw1mS9mmVOlL6IIHdwTplKYDYyu781kz1rqDOmdyMFWcH0pCnNxQW8HCEr&X-Amz-Signature=73ea585c0bed4c4548a218786f961a164aa9d1d438daf9750f7efd1f2596d9f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645PFN6YI%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIF7nh7f8zTgowQm1en9D4aWT6G7Hn%2FVs1oiPDtBFpDPsAiEA3K5dC5wdw68oZrJEtL296zYzoZu2pSTEu6ZCI4PLKnMqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGTb8xt8YvOVL%2BDVGircA9zKGC75BvJazqDkPWTTVc%2B7GSOL11J6RdhobV5%2BYTbkyjDB66xgJd6mnX0QBUPvoXWPovxkbtzwTFsjOv4Kd4IpwzFZc0FMhEuN%2FNodkie3bRWmg%2FtWM4BZ4AG%2FRqdkLC6TS8UGpf91c5pl7yLsI%2BNiS%2BHc8J%2BY3q5GDUqQeBOU5R8jS0%2FQ0%2BoZYu3oMVKC5V9vbcTHJBxhHHP4EjaDsT72oWV%2BHPlRoVxIc%2BtHzV2RLyUf%2FqTzhh0ykkcUJuziqatw7dX4ws5T1s7elB3qxyDr6gi5iCHKiHD9Z4SrgBYIjUC4AUk9RCGYAAIkTp7ksz1FZqD%2BerUu9ZgkPZsfdi7uq%2Fdnn3U4CMWdGAQ85VzXEYEpG9fq2%2BTzhJg%2B0mp6S2BLZVpNmLBVfBLsUVPb4hTml%2B%2F4Oxwq70nBz6Opz3mB6qlR4CHp8khw1tb441KJBl6g%2BEx%2FtTMdj0KVkbiOzMwxoROfk3mqiUHSJO7TgudKrnwqLYvlq5B7Hada7HWXQSho5ph%2FsV7ZAZtI8ieOiBx865Q4kXHcohj%2BrnRsHIPIowMnMeH2JCpoOZAN4PKiOdQBL20%2FPwzT%2BcLMen5I%2FSC2cl8fNV7P%2FwabFEKxKhuXOTXeKSPoIjm8P4AZMOO5hs8GOqUBWv69eXMVp6LjmQfetM1%2F5aTyBDO4ybXOAv5z5qzToekt63Ks2%2BdneqTXzm7oDO8B8Q2GSh%2BF4gs8wqq%2F7RR%2BB1laDi9PzQqYcnGj25NOxGCC4PKvR3%2FfMB%2FYeoTj2u0qlZqxITx0FimCD16DtZX9sVujZoFDzZbZbYSw1mS9mmVOlL6IIHdwTplKYDYyu781kz1rqDOmdyMFWcH0pCnNxQW8HCEr&X-Amz-Signature=ea24d6c117429e0c444056e1efd910d37779b99a62502c90838eeb8cf8e45800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

