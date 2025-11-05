---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SALPVTHQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLzFxl5vxjYFAUGAwMAlsK7T4fULeaoL1D9LNg28%2FscwIhAN4zuRZ%2FzXsKCuSmyG8PEq7t%2BAb3H%2BMkFVVEFTJcwWFVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLax4tk2nv0GyyJWQq3APjKWB6MguG6Q2h91%2FjVu2eMPtj0DI%2Bu1kD3X2yzrNpEFgVVKDZhF%2BNPDfGKD5XXB9EAV8bIaxKhlGMvXAmpKOIZTrH%2F0s3jiIn4hESZA%2FgolqZSULZTAgdSuVvTns4tJ7y1nQ%2BYq14s7hWLxVLnRgjD%2B8OeShZiMtudGUCCbk%2Fal6F0uIavf%2FkoOk9QCi2iRvXF1soLAAHz99J8huBGUHpqIwsLjMgJsJr6ozkn40rtQUTOD2TI9OWKrdNmnin8422mLLx%2FCcTQLypFTWDtfZhvQMHSJkzSufSLc8Dd0gV24W%2Flog6hDGkyhbnvJatuzDXSYhvjcwc5CVud0QhDQGM51Bjl%2BCpEcdb7GHq%2BJGWoE3p1%2FJCt%2BLQO2l3C%2Bi5X7KyOFDwSCGOm2qI2NKl46BVOyjS8jhv5ro8WB8FCz8DYq2Qp3cRK3oXQXi%2B76L1coB2dMyn%2BmcWFFYIUYxVHvB1309dEcbv8hSeFcLFqu8GZRr1VrsVG%2B1UY9gNmDZ9c9Ces0Re1r43zHy09U7dH3TVUZ3dPF7fOh8OvajPSX%2BZHN984JYGLsiIlZVfmcoL9nUkO0h8QJXs8SfBigapoMVkPx9ZJ6ePnSzJ0bItjW2FaEV%2FNMQekXdlExytCDD%2BoqzIBjqkASNRB9v7L2w8PByTctlO0dl6nmjRMNdU3Y2CorYALxdMnGCfjStRx4i%2BQ4%2F7q1ONsYvcToeKhEEoHbl82F9kw9Dnc%2FiNabKQRdogP79n0lG18NIWBevzN9%2BXK2tQVzYLukEtQxdjU9c4y%2FWu3aOtpFPodXRWi7w7RDyy1CSCZJFHPrlLVjp%2B4vKveDpFfXKtt5BvjW2e%2FsgGi87KnwHDEsLbvJME&X-Amz-Signature=6a6bef76573ea35f1ea4c09ac4dacf763b49a871fe83d570ec961b6072dbc96c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SALPVTHQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLzFxl5vxjYFAUGAwMAlsK7T4fULeaoL1D9LNg28%2FscwIhAN4zuRZ%2FzXsKCuSmyG8PEq7t%2BAb3H%2BMkFVVEFTJcwWFVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLax4tk2nv0GyyJWQq3APjKWB6MguG6Q2h91%2FjVu2eMPtj0DI%2Bu1kD3X2yzrNpEFgVVKDZhF%2BNPDfGKD5XXB9EAV8bIaxKhlGMvXAmpKOIZTrH%2F0s3jiIn4hESZA%2FgolqZSULZTAgdSuVvTns4tJ7y1nQ%2BYq14s7hWLxVLnRgjD%2B8OeShZiMtudGUCCbk%2Fal6F0uIavf%2FkoOk9QCi2iRvXF1soLAAHz99J8huBGUHpqIwsLjMgJsJr6ozkn40rtQUTOD2TI9OWKrdNmnin8422mLLx%2FCcTQLypFTWDtfZhvQMHSJkzSufSLc8Dd0gV24W%2Flog6hDGkyhbnvJatuzDXSYhvjcwc5CVud0QhDQGM51Bjl%2BCpEcdb7GHq%2BJGWoE3p1%2FJCt%2BLQO2l3C%2Bi5X7KyOFDwSCGOm2qI2NKl46BVOyjS8jhv5ro8WB8FCz8DYq2Qp3cRK3oXQXi%2B76L1coB2dMyn%2BmcWFFYIUYxVHvB1309dEcbv8hSeFcLFqu8GZRr1VrsVG%2B1UY9gNmDZ9c9Ces0Re1r43zHy09U7dH3TVUZ3dPF7fOh8OvajPSX%2BZHN984JYGLsiIlZVfmcoL9nUkO0h8QJXs8SfBigapoMVkPx9ZJ6ePnSzJ0bItjW2FaEV%2FNMQekXdlExytCDD%2BoqzIBjqkASNRB9v7L2w8PByTctlO0dl6nmjRMNdU3Y2CorYALxdMnGCfjStRx4i%2BQ4%2F7q1ONsYvcToeKhEEoHbl82F9kw9Dnc%2FiNabKQRdogP79n0lG18NIWBevzN9%2BXK2tQVzYLukEtQxdjU9c4y%2FWu3aOtpFPodXRWi7w7RDyy1CSCZJFHPrlLVjp%2B4vKveDpFfXKtt5BvjW2e%2FsgGi87KnwHDEsLbvJME&X-Amz-Signature=48ebb19a8b1e3bea728a8113162f87d8cf38074ba5f873e949fbbfa0ba56b837&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SALPVTHQ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLzFxl5vxjYFAUGAwMAlsK7T4fULeaoL1D9LNg28%2FscwIhAN4zuRZ%2FzXsKCuSmyG8PEq7t%2BAb3H%2BMkFVVEFTJcwWFVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLax4tk2nv0GyyJWQq3APjKWB6MguG6Q2h91%2FjVu2eMPtj0DI%2Bu1kD3X2yzrNpEFgVVKDZhF%2BNPDfGKD5XXB9EAV8bIaxKhlGMvXAmpKOIZTrH%2F0s3jiIn4hESZA%2FgolqZSULZTAgdSuVvTns4tJ7y1nQ%2BYq14s7hWLxVLnRgjD%2B8OeShZiMtudGUCCbk%2Fal6F0uIavf%2FkoOk9QCi2iRvXF1soLAAHz99J8huBGUHpqIwsLjMgJsJr6ozkn40rtQUTOD2TI9OWKrdNmnin8422mLLx%2FCcTQLypFTWDtfZhvQMHSJkzSufSLc8Dd0gV24W%2Flog6hDGkyhbnvJatuzDXSYhvjcwc5CVud0QhDQGM51Bjl%2BCpEcdb7GHq%2BJGWoE3p1%2FJCt%2BLQO2l3C%2Bi5X7KyOFDwSCGOm2qI2NKl46BVOyjS8jhv5ro8WB8FCz8DYq2Qp3cRK3oXQXi%2B76L1coB2dMyn%2BmcWFFYIUYxVHvB1309dEcbv8hSeFcLFqu8GZRr1VrsVG%2B1UY9gNmDZ9c9Ces0Re1r43zHy09U7dH3TVUZ3dPF7fOh8OvajPSX%2BZHN984JYGLsiIlZVfmcoL9nUkO0h8QJXs8SfBigapoMVkPx9ZJ6ePnSzJ0bItjW2FaEV%2FNMQekXdlExytCDD%2BoqzIBjqkASNRB9v7L2w8PByTctlO0dl6nmjRMNdU3Y2CorYALxdMnGCfjStRx4i%2BQ4%2F7q1ONsYvcToeKhEEoHbl82F9kw9Dnc%2FiNabKQRdogP79n0lG18NIWBevzN9%2BXK2tQVzYLukEtQxdjU9c4y%2FWu3aOtpFPodXRWi7w7RDyy1CSCZJFHPrlLVjp%2B4vKveDpFfXKtt5BvjW2e%2FsgGi87KnwHDEsLbvJME&X-Amz-Signature=7fc89010f6384be4e905c610316aa7aa0d55f3aad43dab12d98f19937e9d9c9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

