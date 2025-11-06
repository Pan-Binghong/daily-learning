---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FNC6BVF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg%2F9GD0TRI2SJSngEPPfJP4ts2xlPC1R0zILbGcMOjaAIgYqGqrGRrk2i9VeBHxQXBSo%2FgurB5%2BeVyHp3mGGmAjGkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFisOs8TrdN6MuEIircA%2B1X3Yew3WrMXxT373YdbJW3Sdfr1XVoERwI%2F60B3fD8DlXrPWqKfaHd9cE%2Bf9hSRHt%2F7Nq%2BtuAzNEUZMmJWtcDbq1AVAK%2BMuk3%2FVpBfuzLnKsIMspTaZ0TPFkwiAac7PNGyCsNvFgtoSP%2F0tRBidZk8tAtWFvgC48UWl90AtTLDRByoPF5hkMWS8iEJC3kLaNZ1thbFGBWIvzVx2dahSI3rI3HRmFbH%2B%2F0UXB%2BR4b5Qv8Gub8jwDGz6H4lekzZpJQDrpSABAqLqFwINiXZU4jDBA93LjUiT86XTOdUXBNDUyFxBTn56TowS4AF0p1PAzx0ftlFLMWb5Ktkryj3XormWsr7xSthay%2BBKqrq4o%2FYM8acGMd7CXCqRcfijdhbD7oxkRHsOvSjoqsSybfELW5oKLeALBBWiZalTUr9niL3HUu6Aibt%2B4J%2Bvk4mw7QdVrIMWNiB8Q4yws%2BYbRHjjSiOe%2Flp6I%2FmCy2SK89KDiozpOrG2F4Wr9WiFvW00oXPg9rw90AzJBJ%2FP%2FG%2B4gz%2FuhL2hQTRg8f3hI6%2B%2FXASebob0yZRpXeVaqIdNmatuBvguwkCb%2B7eujksAQaoRjCK%2Br5Eqj9oC0CHTGM4Zl2tikXFHWqJZFv5HyjBwehv0MIiWsMgGOqUBjYVl1ZrfSyAMnwW5ZxlYD6YHV9sVRXgQqhlYI%2BAaK8EiR5zfvF2H9EKCuOk7gMihXhAcQy7uMV2z5LjGdqZGc1MbiRGpe1cwNniIVowlH6qD%2FUZHoxhik0wh353ENclKS406cOEtRGfQdxKxWqMG0vKCD9AFxy9TT%2FLau6shMAAjVmBwagYC2OiCoI1Ktg6WywRQUtxCt7itWGsB8j5Sx3E3rJOe&X-Amz-Signature=e7ac6fa1f2af3e797192909386135c3b9b67c11bb9027e2eea3585c9ac39397f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FNC6BVF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg%2F9GD0TRI2SJSngEPPfJP4ts2xlPC1R0zILbGcMOjaAIgYqGqrGRrk2i9VeBHxQXBSo%2FgurB5%2BeVyHp3mGGmAjGkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFisOs8TrdN6MuEIircA%2B1X3Yew3WrMXxT373YdbJW3Sdfr1XVoERwI%2F60B3fD8DlXrPWqKfaHd9cE%2Bf9hSRHt%2F7Nq%2BtuAzNEUZMmJWtcDbq1AVAK%2BMuk3%2FVpBfuzLnKsIMspTaZ0TPFkwiAac7PNGyCsNvFgtoSP%2F0tRBidZk8tAtWFvgC48UWl90AtTLDRByoPF5hkMWS8iEJC3kLaNZ1thbFGBWIvzVx2dahSI3rI3HRmFbH%2B%2F0UXB%2BR4b5Qv8Gub8jwDGz6H4lekzZpJQDrpSABAqLqFwINiXZU4jDBA93LjUiT86XTOdUXBNDUyFxBTn56TowS4AF0p1PAzx0ftlFLMWb5Ktkryj3XormWsr7xSthay%2BBKqrq4o%2FYM8acGMd7CXCqRcfijdhbD7oxkRHsOvSjoqsSybfELW5oKLeALBBWiZalTUr9niL3HUu6Aibt%2B4J%2Bvk4mw7QdVrIMWNiB8Q4yws%2BYbRHjjSiOe%2Flp6I%2FmCy2SK89KDiozpOrG2F4Wr9WiFvW00oXPg9rw90AzJBJ%2FP%2FG%2B4gz%2FuhL2hQTRg8f3hI6%2B%2FXASebob0yZRpXeVaqIdNmatuBvguwkCb%2B7eujksAQaoRjCK%2Br5Eqj9oC0CHTGM4Zl2tikXFHWqJZFv5HyjBwehv0MIiWsMgGOqUBjYVl1ZrfSyAMnwW5ZxlYD6YHV9sVRXgQqhlYI%2BAaK8EiR5zfvF2H9EKCuOk7gMihXhAcQy7uMV2z5LjGdqZGc1MbiRGpe1cwNniIVowlH6qD%2FUZHoxhik0wh353ENclKS406cOEtRGfQdxKxWqMG0vKCD9AFxy9TT%2FLau6shMAAjVmBwagYC2OiCoI1Ktg6WywRQUtxCt7itWGsB8j5Sx3E3rJOe&X-Amz-Signature=938bcd01dc5c33361e0ea1b22a872239236f397f8201b994b91bda835da64273&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FNC6BVF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg%2F9GD0TRI2SJSngEPPfJP4ts2xlPC1R0zILbGcMOjaAIgYqGqrGRrk2i9VeBHxQXBSo%2FgurB5%2BeVyHp3mGGmAjGkqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFisOs8TrdN6MuEIircA%2B1X3Yew3WrMXxT373YdbJW3Sdfr1XVoERwI%2F60B3fD8DlXrPWqKfaHd9cE%2Bf9hSRHt%2F7Nq%2BtuAzNEUZMmJWtcDbq1AVAK%2BMuk3%2FVpBfuzLnKsIMspTaZ0TPFkwiAac7PNGyCsNvFgtoSP%2F0tRBidZk8tAtWFvgC48UWl90AtTLDRByoPF5hkMWS8iEJC3kLaNZ1thbFGBWIvzVx2dahSI3rI3HRmFbH%2B%2F0UXB%2BR4b5Qv8Gub8jwDGz6H4lekzZpJQDrpSABAqLqFwINiXZU4jDBA93LjUiT86XTOdUXBNDUyFxBTn56TowS4AF0p1PAzx0ftlFLMWb5Ktkryj3XormWsr7xSthay%2BBKqrq4o%2FYM8acGMd7CXCqRcfijdhbD7oxkRHsOvSjoqsSybfELW5oKLeALBBWiZalTUr9niL3HUu6Aibt%2B4J%2Bvk4mw7QdVrIMWNiB8Q4yws%2BYbRHjjSiOe%2Flp6I%2FmCy2SK89KDiozpOrG2F4Wr9WiFvW00oXPg9rw90AzJBJ%2FP%2FG%2B4gz%2FuhL2hQTRg8f3hI6%2B%2FXASebob0yZRpXeVaqIdNmatuBvguwkCb%2B7eujksAQaoRjCK%2Br5Eqj9oC0CHTGM4Zl2tikXFHWqJZFv5HyjBwehv0MIiWsMgGOqUBjYVl1ZrfSyAMnwW5ZxlYD6YHV9sVRXgQqhlYI%2BAaK8EiR5zfvF2H9EKCuOk7gMihXhAcQy7uMV2z5LjGdqZGc1MbiRGpe1cwNniIVowlH6qD%2FUZHoxhik0wh353ENclKS406cOEtRGfQdxKxWqMG0vKCD9AFxy9TT%2FLau6shMAAjVmBwagYC2OiCoI1Ktg6WywRQUtxCt7itWGsB8j5Sx3E3rJOe&X-Amz-Signature=4658dc327b8f56b4f46b803008bedb529ae97908e91a18f632388ba589c066fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

