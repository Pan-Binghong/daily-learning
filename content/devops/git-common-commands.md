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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZELRUKDB%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDUII3j4z0cBfGzewx805P5td9QJkYvvIjNs34hlIhoxQIhAMO5YDw9bQZ7EJivdcl4DwyYd0lcosjOWjrLGZHe5N7YKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs2xpEsKESOMLrnxUq3AOgus7NBNTb0fbGHfmBY7rCrsEVwks3hBOPlrocokXQiWEr9c4%2F7r9oU22Wq01tx83uogq2h%2FzxCQ7dPE%2F4yzYK9X8jjhWPmPElXSn6mp3vMlTt6dtbJECt3tOpeDlicd9h12KjKr%2FQrz1bdg2Fri0MnXuveop%2BlNg61Iv70wkImcPbzWMGK%2F1Z%2BLu4DUsVn7gJihLKr0FmPC7N0ZtGUqSF4sPBQvnXAB8L%2Feu%2BrpFtX9gwMT%2Fu2C7irN7aFPZ2uX8RFX9Cu4llVXSdh7nEJv9NPccO%2BplTXfdp4opXBx%2BOIX5izTz8DC5S36tLQxcxwHqO0IB%2FdqMiAM7ZtXdVdqj3qjzGhybK3m5a%2B8V8szwz68D0OKvj1LHPbMolnveiwROPo1XaMnVL2T1rgW4og4fAsl442kYqvtWBYzyCCOg88yffUyS%2BiABp8gVKy52SkYnpfKdVAyNCnuDjeQIfhwKuadFw9PpGLWoHSH2Py80rI5bb04d6RSjz8DhJ3BioCch56q0rfVb2zPQmImESuLEt3catSCi44aiz4PEH9kRQG86EWXOirXxMrJESGRUL%2Bn1FcRWn9L4wHPEzYC2nc0Dd3It22uaYHNbDYmIROkoE%2F7DAhnlR%2Bsxeqts3ZTC3h4DMBjqkAfpHHBLQuEhhgDo%2Banm7Tcj%2FUPB1rGHHtEhG%2FLNi872vAB%2FWvQhhiiiEfr0L6aS1EI6UVaCv%2FybKm8nLvgGx%2FUHYpwVm%2BZm16pM6tPGrRSKE%2BSt0Uk8bS3HGXrk8yhOZl25LgDX6sBVrVgZrOz0QJtP5h%2BdZHJ5cGHsjHXgCbbZN5hNEZCTDz1fG0%2FCAAqRFXLSSDverq9ls%2BK4iA%2Bq1k1tN2UhX&X-Amz-Signature=3e7cbb8b368e1b87499b1b7b444ede4d5b87af0d52fc380b1763a12c0aa25a12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

