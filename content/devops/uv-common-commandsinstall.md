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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672CNHQHT%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6eK%2BYrVo9E0PysPqjHBSeEsQ5UgaxMUjEdcFc%2F28NTgIhANFeL1W4Yhiz1uaiA3%2FoKHekCdSrowdi8eiBzPY1Z93GKv8DCGIQABoMNjM3NDIzMTgzODA1IgyKIUkMapnZK8Nr1FQq3AOgparcmNc8IO9Gb2VKQmlHxXuirYNltIvVs5Guqbh9Qz%2FxAwTHP%2BnujH9b3u98WygPfl%2Fqq9wC7%2FjW7Qrw8xTP6%2FwI27Fl7lL0dRqQOkc6EIrvlT4bo6XlUVFg2nQFZPzdGKDZk6LthU7LHH7q5kHEY3zA0ss32H18vcw1QceR2it9Ux2Nx9Pe%2B%2F%2FUe3R6%2BysOcIJBcoehj0eN8OmGbO0ETBTN7a0NnSnYM0SuDvrQVlKsmvy5FNziXdVmvOc46BMc6uY0%2BslmOIxQBlYUnGkg2Z1C5NFLZ%2BvrHnzXpKJoM4D86Y%2FKqm3QnZLf24VceDuTH65BwagK9rUZjKn%2BmVs5Ip93mN5Wt5s67f%2BBVlAZaAOrYL6%2BdipjLcXlvdyOr3X67nYpSGA%2FtLl8B55G7swvs9Yazp4whJH9w44aQrX9PHZSFNSc3HHmqPLisR7uPSNUEjYYIiBlCUN2qNqhKcrrUFDjZdhNvoKdK6B7Qlor8qTv%2BwMQqwbRAgDJ6FiPMzbJhMIOhgf10TUwhvXyAY584%2FLpG98adCDeAxeTjHrIZMQhiJN4vERO47OIaVGJIQsVCynHYkGGS3e352%2FHdK7%2BDyPGhm2brxyNDiKTF7TfNEqz6fu7JVTWiDywrjCw5rzKBjqkAcnGLb49QxFZB6%2Be0rKNKs%2FtGDiwff%2BZ9sVzNLC1HCvIlru%2FI2wBFQMMU016dEkdSTpu6F6Ze8WqRsc1ubh5%2BR9VXCcIg7LmE6c6gJ7h7fiAOeq2ZHFcUB8pxbZisQzrNeDoKBYayhxTDFtehJ33ptnGjaFZ35XcsSbnvDeTjKx2Twlybta%2FXF1jzsolwfswZKGTg%2Ff5UcrVO16QjiWIG3zVeqc%2B&X-Amz-Signature=144855ad3f88ff8efc0352ac51ec65abe864c53a6344d7493490fe3a7ad28381&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672CNHQHT%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6eK%2BYrVo9E0PysPqjHBSeEsQ5UgaxMUjEdcFc%2F28NTgIhANFeL1W4Yhiz1uaiA3%2FoKHekCdSrowdi8eiBzPY1Z93GKv8DCGIQABoMNjM3NDIzMTgzODA1IgyKIUkMapnZK8Nr1FQq3AOgparcmNc8IO9Gb2VKQmlHxXuirYNltIvVs5Guqbh9Qz%2FxAwTHP%2BnujH9b3u98WygPfl%2Fqq9wC7%2FjW7Qrw8xTP6%2FwI27Fl7lL0dRqQOkc6EIrvlT4bo6XlUVFg2nQFZPzdGKDZk6LthU7LHH7q5kHEY3zA0ss32H18vcw1QceR2it9Ux2Nx9Pe%2B%2F%2FUe3R6%2BysOcIJBcoehj0eN8OmGbO0ETBTN7a0NnSnYM0SuDvrQVlKsmvy5FNziXdVmvOc46BMc6uY0%2BslmOIxQBlYUnGkg2Z1C5NFLZ%2BvrHnzXpKJoM4D86Y%2FKqm3QnZLf24VceDuTH65BwagK9rUZjKn%2BmVs5Ip93mN5Wt5s67f%2BBVlAZaAOrYL6%2BdipjLcXlvdyOr3X67nYpSGA%2FtLl8B55G7swvs9Yazp4whJH9w44aQrX9PHZSFNSc3HHmqPLisR7uPSNUEjYYIiBlCUN2qNqhKcrrUFDjZdhNvoKdK6B7Qlor8qTv%2BwMQqwbRAgDJ6FiPMzbJhMIOhgf10TUwhvXyAY584%2FLpG98adCDeAxeTjHrIZMQhiJN4vERO47OIaVGJIQsVCynHYkGGS3e352%2FHdK7%2BDyPGhm2brxyNDiKTF7TfNEqz6fu7JVTWiDywrjCw5rzKBjqkAcnGLb49QxFZB6%2Be0rKNKs%2FtGDiwff%2BZ9sVzNLC1HCvIlru%2FI2wBFQMMU016dEkdSTpu6F6Ze8WqRsc1ubh5%2BR9VXCcIg7LmE6c6gJ7h7fiAOeq2ZHFcUB8pxbZisQzrNeDoKBYayhxTDFtehJ33ptnGjaFZ35XcsSbnvDeTjKx2Twlybta%2FXF1jzsolwfswZKGTg%2Ff5UcrVO16QjiWIG3zVeqc%2B&X-Amz-Signature=1a414b40b71df364a91823e6374bb12e9ed0c1f562a10d353e611e14800695b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672CNHQHT%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6eK%2BYrVo9E0PysPqjHBSeEsQ5UgaxMUjEdcFc%2F28NTgIhANFeL1W4Yhiz1uaiA3%2FoKHekCdSrowdi8eiBzPY1Z93GKv8DCGIQABoMNjM3NDIzMTgzODA1IgyKIUkMapnZK8Nr1FQq3AOgparcmNc8IO9Gb2VKQmlHxXuirYNltIvVs5Guqbh9Qz%2FxAwTHP%2BnujH9b3u98WygPfl%2Fqq9wC7%2FjW7Qrw8xTP6%2FwI27Fl7lL0dRqQOkc6EIrvlT4bo6XlUVFg2nQFZPzdGKDZk6LthU7LHH7q5kHEY3zA0ss32H18vcw1QceR2it9Ux2Nx9Pe%2B%2F%2FUe3R6%2BysOcIJBcoehj0eN8OmGbO0ETBTN7a0NnSnYM0SuDvrQVlKsmvy5FNziXdVmvOc46BMc6uY0%2BslmOIxQBlYUnGkg2Z1C5NFLZ%2BvrHnzXpKJoM4D86Y%2FKqm3QnZLf24VceDuTH65BwagK9rUZjKn%2BmVs5Ip93mN5Wt5s67f%2BBVlAZaAOrYL6%2BdipjLcXlvdyOr3X67nYpSGA%2FtLl8B55G7swvs9Yazp4whJH9w44aQrX9PHZSFNSc3HHmqPLisR7uPSNUEjYYIiBlCUN2qNqhKcrrUFDjZdhNvoKdK6B7Qlor8qTv%2BwMQqwbRAgDJ6FiPMzbJhMIOhgf10TUwhvXyAY584%2FLpG98adCDeAxeTjHrIZMQhiJN4vERO47OIaVGJIQsVCynHYkGGS3e352%2FHdK7%2BDyPGhm2brxyNDiKTF7TfNEqz6fu7JVTWiDywrjCw5rzKBjqkAcnGLb49QxFZB6%2Be0rKNKs%2FtGDiwff%2BZ9sVzNLC1HCvIlru%2FI2wBFQMMU016dEkdSTpu6F6Ze8WqRsc1ubh5%2BR9VXCcIg7LmE6c6gJ7h7fiAOeq2ZHFcUB8pxbZisQzrNeDoKBYayhxTDFtehJ33ptnGjaFZ35XcsSbnvDeTjKx2Twlybta%2FXF1jzsolwfswZKGTg%2Ff5UcrVO16QjiWIG3zVeqc%2B&X-Amz-Signature=1d139ca471ffc3c30bdc50e35f1839e942a24732f5665c1a9b1e2bdefb8e431e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

