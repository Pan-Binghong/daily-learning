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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WWRHCFE%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzWlX6gs%2FOGJ705WUpdlqJ18CrRPuqcPdmriIAPgynlQIhAJsc821WY8NGHA138MiFrzLNTY9ioWEeSisyq9D6ok%2FpKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFp4Xw6XATp5i2V%2Bgq3ANe9HrKAaW%2BgeYjYcix5rVggRLIP%2FGCy%2B0m3tZib5Tgs1pzwhLS%2F1LStwEkV6t%2FljGjlHcaUnIxDupouEluHNc3xNbfvoF%2BGY8aOjtCuzWRMnvHIMvNrfJSP5U257AakHcZXFgkt4rK8x2LahIQ6d1ZUEza4GDX9mjxHpM5a5IHd5J8Jym%2Fgh7CPRxsSzFbpRhhu5NyuwA%2Fkn680hn2qdTRSjqdMPLNX%2BqreKIyZZjSh%2BHBXDfPnEOBztOKlWx5kv6OcDtDzyWWW0rOjO1XUe07FH5z%2BCiPL4VOnmSI%2FwolLCJr4BqTNE2EDwVxyLkm7dGnh3OnnZ7lqFrRBTydjd7JfNOSn91lx8meMb1aivfe9bNF%2Ba7K4JUfrYhTnTXMT0fsdJJbxtTLsbmSrxbmIs9muMkzPsvzZg0McffveMOC8ScaFDt6AGUedO4tYWhC4PeXriCa4nxSWJkvrYbxymfDhC5L80PmDOMKL6axe3zhpmmT14SHvRZbrApPFeAxC6LK%2FsJ8mnkU6ni8woTXYDd0OXV%2FFqeS1IkXziL2j3gTn5NGbNmmC2qTVfEVED%2BO27%2FluMwcXox2MtVxV8jgw%2Bnz2l7sop0%2FlGctbnARswtJZCn7IHK8YdJMmXsq1jDpkLbPBjqkAW8HATeYlkNf%2F1B1a1bPRw8aatS4nSRxOj4K0DlBIxXxDji4eNoyqRrDZYkd%2BcM2stpeEe1xsYNcv6rUGLy3ZzJMICKlXlRH%2B17v6BZOnmOcPU3zQN7pFOLO%2BSnXWvNNJSns0SXTavZB6czxUjXKoCn2B92w7TqT%2FhJ9o%2FXnBJAA0vs3gYMgvjNtitPAC1%2FxRX0YPXs6jIeQUIYdHPE7erXSOka2&X-Amz-Signature=c5e87329091cf4a9c534be8a8d3b2639be72ae43956288be750b9beb11783e99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WWRHCFE%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzWlX6gs%2FOGJ705WUpdlqJ18CrRPuqcPdmriIAPgynlQIhAJsc821WY8NGHA138MiFrzLNTY9ioWEeSisyq9D6ok%2FpKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFp4Xw6XATp5i2V%2Bgq3ANe9HrKAaW%2BgeYjYcix5rVggRLIP%2FGCy%2B0m3tZib5Tgs1pzwhLS%2F1LStwEkV6t%2FljGjlHcaUnIxDupouEluHNc3xNbfvoF%2BGY8aOjtCuzWRMnvHIMvNrfJSP5U257AakHcZXFgkt4rK8x2LahIQ6d1ZUEza4GDX9mjxHpM5a5IHd5J8Jym%2Fgh7CPRxsSzFbpRhhu5NyuwA%2Fkn680hn2qdTRSjqdMPLNX%2BqreKIyZZjSh%2BHBXDfPnEOBztOKlWx5kv6OcDtDzyWWW0rOjO1XUe07FH5z%2BCiPL4VOnmSI%2FwolLCJr4BqTNE2EDwVxyLkm7dGnh3OnnZ7lqFrRBTydjd7JfNOSn91lx8meMb1aivfe9bNF%2Ba7K4JUfrYhTnTXMT0fsdJJbxtTLsbmSrxbmIs9muMkzPsvzZg0McffveMOC8ScaFDt6AGUedO4tYWhC4PeXriCa4nxSWJkvrYbxymfDhC5L80PmDOMKL6axe3zhpmmT14SHvRZbrApPFeAxC6LK%2FsJ8mnkU6ni8woTXYDd0OXV%2FFqeS1IkXziL2j3gTn5NGbNmmC2qTVfEVED%2BO27%2FluMwcXox2MtVxV8jgw%2Bnz2l7sop0%2FlGctbnARswtJZCn7IHK8YdJMmXsq1jDpkLbPBjqkAW8HATeYlkNf%2F1B1a1bPRw8aatS4nSRxOj4K0DlBIxXxDji4eNoyqRrDZYkd%2BcM2stpeEe1xsYNcv6rUGLy3ZzJMICKlXlRH%2B17v6BZOnmOcPU3zQN7pFOLO%2BSnXWvNNJSns0SXTavZB6czxUjXKoCn2B92w7TqT%2FhJ9o%2FXnBJAA0vs3gYMgvjNtitPAC1%2FxRX0YPXs6jIeQUIYdHPE7erXSOka2&X-Amz-Signature=7ee1831ca1df6019690392a43be07cce53fbfd1e6b9323cfbbf92f09e0bd2ee2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WWRHCFE%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzWlX6gs%2FOGJ705WUpdlqJ18CrRPuqcPdmriIAPgynlQIhAJsc821WY8NGHA138MiFrzLNTY9ioWEeSisyq9D6ok%2FpKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFp4Xw6XATp5i2V%2Bgq3ANe9HrKAaW%2BgeYjYcix5rVggRLIP%2FGCy%2B0m3tZib5Tgs1pzwhLS%2F1LStwEkV6t%2FljGjlHcaUnIxDupouEluHNc3xNbfvoF%2BGY8aOjtCuzWRMnvHIMvNrfJSP5U257AakHcZXFgkt4rK8x2LahIQ6d1ZUEza4GDX9mjxHpM5a5IHd5J8Jym%2Fgh7CPRxsSzFbpRhhu5NyuwA%2Fkn680hn2qdTRSjqdMPLNX%2BqreKIyZZjSh%2BHBXDfPnEOBztOKlWx5kv6OcDtDzyWWW0rOjO1XUe07FH5z%2BCiPL4VOnmSI%2FwolLCJr4BqTNE2EDwVxyLkm7dGnh3OnnZ7lqFrRBTydjd7JfNOSn91lx8meMb1aivfe9bNF%2Ba7K4JUfrYhTnTXMT0fsdJJbxtTLsbmSrxbmIs9muMkzPsvzZg0McffveMOC8ScaFDt6AGUedO4tYWhC4PeXriCa4nxSWJkvrYbxymfDhC5L80PmDOMKL6axe3zhpmmT14SHvRZbrApPFeAxC6LK%2FsJ8mnkU6ni8woTXYDd0OXV%2FFqeS1IkXziL2j3gTn5NGbNmmC2qTVfEVED%2BO27%2FluMwcXox2MtVxV8jgw%2Bnz2l7sop0%2FlGctbnARswtJZCn7IHK8YdJMmXsq1jDpkLbPBjqkAW8HATeYlkNf%2F1B1a1bPRw8aatS4nSRxOj4K0DlBIxXxDji4eNoyqRrDZYkd%2BcM2stpeEe1xsYNcv6rUGLy3ZzJMICKlXlRH%2B17v6BZOnmOcPU3zQN7pFOLO%2BSnXWvNNJSns0SXTavZB6czxUjXKoCn2B92w7TqT%2FhJ9o%2FXnBJAA0vs3gYMgvjNtitPAC1%2FxRX0YPXs6jIeQUIYdHPE7erXSOka2&X-Amz-Signature=a5eae7ad6e90795692f720e6d9c251b555c28cace05086a2fbe466f6c5b7b9ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

