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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJX7HFA%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCk9O%2B2jZuvinXB2FGF8a%2Fz15bYEWXq2thyiOkdKZHCawIhANVxv7PWBrenRaJX99ojO2Sw7fReA2oj8Cy%2FxPZeVkA7KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtH7i4ZND%2FKVevj0Eq3ANaECpoEozfF204QJ4GonyeyVTfW9QUJR8NcNH1oIOEPFqi8%2Brrdhgl%2FQ7hIMYU%2Fz0uXIzmNUSE7b1LA0WWEClHptfZz1MqeNoblcFWzEOsSlfoDANwYxBRFUqEXKwJwyH8KrHMqvlO6iJOpWEsOKqYes%2FgKznbHtDgH7c%2BHNVKh9tOBOEhCNBSsYyQZPc2llTT0t%2FY2stjiX5MIUBxPJGi8icA9%2FKtHLR1pPr9eCCT4adou64e5ZTRJN3ZW0AG%2FBID%2BEmJ4XKlnE3TY5iu7vi%2FUfl%2BtVfnseoDMpX1ubbx3iV2PrK1RSSmf0fYjXY17pdOrtcLE0074xNsRgJGeBHvKFHH29yGCp5cfbYsBnd4L7AOPNTVQ%2F0ad54lB3WzPB2h0E8B59Rse7xkBW%2Bhxlv2BsTV2%2BLUTbE%2BJi1cBuuSazJyPTnGxJhBPRh6YWewKYDZTHW1kwoELXZSpU%2BbDZv%2FGgr6PCS4Lm4asj4VDGs43KlL2OQ82LhNXrl4cR8kegJdAbuZHbBzqzoTW8g2%2FwvBsq8hqibGbXwzsB3r0wOJMbNaXCRozuTNz4d3kg4Cs%2B2I1nNM5iP4VsvUIeTjZp6Fr3ijh%2FB8MbT%2BsmtRKhj0VkrAKoEEE5PbDFY22zC3lqXMBjqkAdyn5wARVP7ONeTxJQgTe1gdIF4K45gVptYnEpA78Kwspk4Ga0AZ6O9IaFH11p79PveJDArltJdcrEqbBv2qb%2Fk8igRNHQ5caNKpH80JamV0Kku7rMOP%2Be0pYUFbMHSNVwDRsDBgEesrtNIOy3Hf0OiLAgn%2FMl1BFiY5fjHkQWGQAuXzN8U0jFZxy8fhujUqF4YQOiHKQvJ6qbdtL7xwjc1Toqyb&X-Amz-Signature=4cd727e25a87aa61a268417e6884e51bbdb515738bbb7760ffe2a49f6e02f723&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJX7HFA%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCk9O%2B2jZuvinXB2FGF8a%2Fz15bYEWXq2thyiOkdKZHCawIhANVxv7PWBrenRaJX99ojO2Sw7fReA2oj8Cy%2FxPZeVkA7KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtH7i4ZND%2FKVevj0Eq3ANaECpoEozfF204QJ4GonyeyVTfW9QUJR8NcNH1oIOEPFqi8%2Brrdhgl%2FQ7hIMYU%2Fz0uXIzmNUSE7b1LA0WWEClHptfZz1MqeNoblcFWzEOsSlfoDANwYxBRFUqEXKwJwyH8KrHMqvlO6iJOpWEsOKqYes%2FgKznbHtDgH7c%2BHNVKh9tOBOEhCNBSsYyQZPc2llTT0t%2FY2stjiX5MIUBxPJGi8icA9%2FKtHLR1pPr9eCCT4adou64e5ZTRJN3ZW0AG%2FBID%2BEmJ4XKlnE3TY5iu7vi%2FUfl%2BtVfnseoDMpX1ubbx3iV2PrK1RSSmf0fYjXY17pdOrtcLE0074xNsRgJGeBHvKFHH29yGCp5cfbYsBnd4L7AOPNTVQ%2F0ad54lB3WzPB2h0E8B59Rse7xkBW%2Bhxlv2BsTV2%2BLUTbE%2BJi1cBuuSazJyPTnGxJhBPRh6YWewKYDZTHW1kwoELXZSpU%2BbDZv%2FGgr6PCS4Lm4asj4VDGs43KlL2OQ82LhNXrl4cR8kegJdAbuZHbBzqzoTW8g2%2FwvBsq8hqibGbXwzsB3r0wOJMbNaXCRozuTNz4d3kg4Cs%2B2I1nNM5iP4VsvUIeTjZp6Fr3ijh%2FB8MbT%2BsmtRKhj0VkrAKoEEE5PbDFY22zC3lqXMBjqkAdyn5wARVP7ONeTxJQgTe1gdIF4K45gVptYnEpA78Kwspk4Ga0AZ6O9IaFH11p79PveJDArltJdcrEqbBv2qb%2Fk8igRNHQ5caNKpH80JamV0Kku7rMOP%2Be0pYUFbMHSNVwDRsDBgEesrtNIOy3Hf0OiLAgn%2FMl1BFiY5fjHkQWGQAuXzN8U0jFZxy8fhujUqF4YQOiHKQvJ6qbdtL7xwjc1Toqyb&X-Amz-Signature=c1c56e8e11c41b00e2a1abc01ebbb133feacdee428a7aab9f989e9bfcd9b4674&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJX7HFA%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCk9O%2B2jZuvinXB2FGF8a%2Fz15bYEWXq2thyiOkdKZHCawIhANVxv7PWBrenRaJX99ojO2Sw7fReA2oj8Cy%2FxPZeVkA7KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtH7i4ZND%2FKVevj0Eq3ANaECpoEozfF204QJ4GonyeyVTfW9QUJR8NcNH1oIOEPFqi8%2Brrdhgl%2FQ7hIMYU%2Fz0uXIzmNUSE7b1LA0WWEClHptfZz1MqeNoblcFWzEOsSlfoDANwYxBRFUqEXKwJwyH8KrHMqvlO6iJOpWEsOKqYes%2FgKznbHtDgH7c%2BHNVKh9tOBOEhCNBSsYyQZPc2llTT0t%2FY2stjiX5MIUBxPJGi8icA9%2FKtHLR1pPr9eCCT4adou64e5ZTRJN3ZW0AG%2FBID%2BEmJ4XKlnE3TY5iu7vi%2FUfl%2BtVfnseoDMpX1ubbx3iV2PrK1RSSmf0fYjXY17pdOrtcLE0074xNsRgJGeBHvKFHH29yGCp5cfbYsBnd4L7AOPNTVQ%2F0ad54lB3WzPB2h0E8B59Rse7xkBW%2Bhxlv2BsTV2%2BLUTbE%2BJi1cBuuSazJyPTnGxJhBPRh6YWewKYDZTHW1kwoELXZSpU%2BbDZv%2FGgr6PCS4Lm4asj4VDGs43KlL2OQ82LhNXrl4cR8kegJdAbuZHbBzqzoTW8g2%2FwvBsq8hqibGbXwzsB3r0wOJMbNaXCRozuTNz4d3kg4Cs%2B2I1nNM5iP4VsvUIeTjZp6Fr3ijh%2FB8MbT%2BsmtRKhj0VkrAKoEEE5PbDFY22zC3lqXMBjqkAdyn5wARVP7ONeTxJQgTe1gdIF4K45gVptYnEpA78Kwspk4Ga0AZ6O9IaFH11p79PveJDArltJdcrEqbBv2qb%2Fk8igRNHQ5caNKpH80JamV0Kku7rMOP%2Be0pYUFbMHSNVwDRsDBgEesrtNIOy3Hf0OiLAgn%2FMl1BFiY5fjHkQWGQAuXzN8U0jFZxy8fhujUqF4YQOiHKQvJ6qbdtL7xwjc1Toqyb&X-Amz-Signature=8229fa0da2ab8fae49f37473321faa9d9d0c92e6cb8fb788d6729050a99a3f1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

