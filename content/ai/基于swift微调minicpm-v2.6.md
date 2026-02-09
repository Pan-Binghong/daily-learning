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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VLHGQL%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8%2FJNCe%2FJS%2B6hwvfxl2zy6wAW0iHNZDKnmi%2FPF5269RAiBl6szhBtDd1guLNUGws6X7iHCi21K6Lx5Suc4D8IVpcCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ5RQwy9Ll%2FS1uz9cKtwD8T%2BjMUvQZd4KLQfBBfrZeHrKUorT0xP%2FhBYBAKeBJ3xkQrld5nmwts281DtkovFTrpErzrpV%2FMt6P8y3WvCnVquA7mnfF%2FCESXdKweybVZAHN16RhWwZQMVgmX0XPcCMSR6ZJ%2FOWVGCt0%2F%2BDGeqNzu5CqxfjqnDVY7AIYJHS387a3D1NRzg1T0UdQCkneXrPVv0iwCPBuu0Z9Wh702rjUWAKcs6YgKJv5k%2FN0koZH8hRBukcjj9TfDpzM%2BKWBITNKzP2olbnciM4sQwbtwCNgTJhXHp9JRSOdeXDJcat2Nxy4Z1P7XlwFW4lHluH1UCiiyXBB7BUCfApq24enNHuvqtvjS4cPp0f3VndSlV%2FYtEEkN7TDwn6H8lJa30mawsXMcawRZq46Bstlxo96pvAhOPG%2FxGPBfhiBDW1kLdGt1dVOAlx4HUfwO1%2Bw9UdsRwggTnelpjqv97tUsHII2dsOZySb3cRcsoBMWs1tDPJcdkPbjMfY59u%2BN%2F1WZVYnWT0lwtYuS1KSyM2SLX6sSy7THPB7jzl5%2F73C6kYKv9fhwkU426QLTfxkb6r%2FmVHfwNhzjfu3%2BP%2B%2FOIbOgAjQ8msIdJhM1usvA1m0JMePSVQiT6P4P%2FWXhNkKQWa6QUwjZalzAY6pgEplMQq91ElgGVfvk8VPqt%2BJLb5WUA%2FtfeJleQkqZjsM4NEiSJRTpI5Fts%2Bli471uawVaZtZcT2cQU3rtb14Wta2%2FnMHNH6Z0ubqfJF%2FiN8TNNEnHcCWJfU8XRF18dxqLzPHFNHlDGL7GJiKadeTQwcc0YvL9FTQOoxGd%2B9sxdhzCMBwB7IBBIF8%2FAe1cfsZ%2FyGnMuzLwXBr%2FSPLK5qZGc6cHAKYTjH&X-Amz-Signature=dacbd647c474d1e3379844a2f04fde999eb4b9b7e71bf68dc3618d6dbe39f6fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VLHGQL%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8%2FJNCe%2FJS%2B6hwvfxl2zy6wAW0iHNZDKnmi%2FPF5269RAiBl6szhBtDd1guLNUGws6X7iHCi21K6Lx5Suc4D8IVpcCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ5RQwy9Ll%2FS1uz9cKtwD8T%2BjMUvQZd4KLQfBBfrZeHrKUorT0xP%2FhBYBAKeBJ3xkQrld5nmwts281DtkovFTrpErzrpV%2FMt6P8y3WvCnVquA7mnfF%2FCESXdKweybVZAHN16RhWwZQMVgmX0XPcCMSR6ZJ%2FOWVGCt0%2F%2BDGeqNzu5CqxfjqnDVY7AIYJHS387a3D1NRzg1T0UdQCkneXrPVv0iwCPBuu0Z9Wh702rjUWAKcs6YgKJv5k%2FN0koZH8hRBukcjj9TfDpzM%2BKWBITNKzP2olbnciM4sQwbtwCNgTJhXHp9JRSOdeXDJcat2Nxy4Z1P7XlwFW4lHluH1UCiiyXBB7BUCfApq24enNHuvqtvjS4cPp0f3VndSlV%2FYtEEkN7TDwn6H8lJa30mawsXMcawRZq46Bstlxo96pvAhOPG%2FxGPBfhiBDW1kLdGt1dVOAlx4HUfwO1%2Bw9UdsRwggTnelpjqv97tUsHII2dsOZySb3cRcsoBMWs1tDPJcdkPbjMfY59u%2BN%2F1WZVYnWT0lwtYuS1KSyM2SLX6sSy7THPB7jzl5%2F73C6kYKv9fhwkU426QLTfxkb6r%2FmVHfwNhzjfu3%2BP%2B%2FOIbOgAjQ8msIdJhM1usvA1m0JMePSVQiT6P4P%2FWXhNkKQWa6QUwjZalzAY6pgEplMQq91ElgGVfvk8VPqt%2BJLb5WUA%2FtfeJleQkqZjsM4NEiSJRTpI5Fts%2Bli471uawVaZtZcT2cQU3rtb14Wta2%2FnMHNH6Z0ubqfJF%2FiN8TNNEnHcCWJfU8XRF18dxqLzPHFNHlDGL7GJiKadeTQwcc0YvL9FTQOoxGd%2B9sxdhzCMBwB7IBBIF8%2FAe1cfsZ%2FyGnMuzLwXBr%2FSPLK5qZGc6cHAKYTjH&X-Amz-Signature=16688cc3b22fc339e7d4f849dae012c23a089e0516822661c1364493184593ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3VLHGQL%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8%2FJNCe%2FJS%2B6hwvfxl2zy6wAW0iHNZDKnmi%2FPF5269RAiBl6szhBtDd1guLNUGws6X7iHCi21K6Lx5Suc4D8IVpcCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJ5RQwy9Ll%2FS1uz9cKtwD8T%2BjMUvQZd4KLQfBBfrZeHrKUorT0xP%2FhBYBAKeBJ3xkQrld5nmwts281DtkovFTrpErzrpV%2FMt6P8y3WvCnVquA7mnfF%2FCESXdKweybVZAHN16RhWwZQMVgmX0XPcCMSR6ZJ%2FOWVGCt0%2F%2BDGeqNzu5CqxfjqnDVY7AIYJHS387a3D1NRzg1T0UdQCkneXrPVv0iwCPBuu0Z9Wh702rjUWAKcs6YgKJv5k%2FN0koZH8hRBukcjj9TfDpzM%2BKWBITNKzP2olbnciM4sQwbtwCNgTJhXHp9JRSOdeXDJcat2Nxy4Z1P7XlwFW4lHluH1UCiiyXBB7BUCfApq24enNHuvqtvjS4cPp0f3VndSlV%2FYtEEkN7TDwn6H8lJa30mawsXMcawRZq46Bstlxo96pvAhOPG%2FxGPBfhiBDW1kLdGt1dVOAlx4HUfwO1%2Bw9UdsRwggTnelpjqv97tUsHII2dsOZySb3cRcsoBMWs1tDPJcdkPbjMfY59u%2BN%2F1WZVYnWT0lwtYuS1KSyM2SLX6sSy7THPB7jzl5%2F73C6kYKv9fhwkU426QLTfxkb6r%2FmVHfwNhzjfu3%2BP%2B%2FOIbOgAjQ8msIdJhM1usvA1m0JMePSVQiT6P4P%2FWXhNkKQWa6QUwjZalzAY6pgEplMQq91ElgGVfvk8VPqt%2BJLb5WUA%2FtfeJleQkqZjsM4NEiSJRTpI5Fts%2Bli471uawVaZtZcT2cQU3rtb14Wta2%2FnMHNH6Z0ubqfJF%2FiN8TNNEnHcCWJfU8XRF18dxqLzPHFNHlDGL7GJiKadeTQwcc0YvL9FTQOoxGd%2B9sxdhzCMBwB7IBBIF8%2FAe1cfsZ%2FyGnMuzLwXBr%2FSPLK5qZGc6cHAKYTjH&X-Amz-Signature=5c8896b985260f004555df4a0e31c640290947b138cad891a19c82817979fe53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

