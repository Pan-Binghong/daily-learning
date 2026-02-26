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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU6ODV2D%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQD%2FiB5MCNSiq69DtDgAgvf95OpwZzyAxlG89rYtovkGegIgd2jU7Dzl9fOdqQUyTP9p5pm5c7H%2B4bi9ETTszwFQC6Eq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDBSnbUGKt79kuJ1NnSrcA5VsPV5mB%2FPmintcO%2B8LVz2k3ETozTTZjQN6%2BJ0KLpdAIMoqvosVwzoOTdtbQE0hJX%2BDvZRYjPXCKyYFB%2BAXBpW7OAqAnP7eMVmG5AZLI7oJShQxZ5CRXR6xTDf%2Famtfla9T5GZe3JCWKMEs7KECYEpLUOi%2FjuWJtjR2zQDZcDx%2Ffslkz%2Bbik6SbkA6U3P6Nk1y2XAhTW8sLESdzFpf2LiKAsDV9RWN7zdQicdJDlSDUnOK1coZG%2BgJmWCFTtadf44OUJIAnab0iitTQ38TPjuXPUjeYXOqS%2BEToEfbniSxbsMkGmnrsv1pNPawO5YbpqYoUHgU20sHWinzltkj1Fkoif6LFsmKeGx96Jf5Q1uQExSlgs252CFuuF6r%2BR4stxCdTQbht%2F49ffAZEn5GfohntdZBGGVGKjeE1mie38YtsbPts%2FL0AugCNchHzsi0fdLlUZbwg5mZ3AEEL99FSJ%2BqFBe78sW%2FcGmFnUlQjRUoE0R8D5gzVlrh1pHw0dWtGEoFS2HkJ6sxI7V3LDqNWNgKlRgEV8PDKbjgrS%2BXjy8djmjo5%2BMQU%2FUvrd9Z62SnU0JCF2r4081nfE9WHJyUD2oXSXhOIYIc4g1o%2B%2Bxxk4Cgw0HflREumTfd41p%2B1MK%2F1%2FswGOqUBQhvxNYZjMTvLZINpJp0souQtGCPBHtudNj6Q3BeT1Bp1myVdrzLA7GZkss90Skg8Df%2BZnHnJ4%2FfY4AnxJUiCLP0cZbT8M%2BGI1B8MwoM0EWSdxmw1eGQG3eRyuMOvruJcf8YfTUDr4XWUmYqF8LrpC5IO6hUTUBLsJb7D8edHiFDx%2BrdrLKO%2BCmAyoX%2BhTipKVaKoj86aSCBm3jnR9yKLiYYKsnmx&X-Amz-Signature=119f7a5b593e28e2c32618ef66b6903b2243a65640f6fda940e731b65f575623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU6ODV2D%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQD%2FiB5MCNSiq69DtDgAgvf95OpwZzyAxlG89rYtovkGegIgd2jU7Dzl9fOdqQUyTP9p5pm5c7H%2B4bi9ETTszwFQC6Eq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDBSnbUGKt79kuJ1NnSrcA5VsPV5mB%2FPmintcO%2B8LVz2k3ETozTTZjQN6%2BJ0KLpdAIMoqvosVwzoOTdtbQE0hJX%2BDvZRYjPXCKyYFB%2BAXBpW7OAqAnP7eMVmG5AZLI7oJShQxZ5CRXR6xTDf%2Famtfla9T5GZe3JCWKMEs7KECYEpLUOi%2FjuWJtjR2zQDZcDx%2Ffslkz%2Bbik6SbkA6U3P6Nk1y2XAhTW8sLESdzFpf2LiKAsDV9RWN7zdQicdJDlSDUnOK1coZG%2BgJmWCFTtadf44OUJIAnab0iitTQ38TPjuXPUjeYXOqS%2BEToEfbniSxbsMkGmnrsv1pNPawO5YbpqYoUHgU20sHWinzltkj1Fkoif6LFsmKeGx96Jf5Q1uQExSlgs252CFuuF6r%2BR4stxCdTQbht%2F49ffAZEn5GfohntdZBGGVGKjeE1mie38YtsbPts%2FL0AugCNchHzsi0fdLlUZbwg5mZ3AEEL99FSJ%2BqFBe78sW%2FcGmFnUlQjRUoE0R8D5gzVlrh1pHw0dWtGEoFS2HkJ6sxI7V3LDqNWNgKlRgEV8PDKbjgrS%2BXjy8djmjo5%2BMQU%2FUvrd9Z62SnU0JCF2r4081nfE9WHJyUD2oXSXhOIYIc4g1o%2B%2Bxxk4Cgw0HflREumTfd41p%2B1MK%2F1%2FswGOqUBQhvxNYZjMTvLZINpJp0souQtGCPBHtudNj6Q3BeT1Bp1myVdrzLA7GZkss90Skg8Df%2BZnHnJ4%2FfY4AnxJUiCLP0cZbT8M%2BGI1B8MwoM0EWSdxmw1eGQG3eRyuMOvruJcf8YfTUDr4XWUmYqF8LrpC5IO6hUTUBLsJb7D8edHiFDx%2BrdrLKO%2BCmAyoX%2BhTipKVaKoj86aSCBm3jnR9yKLiYYKsnmx&X-Amz-Signature=d7c1f0f222532753b76ce9ce4dde321cadcc2b76ff71806f7885b1ff80db4a31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



