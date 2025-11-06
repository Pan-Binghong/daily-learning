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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGAT7ZAH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEO6VXCVyeBMDmtHaPFVfOXGlXpeoRCLNtZswXxpCiKGAiB2Sf8utrwq43NizMxnyknx6nGSzrpTS3k%2BdYTZTtklJiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqK0Ut7EBOHM11yXGKtwDWTfnGaDdHZ7tzVDRnSPcKOnf3lWH5c7yxhpyCz%2BdROoCdZ26nV3kWJ%2BFcGNN6GL%2BP1vDY2Yhjz6HkipRnR0eciWqo8mfhfdVhuVWSLvYX0S7UiX%2BRbEgJ9xdaWRGUOf3Y5BQYC%2BosN8oafQvnHLmtlqPLWK2cGnAsl6lxOjnNb2ycQAwyjDK3zGY76mz%2BVdxJmPXFraoJdAJGNgkbD9B7Q3jQQUQrH6cu4tVs3ABE7NEK1E1dEnhmVURfT7l%2BPC7S2u7iYdU1HOi7gYlBXqbAClrIs9B3xTgE%2Fm3i9GX2NHHOE%2FqYaw%2BCSgYFrfhVRg2ikSKfo%2BnSqG1Y%2FjEFFVq6yWWyPRiG9TISe1HaB%2BXU9dAKHBAJKxeCPLzFgDJwrSFPZcGQDRCNpzrQMy6btpkuOzsiDDwO5aNHtwHoZ%2BNmY4SkOJSGqFV8b0plUcukPEy4rIuk%2FogXwPYKGGTH64TU6gFcOZG%2F1XDWN3a0%2Bt%2BD6wgvHEoRYD%2BM7D8eSLIWnJsZnhOwYJIdrXvG0WiTI7flvI0%2BeI18qu7K9af5P6W1cKNSxMWagk%2FUnYPuZ9X7c87JtLvs1DlhN2FEb0CBwPVLOtH4rodjPFVIIotAkIBhjXq3oNy8E2vUyRO14cwkvCvyAY6pgEbvwVG1JGr%2FbL6KDJFtNHDjo%2FZKDOdbVe2%2FknlERmx%2BxboldsV%2B8Idhh8Mn0zjW%2FyMrRcfhir%2BsWyony50d2C6J%2BpNEVPY0fYBHx%2F6srv5JgWRbSErfTQlpKdkF%2FRjtcejXV292DV2I8LUB46xfUZJqIcTaKXy0Xe6aV3VmZ2dGAikWza%2BR21hVMvgaWQEJROVHrJT0oxE0QlRQvQpD0ZJWZ7GIAy6&X-Amz-Signature=d7fc8388c2dce98d70808343e01d2d3a94961352c17bda2a2c31974be35e1144&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGAT7ZAH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEO6VXCVyeBMDmtHaPFVfOXGlXpeoRCLNtZswXxpCiKGAiB2Sf8utrwq43NizMxnyknx6nGSzrpTS3k%2BdYTZTtklJiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqK0Ut7EBOHM11yXGKtwDWTfnGaDdHZ7tzVDRnSPcKOnf3lWH5c7yxhpyCz%2BdROoCdZ26nV3kWJ%2BFcGNN6GL%2BP1vDY2Yhjz6HkipRnR0eciWqo8mfhfdVhuVWSLvYX0S7UiX%2BRbEgJ9xdaWRGUOf3Y5BQYC%2BosN8oafQvnHLmtlqPLWK2cGnAsl6lxOjnNb2ycQAwyjDK3zGY76mz%2BVdxJmPXFraoJdAJGNgkbD9B7Q3jQQUQrH6cu4tVs3ABE7NEK1E1dEnhmVURfT7l%2BPC7S2u7iYdU1HOi7gYlBXqbAClrIs9B3xTgE%2Fm3i9GX2NHHOE%2FqYaw%2BCSgYFrfhVRg2ikSKfo%2BnSqG1Y%2FjEFFVq6yWWyPRiG9TISe1HaB%2BXU9dAKHBAJKxeCPLzFgDJwrSFPZcGQDRCNpzrQMy6btpkuOzsiDDwO5aNHtwHoZ%2BNmY4SkOJSGqFV8b0plUcukPEy4rIuk%2FogXwPYKGGTH64TU6gFcOZG%2F1XDWN3a0%2Bt%2BD6wgvHEoRYD%2BM7D8eSLIWnJsZnhOwYJIdrXvG0WiTI7flvI0%2BeI18qu7K9af5P6W1cKNSxMWagk%2FUnYPuZ9X7c87JtLvs1DlhN2FEb0CBwPVLOtH4rodjPFVIIotAkIBhjXq3oNy8E2vUyRO14cwkvCvyAY6pgEbvwVG1JGr%2FbL6KDJFtNHDjo%2FZKDOdbVe2%2FknlERmx%2BxboldsV%2B8Idhh8Mn0zjW%2FyMrRcfhir%2BsWyony50d2C6J%2BpNEVPY0fYBHx%2F6srv5JgWRbSErfTQlpKdkF%2FRjtcejXV292DV2I8LUB46xfUZJqIcTaKXy0Xe6aV3VmZ2dGAikWza%2BR21hVMvgaWQEJROVHrJT0oxE0QlRQvQpD0ZJWZ7GIAy6&X-Amz-Signature=291eebf31c6ec933ac8aecdfb93ec1d52c1cdd0dfc1461cc53eccc6c2e3d1eb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGAT7ZAH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEO6VXCVyeBMDmtHaPFVfOXGlXpeoRCLNtZswXxpCiKGAiB2Sf8utrwq43NizMxnyknx6nGSzrpTS3k%2BdYTZTtklJiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqK0Ut7EBOHM11yXGKtwDWTfnGaDdHZ7tzVDRnSPcKOnf3lWH5c7yxhpyCz%2BdROoCdZ26nV3kWJ%2BFcGNN6GL%2BP1vDY2Yhjz6HkipRnR0eciWqo8mfhfdVhuVWSLvYX0S7UiX%2BRbEgJ9xdaWRGUOf3Y5BQYC%2BosN8oafQvnHLmtlqPLWK2cGnAsl6lxOjnNb2ycQAwyjDK3zGY76mz%2BVdxJmPXFraoJdAJGNgkbD9B7Q3jQQUQrH6cu4tVs3ABE7NEK1E1dEnhmVURfT7l%2BPC7S2u7iYdU1HOi7gYlBXqbAClrIs9B3xTgE%2Fm3i9GX2NHHOE%2FqYaw%2BCSgYFrfhVRg2ikSKfo%2BnSqG1Y%2FjEFFVq6yWWyPRiG9TISe1HaB%2BXU9dAKHBAJKxeCPLzFgDJwrSFPZcGQDRCNpzrQMy6btpkuOzsiDDwO5aNHtwHoZ%2BNmY4SkOJSGqFV8b0plUcukPEy4rIuk%2FogXwPYKGGTH64TU6gFcOZG%2F1XDWN3a0%2Bt%2BD6wgvHEoRYD%2BM7D8eSLIWnJsZnhOwYJIdrXvG0WiTI7flvI0%2BeI18qu7K9af5P6W1cKNSxMWagk%2FUnYPuZ9X7c87JtLvs1DlhN2FEb0CBwPVLOtH4rodjPFVIIotAkIBhjXq3oNy8E2vUyRO14cwkvCvyAY6pgEbvwVG1JGr%2FbL6KDJFtNHDjo%2FZKDOdbVe2%2FknlERmx%2BxboldsV%2B8Idhh8Mn0zjW%2FyMrRcfhir%2BsWyony50d2C6J%2BpNEVPY0fYBHx%2F6srv5JgWRbSErfTQlpKdkF%2FRjtcejXV292DV2I8LUB46xfUZJqIcTaKXy0Xe6aV3VmZ2dGAikWza%2BR21hVMvgaWQEJROVHrJT0oxE0QlRQvQpD0ZJWZ7GIAy6&X-Amz-Signature=a508b162f0c3410273925b0bb36a7301185e441912243af93d09333eaabc6f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

