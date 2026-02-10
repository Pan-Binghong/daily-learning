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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665PIRKSR%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXSG%2BYJLyk3QKteL7TudXryfjcgsIhTllQdQiLh81onAiEAn1nbq%2FVz4BJFRDlX2yKXwahqwtmPZSYjYrJmfPVS2JcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGE5jW2Zmh%2B3MnK0rSrcA0NMELreyWTyJL%2FASVNLsZxC0fO92kaSKXP%2BxZTirCFtk45UquejLTsXwQOeWtVr%2F4Sy1oDTNlvR%2FslPIVGC1Tt5WgT4C03gOax9%2BGwaSMJUByWo3PAkX9uBQAohoSFpgeS%2FhH61DZj8Pu%2BIS8Ef55DJ4ROsH0SmESy%2BpA3eXzZrpY1xHvZRxEtKwfd7BML97hGP0YQsTctCO92yABCgCVZ918WgqueSkSfU0kv07vWoCLcxSrcZqCwEH5DtsNHbeamhXL3iZXqUCu8TI%2F3SBlevH7SO2MYOnZQUcze9gKPSYL5bfiMSkAvu9otpVMDBGHqWW3mf216e0Mly%2BK15LPN8IiflAMU4Ev25tLIyKvCs0GTG2KB8qmv%2FRaRwu92VC1m2XjpH8sTVl9U3CtCxCzW6pOac1oZb1jKW9hrC5H4yobYm6115gTnE9VKqylJkvepJWvK5Inp%2Fsg40ZllQompTleFU1cSnkfdv4Zuy9aWMLgRzPjkRGPlmIbWAIcv2SbS4ohlMyE7S32C6Mmsax7miUxLwuqQvcRsnbq2Aoh%2B0vxhPTW53lP8OjNOqm6ETh%2FrmDsy1%2FrpVBjZj5e4P4f4rgb3ykXvi02i47r9YOJR2qXFr9YPZgat%2FborpMNrDqswGOqUB%2FGGmWdljc%2BncTd3qCX6sK9vd0ee%2F6fu6SrUUDMESpA2Iq4glnnwWK2BUU1Vlr27r5KEJuetAmSwmrLUjerxQBmtCLuHv2As4p1BCQIO4B%2F5EoXQdpZ9CTPso3BcV2skt0McCpM4ShUY0kXA6MwFk031k8SYDAuU1j5AAl0maoDI5RxqQTdw89BDUdViD00GurqYvnuDUv0GAxxDgccggdlP96obl&X-Amz-Signature=1ca07e3b8e2b2219a825d73a4d7fb65c505bae47e8429a3adbd68151505c92f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

