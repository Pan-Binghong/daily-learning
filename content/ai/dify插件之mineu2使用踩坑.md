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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZEOILDZ%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6zA9w8iJQzAw1aGisKBDALTXFoyc4ijEIK%2BIxZDi1yAiEA2oNuNDvGKDAn38rfiilzCYS4vHK%2F7jPz9mm2WYcgoG8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG3%2Fm1szd25%2FNYD2UircAygyDSgf2aUuVszfO4yqlQKDjGAdOkMYyPFtoTBemUQ2jNFhyZrD5sj%2FvBAtRv4K81n4oQyKUlh3wCJNry65nk5rj3BQq8W6POYnd%2FmQdQh6Zw6JJPk5mrNfmDjeaZjRNFCnzsddYbP43FRu6t7BF2htWDnZMiPm0AIfLb0EnuxKvUhhByA9NtFeZXQoxbRgwjBseY7XBBmX1cAAWK2mMO2pq2Jkt4Uy%2BcGM7l2wK1ylvLmjV6QtzOlYXIod9sjAn7Gq2Xjjt%2F11NeGLCGOqKQLu7MWfSJ13G2lkKUhp2eKFYMS4492UxlaUc557EJbk6RRezpm0qJsV6o096yKaGaqtV0l2cvZf0WRjJqPTwGgDNanKq90hk8VCcc65goSU7nPqmrBquHGzOn4GD63TslIWUlH8uMWBBS1xGDMu3u37EdxEYhoqJKYd1ye4Prgvq65mh4IIp%2BmeDS9g97Gbuyj50cON4HlN7e8bin7ZUuUQLxNCtxCUJ591U8RTTS2vlpUJxC4gc%2FFBqZyoUTYQby2XoqbGToiJ1k8YRRN%2Foz%2BjEN%2B93gLihWjAU%2B%2FzFfJQFlrClxzzW%2BZs%2Bo85eYKBU9y58wP0eZyXHApiYoe89asDoN%2BxVvMh7BJDcbCAMPiwzM4GOqUBPZCnzQJNEHSXztxAPMcDzav3EnyHkd6PIasKos992VxC848jKsKlIcxzofCUrooq9p0rcmybjuUK9rYMpEsAjb0Oxcdi1ilywOiOqOo0w7idnk7h5HNg6TEjPKjh%2BP6%2BwOfU%2FC9dNXS3hDV0j4F9RiPQEGk5PaKg3H25nerCsNxl9Qon08vuaLi4aTALhyvnyjOnukXAS9nyMc1yM5LXDWRxZDAC&X-Amz-Signature=44f86f324088a509ad65818dfd7e01b32e16a4c10cdc9867a778cfe9d26654f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZEOILDZ%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA6zA9w8iJQzAw1aGisKBDALTXFoyc4ijEIK%2BIxZDi1yAiEA2oNuNDvGKDAn38rfiilzCYS4vHK%2F7jPz9mm2WYcgoG8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG3%2Fm1szd25%2FNYD2UircAygyDSgf2aUuVszfO4yqlQKDjGAdOkMYyPFtoTBemUQ2jNFhyZrD5sj%2FvBAtRv4K81n4oQyKUlh3wCJNry65nk5rj3BQq8W6POYnd%2FmQdQh6Zw6JJPk5mrNfmDjeaZjRNFCnzsddYbP43FRu6t7BF2htWDnZMiPm0AIfLb0EnuxKvUhhByA9NtFeZXQoxbRgwjBseY7XBBmX1cAAWK2mMO2pq2Jkt4Uy%2BcGM7l2wK1ylvLmjV6QtzOlYXIod9sjAn7Gq2Xjjt%2F11NeGLCGOqKQLu7MWfSJ13G2lkKUhp2eKFYMS4492UxlaUc557EJbk6RRezpm0qJsV6o096yKaGaqtV0l2cvZf0WRjJqPTwGgDNanKq90hk8VCcc65goSU7nPqmrBquHGzOn4GD63TslIWUlH8uMWBBS1xGDMu3u37EdxEYhoqJKYd1ye4Prgvq65mh4IIp%2BmeDS9g97Gbuyj50cON4HlN7e8bin7ZUuUQLxNCtxCUJ591U8RTTS2vlpUJxC4gc%2FFBqZyoUTYQby2XoqbGToiJ1k8YRRN%2Foz%2BjEN%2B93gLihWjAU%2B%2FzFfJQFlrClxzzW%2BZs%2Bo85eYKBU9y58wP0eZyXHApiYoe89asDoN%2BxVvMh7BJDcbCAMPiwzM4GOqUBPZCnzQJNEHSXztxAPMcDzav3EnyHkd6PIasKos992VxC848jKsKlIcxzofCUrooq9p0rcmybjuUK9rYMpEsAjb0Oxcdi1ilywOiOqOo0w7idnk7h5HNg6TEjPKjh%2BP6%2BwOfU%2FC9dNXS3hDV0j4F9RiPQEGk5PaKg3H25nerCsNxl9Qon08vuaLi4aTALhyvnyjOnukXAS9nyMc1yM5LXDWRxZDAC&X-Amz-Signature=38f6c6c282093d9ee181605fe6150cbac39f9b271247f48cf1921deb4a46e2d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



