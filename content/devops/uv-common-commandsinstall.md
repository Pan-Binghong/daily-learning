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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKSFXRST%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDCuSWhgJljUb9ydjN1Znn6CXu4ucUqs8%2FyNh87z4y0jwIhAPJgjAdKrPzbpwnLgaMrtKHUxlktE6ggDT9i7l4wf9QdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1eBVwFiUdAJfN1Kkq3APLcKa7jZp2B03sFLWBQENx5FKyCqXmGRjf0V5UW0ZKfwSvk8zqD%2Boi7y9dJb6pEMp0UK6Gf3B5PxS%2FCfPcqZN%2BM1ENcMPgleKldUiC7I%2FQQr0rRyVm997Y5pdcslFOo4XTGgptZPjZNXYarrbebMPnncpWDobiLIUNgTYIvsF6UPMVUYZdSc1WcIkMBAdf%2FZEP1%2B62kU0z6sJngETRQwnHsZSNBysZnncxXhJedyZcKjMspS6Lp3hKIswzZZcgR9ptsl3PH6BlIEqCqXypUCT%2FJlFoi%2Fg7evWh3K2OLGAdHMXCIg74jITenvJ%2BfHb8GJ37xX8lQe4BPbIkriHl%2BrgksMRK2QcDBDY5PA6Mg5OpE9VMvhQTkx8Njknh0QaqkQ91mmrTpUQmL8qPyG%2BclzRNQqF2Fw16SruKpPffSfoCoUKs9ZntN0hm61CP9XXKPxJrQbwHKv3Nqa1HWmwSkMCwStoGwoDhTjRS0KIMwdliUeBJrF5XovxRk%2Bz0pS5fDBJs4WmFRDrpQnagbMMwrl93O1%2BDmgg4GCeK0RAa6AWgQxthyMJeYPQZYRHsVl6mspdPaRoNElDRsALyK398W8g20Hdi9wNIbepOEaIQ%2BR5wJfzrOTwTd3d%2FCeXpazCN%2BZzKBjqkAfOPnqBKOIwVcghhyHvrekp%2FJrZBnxStEdqVEAmnqB8vYVAxq8VaJgnOjgCKSwJzMBGRW9iopyGV3LcLvQsVNCJIRBFWwl%2FAGvkxVIA6Cjnvd4whWdzkia4o%2B3whMsyuFfEC2zh0UdztNK0gD48UxbqDlOdBhmHpfEjcgfGmlwmELVCQSr43wmLDUtJlD0fUd%2BA%2Bp8QzxWo0XE05IO2%2FaS4C4uA6&X-Amz-Signature=4c1400af234f5e37151d7d6008dd0b7ea3b6b51ad6efc54f655ea5c6630dd61e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKSFXRST%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDCuSWhgJljUb9ydjN1Znn6CXu4ucUqs8%2FyNh87z4y0jwIhAPJgjAdKrPzbpwnLgaMrtKHUxlktE6ggDT9i7l4wf9QdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1eBVwFiUdAJfN1Kkq3APLcKa7jZp2B03sFLWBQENx5FKyCqXmGRjf0V5UW0ZKfwSvk8zqD%2Boi7y9dJb6pEMp0UK6Gf3B5PxS%2FCfPcqZN%2BM1ENcMPgleKldUiC7I%2FQQr0rRyVm997Y5pdcslFOo4XTGgptZPjZNXYarrbebMPnncpWDobiLIUNgTYIvsF6UPMVUYZdSc1WcIkMBAdf%2FZEP1%2B62kU0z6sJngETRQwnHsZSNBysZnncxXhJedyZcKjMspS6Lp3hKIswzZZcgR9ptsl3PH6BlIEqCqXypUCT%2FJlFoi%2Fg7evWh3K2OLGAdHMXCIg74jITenvJ%2BfHb8GJ37xX8lQe4BPbIkriHl%2BrgksMRK2QcDBDY5PA6Mg5OpE9VMvhQTkx8Njknh0QaqkQ91mmrTpUQmL8qPyG%2BclzRNQqF2Fw16SruKpPffSfoCoUKs9ZntN0hm61CP9XXKPxJrQbwHKv3Nqa1HWmwSkMCwStoGwoDhTjRS0KIMwdliUeBJrF5XovxRk%2Bz0pS5fDBJs4WmFRDrpQnagbMMwrl93O1%2BDmgg4GCeK0RAa6AWgQxthyMJeYPQZYRHsVl6mspdPaRoNElDRsALyK398W8g20Hdi9wNIbepOEaIQ%2BR5wJfzrOTwTd3d%2FCeXpazCN%2BZzKBjqkAfOPnqBKOIwVcghhyHvrekp%2FJrZBnxStEdqVEAmnqB8vYVAxq8VaJgnOjgCKSwJzMBGRW9iopyGV3LcLvQsVNCJIRBFWwl%2FAGvkxVIA6Cjnvd4whWdzkia4o%2B3whMsyuFfEC2zh0UdztNK0gD48UxbqDlOdBhmHpfEjcgfGmlwmELVCQSr43wmLDUtJlD0fUd%2BA%2Bp8QzxWo0XE05IO2%2FaS4C4uA6&X-Amz-Signature=8afebd4f6f98c6057136ba857f1704deec12c718fa1f04ec1819e7f479390eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKSFXRST%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDCuSWhgJljUb9ydjN1Znn6CXu4ucUqs8%2FyNh87z4y0jwIhAPJgjAdKrPzbpwnLgaMrtKHUxlktE6ggDT9i7l4wf9QdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1eBVwFiUdAJfN1Kkq3APLcKa7jZp2B03sFLWBQENx5FKyCqXmGRjf0V5UW0ZKfwSvk8zqD%2Boi7y9dJb6pEMp0UK6Gf3B5PxS%2FCfPcqZN%2BM1ENcMPgleKldUiC7I%2FQQr0rRyVm997Y5pdcslFOo4XTGgptZPjZNXYarrbebMPnncpWDobiLIUNgTYIvsF6UPMVUYZdSc1WcIkMBAdf%2FZEP1%2B62kU0z6sJngETRQwnHsZSNBysZnncxXhJedyZcKjMspS6Lp3hKIswzZZcgR9ptsl3PH6BlIEqCqXypUCT%2FJlFoi%2Fg7evWh3K2OLGAdHMXCIg74jITenvJ%2BfHb8GJ37xX8lQe4BPbIkriHl%2BrgksMRK2QcDBDY5PA6Mg5OpE9VMvhQTkx8Njknh0QaqkQ91mmrTpUQmL8qPyG%2BclzRNQqF2Fw16SruKpPffSfoCoUKs9ZntN0hm61CP9XXKPxJrQbwHKv3Nqa1HWmwSkMCwStoGwoDhTjRS0KIMwdliUeBJrF5XovxRk%2Bz0pS5fDBJs4WmFRDrpQnagbMMwrl93O1%2BDmgg4GCeK0RAa6AWgQxthyMJeYPQZYRHsVl6mspdPaRoNElDRsALyK398W8g20Hdi9wNIbepOEaIQ%2BR5wJfzrOTwTd3d%2FCeXpazCN%2BZzKBjqkAfOPnqBKOIwVcghhyHvrekp%2FJrZBnxStEdqVEAmnqB8vYVAxq8VaJgnOjgCKSwJzMBGRW9iopyGV3LcLvQsVNCJIRBFWwl%2FAGvkxVIA6Cjnvd4whWdzkia4o%2B3whMsyuFfEC2zh0UdztNK0gD48UxbqDlOdBhmHpfEjcgfGmlwmELVCQSr43wmLDUtJlD0fUd%2BA%2Bp8QzxWo0XE05IO2%2FaS4C4uA6&X-Amz-Signature=d77f450afd0b4a82cb589b1de873bf1b0da2095bb4a5375c8775447602dc4038&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

