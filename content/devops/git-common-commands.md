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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/957b9d02-7d7c-45ab-bcf8-38731684567f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPJAYIJK%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIA8WmH66jmId3oimUxiGb8yAlQuYTwHmbLx%2FM9U7Kx43AiEArHtgFxUTyqUNMRTRDvcq4fHlXcJ6jqfwHHjYqf5lA1kqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHs%2BbAySaC6y1LK1yircA8lC33dK7KMeskLqgpjR3%2FoNT54d6QMcZaryJUQUoOp1qtroQUFKhjmBqhm3W9akcrTzm7VG8fboq4Fr11M9u1q2aZYIiVJI09AN3edcNcOfdL%2FubkUCqqXLH8j%2BO23%2BAq%2Bj6W0P6v7PgNch95cuBxKS1f77e4XZYdN%2B%2FcymqugjzWnjQYtiR%2F8jwVahvnrb92ECXsLTy%2FxFhcl7y18hF%2F8XnAkBeevzzMyxgS5%2B3tml98%2B%2Bky9Sg1KQYkoGmq5wQkATv%2B0JlneYm9cFgq0sWUYDFwfKb2HPQWcxDZvwszRstlKhF3uWPf8P%2FKXd4ywQ7OOK06CW8pXurqtNH%2FerlqtJ%2BEPyfyfsPHNrqXSxrgjmuNDh8zoc%2BOY1VdnkIIFLxkz0Cjqm5t40exNqb34d1M6WysANHgfn4VqHDV2FE2G4KFr%2FvuQi9%2FgeyaI1qMLCoCvF8mDzbB86ROL6%2BPjxL8uCANOSM06AI8TER%2FCsH9H9Socz0q9%2BkbrhRpz6DV9j%2FOxpR%2B44VQ3FIc1K1Wu3ms1lfp%2FJRlzdy0rQZHHl4RLSu%2BDcrZYfDpjgbtivq1zv2bc3bwM4eIIBw6Iv%2FU4ANUaWJz4iZ9Ea7%2Fw3%2FLlBdQWZppZ0BXcLhutaxIluMKWCjMsGOqUBbqre05lHmwFYO2l4JckqD90IItWt50OoJ2Ct4yXregRjwMRZc4wgSQgVMacnTUyJZTG5bQQPssThqmxHFAXPRnj%2BQsYvPXGH%2Bih1HUbTzwlOuD3%2BdAlKja87Jfr9fUCYh1NZ%2FhFOzFBUWUYhT2Pz5GveehuZbChMTSSQqWVjpkKlkAG8aOG5k%2FrosMnxXY8qUupUytLbovPzViXY3tVJXxRtjwIt&X-Amz-Signature=4f2f1a8f3c5e3cdf0734d3ccde55bfdcabae10e3b542f880ab4f8ee5fe6653d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

