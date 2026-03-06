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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4AC6AZS%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQD7UAYuUiNal1%2B5zfLZ%2B7aE%2BDfayZO5O3IIE0lLAh2DhAIgRDPrLJmq1DLxX8MLC0x330FS%2Fy7hiDpT5a1un7jPk2QqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFo9DHbZNeItZv9KCrcA%2BRYjuFnq7IwHDLAfahZuwBKQNWhaL%2FNXscEGbupOYDLghzswtQjaPOGmf0QtfFu7JFl%2Bg00cDOh2OMKaBfXRvIIIBiM3eUBCSq%2FaBQm77WkiwTarYnSxoFj%2FmXEE8qfpUYyqeZtIR6JQF%2BnL13ymtDV90JvX%2BTqyKqabQJQkniumsEoA%2FnXGS1%2B5HzeowstMnRtQ2NnVP5hGag2qmPK0wlaMNaBGWeW92nzZmc7Q8TJSdgg07%2B535aq0ZDFlM7yQjJUODA4SS6r3ae9JRtUIE5qec%2FzLVKhrf5b6XhHyi6q1W%2B61LhyiHZjYFuJYjNdg7NxbCUBGJglRnK9fPnFJg6yIJ%2BrIbGJxFhKxiabyLQd9z3z%2BRlcDycjXQdE9pGvGqRicmcVUwq9jL%2FMxZbyKVBp9Xt18UG20Tci1EkcYDRhBjiirOV4u7nbHu8JvLCUJjGhsN4FgogKgbld21iNUr6xxNM44yV7wH7KQwms59M6EUDPWzu%2Fxi1%2BBsg0VVN9yle%2B9VkRv1j7quUGfo2gcqYSZvcWJgAaVLdVWXcOQvg%2FVHEta4uAsvMGopzAMMBPyrrU7%2F981SJ714I7EeEBD4F7U63q5o668TnibIU4nOjswP1JbC9EpVIK3kgoMITQqM0GOqUBdTJz%2FJu1eBOLhH2fLQDL5HlLNmKOT6A0N4BnmTNUaCU1nqeaR5lhYsxX5SN%2FGQng1TKg7%2BZNwZTjzMfkujGF5UjK9SPCL1yIt4AyL9px6uTKVK9yE8LzktKDiRQxssTypZFjeTNd%2F4sNfoULe4R8nSKHw%2BDkWeqzWsyYF8kwmzhkW0JE9EY1RdjD08PVdAbB3Phn5pG5nWycVxvbOSGKaCf78dKV&X-Amz-Signature=c983dc1732af679d5a0c3a91b842ba7124e318772a8fcf038ad5a0a0f462ff01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4AC6AZS%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQD7UAYuUiNal1%2B5zfLZ%2B7aE%2BDfayZO5O3IIE0lLAh2DhAIgRDPrLJmq1DLxX8MLC0x330FS%2Fy7hiDpT5a1un7jPk2QqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFo9DHbZNeItZv9KCrcA%2BRYjuFnq7IwHDLAfahZuwBKQNWhaL%2FNXscEGbupOYDLghzswtQjaPOGmf0QtfFu7JFl%2Bg00cDOh2OMKaBfXRvIIIBiM3eUBCSq%2FaBQm77WkiwTarYnSxoFj%2FmXEE8qfpUYyqeZtIR6JQF%2BnL13ymtDV90JvX%2BTqyKqabQJQkniumsEoA%2FnXGS1%2B5HzeowstMnRtQ2NnVP5hGag2qmPK0wlaMNaBGWeW92nzZmc7Q8TJSdgg07%2B535aq0ZDFlM7yQjJUODA4SS6r3ae9JRtUIE5qec%2FzLVKhrf5b6XhHyi6q1W%2B61LhyiHZjYFuJYjNdg7NxbCUBGJglRnK9fPnFJg6yIJ%2BrIbGJxFhKxiabyLQd9z3z%2BRlcDycjXQdE9pGvGqRicmcVUwq9jL%2FMxZbyKVBp9Xt18UG20Tci1EkcYDRhBjiirOV4u7nbHu8JvLCUJjGhsN4FgogKgbld21iNUr6xxNM44yV7wH7KQwms59M6EUDPWzu%2Fxi1%2BBsg0VVN9yle%2B9VkRv1j7quUGfo2gcqYSZvcWJgAaVLdVWXcOQvg%2FVHEta4uAsvMGopzAMMBPyrrU7%2F981SJ714I7EeEBD4F7U63q5o668TnibIU4nOjswP1JbC9EpVIK3kgoMITQqM0GOqUBdTJz%2FJu1eBOLhH2fLQDL5HlLNmKOT6A0N4BnmTNUaCU1nqeaR5lhYsxX5SN%2FGQng1TKg7%2BZNwZTjzMfkujGF5UjK9SPCL1yIt4AyL9px6uTKVK9yE8LzktKDiRQxssTypZFjeTNd%2F4sNfoULe4R8nSKHw%2BDkWeqzWsyYF8kwmzhkW0JE9EY1RdjD08PVdAbB3Phn5pG5nWycVxvbOSGKaCf78dKV&X-Amz-Signature=467a6a1aaa9c8d3cad29e54f094376c73f9254c93a755aaac86724a320891b9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4AC6AZS%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQD7UAYuUiNal1%2B5zfLZ%2B7aE%2BDfayZO5O3IIE0lLAh2DhAIgRDPrLJmq1DLxX8MLC0x330FS%2Fy7hiDpT5a1un7jPk2QqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDFo9DHbZNeItZv9KCrcA%2BRYjuFnq7IwHDLAfahZuwBKQNWhaL%2FNXscEGbupOYDLghzswtQjaPOGmf0QtfFu7JFl%2Bg00cDOh2OMKaBfXRvIIIBiM3eUBCSq%2FaBQm77WkiwTarYnSxoFj%2FmXEE8qfpUYyqeZtIR6JQF%2BnL13ymtDV90JvX%2BTqyKqabQJQkniumsEoA%2FnXGS1%2B5HzeowstMnRtQ2NnVP5hGag2qmPK0wlaMNaBGWeW92nzZmc7Q8TJSdgg07%2B535aq0ZDFlM7yQjJUODA4SS6r3ae9JRtUIE5qec%2FzLVKhrf5b6XhHyi6q1W%2B61LhyiHZjYFuJYjNdg7NxbCUBGJglRnK9fPnFJg6yIJ%2BrIbGJxFhKxiabyLQd9z3z%2BRlcDycjXQdE9pGvGqRicmcVUwq9jL%2FMxZbyKVBp9Xt18UG20Tci1EkcYDRhBjiirOV4u7nbHu8JvLCUJjGhsN4FgogKgbld21iNUr6xxNM44yV7wH7KQwms59M6EUDPWzu%2Fxi1%2BBsg0VVN9yle%2B9VkRv1j7quUGfo2gcqYSZvcWJgAaVLdVWXcOQvg%2FVHEta4uAsvMGopzAMMBPyrrU7%2F981SJ714I7EeEBD4F7U63q5o668TnibIU4nOjswP1JbC9EpVIK3kgoMITQqM0GOqUBdTJz%2FJu1eBOLhH2fLQDL5HlLNmKOT6A0N4BnmTNUaCU1nqeaR5lhYsxX5SN%2FGQng1TKg7%2BZNwZTjzMfkujGF5UjK9SPCL1yIt4AyL9px6uTKVK9yE8LzktKDiRQxssTypZFjeTNd%2F4sNfoULe4R8nSKHw%2BDkWeqzWsyYF8kwmzhkW0JE9EY1RdjD08PVdAbB3Phn5pG5nWycVxvbOSGKaCf78dKV&X-Amz-Signature=978cf21c73bca678801200ace3cbf346a1f015d4eae10de786b50b910cf4408d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

