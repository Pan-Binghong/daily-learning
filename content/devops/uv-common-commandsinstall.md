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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWFZ7HR%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwzo6rB0c%2BiJvTm%2B9jqBpl91v9OdXboPiQjvz%2BufGihAIgJPAI84xz4bgbejuq6yZErT2awwuyeMoIxXUuq9Pu%2B3AqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKEgQNjKYcQidOnqCrcA%2BGqVKqayjmJW4yXIO6gNVRgp6220R3jyohvYXQfdu%2BeAHQYKHmcIhU7u1HsZsHj4AsuY%2FbCEA%2By1HRMoxRzT%2F1AVZW0q4I9fotrOcuNYyXJmAkyPds8XZCxapeMk3WKzznpGXcoQcFh6NGZ40h9VrJ6Ioz7djPQ3e1ThQXkVKSa5euMnnO3eXQjG4srbd80BswCL9ktclyy335sOteo37g7Zw3zGgIlQQ9K4Zf8KDcf7Opwcdw8B7UZwTUUM7VB1knX%2FidY3NCZNp%2FzCBwEpnUGZuC5g9694miaH08M%2FAVO8RmY22nZ%2FRRmXDdhyPSj9%2F5Cjur81qfY9i5VTScDOQ3%2FrONxMDCH%2BQu6bjAV5Q8UrIFOTMEt4aob%2BkRnV35QOWy67zJQ9ex4zYfsey2EPu%2BuGjXAtibqXxrN0fPckc%2FKSxO%2FhOEstmvZO%2B9dyVh5q3QR5QJIhqkgB4u4rea3TjbSjk4cdL%2FDKpBnECVyECIFhUZRd1xQh1TZhC%2FyJB0rVUUgMsTMZOZvyPxATveLkPHzTASQMBNDnpGxp4JP%2BtU31ZoIB%2FJji9wyP4NqXbnbhffdkTv1CmuP%2Byw3I%2BIgEaypyX0wpjF1z3CI%2BoQA3BFA%2FWu6g20y7g%2BGL9RpMN%2Bp%2FMoGOqUBuuN7u3peUJXp%2B2g6vIL%2B11%2B1Z38c%2FfNnEa01BZJRITyIbZH0vuArJFNgmzJphqUrkevlVwyBukge%2FavrfQiTubC8JK0nbGF94ggEu5AzlyYJevd%2B7qaWMyOLMd9jwMMSLVWrSJpAcK9ir1NC5BwZ%2F%2BcXZRir8GC2UF0phvVV3HP4homZmPsYCKK7jD4Gu8XLbHT5k2lqVIABXN3Pyyy2ZKM2UbWd&X-Amz-Signature=0753c7b1dc4a8a425bde8338a459745acf14de94c49279d46f452a0da3809f10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWFZ7HR%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwzo6rB0c%2BiJvTm%2B9jqBpl91v9OdXboPiQjvz%2BufGihAIgJPAI84xz4bgbejuq6yZErT2awwuyeMoIxXUuq9Pu%2B3AqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKEgQNjKYcQidOnqCrcA%2BGqVKqayjmJW4yXIO6gNVRgp6220R3jyohvYXQfdu%2BeAHQYKHmcIhU7u1HsZsHj4AsuY%2FbCEA%2By1HRMoxRzT%2F1AVZW0q4I9fotrOcuNYyXJmAkyPds8XZCxapeMk3WKzznpGXcoQcFh6NGZ40h9VrJ6Ioz7djPQ3e1ThQXkVKSa5euMnnO3eXQjG4srbd80BswCL9ktclyy335sOteo37g7Zw3zGgIlQQ9K4Zf8KDcf7Opwcdw8B7UZwTUUM7VB1knX%2FidY3NCZNp%2FzCBwEpnUGZuC5g9694miaH08M%2FAVO8RmY22nZ%2FRRmXDdhyPSj9%2F5Cjur81qfY9i5VTScDOQ3%2FrONxMDCH%2BQu6bjAV5Q8UrIFOTMEt4aob%2BkRnV35QOWy67zJQ9ex4zYfsey2EPu%2BuGjXAtibqXxrN0fPckc%2FKSxO%2FhOEstmvZO%2B9dyVh5q3QR5QJIhqkgB4u4rea3TjbSjk4cdL%2FDKpBnECVyECIFhUZRd1xQh1TZhC%2FyJB0rVUUgMsTMZOZvyPxATveLkPHzTASQMBNDnpGxp4JP%2BtU31ZoIB%2FJji9wyP4NqXbnbhffdkTv1CmuP%2Byw3I%2BIgEaypyX0wpjF1z3CI%2BoQA3BFA%2FWu6g20y7g%2BGL9RpMN%2Bp%2FMoGOqUBuuN7u3peUJXp%2B2g6vIL%2B11%2B1Z38c%2FfNnEa01BZJRITyIbZH0vuArJFNgmzJphqUrkevlVwyBukge%2FavrfQiTubC8JK0nbGF94ggEu5AzlyYJevd%2B7qaWMyOLMd9jwMMSLVWrSJpAcK9ir1NC5BwZ%2F%2BcXZRir8GC2UF0phvVV3HP4homZmPsYCKK7jD4Gu8XLbHT5k2lqVIABXN3Pyyy2ZKM2UbWd&X-Amz-Signature=d6bcf393008dd88abb11b2242cc6b734dbe01575f63aa2a167f351f78fbe557d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWFZ7HR%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwzo6rB0c%2BiJvTm%2B9jqBpl91v9OdXboPiQjvz%2BufGihAIgJPAI84xz4bgbejuq6yZErT2awwuyeMoIxXUuq9Pu%2B3AqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKEgQNjKYcQidOnqCrcA%2BGqVKqayjmJW4yXIO6gNVRgp6220R3jyohvYXQfdu%2BeAHQYKHmcIhU7u1HsZsHj4AsuY%2FbCEA%2By1HRMoxRzT%2F1AVZW0q4I9fotrOcuNYyXJmAkyPds8XZCxapeMk3WKzznpGXcoQcFh6NGZ40h9VrJ6Ioz7djPQ3e1ThQXkVKSa5euMnnO3eXQjG4srbd80BswCL9ktclyy335sOteo37g7Zw3zGgIlQQ9K4Zf8KDcf7Opwcdw8B7UZwTUUM7VB1knX%2FidY3NCZNp%2FzCBwEpnUGZuC5g9694miaH08M%2FAVO8RmY22nZ%2FRRmXDdhyPSj9%2F5Cjur81qfY9i5VTScDOQ3%2FrONxMDCH%2BQu6bjAV5Q8UrIFOTMEt4aob%2BkRnV35QOWy67zJQ9ex4zYfsey2EPu%2BuGjXAtibqXxrN0fPckc%2FKSxO%2FhOEstmvZO%2B9dyVh5q3QR5QJIhqkgB4u4rea3TjbSjk4cdL%2FDKpBnECVyECIFhUZRd1xQh1TZhC%2FyJB0rVUUgMsTMZOZvyPxATveLkPHzTASQMBNDnpGxp4JP%2BtU31ZoIB%2FJji9wyP4NqXbnbhffdkTv1CmuP%2Byw3I%2BIgEaypyX0wpjF1z3CI%2BoQA3BFA%2FWu6g20y7g%2BGL9RpMN%2Bp%2FMoGOqUBuuN7u3peUJXp%2B2g6vIL%2B11%2B1Z38c%2FfNnEa01BZJRITyIbZH0vuArJFNgmzJphqUrkevlVwyBukge%2FavrfQiTubC8JK0nbGF94ggEu5AzlyYJevd%2B7qaWMyOLMd9jwMMSLVWrSJpAcK9ir1NC5BwZ%2F%2BcXZRir8GC2UF0phvVV3HP4homZmPsYCKK7jD4Gu8XLbHT5k2lqVIABXN3Pyyy2ZKM2UbWd&X-Amz-Signature=1fedd755d3d814e9697d8f5db7b316de6afb1415935635f6389e34d266a0c0a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

