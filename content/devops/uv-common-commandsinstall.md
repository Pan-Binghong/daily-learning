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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667POKSHOW%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnRGMVCqTZWdFnm0CBg0bs9zDNUm0AzaP1cTOVTnyicAiEAn2lyo5X8lAwF3IsGrX11g0cmk26x0wlU%2FGD9e0Y4HZEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDIP9t51jxhhRWmPR7SrcA0UJ40jAOBGpZhmlg44HOQLfXXbD26aa12gRhvvDBrfHxVgx8WFC1V0kNXevnpS12hSIE%2BgC4PSzjcTojlHfmM0MCTY3rFM9HIPsxuJySvzP%2FY7irkfbYp9mEZHBT7CStY3aQIZLIAlvX%2FxWGZm47lZnK5sPgSzrvGQIzqoPtzZyvTN4WbxIHEJ3I96DUkaNfzMnY0HDs4GHusol%2F292bS66U3Wprxdb0nLrwmy0Jzo14sJoZV0EyiX0JZ%2BUeAVI4aXw4vWvBLA38uM4sdU%2FGZ3XzlMGowRXBktJoNpvrxAoKgcbjEp6pK2DUDH5Jrmafe2b8dHTIEsztRdVAAombU2EfAWVHmJNOKLnwENY31D6z7mrUDNWg5qE%2BsTa0x5M52QFXPfP3aQpv2uH%2FmxlqRL6wCbsVlXDCU%2FokhsNAqo8H8GBkjUy%2FOQ3X62MT2O%2BfyNw9IGSgDZeoaVPujbW74N42cNawQTPXucsrrmDJLYO3cj3GvCJ%2Fo9lOXbI3ppKu6a15hem3JSDxDe8Ciyi3V588XnLziyoUqz33mRKvJ404JOTs77xTBVZMNitJkGjswLSwGi7rFDj%2FEA2jbQ3bKpg7gFq%2FkBql2vDc9T4lizMNajM52oV9N5sgfY%2BMOenzskGOqUBbUaDP1lN4hP4kiqj%2FyGykqUcaC9EX2gs4vtufqf91KHJsHe7Qlyv7ds7AOSe3V9CVSTyiwBBDEz2CrazkaYUJCrUhq0fsQfgZOjAFe5MASxh9xiitTzPbB4%2FpnxOmvHkuYcKBU53GKy%2BKNsVIOFXi5vfdXPaO5GXjwPQJrXjgammnniwmQcUylDM9tUakymoAZv9vr3B2b2k0kkYGOe2eBYrVOH9&X-Amz-Signature=4d49f7653b20226a939f701b14f59464058d049e22b017e468be51b24227dd63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667POKSHOW%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnRGMVCqTZWdFnm0CBg0bs9zDNUm0AzaP1cTOVTnyicAiEAn2lyo5X8lAwF3IsGrX11g0cmk26x0wlU%2FGD9e0Y4HZEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDIP9t51jxhhRWmPR7SrcA0UJ40jAOBGpZhmlg44HOQLfXXbD26aa12gRhvvDBrfHxVgx8WFC1V0kNXevnpS12hSIE%2BgC4PSzjcTojlHfmM0MCTY3rFM9HIPsxuJySvzP%2FY7irkfbYp9mEZHBT7CStY3aQIZLIAlvX%2FxWGZm47lZnK5sPgSzrvGQIzqoPtzZyvTN4WbxIHEJ3I96DUkaNfzMnY0HDs4GHusol%2F292bS66U3Wprxdb0nLrwmy0Jzo14sJoZV0EyiX0JZ%2BUeAVI4aXw4vWvBLA38uM4sdU%2FGZ3XzlMGowRXBktJoNpvrxAoKgcbjEp6pK2DUDH5Jrmafe2b8dHTIEsztRdVAAombU2EfAWVHmJNOKLnwENY31D6z7mrUDNWg5qE%2BsTa0x5M52QFXPfP3aQpv2uH%2FmxlqRL6wCbsVlXDCU%2FokhsNAqo8H8GBkjUy%2FOQ3X62MT2O%2BfyNw9IGSgDZeoaVPujbW74N42cNawQTPXucsrrmDJLYO3cj3GvCJ%2Fo9lOXbI3ppKu6a15hem3JSDxDe8Ciyi3V588XnLziyoUqz33mRKvJ404JOTs77xTBVZMNitJkGjswLSwGi7rFDj%2FEA2jbQ3bKpg7gFq%2FkBql2vDc9T4lizMNajM52oV9N5sgfY%2BMOenzskGOqUBbUaDP1lN4hP4kiqj%2FyGykqUcaC9EX2gs4vtufqf91KHJsHe7Qlyv7ds7AOSe3V9CVSTyiwBBDEz2CrazkaYUJCrUhq0fsQfgZOjAFe5MASxh9xiitTzPbB4%2FpnxOmvHkuYcKBU53GKy%2BKNsVIOFXi5vfdXPaO5GXjwPQJrXjgammnniwmQcUylDM9tUakymoAZv9vr3B2b2k0kkYGOe2eBYrVOH9&X-Amz-Signature=15b8290167fbe78a8882f46d4965ded1bce892460b37d7e9510e2b65332ea228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667POKSHOW%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnRGMVCqTZWdFnm0CBg0bs9zDNUm0AzaP1cTOVTnyicAiEAn2lyo5X8lAwF3IsGrX11g0cmk26x0wlU%2FGD9e0Y4HZEq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDIP9t51jxhhRWmPR7SrcA0UJ40jAOBGpZhmlg44HOQLfXXbD26aa12gRhvvDBrfHxVgx8WFC1V0kNXevnpS12hSIE%2BgC4PSzjcTojlHfmM0MCTY3rFM9HIPsxuJySvzP%2FY7irkfbYp9mEZHBT7CStY3aQIZLIAlvX%2FxWGZm47lZnK5sPgSzrvGQIzqoPtzZyvTN4WbxIHEJ3I96DUkaNfzMnY0HDs4GHusol%2F292bS66U3Wprxdb0nLrwmy0Jzo14sJoZV0EyiX0JZ%2BUeAVI4aXw4vWvBLA38uM4sdU%2FGZ3XzlMGowRXBktJoNpvrxAoKgcbjEp6pK2DUDH5Jrmafe2b8dHTIEsztRdVAAombU2EfAWVHmJNOKLnwENY31D6z7mrUDNWg5qE%2BsTa0x5M52QFXPfP3aQpv2uH%2FmxlqRL6wCbsVlXDCU%2FokhsNAqo8H8GBkjUy%2FOQ3X62MT2O%2BfyNw9IGSgDZeoaVPujbW74N42cNawQTPXucsrrmDJLYO3cj3GvCJ%2Fo9lOXbI3ppKu6a15hem3JSDxDe8Ciyi3V588XnLziyoUqz33mRKvJ404JOTs77xTBVZMNitJkGjswLSwGi7rFDj%2FEA2jbQ3bKpg7gFq%2FkBql2vDc9T4lizMNajM52oV9N5sgfY%2BMOenzskGOqUBbUaDP1lN4hP4kiqj%2FyGykqUcaC9EX2gs4vtufqf91KHJsHe7Qlyv7ds7AOSe3V9CVSTyiwBBDEz2CrazkaYUJCrUhq0fsQfgZOjAFe5MASxh9xiitTzPbB4%2FpnxOmvHkuYcKBU53GKy%2BKNsVIOFXi5vfdXPaO5GXjwPQJrXjgammnniwmQcUylDM9tUakymoAZv9vr3B2b2k0kkYGOe2eBYrVOH9&X-Amz-Signature=9e16b12fcac72ef99d3032c6538fa25d01a279ae7a57cb5002cfaf4a07a5103a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

