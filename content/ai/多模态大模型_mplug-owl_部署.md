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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDMKULBM%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCe5j6YNT9ENcn7z3%2Bcgs%2BL32zsaFREkDZpXmtcNNniXAIhAN0F0fIs2BD7hvnXd6mWgZ70xmoKkko0sfM7AGy3%2FCQGKv8DCDIQABoMNjM3NDIzMTgzODA1IgzfAdKYYAPHAKrw%2Bpgq3ANyaj%2BDQIzyRtVMmD3IdFVzqRWxBjGpRoJnOnzfzk%2FC5II%2BqNs6NrJM%2BB9eAjUnH6XT42JnJLRYAk05PsKWkXRjeT8hHaeAQDmKP2KZf%2F9Gy8q0Tbdpa8MmAPeeTDb9m7WEvTvAfqs0D1bNABX4okaRBjHe6Mj8IGrShhe747gerzjFidk6bUhQiXXk7y8d%2FtEEBO%2FOwVzYWMvsZsRaj%2F4DIOqWhsj9g7wmmq6siaXc6w7XOERX6vBSPIdGR%2FV%2F89rCNzMm8jpzFFc%2FAwsrCqNgnv0jTRFrx6isu4GBUAqB%2FR9nlhKkqXKHaagQmFQq2JF44HtuJuOHFSEcrEAiUhUnlmcKmxxc2C30rNnalaLLRVbR%2FH9Ku5psFeUDYZ8PJUAVWmZB5wIl07oWenfD6GkiwzB%2BEGQCQleliuj7pKOXu2UlYCEKnw2ZeJtD1BZdMvNFJqroE5l1voCWeDHI3Z1lXMWl9wUvQ1PTssAXKlyl3h%2BBc1UC%2FZGhu8iyNUzsrHWPsvk61fzKrG5%2FWagx57arrEaZjsHfHuoYyl1uNEWNcV%2F3rc3tshAeui7xHir1isWJtRAMQF8BYKZN1t3ppVMefbmudE0hDFOcYFJBYbJgYau86QIk0CASt9%2BBtzC4obLKBjqkAUs8ihQkJy0fZabfhBCqO%2Fox7bPTEFVHSSmqA4snrOp%2FNtbbAR3f%2Fey%2FtBVhymsiptlzm%2FG95f3lTxQohhVHqrraHs4v7a7m%2FrCxIWLErYf0kM%2FYTYrAoCMFB3mke2Hj1tsKqET%2BGKW2QKmIHXfsECLOc%2FduFI24ITMQNXTlFbcHa2rjEyuOhnAV%2BbaKCy44D03oL%2FtQyK1rq%2BkyruZbhHSmt2iL&X-Amz-Signature=2beafabaad1abd3b4bcb1bb8b826c12c681f9a88eeb98c3a5fea5f66f5004e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDMKULBM%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCe5j6YNT9ENcn7z3%2Bcgs%2BL32zsaFREkDZpXmtcNNniXAIhAN0F0fIs2BD7hvnXd6mWgZ70xmoKkko0sfM7AGy3%2FCQGKv8DCDIQABoMNjM3NDIzMTgzODA1IgzfAdKYYAPHAKrw%2Bpgq3ANyaj%2BDQIzyRtVMmD3IdFVzqRWxBjGpRoJnOnzfzk%2FC5II%2BqNs6NrJM%2BB9eAjUnH6XT42JnJLRYAk05PsKWkXRjeT8hHaeAQDmKP2KZf%2F9Gy8q0Tbdpa8MmAPeeTDb9m7WEvTvAfqs0D1bNABX4okaRBjHe6Mj8IGrShhe747gerzjFidk6bUhQiXXk7y8d%2FtEEBO%2FOwVzYWMvsZsRaj%2F4DIOqWhsj9g7wmmq6siaXc6w7XOERX6vBSPIdGR%2FV%2F89rCNzMm8jpzFFc%2FAwsrCqNgnv0jTRFrx6isu4GBUAqB%2FR9nlhKkqXKHaagQmFQq2JF44HtuJuOHFSEcrEAiUhUnlmcKmxxc2C30rNnalaLLRVbR%2FH9Ku5psFeUDYZ8PJUAVWmZB5wIl07oWenfD6GkiwzB%2BEGQCQleliuj7pKOXu2UlYCEKnw2ZeJtD1BZdMvNFJqroE5l1voCWeDHI3Z1lXMWl9wUvQ1PTssAXKlyl3h%2BBc1UC%2FZGhu8iyNUzsrHWPsvk61fzKrG5%2FWagx57arrEaZjsHfHuoYyl1uNEWNcV%2F3rc3tshAeui7xHir1isWJtRAMQF8BYKZN1t3ppVMefbmudE0hDFOcYFJBYbJgYau86QIk0CASt9%2BBtzC4obLKBjqkAUs8ihQkJy0fZabfhBCqO%2Fox7bPTEFVHSSmqA4snrOp%2FNtbbAR3f%2Fey%2FtBVhymsiptlzm%2FG95f3lTxQohhVHqrraHs4v7a7m%2FrCxIWLErYf0kM%2FYTYrAoCMFB3mke2Hj1tsKqET%2BGKW2QKmIHXfsECLOc%2FduFI24ITMQNXTlFbcHa2rjEyuOhnAV%2BbaKCy44D03oL%2FtQyK1rq%2BkyruZbhHSmt2iL&X-Amz-Signature=a27faae1f92fdf4446da4c975632c09c21c936e92c8c42e5128f08b540c1104f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

