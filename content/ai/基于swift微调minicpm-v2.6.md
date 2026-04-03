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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYN5PW2%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEtEmeoCb9pwZnro8I5IiiFrh8%2FmJyVtc4wGq6Iv9dlQIhAJKFGc5TvvxYpEeJjVYUGIneY2foRguMC%2B0u5qKGf4%2BVKv8DCH8QABoMNjM3NDIzMTgzODA1IgzFe249nSKw0AOzr20q3AMb4FeP84oWPd3O91UvImQpDYCBgBuEjmm%2F%2FztBKMKEuxoaIIz0o831NkzaOF422uljdYvNem4NwC%2BzOWaBps6txh8cT6iS4AJWCNubcLHfZwO%2BAM3wxKxneHbGUQ4iSdJbJmZU6Ms%2F%2BVGN3BdbABdTDm9bp5IwuoIqs%2BdLua%2BxwYEIehApX8E1AbHTdhZZK17AEEHZEpnnSkF7FXXVK5EnxOVy1X5OtNMymNOf9i3BDpc1MS2HT0TuARJYdSBSiLUs553LDy8C5r3YyL3q2Wrvkh93gr9y2247WuaIskS5QUyS5zHeniBvZyYaHVryZKIgRqj%2Fe3mLnxjhsIL7N89MOtVN3zsRavq%2Fa%2BftvcEOiO3HBTCMVyh4os0UpzqOCj%2Fn1NazIOMu3GmjJQOoUp1lroScXxP%2BIfTqM%2FQPTGH%2BsiZSDmrT%2B9CQ%2B8bK%2BaCHuvmx6BGPY%2B48UzT%2B6FC6rgGrTHI%2FQwaJ1g4dYo94OHz6woY%2BUadXy9CnDf%2BLFQDWJQIV6f0NjduRhQdlwxhTCUFBB9TqUzjBzWiPf6qx0pln7aC0YbrA7tMZo5yCxNzSWTgsbQWQ2oZ%2B2BY5WYMZz%2FzpB2e3p6wP1c9tFk6mDAFMoy97fvH8W4KZkKP3CjCsrL3OBjqkAeYPSwBdXd59g8N%2B9n%2FEwSTrczNazhJyjfukhzeg6CYW4a4kUZOsTLuVgoyogJOt8fnCpovILcio03sFrdIPV5LEQc8INJ0f1HiekiNVI3iqMcWcs2mDCN0dscI%2BOMvQZBe4Z3zw2l5ynVmALJaJ5t0PN13J6lPmVEZ%2Fv65m5w85L4NcwjoGcQHQM%2FUwZkD0%2BkBuVwoQCC%2F3zk4RUihQfHgx%2B6kT&X-Amz-Signature=8b5f9bb9a79acec77626dc3e14e4d237c5423c562973f29a36f8c3a32e8e18ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYN5PW2%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEtEmeoCb9pwZnro8I5IiiFrh8%2FmJyVtc4wGq6Iv9dlQIhAJKFGc5TvvxYpEeJjVYUGIneY2foRguMC%2B0u5qKGf4%2BVKv8DCH8QABoMNjM3NDIzMTgzODA1IgzFe249nSKw0AOzr20q3AMb4FeP84oWPd3O91UvImQpDYCBgBuEjmm%2F%2FztBKMKEuxoaIIz0o831NkzaOF422uljdYvNem4NwC%2BzOWaBps6txh8cT6iS4AJWCNubcLHfZwO%2BAM3wxKxneHbGUQ4iSdJbJmZU6Ms%2F%2BVGN3BdbABdTDm9bp5IwuoIqs%2BdLua%2BxwYEIehApX8E1AbHTdhZZK17AEEHZEpnnSkF7FXXVK5EnxOVy1X5OtNMymNOf9i3BDpc1MS2HT0TuARJYdSBSiLUs553LDy8C5r3YyL3q2Wrvkh93gr9y2247WuaIskS5QUyS5zHeniBvZyYaHVryZKIgRqj%2Fe3mLnxjhsIL7N89MOtVN3zsRavq%2Fa%2BftvcEOiO3HBTCMVyh4os0UpzqOCj%2Fn1NazIOMu3GmjJQOoUp1lroScXxP%2BIfTqM%2FQPTGH%2BsiZSDmrT%2B9CQ%2B8bK%2BaCHuvmx6BGPY%2B48UzT%2B6FC6rgGrTHI%2FQwaJ1g4dYo94OHz6woY%2BUadXy9CnDf%2BLFQDWJQIV6f0NjduRhQdlwxhTCUFBB9TqUzjBzWiPf6qx0pln7aC0YbrA7tMZo5yCxNzSWTgsbQWQ2oZ%2B2BY5WYMZz%2FzpB2e3p6wP1c9tFk6mDAFMoy97fvH8W4KZkKP3CjCsrL3OBjqkAeYPSwBdXd59g8N%2B9n%2FEwSTrczNazhJyjfukhzeg6CYW4a4kUZOsTLuVgoyogJOt8fnCpovILcio03sFrdIPV5LEQc8INJ0f1HiekiNVI3iqMcWcs2mDCN0dscI%2BOMvQZBe4Z3zw2l5ynVmALJaJ5t0PN13J6lPmVEZ%2Fv65m5w85L4NcwjoGcQHQM%2FUwZkD0%2BkBuVwoQCC%2F3zk4RUihQfHgx%2B6kT&X-Amz-Signature=4ea5a39061f850d27c95eafb7d1425626b59fb7073eb1103c0c92039c056e5cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYN5PW2%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEtEmeoCb9pwZnro8I5IiiFrh8%2FmJyVtc4wGq6Iv9dlQIhAJKFGc5TvvxYpEeJjVYUGIneY2foRguMC%2B0u5qKGf4%2BVKv8DCH8QABoMNjM3NDIzMTgzODA1IgzFe249nSKw0AOzr20q3AMb4FeP84oWPd3O91UvImQpDYCBgBuEjmm%2F%2FztBKMKEuxoaIIz0o831NkzaOF422uljdYvNem4NwC%2BzOWaBps6txh8cT6iS4AJWCNubcLHfZwO%2BAM3wxKxneHbGUQ4iSdJbJmZU6Ms%2F%2BVGN3BdbABdTDm9bp5IwuoIqs%2BdLua%2BxwYEIehApX8E1AbHTdhZZK17AEEHZEpnnSkF7FXXVK5EnxOVy1X5OtNMymNOf9i3BDpc1MS2HT0TuARJYdSBSiLUs553LDy8C5r3YyL3q2Wrvkh93gr9y2247WuaIskS5QUyS5zHeniBvZyYaHVryZKIgRqj%2Fe3mLnxjhsIL7N89MOtVN3zsRavq%2Fa%2BftvcEOiO3HBTCMVyh4os0UpzqOCj%2Fn1NazIOMu3GmjJQOoUp1lroScXxP%2BIfTqM%2FQPTGH%2BsiZSDmrT%2B9CQ%2B8bK%2BaCHuvmx6BGPY%2B48UzT%2B6FC6rgGrTHI%2FQwaJ1g4dYo94OHz6woY%2BUadXy9CnDf%2BLFQDWJQIV6f0NjduRhQdlwxhTCUFBB9TqUzjBzWiPf6qx0pln7aC0YbrA7tMZo5yCxNzSWTgsbQWQ2oZ%2B2BY5WYMZz%2FzpB2e3p6wP1c9tFk6mDAFMoy97fvH8W4KZkKP3CjCsrL3OBjqkAeYPSwBdXd59g8N%2B9n%2FEwSTrczNazhJyjfukhzeg6CYW4a4kUZOsTLuVgoyogJOt8fnCpovILcio03sFrdIPV5LEQc8INJ0f1HiekiNVI3iqMcWcs2mDCN0dscI%2BOMvQZBe4Z3zw2l5ynVmALJaJ5t0PN13J6lPmVEZ%2Fv65m5w85L4NcwjoGcQHQM%2FUwZkD0%2BkBuVwoQCC%2F3zk4RUihQfHgx%2B6kT&X-Amz-Signature=b16bd38088a2da6161c4a26ca88ff37893662b6171ff42d93071502ecb72b4d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

