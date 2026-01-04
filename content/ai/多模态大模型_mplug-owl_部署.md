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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCD54LQV%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICCTNjEsfxI%2BjWVwh%2F3oygfHXCQyNVWX%2BKkJk0OOHsSmAiEA2eUnFHSm%2FZmbsgyV%2BjDalzAVCxQ0HAH%2BqMIdEnodSlEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDWoomZ759%2FuRE25%2FSrcA%2Bnh0Xu97yw8MuuM7smXYyqZZnPC%2BfDI26CLneccAlwPoHecxMK%2FbT7JgNCgNrcmqcuBTolE6iQ%2FFueRx7YGdsdMed1ZHBeHpJdJFYY3XJS60vTyspuxkYRBH0sFiaLoFcghvKV6rUv%2FPZcyOEftjYWk%2FL6gtXDFwZqzeCiDSEnJl%2F6Qx%2FX0WWZXyN7c45QAS3GdDtFVaDaxOsfufZV3aNjs%2BIGygf26%2B9oEKU6XKS7kKOGXCmjfMrOqf7Nl9KSa4moD%2BM75bpIRuXyjWwyxFoHse8BXBpUxdqk3Ofmg7aWGq5UzzkIMG8%2BP8tFpTyoSvIgKyZtFjicpi8HDZnnh91moQHcNVEQrKYsnTm%2BacnPNT%2BJ2Y2aZ0%2B4yxbulLKQbubfrZWljp6Pf%2Fz3bx0eaghk%2BDsuqpimeGO3HTHSXlEzzh9Y8yX%2F1uo8hIqG7xE37uhS5azydnWcQnQf4rAfqUn%2FtzleF5ruz6C%2BvmQApN%2BPMyh84vLvKaCszKhBZYl7A0M3nAoZMwP2Tnh%2BukU%2B%2Bn08Gygk43q1oy6TnEyyQ3S4XqNv5%2B%2BgEZcYpP1eTxGYe9CqE%2BeLisW3%2BrSJxKvluiHqoCvoAs8FVmAOay0Eata2NmDCr40oVoM%2Fs64ycMNvs5soGOqUBFobhtUF95Joo5U%2BhPbR8m6UaKNUEAHcJfRgY%2FURtZiTnyOro9Ed88MEAUWJyDjVErtnZxvA5RQ18T4JYD9Y2GG4CYE9X1LsYMcXVtyBNYhfX3LcAlUh08nGWFtWFhtawgETFlIVOingo7FNCpP5nc8ORyP00sDfBfPne5%2BH1qVRsmBEWd4ESN%2BWO%2BINsce7PIahMmRCoxawqWEsNGP709voI%2BYjH&X-Amz-Signature=0903f80e7cc1ddaafd9d88ed44e36fb0e71c9c812c3add59895a1270f525690d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCD54LQV%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICCTNjEsfxI%2BjWVwh%2F3oygfHXCQyNVWX%2BKkJk0OOHsSmAiEA2eUnFHSm%2FZmbsgyV%2BjDalzAVCxQ0HAH%2BqMIdEnodSlEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDWoomZ759%2FuRE25%2FSrcA%2Bnh0Xu97yw8MuuM7smXYyqZZnPC%2BfDI26CLneccAlwPoHecxMK%2FbT7JgNCgNrcmqcuBTolE6iQ%2FFueRx7YGdsdMed1ZHBeHpJdJFYY3XJS60vTyspuxkYRBH0sFiaLoFcghvKV6rUv%2FPZcyOEftjYWk%2FL6gtXDFwZqzeCiDSEnJl%2F6Qx%2FX0WWZXyN7c45QAS3GdDtFVaDaxOsfufZV3aNjs%2BIGygf26%2B9oEKU6XKS7kKOGXCmjfMrOqf7Nl9KSa4moD%2BM75bpIRuXyjWwyxFoHse8BXBpUxdqk3Ofmg7aWGq5UzzkIMG8%2BP8tFpTyoSvIgKyZtFjicpi8HDZnnh91moQHcNVEQrKYsnTm%2BacnPNT%2BJ2Y2aZ0%2B4yxbulLKQbubfrZWljp6Pf%2Fz3bx0eaghk%2BDsuqpimeGO3HTHSXlEzzh9Y8yX%2F1uo8hIqG7xE37uhS5azydnWcQnQf4rAfqUn%2FtzleF5ruz6C%2BvmQApN%2BPMyh84vLvKaCszKhBZYl7A0M3nAoZMwP2Tnh%2BukU%2B%2Bn08Gygk43q1oy6TnEyyQ3S4XqNv5%2B%2BgEZcYpP1eTxGYe9CqE%2BeLisW3%2BrSJxKvluiHqoCvoAs8FVmAOay0Eata2NmDCr40oVoM%2Fs64ycMNvs5soGOqUBFobhtUF95Joo5U%2BhPbR8m6UaKNUEAHcJfRgY%2FURtZiTnyOro9Ed88MEAUWJyDjVErtnZxvA5RQ18T4JYD9Y2GG4CYE9X1LsYMcXVtyBNYhfX3LcAlUh08nGWFtWFhtawgETFlIVOingo7FNCpP5nc8ORyP00sDfBfPne5%2BH1qVRsmBEWd4ESN%2BWO%2BINsce7PIahMmRCoxawqWEsNGP709voI%2BYjH&X-Amz-Signature=fc880322a88d642b14276939c9049990a81d4bce50c59fec26f73f47ca15494c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

