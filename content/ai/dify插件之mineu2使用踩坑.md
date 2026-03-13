---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DKN3BN%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFXicJrJOJ1MHFaYnQo3cDsGG%2FPE5hnRZtY0vo7EidkiAiA17aEok6HcbuHFWnIQs7bmaXVzKcrCVHuMV3lpsoRjMiqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGD2aZzbEvXAMIOfyKtwDVBqZVov49D232hQYbHjsZc%2FoBUveykyO4MnDjiP%2FvzdiTn7iV1cRSFfjt82hfEFGvXuZWTbdh7uDjEgwsPA7OauN98lJAe3bEgwO3HyFRkN%2B%2BIzhZGuMJ1KDcl%2FGOZdfTkxf%2FsSrsGLF%2BFuS%2FYcXTwLNQ3LiiwHqSZgUGZ%2FWGGt%2BYiVzXKNTVv2ti9%2FexsTt7th6Ya3GQq40J3CpIE4VO23ChAUB5etiHLo48JfhaLZW4yDQr5LWYEB9K3NvVcfNjySzdQKj46YEGN4p2STlyG6kRyNkcPIzdHru6t%2FSIwVzd5vZCY34hboqMVmsiEdcq%2F%2BTXHcEALGVjjCE7D7BV4LyaKtiUgGn2xMxnmLKgN3Tztber0IPU20ero%2FT16ljC4rH0Dudm8dxsqaSVzWvkykdDPkfdwfnAE49zksXOjfSVKjO9HbiaH111IdEajzjuZleT7O%2F7iCrh%2F81eHdCKyol1tuRLct%2B1Ck%2FFshlqZWRPJicz0tO1p00QEzm%2Bj4y1nBU3zH0dFiwoOgzpnwnV4VSL%2BuRAH3I%2BJeMFixOW8NkAVqPnMbkso0oadAsKqEiNlKdo9Qfn2YOKVWl3%2BTjVI5pCMvcHBYpJp2FK9Y1lSsXiGuvnu%2BEwScYX1cw1bfNzQY6pgGuY0NjAmTtuiVpN%2FdNUAmbVgNuYPhYNr7ji52WLKlf2GxiAmEZKYwpLDuA7%2BoXtYH40lH7YyIoHtqGhHu0sDmplLx925rkDqK92vnUOWX%2FdT99ICIhL%2B5xq4sxhN2fgVSeZT7ARcQvOQnmt67XwIdElPlnp12CLorVFfxjNfdnJ5OXc8A%2FKGr5IgORiqVh0BJQj1XIKfsko%2FcUOEsX9k1bXwZaULBi&X-Amz-Signature=93058c5e011243ddd36f928a974daad098dd8d290b7bb8f28735a52bd552b578&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DKN3BN%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFXicJrJOJ1MHFaYnQo3cDsGG%2FPE5hnRZtY0vo7EidkiAiA17aEok6HcbuHFWnIQs7bmaXVzKcrCVHuMV3lpsoRjMiqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGD2aZzbEvXAMIOfyKtwDVBqZVov49D232hQYbHjsZc%2FoBUveykyO4MnDjiP%2FvzdiTn7iV1cRSFfjt82hfEFGvXuZWTbdh7uDjEgwsPA7OauN98lJAe3bEgwO3HyFRkN%2B%2BIzhZGuMJ1KDcl%2FGOZdfTkxf%2FsSrsGLF%2BFuS%2FYcXTwLNQ3LiiwHqSZgUGZ%2FWGGt%2BYiVzXKNTVv2ti9%2FexsTt7th6Ya3GQq40J3CpIE4VO23ChAUB5etiHLo48JfhaLZW4yDQr5LWYEB9K3NvVcfNjySzdQKj46YEGN4p2STlyG6kRyNkcPIzdHru6t%2FSIwVzd5vZCY34hboqMVmsiEdcq%2F%2BTXHcEALGVjjCE7D7BV4LyaKtiUgGn2xMxnmLKgN3Tztber0IPU20ero%2FT16ljC4rH0Dudm8dxsqaSVzWvkykdDPkfdwfnAE49zksXOjfSVKjO9HbiaH111IdEajzjuZleT7O%2F7iCrh%2F81eHdCKyol1tuRLct%2B1Ck%2FFshlqZWRPJicz0tO1p00QEzm%2Bj4y1nBU3zH0dFiwoOgzpnwnV4VSL%2BuRAH3I%2BJeMFixOW8NkAVqPnMbkso0oadAsKqEiNlKdo9Qfn2YOKVWl3%2BTjVI5pCMvcHBYpJp2FK9Y1lSsXiGuvnu%2BEwScYX1cw1bfNzQY6pgGuY0NjAmTtuiVpN%2FdNUAmbVgNuYPhYNr7ji52WLKlf2GxiAmEZKYwpLDuA7%2BoXtYH40lH7YyIoHtqGhHu0sDmplLx925rkDqK92vnUOWX%2FdT99ICIhL%2B5xq4sxhN2fgVSeZT7ARcQvOQnmt67XwIdElPlnp12CLorVFfxjNfdnJ5OXc8A%2FKGr5IgORiqVh0BJQj1XIKfsko%2FcUOEsX9k1bXwZaULBi&X-Amz-Signature=9211fbecd513ca436d6711e01b623beff42279ddc60a2504ee8f63e80266b65a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



