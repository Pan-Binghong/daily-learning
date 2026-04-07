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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVDHBH67%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQD4pl4PfYZnr9xURs53yBfw%2B9nhfJY5q2Ty%2FcK%2FSt%2F%2BfAIhAM38XNpsybDSmtBh%2BHTcbDk2adbNoYdPUFoOG%2Fyzm6M3KogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGBWWlcLMoJlJkzIAq3APoYftj24wvztrG2kApNXYeEOXCA2vRpaCwwg6HsaZ1NCFzE3aDc2lf4LBsvJGrS%2BY35ZLsvV2tDA9JfPncQ23%2Fv7a274nO4XfoLTibwQzhVIq71FpJo%2F8Hb%2FMG1PHjVW%2FpcN2wRyVgGHtfDegoFUTraSdFxKUdkVNrYksdaEQ1RhL0z%2BIQkO9ms2NbagnaEr501cKczZHG4pc%2Boz5P5RqqfsBvvWewimNjV5fubV%2BCGxVY%2F9TDzz%2Bb8XbgLTGg94VBNUXiSTUXW8MkdBHZSb47F3QD1QsOJ0i%2F015ii0%2FMEIit8yx%2BM%2FTQLOX9wmdwDTHT2PtanQ5T%2FV%2BH9uNjO0tq%2B4r6ZwePho9r%2F4mvAA2OQbebsCu0y9hmc4EXsccjp2wvDZDPT%2Bozn3i8t6Q9kepYpa6FhVnu97ltewHVWQHn%2BJ7jFWVjA9VvJpGIgGO8vtS5k5wpZWFE42wE26d%2Bh0TjumtL8HC84gPCOYfxtL8Y65qGCwXoDlPHgUSH93K7n2GH8nmsD5qlAtDPzIQFQhfV1M1SZByjGE6vOjICDgvu9TZAvRqZ2e10d4kv%2FhqvfaO%2F9BNxsjzdtHZ%2FmS03liOlrdipJC5L2REe4yS%2BMas6NtjWfVwaEgftx%2BMvFzCJ9NHOBjqkAc5QdSNvigN2Rai3bav%2Bk4rm92f8UelGt4encGpGRQskdjEnts0Vc2yDD01ioH1kem6ZOVE2O29jw16aFzcCGq0QlV1cEdyxgoch%2FROXxk6GCaVtmcCSxV1Xj8CyoYopjrichYP2r9TDRIHWHzHPSlKG26B7BMpCBPzD%2BPaUsg8u88HQMBAlwkj5MjhFtgHC8NJpg05%2FWHiPglqWaLEJK0gx7imj&X-Amz-Signature=0447d21864278754e82ab6eb2e7c32ecd1a3d035c7dc2b8bd6c346993430d62c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

