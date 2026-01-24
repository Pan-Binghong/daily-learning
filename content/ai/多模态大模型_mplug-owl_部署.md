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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQKZFPYM%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBtACjBkw23KCfNENHhRvdeRG4rKRz3oi5SjeXCNMZ%2F1AiBkejpXbA1JuPOwIvbGIkPtIHqs8INwFM74452EOKpFkir%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMoy7qigKG11m4r54UKtwDd2L6PPimjePYTmbRpbfmLmbPrYksVzMtMedLSeAC7UJkDbGS7NUdbciGuCm%2FrEdjLmlzmU%2FwBriSEGpN1p2J3%2BGBo1wtlAgtaWMsEU1b7ljAuzYQYNxCxuV8lCe5MkUJ%2FljmP1UuOQxNu%2BiKY41MrFYWEefIuUxZ5Jb86FuC%2F6CcEBHQJkstmqNBJKS%2BHs3mLDDzPQOWBnohEziM7tki9wEWU56woF7B%2BMNMsKDcjoeaSovXzgudFVPo8dq9y0memGhp1%2BtEFpmzB%2FyV73frIOZu7cW%2FFOqI5lXKqMCZrgZH9tQfDtxYt14OfbXxd1oCSI8jXKf%2Fg6SICh0kQH8t7pU5B15CwN2pJE%2BUZ%2FhJkVMy7%2BbzweAHng8g1nYG4rEVVOAy8ns2IcfQTnWHI6xNWeiw7Mu9e%2FjCn5Ks1j28RD8dYZGcflScTPwzJ47I96gNVGs9G5uibLffBmPm3eF%2BpmwkVeN1ghvbonqwF2bVvNAadsYUec9dE3qON3qAcHTHUIbYNhqPR2nIzOWbpLrVVpV81Fres3DvjTv%2Bi0zATW1ulYrtLTwOeSXSSBTXGuTecwuvJw0e5CBlYlB8o2IZ7irAHZqB7KDRCn9Es8CsBql4AOsj6GMzB9%2F%2Fa%2Bgw%2Fs3QywY6pgFwzYGLTdsMy1VHSo8IEd8MfaDyeDQrRq0%2ByQpltr5Alibn%2BSQmSkZQO%2BMWyNQlIIQs2tSquAelaRaSW3ik3YeCwT4DW2Yn9LjxaHhoLyVC8gYL1CVyjKk0ed7da7GJKHKN5hwoiOz7NHzaNUVeqdMFPBL9tnxcki7FW0yZaIo6BZ8fLoBdkGs3jDZy4PWGSecYdVqCJ5zQ2TVQGRu4pzgo2A6Dmj5H&X-Amz-Signature=d36fc281d031dad9d4b86b72574a366141c24b65e69e781728058d4375767a82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQKZFPYM%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBtACjBkw23KCfNENHhRvdeRG4rKRz3oi5SjeXCNMZ%2F1AiBkejpXbA1JuPOwIvbGIkPtIHqs8INwFM74452EOKpFkir%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMoy7qigKG11m4r54UKtwDd2L6PPimjePYTmbRpbfmLmbPrYksVzMtMedLSeAC7UJkDbGS7NUdbciGuCm%2FrEdjLmlzmU%2FwBriSEGpN1p2J3%2BGBo1wtlAgtaWMsEU1b7ljAuzYQYNxCxuV8lCe5MkUJ%2FljmP1UuOQxNu%2BiKY41MrFYWEefIuUxZ5Jb86FuC%2F6CcEBHQJkstmqNBJKS%2BHs3mLDDzPQOWBnohEziM7tki9wEWU56woF7B%2BMNMsKDcjoeaSovXzgudFVPo8dq9y0memGhp1%2BtEFpmzB%2FyV73frIOZu7cW%2FFOqI5lXKqMCZrgZH9tQfDtxYt14OfbXxd1oCSI8jXKf%2Fg6SICh0kQH8t7pU5B15CwN2pJE%2BUZ%2FhJkVMy7%2BbzweAHng8g1nYG4rEVVOAy8ns2IcfQTnWHI6xNWeiw7Mu9e%2FjCn5Ks1j28RD8dYZGcflScTPwzJ47I96gNVGs9G5uibLffBmPm3eF%2BpmwkVeN1ghvbonqwF2bVvNAadsYUec9dE3qON3qAcHTHUIbYNhqPR2nIzOWbpLrVVpV81Fres3DvjTv%2Bi0zATW1ulYrtLTwOeSXSSBTXGuTecwuvJw0e5CBlYlB8o2IZ7irAHZqB7KDRCn9Es8CsBql4AOsj6GMzB9%2F%2Fa%2Bgw%2Fs3QywY6pgFwzYGLTdsMy1VHSo8IEd8MfaDyeDQrRq0%2ByQpltr5Alibn%2BSQmSkZQO%2BMWyNQlIIQs2tSquAelaRaSW3ik3YeCwT4DW2Yn9LjxaHhoLyVC8gYL1CVyjKk0ed7da7GJKHKN5hwoiOz7NHzaNUVeqdMFPBL9tnxcki7FW0yZaIo6BZ8fLoBdkGs3jDZy4PWGSecYdVqCJ5zQ2TVQGRu4pzgo2A6Dmj5H&X-Amz-Signature=fc6b084fb1125c77aa61736c199c7b444e681b4e9ec673bc492fade899e8ff48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

