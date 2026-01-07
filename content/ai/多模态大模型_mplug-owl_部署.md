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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672OU5M2L%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuDthaKey6ynILm%2BtU5Jgg6RrRq4iQ5gPIzjojE%2Bq%2FGQIgCcrJptSmSvN2EO1vY0VaX3%2BF31kBWEaAwxozrZk%2BXgYq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDMFCjcq%2FhpMgbNyBPSrcA0nE0IaC9eOBCda3lW6Wbx73gccBIa3CAVyxF0W9PStSuD%2F4moTr%2BcatwFig9wsrKA7CLlreFCTGZ9%2BKQ%2BJYBuUe%2FOeJDl9qZcPqi4PmpvavTZA7CCPfXmXCv%2F0dod9Y1ZqVaIJLIAylHuD8TBTzD5PQnxtDZl1DaY7qWQhThAnD%2F%2FPKBuccrw3QCodhiqDL0EDv2ZDkuvXbfb8KwtA%2BmhYJZt%2FOm6N1oPFSx70kcPQfQGh12%2Fp%2Ful0l%2FdoK5kCepZ03vOt14Lxp2OkulricOqQC7ozoBOyDYlWXHwfD2WIM9lOhiE3%2FO96Zq45Qu4o0Ko7lYkiCLHXFwKdE9zHreC6jefe%2BqaQCgWjDx7kE%2F%2FBolLQ8NZhTy24fBdFuFKb4Zj89dpScwDFiNoUTIpMn3nC3f4oRmwnOmynj9Fww10NhNBPzRxVgip8Stl%2FDIH8SPlP4UkLjRLh1BuSXs%2BKkgERhonJAGi2L3zB2gyvOBg8yFBJvB4SMERgE6h63d6C6f8ETqFuzNwdOmc6k5%2BL0hlcLyLpIkNsv6zpW%2BNRD2DRX3TCUn6UbRXxuLtrpqiesnzufOqXPECfYrkyut9BCjWiKyDxLHP8Dl9Wbaqb92K%2Bggu0UW6PxnzhAJS1aMJuP98oGOqUBqC7%2FWN7CIPzjkWC6%2FgY0vmMSICC8hwhbzu0vUtU%2Blye9jw%2FZrEFY2xDG3dmzkOB9%2F5V%2FBetZq3MQTNNe697bCdQLrJII4LFunx2lv31dXCHUqKLRB5XSowr7ieYWngcUyqXnjW%2BCSOl8aysQDXcfW8LDUqtZVQ8S888y0dktiPiDgipW%2FgUmKRwfjQE4%2F74ltSNri%2BEa6Bb1hX7SH%2FO5XmXwF5RF&X-Amz-Signature=b34ae670bdecc47339c992c590b3ae2666c7ade2297f3aff48e72b343ff29c2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672OU5M2L%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuDthaKey6ynILm%2BtU5Jgg6RrRq4iQ5gPIzjojE%2Bq%2FGQIgCcrJptSmSvN2EO1vY0VaX3%2BF31kBWEaAwxozrZk%2BXgYq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDMFCjcq%2FhpMgbNyBPSrcA0nE0IaC9eOBCda3lW6Wbx73gccBIa3CAVyxF0W9PStSuD%2F4moTr%2BcatwFig9wsrKA7CLlreFCTGZ9%2BKQ%2BJYBuUe%2FOeJDl9qZcPqi4PmpvavTZA7CCPfXmXCv%2F0dod9Y1ZqVaIJLIAylHuD8TBTzD5PQnxtDZl1DaY7qWQhThAnD%2F%2FPKBuccrw3QCodhiqDL0EDv2ZDkuvXbfb8KwtA%2BmhYJZt%2FOm6N1oPFSx70kcPQfQGh12%2Fp%2Ful0l%2FdoK5kCepZ03vOt14Lxp2OkulricOqQC7ozoBOyDYlWXHwfD2WIM9lOhiE3%2FO96Zq45Qu4o0Ko7lYkiCLHXFwKdE9zHreC6jefe%2BqaQCgWjDx7kE%2F%2FBolLQ8NZhTy24fBdFuFKb4Zj89dpScwDFiNoUTIpMn3nC3f4oRmwnOmynj9Fww10NhNBPzRxVgip8Stl%2FDIH8SPlP4UkLjRLh1BuSXs%2BKkgERhonJAGi2L3zB2gyvOBg8yFBJvB4SMERgE6h63d6C6f8ETqFuzNwdOmc6k5%2BL0hlcLyLpIkNsv6zpW%2BNRD2DRX3TCUn6UbRXxuLtrpqiesnzufOqXPECfYrkyut9BCjWiKyDxLHP8Dl9Wbaqb92K%2Bggu0UW6PxnzhAJS1aMJuP98oGOqUBqC7%2FWN7CIPzjkWC6%2FgY0vmMSICC8hwhbzu0vUtU%2Blye9jw%2FZrEFY2xDG3dmzkOB9%2F5V%2FBetZq3MQTNNe697bCdQLrJII4LFunx2lv31dXCHUqKLRB5XSowr7ieYWngcUyqXnjW%2BCSOl8aysQDXcfW8LDUqtZVQ8S888y0dktiPiDgipW%2FgUmKRwfjQE4%2F74ltSNri%2BEa6Bb1hX7SH%2FO5XmXwF5RF&X-Amz-Signature=a043c3c938e49c21e0703929425379bdfefa2be2016d27e7f3c1a0e4fc19ffbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

