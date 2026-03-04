---
title: Git Common commands
date: '2024-11-20T01:22:00.000Z'
lastmod: '2025-04-03T07:41:00.000Z'
draft: false
tags:
- Git
categories:
- DevOps
---

> 💡 Git代码管理规范说明，以及常用命令。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBTZHVBC%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIByg70soYiiQirwp1DxrCvxh45o80%2FSRRVZpJ0AoFCv7AiAcxhxgwfNZULIveV%2BqI9h2Grc6GmotfJv%2Bc9bwBo7KnSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCBqZu90BfQPD33ghKtwDTOGwacNf4uO%2BeLSB%2FXwoEDAa%2FT3wVF4JZmRwH5YLn%2FkEBWlGvcjj9n73KZoUeLYv8JFZ3qixpsQZ0%2Frh%2F2SyXB1ZcnKQwqiArhRNE8cuvnhklJI2VsP33By21iMqWAnqJYXsFTdC7W6MtinCvV1qyuGd5N3uEaFmacqlQ3kyKPFkCSOutR8L5bg7%2BNgYGLRevdRbW5RvIWRdPSTH9OVlrpbYjgHa6iMcjPW6p0q6%2F6B6j8eNEgBKx2uVEYL27wEd5fDNnEncfcILpJdQy%2BRbitEbMPKQstfrf%2F1KKU8uOvIXwXGYl9UGxz46pDf7KOyvuu03pdftp6q8ZVP2znqIxkmuTFTmGYloTxTp75xp%2BnACGjFJiplqjSU%2F%2BIEWooXDHEP3r0oqJTmLfRQfUa%2BZRLyHFapvYlKals4Tm3Xpy%2BMThgugD6sZyjmtmU1Q2oflWVNCvYio2%2FHT5PE9zgERGLYcrajnFaFRtPDOABtX7y58Vp2xLdXLGa2aQa%2F8wOn37YVLqbDsz9YYjbhFPDdnDhQNxWFv68wr3xqHh6iXsI%2FCcehzqH4zMJHUXEzzFTFIZxuVjVcEjNSsmWXsub2l%2Fo70xvZEYUIx%2BNSG9%2F2RfTyFkXW%2Bsm4lDO5tv80w7ZiezQY6pgEtlCJEkI%2BS%2FoIoVZSGpsjK7LsCNnFa8mPEIPyFr7OJTyZ3LIpMJaEVvMFWN0suIEvcLMS85iFW0lJS3Q%2FDfqZxuNwG%2B0VaImJFQ31O45sKwclAgNzpxXk6VEB6O9DDzynS1%2BqmIImQTiJsxstaOnL%2Fn2i05%2FY0WcC3fkmqKhuFWsoDRcJFnzTnHOXS0HoQWmzDe188HVx76qLoa7qjzLlMx8U5w9vM&X-Amz-Signature=b2855183eee413449e3dc98f25ad34f1bd86626c9450fc0f2ed4fe660e9f0212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 分支说明

最常见的三种类型分支，名称与解释。

- main
- develop
- test
开发人员经常创建的两种临时分支。

- featrue（功能）
- bugfix（Bug修复）
---

## 工作环境常用命令

### Git基础常用命令

> 💡 想多看就继续看吧。以下主要涉及：上传并提交，合并，标签等操作。

1. 添加到暂存区
1. 提交到HEAD
1. 提交到服务器内的仓库中
1. 分支操作
1. 拉取以及合并
1. 标签
1. 替换本地改动
---

### Git常用配置

- 解决win和linux换行符格式问题
- 解决旧版本初始化分支名称为master问题
---

### 实战经历

```bash
# 初始化本地仓库
git init

# 创建并切换到 main 分支
git checkout -b main

# 添加文件
git add .

# 初始提交
git commit -m "Initial commit"

# 推送代码到远程仓库
git push -u origin main
```

> References

