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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7BEH5KL%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6N8b7Atp5aJZQQwIQN0D1ek3cha0oiA0ots1PQ8ybcAIgJZr8vR7RTUPhEBQdfgiOXOEfmGi2aUV0iqkuWZ2YEB4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHENRVeuUS7fs%2BVugSrcA8XYEhxwMeGeSX93wKyj3GChAakJuPXl8BCkyUVvB6DPko6Qs%2F9%2BuoEVczZawXIF%2FDRkkhAcRGtz7IAztziVXWREtqdOhi2mKXCP9yxibntIfgQHbuPO6ZP5ZVAqa00eJe5Fwduj3TbVpNIQgfU2inBvq%2BLoV9xhGuQcf22NT50M9McuwrE%2Fz%2FtLq%2BMc2cVsbkD8%2B7cCvaKFjnmv46eLsJtR42P2mdeuiaVbHtdKJMZFgxzriW8zXe3MDKjGgv3a4%2BNaT9C7XCCqfM5W%2Bp%2B8ZuwvBqwWhVQowiIv%2BcZcK%2BdXqhs0L9OjLSIBt3fpT8eVfOdYBrZuNtuZBcfMu6FFUfGEyZ37qN7PLxh0EMB7JED7b%2B2spV4YZI8a8y4cc7Gxo1aUZdEMokX64qXsyFFPi%2BqCJZFrcxMw92gVF512OqtjNKLaBaa%2Bkg6xe1236fh2BMbjpEVW%2BG7xqJ7ZpXV0c8wS3U7xFCHhoG3Dg5ny3hOBl%2F9yw0MPuL2peYZiFT3wTVIYtt89c5GUDJQ6rBe0b9qrKgeVj%2BYpDmoxlZf2zijW%2BZCvdwtD6efhaTUZ8GCZKwOrz6CbrMbgsigNWQMy2LaXIcsPL%2ByVqyB4toE8unIUu2ySYROAMe%2FLt2S1MMGY78gGOqUB0a7Zx3%2BoZ%2BtUlJ0rtbbSTsluw1qAjpHb96EHfWBWOCMVoNeVx4mBJKZJCFwjzYOKjrpoT%2BwmVWycIP%2BG8u4jqe8lyZXwnFboE%2FfYuluvaSx6khNU0XavT3dfBzq%2BiVm8Vi5UZNYOu7Nrs5C%2FiTjs62Sb3uuIcoobeZWBXSUxKBM0XiYR508pdSfAH3z3UMimvpkP9K4SK%2FqTEPnxxo%2BItaoGxbM%2F&X-Amz-Signature=7b3a5bf28b2125469a7fdb570cca38b7213fd112ecfd3a0c7a78b1a1fb25ec5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

