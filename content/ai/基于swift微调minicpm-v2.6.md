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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ABONEC%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIB8FJ4m%2F7aaIKxuohaIcky2%2BPQGmbLcHPdJi6Y%2F%2FQD3PAiAqGU3LF8gXX%2FceRS%2FQi3cra8CJMyZNrJhwgM8YTC7vXir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMacMYS8wPKc0TdiYrKtwDjtTyrGwmvKoI4ngU72QcYOMPki9LGGdImdGKoW%2FcZFWDKeOXCKcSHEvLAij0jfJx%2FtSSC1ifccWUDvBm4bAjvR%2F%2FI%2BNCItkljnGxEYaGcAU5Rhk71WtsxXWTfldMFCrDReWtjCqIOzFuLCN3sIwGbh%2BYnnByTrVGP3JsWZp4t59MsbRe3zPHb%2Bi0qD01zUJy%2FjhfVDzBNnO3bf8%2F8VT4zfi6DiJz%2Bk9cbnEa54vXm%2FZ5rsDRoKtM%2F35k8vKnamIW1GfsizgB3inFyATsPZRcivymfTXwZfDRQ8%2Be%2Fktj4dVS1hcBWYUzVWyO0sC9dfzrgHpa%2Bal8Rq82nHjVToCi3W7IxZ%2F3GK6coXyN1PCER4n0%2FMCIfzKv6342Rv0b5fpe2Q3wJ8cmItQoFucJYQZX1NxFANnFUIOZsUvSDGvRP3C1PcedQYlavBqFwrVHRSQ1I2fLZ7gMAsFUNQLFgvqj6V6%2Fypj7utOdp8Ts55hJCLfq9NXtTDNxU6faEGnPdciL9eGC%2B71X8RoEx5Fb3P%2B3UY0P8xYxU46m6LzvkxQUJBa2q9G8g%2FmWdhtdRF%2FIrzvbIF67uT1DUmlzoMaHgNNcCJIV8VIcn6YPuwr3JNJC%2FkdzHJmDVpSYrOWNn7kwz7DaywY6pgExvGgC3CL%2BdcAMcXVuEfuskTf1ZpMOAeeegZm0MvmMwaQ%2Fd8hi%2Feex93WiJRVnePnqz%2BpxhnM4s4FEtDjKB7sqoSS1ELG3bLpSTb2gNY8atTrIk9AL9fcsPrsZnnHgvuSWN4pfy%2F%2FUvvHip9lp6s2YoRRQNVGRdinlNqfZERlNY%2FFGrvjHFhImKZmcsk8qi%2BhXr4w2jzKjj6G5gCEIH48vqOfj%2BJoc&X-Amz-Signature=97ac49699a2814c179cf37e345c744c7d352c5097d220422814088ba9b419eaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ABONEC%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIB8FJ4m%2F7aaIKxuohaIcky2%2BPQGmbLcHPdJi6Y%2F%2FQD3PAiAqGU3LF8gXX%2FceRS%2FQi3cra8CJMyZNrJhwgM8YTC7vXir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMacMYS8wPKc0TdiYrKtwDjtTyrGwmvKoI4ngU72QcYOMPki9LGGdImdGKoW%2FcZFWDKeOXCKcSHEvLAij0jfJx%2FtSSC1ifccWUDvBm4bAjvR%2F%2FI%2BNCItkljnGxEYaGcAU5Rhk71WtsxXWTfldMFCrDReWtjCqIOzFuLCN3sIwGbh%2BYnnByTrVGP3JsWZp4t59MsbRe3zPHb%2Bi0qD01zUJy%2FjhfVDzBNnO3bf8%2F8VT4zfi6DiJz%2Bk9cbnEa54vXm%2FZ5rsDRoKtM%2F35k8vKnamIW1GfsizgB3inFyATsPZRcivymfTXwZfDRQ8%2Be%2Fktj4dVS1hcBWYUzVWyO0sC9dfzrgHpa%2Bal8Rq82nHjVToCi3W7IxZ%2F3GK6coXyN1PCER4n0%2FMCIfzKv6342Rv0b5fpe2Q3wJ8cmItQoFucJYQZX1NxFANnFUIOZsUvSDGvRP3C1PcedQYlavBqFwrVHRSQ1I2fLZ7gMAsFUNQLFgvqj6V6%2Fypj7utOdp8Ts55hJCLfq9NXtTDNxU6faEGnPdciL9eGC%2B71X8RoEx5Fb3P%2B3UY0P8xYxU46m6LzvkxQUJBa2q9G8g%2FmWdhtdRF%2FIrzvbIF67uT1DUmlzoMaHgNNcCJIV8VIcn6YPuwr3JNJC%2FkdzHJmDVpSYrOWNn7kwz7DaywY6pgExvGgC3CL%2BdcAMcXVuEfuskTf1ZpMOAeeegZm0MvmMwaQ%2Fd8hi%2Feex93WiJRVnePnqz%2BpxhnM4s4FEtDjKB7sqoSS1ELG3bLpSTb2gNY8atTrIk9AL9fcsPrsZnnHgvuSWN4pfy%2F%2FUvvHip9lp6s2YoRRQNVGRdinlNqfZERlNY%2FFGrvjHFhImKZmcsk8qi%2BhXr4w2jzKjj6G5gCEIH48vqOfj%2BJoc&X-Amz-Signature=1d08b2842e16518d46f8a30cf48f3994b5cc19cee0387ae15564410a226c9f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633ABONEC%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIB8FJ4m%2F7aaIKxuohaIcky2%2BPQGmbLcHPdJi6Y%2F%2FQD3PAiAqGU3LF8gXX%2FceRS%2FQi3cra8CJMyZNrJhwgM8YTC7vXir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMacMYS8wPKc0TdiYrKtwDjtTyrGwmvKoI4ngU72QcYOMPki9LGGdImdGKoW%2FcZFWDKeOXCKcSHEvLAij0jfJx%2FtSSC1ifccWUDvBm4bAjvR%2F%2FI%2BNCItkljnGxEYaGcAU5Rhk71WtsxXWTfldMFCrDReWtjCqIOzFuLCN3sIwGbh%2BYnnByTrVGP3JsWZp4t59MsbRe3zPHb%2Bi0qD01zUJy%2FjhfVDzBNnO3bf8%2F8VT4zfi6DiJz%2Bk9cbnEa54vXm%2FZ5rsDRoKtM%2F35k8vKnamIW1GfsizgB3inFyATsPZRcivymfTXwZfDRQ8%2Be%2Fktj4dVS1hcBWYUzVWyO0sC9dfzrgHpa%2Bal8Rq82nHjVToCi3W7IxZ%2F3GK6coXyN1PCER4n0%2FMCIfzKv6342Rv0b5fpe2Q3wJ8cmItQoFucJYQZX1NxFANnFUIOZsUvSDGvRP3C1PcedQYlavBqFwrVHRSQ1I2fLZ7gMAsFUNQLFgvqj6V6%2Fypj7utOdp8Ts55hJCLfq9NXtTDNxU6faEGnPdciL9eGC%2B71X8RoEx5Fb3P%2B3UY0P8xYxU46m6LzvkxQUJBa2q9G8g%2FmWdhtdRF%2FIrzvbIF67uT1DUmlzoMaHgNNcCJIV8VIcn6YPuwr3JNJC%2FkdzHJmDVpSYrOWNn7kwz7DaywY6pgExvGgC3CL%2BdcAMcXVuEfuskTf1ZpMOAeeegZm0MvmMwaQ%2Fd8hi%2Feex93WiJRVnePnqz%2BpxhnM4s4FEtDjKB7sqoSS1ELG3bLpSTb2gNY8atTrIk9AL9fcsPrsZnnHgvuSWN4pfy%2F%2FUvvHip9lp6s2YoRRQNVGRdinlNqfZERlNY%2FFGrvjHFhImKZmcsk8qi%2BhXr4w2jzKjj6G5gCEIH48vqOfj%2BJoc&X-Amz-Signature=0c1118ab198f023551d29caf748bfc6508a97291c533252e20798d7460ae49e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

