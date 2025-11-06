---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUHNH6N7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8vsBYxuiC%2FVxLj50EcDZN3F634gSGXkzoxMQVWgJCmAiAWC%2F%2Fc8qbUVMZzXgbYQNp2hQCIYSH%2BTuLnqC1ApUxvSyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08CJDXrAft6vxo%2BXKtwDB2z%2Bli2iX82zrTRLN16CY3ouNm%2Fsm%2F3aErTuR4J2x2u5YWbt7j4RTsfNGHe01%2BFHMudXplF09hZemmWmeyn7iOM%2B3AIK1VVTPWz4%2FaMnKJBLfIL1WYhd%2Fi0nzwUZ3C7wMMz6uUxHleKHsc%2FJzUA8%2BglNlQqdKChZnEl25bzJDpfjVOfeNZraF6K3AIKiySh4qPmWOAzGUnb7NMghhZAPEqya94PUzLp%2F3LPZvatLxVcochy6f2jrk64F5Fvwba9royH%2BEjtoRRm83Qxh%2Bmna1D2fpFsOP2ulLJ4VSvJXKxYKz3wqEhMsDdIAK0GwWYOdh%2B3j70foeS6XwQ15QnCU4Yqi9rAbHuqLxRYofRSLPL1PmQCzlYkgGPJXiallnWty3jcYLoTrnPtTI4tBpYyK9Mb5vvO68aLKidYZ8ZxqQv%2F07JNyamBpQjYMcSiox6hrhE20c2urvsMYlFAxz0Rac82ARaxpzGdhRzGq3WC1eLBz7CmHDl93JFq7g65jHxLeUx8ydY%2BRAUGVox3Me3aC7l%2BAm2RzKP3emoXI5H8AQj6jYF9a%2FjpySC3kiiIGLcIeyQlA1ZWLz0Kc2nMxcuOdH4kNqXBs6GYeuswg0v%2B6kF3HOytXyRWPCEbfHpkwjvKvyAY6pgGRQZq2UthWPKIXsSnwzyJSkulceWhQcwAaUAObGGUJHYZEXUNC%2B0PbDrwx6luqmLohfgKbHeeXP%2FVcN53PqoIKtjweOyzK8pcEpE35MecYdZ6MT8zjclgtfTqmzxDmO9cMIYBrQXKkP2wnqs2hKT6qmW1NqM1UvSWekhSfdTCHmvYCwP5BMXLNGz3GLu954H07eHee67E7WKr0qXvRCjD3i0uhvc5F&X-Amz-Signature=a52f1aad62b625c824fef52f3576ae4c2ac02c4dcd0e74c188488f0983013658&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUHNH6N7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8vsBYxuiC%2FVxLj50EcDZN3F634gSGXkzoxMQVWgJCmAiAWC%2F%2Fc8qbUVMZzXgbYQNp2hQCIYSH%2BTuLnqC1ApUxvSyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08CJDXrAft6vxo%2BXKtwDB2z%2Bli2iX82zrTRLN16CY3ouNm%2Fsm%2F3aErTuR4J2x2u5YWbt7j4RTsfNGHe01%2BFHMudXplF09hZemmWmeyn7iOM%2B3AIK1VVTPWz4%2FaMnKJBLfIL1WYhd%2Fi0nzwUZ3C7wMMz6uUxHleKHsc%2FJzUA8%2BglNlQqdKChZnEl25bzJDpfjVOfeNZraF6K3AIKiySh4qPmWOAzGUnb7NMghhZAPEqya94PUzLp%2F3LPZvatLxVcochy6f2jrk64F5Fvwba9royH%2BEjtoRRm83Qxh%2Bmna1D2fpFsOP2ulLJ4VSvJXKxYKz3wqEhMsDdIAK0GwWYOdh%2B3j70foeS6XwQ15QnCU4Yqi9rAbHuqLxRYofRSLPL1PmQCzlYkgGPJXiallnWty3jcYLoTrnPtTI4tBpYyK9Mb5vvO68aLKidYZ8ZxqQv%2F07JNyamBpQjYMcSiox6hrhE20c2urvsMYlFAxz0Rac82ARaxpzGdhRzGq3WC1eLBz7CmHDl93JFq7g65jHxLeUx8ydY%2BRAUGVox3Me3aC7l%2BAm2RzKP3emoXI5H8AQj6jYF9a%2FjpySC3kiiIGLcIeyQlA1ZWLz0Kc2nMxcuOdH4kNqXBs6GYeuswg0v%2B6kF3HOytXyRWPCEbfHpkwjvKvyAY6pgGRQZq2UthWPKIXsSnwzyJSkulceWhQcwAaUAObGGUJHYZEXUNC%2B0PbDrwx6luqmLohfgKbHeeXP%2FVcN53PqoIKtjweOyzK8pcEpE35MecYdZ6MT8zjclgtfTqmzxDmO9cMIYBrQXKkP2wnqs2hKT6qmW1NqM1UvSWekhSfdTCHmvYCwP5BMXLNGz3GLu954H07eHee67E7WKr0qXvRCjD3i0uhvc5F&X-Amz-Signature=005197225bf5ca4f37630475aec0072f3cbb160532cbdbcba7ad3f28485bf692&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

