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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3TZPYI%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFdvqqlXbAuPt9EbajxSD4o7WUbJi7UlZ4qvfyNpSEPAiEA3DHcs98kSMlS4m5xXFaEdl%2F3qs2dFFNqxBQpy7tUGhwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXL2RnzvHojkAwwOyrcA8nhYktGQckhUbNjwvsChN%2FTC8ssKMmbXIA8eB1ZzXH9jrRbQTNavbuHeWLr49Zcm0CG3aB7mBXLz%2B2OO5Xeq376RS7WpwslwLxkVRbAk%2BqQFFzzNv6tolsV6zjJZCPE4r8V9qY7DMooxmF%2BdMAWM2W2L%2B9WPBLeN7SJSx0%2BYHkp7yLdYo4No5xDsCGmyAx21y8dgD%2FvtQWg87C21yuyykKOYHw0k0QRFjx7qWCURyrE2x6RX9YeCqMECaegj0N5NiMKI9Uq3daaTnRQr8m0dmGvVtUrc%2FGirHRAevsfFfVLYnTfAcOWttYL3jEumztFtvOvzKfaQrvw5PBX4RzfMU9gUWA04biH1YhTXaANlA6QUz6RMk8RE6Kh5mp%2F33eD2O5QGmOybU%2Bn6JzLVQvmCQDtpkxKVRGtrkuyHAFUeQ5AJr1MwpZHW4sIz6e2Cb9n4AqolpuuSlOCW1e7cIytWzKl6HzIf5mzaEPxo4IkkL8DxmkOyRTlSQS9AXjJ7mWEGfCmbzgHBN3U%2BVNyM9sFnUdK2sBAWai0svj%2B6ZdgJxNSsvGJwLKHaIHVh3s%2FPtHCiO9Kwp6o5sok4IQm5mIOYHHZM3USYlZ9Kx%2FElzTU21tJqaPdOPYdAMozcVWiMPaB080GOqUBxSjLWJgMvVWw0NcdEcZ3TRZIK8u2vZmKbiHBVuc845B4xasjMpzzzstlOkc0%2FOx6%2BTk3Zq130wyKTVReNJvQiPaUIu8HnctdFcOuBIvsi86SexJFhP55JYzpRk6yaEqNM%2BPjJg%2Fc0Kyy4iZ6EOT6c%2F5dZjrmk%2FooP6XTK2YQwKufMXLZ7dVMxXjs%2FMLeDamDTgDB0XsU7b35WXfJMepDSYF4Hjmo&X-Amz-Signature=c3857e64e5a2cc850e72d738d41311dc402dc91d3895112d5f73ec3110309cc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3TZPYI%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFdvqqlXbAuPt9EbajxSD4o7WUbJi7UlZ4qvfyNpSEPAiEA3DHcs98kSMlS4m5xXFaEdl%2F3qs2dFFNqxBQpy7tUGhwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXL2RnzvHojkAwwOyrcA8nhYktGQckhUbNjwvsChN%2FTC8ssKMmbXIA8eB1ZzXH9jrRbQTNavbuHeWLr49Zcm0CG3aB7mBXLz%2B2OO5Xeq376RS7WpwslwLxkVRbAk%2BqQFFzzNv6tolsV6zjJZCPE4r8V9qY7DMooxmF%2BdMAWM2W2L%2B9WPBLeN7SJSx0%2BYHkp7yLdYo4No5xDsCGmyAx21y8dgD%2FvtQWg87C21yuyykKOYHw0k0QRFjx7qWCURyrE2x6RX9YeCqMECaegj0N5NiMKI9Uq3daaTnRQr8m0dmGvVtUrc%2FGirHRAevsfFfVLYnTfAcOWttYL3jEumztFtvOvzKfaQrvw5PBX4RzfMU9gUWA04biH1YhTXaANlA6QUz6RMk8RE6Kh5mp%2F33eD2O5QGmOybU%2Bn6JzLVQvmCQDtpkxKVRGtrkuyHAFUeQ5AJr1MwpZHW4sIz6e2Cb9n4AqolpuuSlOCW1e7cIytWzKl6HzIf5mzaEPxo4IkkL8DxmkOyRTlSQS9AXjJ7mWEGfCmbzgHBN3U%2BVNyM9sFnUdK2sBAWai0svj%2B6ZdgJxNSsvGJwLKHaIHVh3s%2FPtHCiO9Kwp6o5sok4IQm5mIOYHHZM3USYlZ9Kx%2FElzTU21tJqaPdOPYdAMozcVWiMPaB080GOqUBxSjLWJgMvVWw0NcdEcZ3TRZIK8u2vZmKbiHBVuc845B4xasjMpzzzstlOkc0%2FOx6%2BTk3Zq130wyKTVReNJvQiPaUIu8HnctdFcOuBIvsi86SexJFhP55JYzpRk6yaEqNM%2BPjJg%2Fc0Kyy4iZ6EOT6c%2F5dZjrmk%2FooP6XTK2YQwKufMXLZ7dVMxXjs%2FMLeDamDTgDB0XsU7b35WXfJMepDSYF4Hjmo&X-Amz-Signature=4f33799a389f8756978e5c4e75145a2b91bb44afb1b9504bf991a2609f6b2bae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK3TZPYI%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFdvqqlXbAuPt9EbajxSD4o7WUbJi7UlZ4qvfyNpSEPAiEA3DHcs98kSMlS4m5xXFaEdl%2F3qs2dFFNqxBQpy7tUGhwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXL2RnzvHojkAwwOyrcA8nhYktGQckhUbNjwvsChN%2FTC8ssKMmbXIA8eB1ZzXH9jrRbQTNavbuHeWLr49Zcm0CG3aB7mBXLz%2B2OO5Xeq376RS7WpwslwLxkVRbAk%2BqQFFzzNv6tolsV6zjJZCPE4r8V9qY7DMooxmF%2BdMAWM2W2L%2B9WPBLeN7SJSx0%2BYHkp7yLdYo4No5xDsCGmyAx21y8dgD%2FvtQWg87C21yuyykKOYHw0k0QRFjx7qWCURyrE2x6RX9YeCqMECaegj0N5NiMKI9Uq3daaTnRQr8m0dmGvVtUrc%2FGirHRAevsfFfVLYnTfAcOWttYL3jEumztFtvOvzKfaQrvw5PBX4RzfMU9gUWA04biH1YhTXaANlA6QUz6RMk8RE6Kh5mp%2F33eD2O5QGmOybU%2Bn6JzLVQvmCQDtpkxKVRGtrkuyHAFUeQ5AJr1MwpZHW4sIz6e2Cb9n4AqolpuuSlOCW1e7cIytWzKl6HzIf5mzaEPxo4IkkL8DxmkOyRTlSQS9AXjJ7mWEGfCmbzgHBN3U%2BVNyM9sFnUdK2sBAWai0svj%2B6ZdgJxNSsvGJwLKHaIHVh3s%2FPtHCiO9Kwp6o5sok4IQm5mIOYHHZM3USYlZ9Kx%2FElzTU21tJqaPdOPYdAMozcVWiMPaB080GOqUBxSjLWJgMvVWw0NcdEcZ3TRZIK8u2vZmKbiHBVuc845B4xasjMpzzzstlOkc0%2FOx6%2BTk3Zq130wyKTVReNJvQiPaUIu8HnctdFcOuBIvsi86SexJFhP55JYzpRk6yaEqNM%2BPjJg%2Fc0Kyy4iZ6EOT6c%2F5dZjrmk%2FooP6XTK2YQwKufMXLZ7dVMxXjs%2FMLeDamDTgDB0XsU7b35WXfJMepDSYF4Hjmo&X-Amz-Signature=c39dc3c7844f0bb8fef53ffd8724628b487d24145c573f5f2ab2cb36f8e5c46d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

