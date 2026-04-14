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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWNBVV3A%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1WmHfKjjdxYcv8YG4OJn9esJ5ZZ1bvY5GBG2cZc%2BoiAiBdF%2BmO8lrB2iyNJwmFuUkojUhqAWLfubNRkxyx9PLDuCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNETHw7xCSb7LUj92KtwDlj8xtMMJJVtR7FchvB3GfCkmcrBzKqICud3eOnW%2FEaPnR8juPU%2FMqcbuflxM2EluOEKZWkWeWEnxW3HN3Q9xh1v5MofBpPjik3we7bPA3hUdVN47Q1gD8IpjqP25YYCVC%2Be2bfr5gqc1fvFgVUiG5n5SPTu9oxgWx6aYHnp9PxYOkcq%2BbaNzbsdqVHf%2FNzzvjKKLQQZPyOWashjit2aEfgoofZg4VUCaRoZgcYPDek3aFK9L%2BDkF%2BnYaTgu%2FI0G1q6WPZlOJm0C27arCN127%2B4EZd08CpCbGNVflksktxckhIYnuHwCHFltJTAa7Y0BEBPg9HygKVGpQjuCJlwmci8opw1aZCUCayYgAEGeNeXcC8aqS%2Bd%2B8s8FHXODlIibomKbFmq6aLrQ%2BsO0qgzKj%2FcBc%2BOdxxVqI6J0ujMmpYfC2Y4WjCMUsTavBcCuluXaIrTWphgqoLP8Q%2F6xegkUMrpQaiDyxeoZ0JHMLoSPN152zpa61JLcVuVuy6B217KqBNxrkZHO7lKaGlAIToofOWIOY1NxY3VxSrzCqNaxKGa%2FpjwcEe9yPNNT84PpfGfmvTU9e%2Bp93vhlNcAk36au8WYnT7SHkgyhvXe83gDoOjpRnlpdIqqpM0ZkXPfow0uD2zgY6pgGro%2FNi4VQiGELWPx2RvNwZDQaRE1RJVCJhNjt9cPPqVqFOAyYLH%2FB2Cmlk9%2Ba7VKymoP3YPqjUCwhZiqR7wSScN35RayASeLjzgbFpJbHraJYybglhCREpEeQSjD2YaCnZnC9iIk7s3z91qQ7apYipMPMUICp5wEswV5V32DDK%2F32w5e%2By%2FDq6edY%2BAlF7HvZlX1U9w9YDMOp26mfMx0CvaSj%2BkuLV&X-Amz-Signature=3d070f0e490edac417ebe44ebb483e75cb04a3c97e05e0ed903dcae77084fa8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWNBVV3A%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1WmHfKjjdxYcv8YG4OJn9esJ5ZZ1bvY5GBG2cZc%2BoiAiBdF%2BmO8lrB2iyNJwmFuUkojUhqAWLfubNRkxyx9PLDuCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNETHw7xCSb7LUj92KtwDlj8xtMMJJVtR7FchvB3GfCkmcrBzKqICud3eOnW%2FEaPnR8juPU%2FMqcbuflxM2EluOEKZWkWeWEnxW3HN3Q9xh1v5MofBpPjik3we7bPA3hUdVN47Q1gD8IpjqP25YYCVC%2Be2bfr5gqc1fvFgVUiG5n5SPTu9oxgWx6aYHnp9PxYOkcq%2BbaNzbsdqVHf%2FNzzvjKKLQQZPyOWashjit2aEfgoofZg4VUCaRoZgcYPDek3aFK9L%2BDkF%2BnYaTgu%2FI0G1q6WPZlOJm0C27arCN127%2B4EZd08CpCbGNVflksktxckhIYnuHwCHFltJTAa7Y0BEBPg9HygKVGpQjuCJlwmci8opw1aZCUCayYgAEGeNeXcC8aqS%2Bd%2B8s8FHXODlIibomKbFmq6aLrQ%2BsO0qgzKj%2FcBc%2BOdxxVqI6J0ujMmpYfC2Y4WjCMUsTavBcCuluXaIrTWphgqoLP8Q%2F6xegkUMrpQaiDyxeoZ0JHMLoSPN152zpa61JLcVuVuy6B217KqBNxrkZHO7lKaGlAIToofOWIOY1NxY3VxSrzCqNaxKGa%2FpjwcEe9yPNNT84PpfGfmvTU9e%2Bp93vhlNcAk36au8WYnT7SHkgyhvXe83gDoOjpRnlpdIqqpM0ZkXPfow0uD2zgY6pgGro%2FNi4VQiGELWPx2RvNwZDQaRE1RJVCJhNjt9cPPqVqFOAyYLH%2FB2Cmlk9%2Ba7VKymoP3YPqjUCwhZiqR7wSScN35RayASeLjzgbFpJbHraJYybglhCREpEeQSjD2YaCnZnC9iIk7s3z91qQ7apYipMPMUICp5wEswV5V32DDK%2F32w5e%2By%2FDq6edY%2BAlF7HvZlX1U9w9YDMOp26mfMx0CvaSj%2BkuLV&X-Amz-Signature=5b26d7d9c3d64d43ae7d21d8648a29c3b5c6fcffcdfc06bdd67128de5bd17629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWNBVV3A%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1WmHfKjjdxYcv8YG4OJn9esJ5ZZ1bvY5GBG2cZc%2BoiAiBdF%2BmO8lrB2iyNJwmFuUkojUhqAWLfubNRkxyx9PLDuCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNETHw7xCSb7LUj92KtwDlj8xtMMJJVtR7FchvB3GfCkmcrBzKqICud3eOnW%2FEaPnR8juPU%2FMqcbuflxM2EluOEKZWkWeWEnxW3HN3Q9xh1v5MofBpPjik3we7bPA3hUdVN47Q1gD8IpjqP25YYCVC%2Be2bfr5gqc1fvFgVUiG5n5SPTu9oxgWx6aYHnp9PxYOkcq%2BbaNzbsdqVHf%2FNzzvjKKLQQZPyOWashjit2aEfgoofZg4VUCaRoZgcYPDek3aFK9L%2BDkF%2BnYaTgu%2FI0G1q6WPZlOJm0C27arCN127%2B4EZd08CpCbGNVflksktxckhIYnuHwCHFltJTAa7Y0BEBPg9HygKVGpQjuCJlwmci8opw1aZCUCayYgAEGeNeXcC8aqS%2Bd%2B8s8FHXODlIibomKbFmq6aLrQ%2BsO0qgzKj%2FcBc%2BOdxxVqI6J0ujMmpYfC2Y4WjCMUsTavBcCuluXaIrTWphgqoLP8Q%2F6xegkUMrpQaiDyxeoZ0JHMLoSPN152zpa61JLcVuVuy6B217KqBNxrkZHO7lKaGlAIToofOWIOY1NxY3VxSrzCqNaxKGa%2FpjwcEe9yPNNT84PpfGfmvTU9e%2Bp93vhlNcAk36au8WYnT7SHkgyhvXe83gDoOjpRnlpdIqqpM0ZkXPfow0uD2zgY6pgGro%2FNi4VQiGELWPx2RvNwZDQaRE1RJVCJhNjt9cPPqVqFOAyYLH%2FB2Cmlk9%2Ba7VKymoP3YPqjUCwhZiqR7wSScN35RayASeLjzgbFpJbHraJYybglhCREpEeQSjD2YaCnZnC9iIk7s3z91qQ7apYipMPMUICp5wEswV5V32DDK%2F32w5e%2By%2FDq6edY%2BAlF7HvZlX1U9w9YDMOp26mfMx0CvaSj%2BkuLV&X-Amz-Signature=e15a6414a87700dbb6116b566c0f721873576dc45f34ad16cc89a0463a046bc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

