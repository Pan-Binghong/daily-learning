---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NZPH5HI%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDUaJq4AahP5UciemxvBrjgFdyeR5jeuFHTu4qzYZXhVQIgdV9m0DdhIZmEFQt3Xhx6gVC5SQ7YCn9B68VRsMoLgVkq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDAokhjxC95qWNsuLByrcA2GQcVr4wDDiz7LqY8ezCAC5zUErF0nD3HdyTiaeW9dkmSQNAg1hCTyPhRVJA%2Fb5YxPt%2FXK588UY8Wwo1%2FTnBZzx%2FXMckhu9%2FVYZ1r8COobvosorMlu%2BAAa5HhChFUSFV%2Fq3vfJ8HQyAAPOso5XDejVZpE08f2KMPQENXDg%2FN7v%2FiFHXSp4U0OTSSeHvuhP4rNRwp%2BZSgO0w0HZXQjlZL1z3UgNL3gf7mHKbnqdmSZ7aU2L%2BnbgWRJoKEDzqxB%2BGoSANGDycHnIB8WXTu5Cggjm%2FjzKrHYR06lduecLNk1eWEsF1UYgjxCnrxdDvjZQl9gO%2FClUZTfGsFB0fQ4QyZvhNr3KF%2FEwlzdwzGOeM4pRH0Hbk3IkInaRwf1XiAlmfnuwmmHVAqdHGRV9RNJLRb6g2vhd81RXWmDm%2Fa2%2FcmlkBT1M7LD4Zbl5QqXk%2Fm7Z9jVEDdJCLSei%2B6OAMzn%2BB38257rXHK1kk1zQRcpkuMcGXJeDuZba71QIjSiuP0JSOInt0n2hpiDytoy15MaL9HArlKofJZQzND4%2BCufhzjyQhJWfbCeKlHPoKNt%2BoFr85EqU23EIGD0k7akhdBHDQeas8MtNpuFVfx5%2B%2BDjvamCaWEbyuB8Gxz439qDsnML3Um88GOqUBij9rbVeROgyEnh%2Bf%2BXwJ28xXKRk%2Bf6XWA289%2FhjZWQfdwd5wQcfmDJ7wQyPTFjmm%2F92mfim4FImBRdu5jES8DXfXW0JqooMcfd47KdXX%2FnVihnws7pnDc71nFXLpz3JoplzkqbnskVhZaP9oQLyHnLioPXOLrWR46K7mUCjRnZnGUNAHo69hRWYdhhSIanz742Tnb39UAla9kIwlbjYIu6UV2iIm&X-Amz-Signature=c3bf803b16b3ad44bb2c52106e53d08427f7377b5731784d96f9d7a131b7e2af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

