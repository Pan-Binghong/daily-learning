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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCQ4NQ3R%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5gPzk5cgO6Fl9%2Bw5%2F0uC0BHC4oQrqMTDVAcb8dn5qZgIhAL%2Fo5hQp%2Bx9bdYCgkjXz3Gx42j8gyeeCTzr2X29O%2FSG0KogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyPbMqTLB9qmrNdu0q3AOGOTh9Yek0kBUMJwZE%2F0XpDfiJuUOWJgPvWeMQKWyNGoL3C%2BBPB8buYezMaZExGHShBUEjvygHdUKv4FhKNQuE952kvz%2FKy7dXmZekvx%2FYVruZzj004Z6T3wnlv0VQdMwWupsIzhzE0MsZpiztyTAkOwiXDdjMaDX5oMUuNv53u3h4zNN%2BvAwkn9sh0%2BJ9R4leRyPBNRZ2uJnxDgcKH%2BgTnBsE4L6lCkDVHpamE9ThdJrGuEeSdjkRPDdJYnv4uRYNfSy8ULzb79%2FZaSX65MHHreXFPXBiM%2FWc0%2FdqTzYxRRvq55dDPgr7flcok%2BnDVdqK%2FUuBN0yy9c62K6OQs9%2Fb3t85RejqyKzVsBn0MN4%2BtZ7xZBhZLlJ4gUyKcYdZGDwO5QnRAqD5%2BG9iqABj%2BPGHmcECF75q2dsOFz9Fen2ruMn%2FbufvBvvI8NDGOqEH47%2BEKQuejZIFPoYoC2g%2FIgp8zHya%2Fw7UXHTQLdnyIo2PCju3k1%2BKzuDkz9Xm7RQy5VXmVOSnEi5vGCoSKPMexTWqCFtbUObjf3XnIEpZSGnB6xqsEzxR14MsQqJ7F8a35wkfF9JRkfPljAbXuzHpxN7B2%2F%2FXfS0wSWqOX7ZD5hYuHAbOOGcvz3SvD7a0ZjD5nMfOBjqkARCROTGK2F0DECKizRo2p6YoOuP6uXXuUTaUKjX%2F3bduZaG2PmE34%2Ft%2BqbjfPmBMTbUFV4OKbZYVM%2BCxmwW4KG3%2FAmwixfy%2F8nAY13osPi7sXZ4614Auo0jfNxgdxWEhONKClMU2jxQ43TH9tuaDAPGM%2FD96FLOiTMUc%2B4N4Gghoh78OMBrCK90QI5zsk0ae2IzrvMCY1WW48%2FufZLst7Tt0a6hd&X-Amz-Signature=ac6da760de217392a447da0bb22d688f8e98f2774b4a506ff0ce6524a237f2d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCQ4NQ3R%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5gPzk5cgO6Fl9%2Bw5%2F0uC0BHC4oQrqMTDVAcb8dn5qZgIhAL%2Fo5hQp%2Bx9bdYCgkjXz3Gx42j8gyeeCTzr2X29O%2FSG0KogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyPbMqTLB9qmrNdu0q3AOGOTh9Yek0kBUMJwZE%2F0XpDfiJuUOWJgPvWeMQKWyNGoL3C%2BBPB8buYezMaZExGHShBUEjvygHdUKv4FhKNQuE952kvz%2FKy7dXmZekvx%2FYVruZzj004Z6T3wnlv0VQdMwWupsIzhzE0MsZpiztyTAkOwiXDdjMaDX5oMUuNv53u3h4zNN%2BvAwkn9sh0%2BJ9R4leRyPBNRZ2uJnxDgcKH%2BgTnBsE4L6lCkDVHpamE9ThdJrGuEeSdjkRPDdJYnv4uRYNfSy8ULzb79%2FZaSX65MHHreXFPXBiM%2FWc0%2FdqTzYxRRvq55dDPgr7flcok%2BnDVdqK%2FUuBN0yy9c62K6OQs9%2Fb3t85RejqyKzVsBn0MN4%2BtZ7xZBhZLlJ4gUyKcYdZGDwO5QnRAqD5%2BG9iqABj%2BPGHmcECF75q2dsOFz9Fen2ruMn%2FbufvBvvI8NDGOqEH47%2BEKQuejZIFPoYoC2g%2FIgp8zHya%2Fw7UXHTQLdnyIo2PCju3k1%2BKzuDkz9Xm7RQy5VXmVOSnEi5vGCoSKPMexTWqCFtbUObjf3XnIEpZSGnB6xqsEzxR14MsQqJ7F8a35wkfF9JRkfPljAbXuzHpxN7B2%2F%2FXfS0wSWqOX7ZD5hYuHAbOOGcvz3SvD7a0ZjD5nMfOBjqkARCROTGK2F0DECKizRo2p6YoOuP6uXXuUTaUKjX%2F3bduZaG2PmE34%2Ft%2BqbjfPmBMTbUFV4OKbZYVM%2BCxmwW4KG3%2FAmwixfy%2F8nAY13osPi7sXZ4614Auo0jfNxgdxWEhONKClMU2jxQ43TH9tuaDAPGM%2FD96FLOiTMUc%2B4N4Gghoh78OMBrCK90QI5zsk0ae2IzrvMCY1WW48%2FufZLst7Tt0a6hd&X-Amz-Signature=90df433b31a1bfb7cd2b8c015d5e00c7fde8ba7bac447ac205387561a1696c15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCQ4NQ3R%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5gPzk5cgO6Fl9%2Bw5%2F0uC0BHC4oQrqMTDVAcb8dn5qZgIhAL%2Fo5hQp%2Bx9bdYCgkjXz3Gx42j8gyeeCTzr2X29O%2FSG0KogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxyPbMqTLB9qmrNdu0q3AOGOTh9Yek0kBUMJwZE%2F0XpDfiJuUOWJgPvWeMQKWyNGoL3C%2BBPB8buYezMaZExGHShBUEjvygHdUKv4FhKNQuE952kvz%2FKy7dXmZekvx%2FYVruZzj004Z6T3wnlv0VQdMwWupsIzhzE0MsZpiztyTAkOwiXDdjMaDX5oMUuNv53u3h4zNN%2BvAwkn9sh0%2BJ9R4leRyPBNRZ2uJnxDgcKH%2BgTnBsE4L6lCkDVHpamE9ThdJrGuEeSdjkRPDdJYnv4uRYNfSy8ULzb79%2FZaSX65MHHreXFPXBiM%2FWc0%2FdqTzYxRRvq55dDPgr7flcok%2BnDVdqK%2FUuBN0yy9c62K6OQs9%2Fb3t85RejqyKzVsBn0MN4%2BtZ7xZBhZLlJ4gUyKcYdZGDwO5QnRAqD5%2BG9iqABj%2BPGHmcECF75q2dsOFz9Fen2ruMn%2FbufvBvvI8NDGOqEH47%2BEKQuejZIFPoYoC2g%2FIgp8zHya%2Fw7UXHTQLdnyIo2PCju3k1%2BKzuDkz9Xm7RQy5VXmVOSnEi5vGCoSKPMexTWqCFtbUObjf3XnIEpZSGnB6xqsEzxR14MsQqJ7F8a35wkfF9JRkfPljAbXuzHpxN7B2%2F%2FXfS0wSWqOX7ZD5hYuHAbOOGcvz3SvD7a0ZjD5nMfOBjqkARCROTGK2F0DECKizRo2p6YoOuP6uXXuUTaUKjX%2F3bduZaG2PmE34%2Ft%2BqbjfPmBMTbUFV4OKbZYVM%2BCxmwW4KG3%2FAmwixfy%2F8nAY13osPi7sXZ4614Auo0jfNxgdxWEhONKClMU2jxQ43TH9tuaDAPGM%2FD96FLOiTMUc%2B4N4Gghoh78OMBrCK90QI5zsk0ae2IzrvMCY1WW48%2FufZLst7Tt0a6hd&X-Amz-Signature=21e4cafc08f2eed8042bd856cb50e1c794ad70590c650bedc34642cfe61feca3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

