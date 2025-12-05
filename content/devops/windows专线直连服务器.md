---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGWXC3Z4%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG4idyH2tPvGOQ1C90wqLG2p8vMqWxVZAXwU5K0Wz%2BaPAiEAmYYnVow059V9gxt%2BLsxIqkrNXNsh37iV8BAxA10qUWMq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDPJgiZ2IK3iRUuSJ%2BircA6s1YmwoWNn5W7Ou6i%2FQH%2B9LFz4pgZ9DDWC2z9uwLvCdv2JwvVjaZbMOnUBie9%2BmWZVSwONo5H1vS%2BLwjjnBT6Vb2EfuxRwnSAwlMH8prcV6M0JQ5W2GzbOne7yksFuiUKzKCe0FhZ9s9Krl3vOcQohdCqZcuryF1qxjyU%2FjLI7ZeR%2FIaX6LD8KCn5VnjlI0hlLRDZLBqNYF3E5zMjIQBU4eLNBbcm5fsDf9uuJ86vIpxkD2ci6Ue9K%2FlUc807x%2BBJN%2B4R79IAQtVcW4oO37VYBUEDTHsvaetvVakar1b4mX06oOsAvQqhtldjLQpovuDv9ho3sYr79BTTRISQfvHi90%2F6YoqnNaRoX%2F6KowyV7IyKbR5CCcoP%2BUZ7RGJPKc8DaobqUj%2B1jaYzHwnqqI%2BayppcbT%2FB6rncfv0Rnz3LKHEixYjg1379Xqdd0SOdrpT1xqedUwtfD1dI1%2BG2vhC9JClAvgP%2BTHnu2hNd2psFy6XvB8criSnUmks6u8bz9BsenwzLz%2BZiPvYMn85BkBI7ifvAWeM5IynCzzh1LaIAes%2B3rkZN2LSYpgZMf9fGvBU7xPlrMP5GK5mDDlq91exzX8dN8af8xLiXMnWup%2B32e1ouV6krvLETRl61JSMKCMyMkGOqUB%2Bd3j8tZD6%2BewtZcGrvnBNKG0Tq9W3AwVUIBbFUpDJy5W3GIYxLUjYPr2WJnuCVUeE1XSu7JwJdOBfM15IKa5JBr3WD74toZuvDNrwutussoVlJvoU7Ovuz4h410uyWiUYRUXjzgwTGW7pXQKfgyU5JLWGanudSpj2%2BIPquPTRDiMzarjJpttb%2BBKuFrHkvWz7EAVaTgzPBnotGfN15iSv88rVT4A&X-Amz-Signature=ba346623528c964f2b6cf99624fdbec33ff28ced30f9c92575e4f549b7493eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

