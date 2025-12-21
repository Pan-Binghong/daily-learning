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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRWRQMXS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDp5u9XltBT%2BK%2FyDk1%2B0EzWaXq3k9tvmHOudD7tyKsnIAIhANRt2jqyPEGSujjTb2ZIogHMbKP%2BE54LY3QU6eE2jhNzKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylQhMn01PRiKTlAk8q3AM7iYOiUqd3PKFYSFH0WsEpNz1%2FzUn%2BqaU4l5T1EM6dwc5CFCCARmFq5fSosV8yV35W8QL6KHdl1s4pTZbf7lem0e7QS9gwBRT25iSgfOOUIbETc3hQ8e2pePLD840qAu2iYxCAuyJaNkpTo5rMStjXCcVtCUK8%2B2ZT0zEPXXluocN0yH3QK8JY3T%2BVKkNrkR8n6Cmmz3vTGED85%2BmtWn3qbiq2VdfXyDhLgXefPtmaQC5uehDZfKgwNSgOLoFHUN4fmNNBPtpURNWyTnK4k4ERBkIc7ThJ6wRm1qkoNjkoxUH88NmaXLOFXGWWz2IrEzJKQL6QliGTsaXN%2BVwCGprx%2B5MulN%2FX0oRuryezIVNgpmwefKDf3Xe%2F6CoGCRQd1xFNfUV7kfDna6pAxWb0Kiq7WOUHn6J2qytQD00EklulG91NqSfrU4orrPjCLHMShEI9mzAncy6GPgnZgdp%2B0X3kgy58vii1ZZMqDcnq%2BNCXUUpRgzcbtUV0EE%2BrnhtQO6uvX6YS9oODoiFVOz5pg9ygs5zrW86Z%2FI%2FZJGltrgu0oVj5yGNYq3zbgeS8w4MCQAfpjr3NanY7jHQbS208%2BmSF5NG2mPbvOkkznsnUdWuy5MdlY3BDwMNBMuHwzTDo95zKBjqkAd%2BykJRX7iYjSV4ncvhsGpnC5to7ulvFQ1r94v4DlGFi2g2l6I3AchPvBwXq40L9UgI7G1pSxpQ18IsWb8p1oygsituObvnVvg3Kj%2BdKS6yyjB1arATUo5sDzXKAsQQPh7UWiB1IJCI1qtEYEtXrXgarM8taazjWd8QQ%2F%2FhJtgrqjhEXwhA7ZXSsdn1jNAm6W4MBZJgNUc%2BPFoqjdr0z6hKATaqh&X-Amz-Signature=1dd28f09501594c44c6fbcfabf165830cfd50c222816b28095fc78b5b73b78f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRWRQMXS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDp5u9XltBT%2BK%2FyDk1%2B0EzWaXq3k9tvmHOudD7tyKsnIAIhANRt2jqyPEGSujjTb2ZIogHMbKP%2BE54LY3QU6eE2jhNzKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylQhMn01PRiKTlAk8q3AM7iYOiUqd3PKFYSFH0WsEpNz1%2FzUn%2BqaU4l5T1EM6dwc5CFCCARmFq5fSosV8yV35W8QL6KHdl1s4pTZbf7lem0e7QS9gwBRT25iSgfOOUIbETc3hQ8e2pePLD840qAu2iYxCAuyJaNkpTo5rMStjXCcVtCUK8%2B2ZT0zEPXXluocN0yH3QK8JY3T%2BVKkNrkR8n6Cmmz3vTGED85%2BmtWn3qbiq2VdfXyDhLgXefPtmaQC5uehDZfKgwNSgOLoFHUN4fmNNBPtpURNWyTnK4k4ERBkIc7ThJ6wRm1qkoNjkoxUH88NmaXLOFXGWWz2IrEzJKQL6QliGTsaXN%2BVwCGprx%2B5MulN%2FX0oRuryezIVNgpmwefKDf3Xe%2F6CoGCRQd1xFNfUV7kfDna6pAxWb0Kiq7WOUHn6J2qytQD00EklulG91NqSfrU4orrPjCLHMShEI9mzAncy6GPgnZgdp%2B0X3kgy58vii1ZZMqDcnq%2BNCXUUpRgzcbtUV0EE%2BrnhtQO6uvX6YS9oODoiFVOz5pg9ygs5zrW86Z%2FI%2FZJGltrgu0oVj5yGNYq3zbgeS8w4MCQAfpjr3NanY7jHQbS208%2BmSF5NG2mPbvOkkznsnUdWuy5MdlY3BDwMNBMuHwzTDo95zKBjqkAd%2BykJRX7iYjSV4ncvhsGpnC5to7ulvFQ1r94v4DlGFi2g2l6I3AchPvBwXq40L9UgI7G1pSxpQ18IsWb8p1oygsituObvnVvg3Kj%2BdKS6yyjB1arATUo5sDzXKAsQQPh7UWiB1IJCI1qtEYEtXrXgarM8taazjWd8QQ%2F%2FhJtgrqjhEXwhA7ZXSsdn1jNAm6W4MBZJgNUc%2BPFoqjdr0z6hKATaqh&X-Amz-Signature=9947f0f33ea1978f04ee921bf99b63679986cc496d58531057d364ca85e286cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

