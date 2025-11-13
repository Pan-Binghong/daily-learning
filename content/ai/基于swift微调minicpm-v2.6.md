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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QQ7ZQJG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICRuqDaVudkDo%2BtlSh%2FGp1Kb2CIDOziGrZ%2BY71907u%2F1AiALow71uhTIRroD6Bpjgh3wo%2F2Mqi8FebO5zE0SIv3Bzyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMVjjfzD%2BuK3VUltv1KtwDnWh8GzeVZTH%2FV6y%2BTfGk26ZKE6PMR5o1KXgUsiwtPL341ohYn%2FxxmYqJ5Tp6srmguj7vd3GVc%2FVlBeE4LpW36dwtIkwrD1Sqtje0jbUra3qkWE5Fe83KJ35PygoD18fWHNE4SzJhBqEN0yHMJb3tWZf4vKnurHrRVqruHihhVzCl7k4oZ2x%2B8pwEn9QQ%2F%2FQZIy1PeGWNhZQIcVz6wofmKU9bXSoSZbSDEr8RlJKQFZtrfYUKw0O2DarTgKqxbGPkdk7RreqEhZy2EiLCN%2F6UY2rwsDhzsKo96%2Ff0Q0uj3zwxfPGW%2F7FNmWN0jdSchgclKyon1UD6uFSOh3v8%2Bd3FU7tGHOpQrdCAF0Wo9qVpKQddAJ7xvw2SZeBEp03YTmG9Lxz9ZG9zKVJkG1f20V62uVNjt8LMGIsXxeExY0rK8%2FRZw%2F%2B%2BYkq3OrlFwjoGjy0bW6ssGfEWwit5eQxX5Gt9Q6CEU7WtvIYFwLaDFGZ2%2F%2B6pjJzvf%2FBf1mzw0a1IwmMNChzCLmvnh9s06IW6KWrxxFbuUtlCWmjcpq57iy%2BUcWqRxtPWsjqwjAQPS%2FofGKFHKZONttYWLbYtSWrpYqtiYg7rqJQ%2BV%2F2USUUtiyVmQf7PzLk5BcmsO6gnOcYwy%2FLUyAY6pgEE0y7e3HH0sSH0SKga%2B7Vi0NfkckYfx0Pt2GzErDfQKiCsin5hq%2Br1IltY2g3AiJ3WKGycGaNKR%2BAbePRSZKP9bg2wl3MH8QtowRHXistZKX%2BwA5OlfxQtZ5iSgVouK2LoYtvoP%2FesXL6kPh4akB7O4qDktj2WH%2BlGc%2BjB%2B5Z8ezUT2Whrz1%2BFaotItwSmWxhp1zp%2BEZg9wu6DZTfAI43Y%2B4JhPpRN&X-Amz-Signature=ad5c3760f27b27eb6cc1275809f3cc68c0024e7e6a2e7bbbac33736a37a9eeb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QQ7ZQJG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICRuqDaVudkDo%2BtlSh%2FGp1Kb2CIDOziGrZ%2BY71907u%2F1AiALow71uhTIRroD6Bpjgh3wo%2F2Mqi8FebO5zE0SIv3Bzyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMVjjfzD%2BuK3VUltv1KtwDnWh8GzeVZTH%2FV6y%2BTfGk26ZKE6PMR5o1KXgUsiwtPL341ohYn%2FxxmYqJ5Tp6srmguj7vd3GVc%2FVlBeE4LpW36dwtIkwrD1Sqtje0jbUra3qkWE5Fe83KJ35PygoD18fWHNE4SzJhBqEN0yHMJb3tWZf4vKnurHrRVqruHihhVzCl7k4oZ2x%2B8pwEn9QQ%2F%2FQZIy1PeGWNhZQIcVz6wofmKU9bXSoSZbSDEr8RlJKQFZtrfYUKw0O2DarTgKqxbGPkdk7RreqEhZy2EiLCN%2F6UY2rwsDhzsKo96%2Ff0Q0uj3zwxfPGW%2F7FNmWN0jdSchgclKyon1UD6uFSOh3v8%2Bd3FU7tGHOpQrdCAF0Wo9qVpKQddAJ7xvw2SZeBEp03YTmG9Lxz9ZG9zKVJkG1f20V62uVNjt8LMGIsXxeExY0rK8%2FRZw%2F%2B%2BYkq3OrlFwjoGjy0bW6ssGfEWwit5eQxX5Gt9Q6CEU7WtvIYFwLaDFGZ2%2F%2B6pjJzvf%2FBf1mzw0a1IwmMNChzCLmvnh9s06IW6KWrxxFbuUtlCWmjcpq57iy%2BUcWqRxtPWsjqwjAQPS%2FofGKFHKZONttYWLbYtSWrpYqtiYg7rqJQ%2BV%2F2USUUtiyVmQf7PzLk5BcmsO6gnOcYwy%2FLUyAY6pgEE0y7e3HH0sSH0SKga%2B7Vi0NfkckYfx0Pt2GzErDfQKiCsin5hq%2Br1IltY2g3AiJ3WKGycGaNKR%2BAbePRSZKP9bg2wl3MH8QtowRHXistZKX%2BwA5OlfxQtZ5iSgVouK2LoYtvoP%2FesXL6kPh4akB7O4qDktj2WH%2BlGc%2BjB%2B5Z8ezUT2Whrz1%2BFaotItwSmWxhp1zp%2BEZg9wu6DZTfAI43Y%2B4JhPpRN&X-Amz-Signature=f2f1c71ed1e3749d109fe5c28b7a71eba3bc328e596f944375dd55869e6e5864&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QQ7ZQJG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCICRuqDaVudkDo%2BtlSh%2FGp1Kb2CIDOziGrZ%2BY71907u%2F1AiALow71uhTIRroD6Bpjgh3wo%2F2Mqi8FebO5zE0SIv3Bzyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMVjjfzD%2BuK3VUltv1KtwDnWh8GzeVZTH%2FV6y%2BTfGk26ZKE6PMR5o1KXgUsiwtPL341ohYn%2FxxmYqJ5Tp6srmguj7vd3GVc%2FVlBeE4LpW36dwtIkwrD1Sqtje0jbUra3qkWE5Fe83KJ35PygoD18fWHNE4SzJhBqEN0yHMJb3tWZf4vKnurHrRVqruHihhVzCl7k4oZ2x%2B8pwEn9QQ%2F%2FQZIy1PeGWNhZQIcVz6wofmKU9bXSoSZbSDEr8RlJKQFZtrfYUKw0O2DarTgKqxbGPkdk7RreqEhZy2EiLCN%2F6UY2rwsDhzsKo96%2Ff0Q0uj3zwxfPGW%2F7FNmWN0jdSchgclKyon1UD6uFSOh3v8%2Bd3FU7tGHOpQrdCAF0Wo9qVpKQddAJ7xvw2SZeBEp03YTmG9Lxz9ZG9zKVJkG1f20V62uVNjt8LMGIsXxeExY0rK8%2FRZw%2F%2B%2BYkq3OrlFwjoGjy0bW6ssGfEWwit5eQxX5Gt9Q6CEU7WtvIYFwLaDFGZ2%2F%2B6pjJzvf%2FBf1mzw0a1IwmMNChzCLmvnh9s06IW6KWrxxFbuUtlCWmjcpq57iy%2BUcWqRxtPWsjqwjAQPS%2FofGKFHKZONttYWLbYtSWrpYqtiYg7rqJQ%2BV%2F2USUUtiyVmQf7PzLk5BcmsO6gnOcYwy%2FLUyAY6pgEE0y7e3HH0sSH0SKga%2B7Vi0NfkckYfx0Pt2GzErDfQKiCsin5hq%2Br1IltY2g3AiJ3WKGycGaNKR%2BAbePRSZKP9bg2wl3MH8QtowRHXistZKX%2BwA5OlfxQtZ5iSgVouK2LoYtvoP%2FesXL6kPh4akB7O4qDktj2WH%2BlGc%2BjB%2B5Z8ezUT2Whrz1%2BFaotItwSmWxhp1zp%2BEZg9wu6DZTfAI43Y%2B4JhPpRN&X-Amz-Signature=3f9b73b2fb038af7c54fb2b20acf788a85d43a048bae48789bff9d9bc9942a54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

