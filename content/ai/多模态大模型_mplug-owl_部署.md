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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMGYBA4%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLI%2FJSHgiMCYLnLkCLtAywsGoW1brUZ9Xj%2FjDEGpptbgIhAKTQv7rwWH%2BKy3zPdWxsxndr3%2Bjv%2BnZQF1OSajSx4S1hKv8DCG0QABoMNjM3NDIzMTgzODA1IgwnqQ%2F8%2B7LXCk8D6vIq3APjQfgtATc2HtnPNCkAMPyXSenRjLtdKEE71onoAfEYf3zErTvjlhL2YCYJfv%2BpwobEpqdIEJQauicFrGVA%2B8NPt58jJ8IRmdOOQsB7CUDID4lOYTTtYUrPeEUZm%2Br%2FsvQcJSISJWR7KhaCJd8fb9UdpME9Wz77DMb5UDZ7voxeeUydrpjn6jH%2Bu6qo7k9dSp2xJmgJhSfIJmoDCFmffk6yYd4L24DkaQeHCsKHKuAU1Rrsi3gwEveq7iqKXTfBKgCLRyXPmPlZflA8G3Go3c1azyWTh4kvnCOZJjHfDwYXM93uchD1Y1519zNd33sAnnRY9o3Zift5ZZmV%2F2widlI5KH11PBebf5hmxc%2FOOGbdXf4xCG1mAatRWmjmilUgUCgHtrJ7vjLL8lvULNexn8xdzY9lIGSWmHKZ6IDMbVIBeN%2Fh6kID%2FFCKsJatLhIAdpSy1EtJaaFDMu9l3wGFdIeCx6WrmHVKuZN2oUeTEqt3FzFQo7LwMFzYQ8HeERD5sMCsrm9cRbGSYHuiFChve59QrL0JLAfIkkJxUsoUlnD%2Bnz%2BIXibz33LfJB62IQdTLeryqmzCQgHGKo5uYn6Q4eACmAwgRelpiJkN3GoqOTtE1F2FEBApDSIptCGWvDDei6DMBjqkAfODSE8jeh0tZtMfGKQJ%2F6VQ23%2F44a7RdWWopUcyRlWXisX8bEgr8q%2BSTjBSNHr6meNN8bOoOcJhtybPZA8tU0O76gKXMKg6Agl8XTV3MxeAsHoWpys%2FgasLh%2F2Qrp4uqJV6xcEvurvriJVuqrHS0whD3exbFbEHCF%2BL3nKPFwu24QU3wBiOBlzS0SSLKyPBo%2FMCIGuTYKN9TcHeyB6lSGIJWbW7&X-Amz-Signature=b8a39eec301088d67c0040b7a01ed2b573a0ad0a26f8342bb243121f8a7a434f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMGYBA4%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLI%2FJSHgiMCYLnLkCLtAywsGoW1brUZ9Xj%2FjDEGpptbgIhAKTQv7rwWH%2BKy3zPdWxsxndr3%2Bjv%2BnZQF1OSajSx4S1hKv8DCG0QABoMNjM3NDIzMTgzODA1IgwnqQ%2F8%2B7LXCk8D6vIq3APjQfgtATc2HtnPNCkAMPyXSenRjLtdKEE71onoAfEYf3zErTvjlhL2YCYJfv%2BpwobEpqdIEJQauicFrGVA%2B8NPt58jJ8IRmdOOQsB7CUDID4lOYTTtYUrPeEUZm%2Br%2FsvQcJSISJWR7KhaCJd8fb9UdpME9Wz77DMb5UDZ7voxeeUydrpjn6jH%2Bu6qo7k9dSp2xJmgJhSfIJmoDCFmffk6yYd4L24DkaQeHCsKHKuAU1Rrsi3gwEveq7iqKXTfBKgCLRyXPmPlZflA8G3Go3c1azyWTh4kvnCOZJjHfDwYXM93uchD1Y1519zNd33sAnnRY9o3Zift5ZZmV%2F2widlI5KH11PBebf5hmxc%2FOOGbdXf4xCG1mAatRWmjmilUgUCgHtrJ7vjLL8lvULNexn8xdzY9lIGSWmHKZ6IDMbVIBeN%2Fh6kID%2FFCKsJatLhIAdpSy1EtJaaFDMu9l3wGFdIeCx6WrmHVKuZN2oUeTEqt3FzFQo7LwMFzYQ8HeERD5sMCsrm9cRbGSYHuiFChve59QrL0JLAfIkkJxUsoUlnD%2Bnz%2BIXibz33LfJB62IQdTLeryqmzCQgHGKo5uYn6Q4eACmAwgRelpiJkN3GoqOTtE1F2FEBApDSIptCGWvDDei6DMBjqkAfODSE8jeh0tZtMfGKQJ%2F6VQ23%2F44a7RdWWopUcyRlWXisX8bEgr8q%2BSTjBSNHr6meNN8bOoOcJhtybPZA8tU0O76gKXMKg6Agl8XTV3MxeAsHoWpys%2FgasLh%2F2Qrp4uqJV6xcEvurvriJVuqrHS0whD3exbFbEHCF%2BL3nKPFwu24QU3wBiOBlzS0SSLKyPBo%2FMCIGuTYKN9TcHeyB6lSGIJWbW7&X-Amz-Signature=9a96bf96b5cde5c02eeee8cec5ee58dc3ecaa885dde12ffc80f71cda1a48f10a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

