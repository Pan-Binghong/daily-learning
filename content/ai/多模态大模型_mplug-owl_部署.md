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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CO32G2C%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQC2mSDF1G2gwK2XDa1gnlN2aknBz7dt5cqtrD4ju8o5zAIgQk7%2BDiYXOizn6jnZGvDaI%2BTimECthrk9T2Q5%2F7PzPc8q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDzb%2BTxoMEVqFjbauSrcA%2BhnhiiAy%2FJeb4n4kH0ZK7vHJ9AIpMFMhef6eiPk%2FWVKS%2BFX3pWYoFcclAE2T7trNZ5qzgWLCohNMrruP%2BgaPJ4MTbMB5xjk01gnsq0WcAPsUfnL%2FgeMH3s1cyd1Z5tlNeXHnvnFjNEm63PwumGRIKXBr78%2BeTqQr5qIw3Rcq%2B6nik%2FwrBtooLFOLLI8sUziv3Lprk0L8rrRdvQMTIeYw4UkYhQD6Qkhqibkmg7iFlh%2Ft25kYKFrr2FALFD%2F5N3w9KqPfHnkWhVaIHUW515KyOOAMf20pcqCEXVe4Bx9AqAOIN1BM2O4yXGk1MfVFtKJPZcoxkL4%2BBF%2BJmkdrc6cvvUHMGM2c5eSVEXbWL8oWmE5JPUmALM8kWUXBrXiMJNu5rR1XEtUnS2bRKEs2C4HtpfbTAslbVC4qc%2Fq7OR2G%2FYj5KrGxHi2V42AyJuQ3muAPUzXOuiXHs6Kurk9JfGJ8rCg2N0lWZP%2BYMJepO0FGbrD6A3oddoz0oCICFUnrETotfTt9501Qcist8TisFknF6IqNeB%2BeKE0NC5ZD6FgKrXBYZvwUeS8GnFb8KbCQPqGUTED5Sl%2FOdNQtw1w5Ii6Y3YhU6fLxre%2BmDidwJpzHiY%2FijTDlZGQoflsK%2FuIMMXa%2FMkGOqUBMfpzKss5eS9EHnnM12nYi5qRot7hFbw%2FUrz5VP02LGo00JYiESmfwPPuCmI%2Bv3H8dXN10V8yWi24KNy9UNT7BfiW2rtTX63FRI4Q%2BEN%2BvhURN6cImHfXw1yaB5CcRju8jfTH4KO5teZt5TQAMB2Apth%2B%2B20c5TWgf1XXE2R6Jk12ctaJGLoM5ZlMsRvBXu9%2Bz1z0Cvh9l54LXSCAnWsbfyJ9tO1e&X-Amz-Signature=881b73e170e174bcbe529d71430be889672f33effebaf0fb27e3d688a9a9431f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CO32G2C%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQC2mSDF1G2gwK2XDa1gnlN2aknBz7dt5cqtrD4ju8o5zAIgQk7%2BDiYXOizn6jnZGvDaI%2BTimECthrk9T2Q5%2F7PzPc8q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDzb%2BTxoMEVqFjbauSrcA%2BhnhiiAy%2FJeb4n4kH0ZK7vHJ9AIpMFMhef6eiPk%2FWVKS%2BFX3pWYoFcclAE2T7trNZ5qzgWLCohNMrruP%2BgaPJ4MTbMB5xjk01gnsq0WcAPsUfnL%2FgeMH3s1cyd1Z5tlNeXHnvnFjNEm63PwumGRIKXBr78%2BeTqQr5qIw3Rcq%2B6nik%2FwrBtooLFOLLI8sUziv3Lprk0L8rrRdvQMTIeYw4UkYhQD6Qkhqibkmg7iFlh%2Ft25kYKFrr2FALFD%2F5N3w9KqPfHnkWhVaIHUW515KyOOAMf20pcqCEXVe4Bx9AqAOIN1BM2O4yXGk1MfVFtKJPZcoxkL4%2BBF%2BJmkdrc6cvvUHMGM2c5eSVEXbWL8oWmE5JPUmALM8kWUXBrXiMJNu5rR1XEtUnS2bRKEs2C4HtpfbTAslbVC4qc%2Fq7OR2G%2FYj5KrGxHi2V42AyJuQ3muAPUzXOuiXHs6Kurk9JfGJ8rCg2N0lWZP%2BYMJepO0FGbrD6A3oddoz0oCICFUnrETotfTt9501Qcist8TisFknF6IqNeB%2BeKE0NC5ZD6FgKrXBYZvwUeS8GnFb8KbCQPqGUTED5Sl%2FOdNQtw1w5Ii6Y3YhU6fLxre%2BmDidwJpzHiY%2FijTDlZGQoflsK%2FuIMMXa%2FMkGOqUBMfpzKss5eS9EHnnM12nYi5qRot7hFbw%2FUrz5VP02LGo00JYiESmfwPPuCmI%2Bv3H8dXN10V8yWi24KNy9UNT7BfiW2rtTX63FRI4Q%2BEN%2BvhURN6cImHfXw1yaB5CcRju8jfTH4KO5teZt5TQAMB2Apth%2B%2B20c5TWgf1XXE2R6Jk12ctaJGLoM5ZlMsRvBXu9%2Bz1z0Cvh9l54LXSCAnWsbfyJ9tO1e&X-Amz-Signature=26e41960344eec547bd3eb408c6e0a148f528482cab807f30954d53463085fec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

