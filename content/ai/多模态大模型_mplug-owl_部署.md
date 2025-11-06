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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672G3CKT5%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHzEQ%2FXW1We%2Bhyfmk5ebrrGOG4KW55DZ%2BADbKsMHsum4CIHF%2BL1B7EX0yneW%2BAMCARMTIKf6ODHGWREv5aODbbvUYKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzI4vbeAncOd%2FNHZZYq3AMGNshbZg1rERBSfgZkOzzouuRkhWE1zzKfg9GX0Ow3f6ZYIsO%2FzFRD2F%2By6ZAo67LQYOJ5IQV%2BgzVoVCxF3dRmuY6VhmhMcsZ0oysn7FfaUCnsfVbD%2FluR7e1NhcMZI8BH7xXcItKe8QGlXhJx6w7dm%2BrLSqkFTXy3mTJPJg1QYnyCJhrU3AbYkobnNI%2Bi0AuaHG1eAt7LkD2Xx1xrsvZb1CiSA%2FAFqGtRZGLfRTg8eDChEqsjBqr2iUgyA8O9HrzDb2FE9oZVz8rJMDNhv1ZuzT7%2Fmd7NjbGbi3sW7oCXxcCEp6IsjJwJvUy%2BhSHdK84BUvpCfzzq2FNbCOIo1sjbS6nbFWEfVxK1hwb8FA8HGTidu0skmFJLl3NNqLja1WCLfCyMw7bDq%2BR%2F8gix%2Bh26ePynU1fBQUQvCrbIvQrlVxXx9csVNSQdbVaDtaxNcgircC69d7Nb7XWJvuh0v83UeK0U7NWJYhb63908wXgZ%2Bj2zBdVFhyioBgIimYr0Oo30x2mPkQkoof90VyXs9ZZAdcX0HXYnApmJCW9Heu2FsqBS6176MmRaTJh8ykbtKk5lv7l7%2FRcpQoFBnZ3awX%2FKxdU%2B4rWRxA7xPNwlmimFLIOZGawyzw3QIlcIUTC88K%2FIBjqnAcyEEOrIVY4qyB6Lob6jUmF0EDYkgEcYk2vbs48Iyr21WtOwN5MU3wR2V%2Bv6r%2BzwofHB4NHJgUHzyUzuElMKVB0F3JqT2M9qUSjKz0r8tsDtYIuxZiuP3mmPchB%2BFRRBsxmOc3hCZz77BRgATYOcJ936a06q4mmth%2BFu6t8F8VZDCwvjq1oF6R4H%2F7c7avkgQK0ywjiOq%2FCfNCZMQKYa4bacjXS4NnDU&X-Amz-Signature=6f2b5e89ff32ea3b17b8f63405784f4283d42f785443c8d09a5ad35e848a8af8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672G3CKT5%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCHzEQ%2FXW1We%2Bhyfmk5ebrrGOG4KW55DZ%2BADbKsMHsum4CIHF%2BL1B7EX0yneW%2BAMCARMTIKf6ODHGWREv5aODbbvUYKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzI4vbeAncOd%2FNHZZYq3AMGNshbZg1rERBSfgZkOzzouuRkhWE1zzKfg9GX0Ow3f6ZYIsO%2FzFRD2F%2By6ZAo67LQYOJ5IQV%2BgzVoVCxF3dRmuY6VhmhMcsZ0oysn7FfaUCnsfVbD%2FluR7e1NhcMZI8BH7xXcItKe8QGlXhJx6w7dm%2BrLSqkFTXy3mTJPJg1QYnyCJhrU3AbYkobnNI%2Bi0AuaHG1eAt7LkD2Xx1xrsvZb1CiSA%2FAFqGtRZGLfRTg8eDChEqsjBqr2iUgyA8O9HrzDb2FE9oZVz8rJMDNhv1ZuzT7%2Fmd7NjbGbi3sW7oCXxcCEp6IsjJwJvUy%2BhSHdK84BUvpCfzzq2FNbCOIo1sjbS6nbFWEfVxK1hwb8FA8HGTidu0skmFJLl3NNqLja1WCLfCyMw7bDq%2BR%2F8gix%2Bh26ePynU1fBQUQvCrbIvQrlVxXx9csVNSQdbVaDtaxNcgircC69d7Nb7XWJvuh0v83UeK0U7NWJYhb63908wXgZ%2Bj2zBdVFhyioBgIimYr0Oo30x2mPkQkoof90VyXs9ZZAdcX0HXYnApmJCW9Heu2FsqBS6176MmRaTJh8ykbtKk5lv7l7%2FRcpQoFBnZ3awX%2FKxdU%2B4rWRxA7xPNwlmimFLIOZGawyzw3QIlcIUTC88K%2FIBjqnAcyEEOrIVY4qyB6Lob6jUmF0EDYkgEcYk2vbs48Iyr21WtOwN5MU3wR2V%2Bv6r%2BzwofHB4NHJgUHzyUzuElMKVB0F3JqT2M9qUSjKz0r8tsDtYIuxZiuP3mmPchB%2BFRRBsxmOc3hCZz77BRgATYOcJ936a06q4mmth%2BFu6t8F8VZDCwvjq1oF6R4H%2F7c7avkgQK0ywjiOq%2FCfNCZMQKYa4bacjXS4NnDU&X-Amz-Signature=62f543765974514d5275de9c286604a701e8a99e6176df3668babc964748a976&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

