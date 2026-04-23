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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V45FKC2%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFr7Nc8G2ysUceOy3q1H5%2BWuw2PcDjVhkPhaO4u9Nhv7AiEAmDlrYo473Mjr%2BBUwup1gQcbAFyJRDPWXlXbjwqEou2kq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDA0n6IT911K2fWzbhyrcA%2FyDX19jEBB9W38vk%2FfkuluJf66uq3av0zTCFioerKpVIMPKqg%2F8mqvPgh0b9aak%2FJyaSkVWJYf6cL5qO05OI%2BxqCt5IRu%2BcB0eGAEm7%2B%2ByOSgGUUgRaKcwVbHV4wmsiu0gGtQQHt%2FTKy6pPDnbrXJFoDfH6grgu5o1UenWcKdMQyPbh%2B1aNxiqro3wnYfkqIr1nuBXtih0kVbQyP3l7JteVwzlatCmx5nLSo4hQl%2FOAbXeeFrSd4%2BLdILXK%2BAby8feXS3WDtq3rlKcPbEGUHFRgcSM%2BsryKcptg1hT0%2FvuAwg%2B3qnbxbk5sMZ4BIIcG96CDjPKx4Hu%2BrB%2Bm11DLqcUBD%2BK7uszB%2FbjwXrFHSlK86ZKdxOIryvOLlZz%2FvLYRLv3Ry0vlIgBtUolANyx%2FLCYWc6SyiZg7G4elwbozj%2F4UgQEiNyoDEGeN3RAqvAgJohOQ2qHYPABTwUDauHG64mzPvyK2j4nPOqoLcJWMH6ASLvjXUQlTdnJtdTwaib3j3spj2QHvBkb%2Bt3QgSynXAlzpKZEQsaYXlkSUANOJW4nEHYcyfuOqyhb2UdF9dYHaK%2BIscPpVnbpMad%2BR1bQt5fcac%2BJvpXNJAVrUBTkJVvxzZppDKtQJXPbZ%2FIz9MNOfps8GOqUBAezu%2B47UHSdg74IQP8dzuFaq61ys4D8xmAqoPoY1wRhmuLy76zQ521BXZfQfmop4RAZSfHliIAtWEzErIXQE6b9iE468RHiAsCC0i%2FEnu0RzLfgMjrvYfrqf%2F%2FblRtN6Mi8xIW1yOL1of6l5Sl3cpNc5Q7%2BPIvrJE13ytOHGJmqBgbsPKo4AmDAMGE34PiVIAKQMh4YskOIGbhFJDvr56uyBABqN&X-Amz-Signature=7c2eacc1b6610f466cc0286f48935da49d577db49b33cf458d60fc1d804c7abd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V45FKC2%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFr7Nc8G2ysUceOy3q1H5%2BWuw2PcDjVhkPhaO4u9Nhv7AiEAmDlrYo473Mjr%2BBUwup1gQcbAFyJRDPWXlXbjwqEou2kq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDA0n6IT911K2fWzbhyrcA%2FyDX19jEBB9W38vk%2FfkuluJf66uq3av0zTCFioerKpVIMPKqg%2F8mqvPgh0b9aak%2FJyaSkVWJYf6cL5qO05OI%2BxqCt5IRu%2BcB0eGAEm7%2B%2ByOSgGUUgRaKcwVbHV4wmsiu0gGtQQHt%2FTKy6pPDnbrXJFoDfH6grgu5o1UenWcKdMQyPbh%2B1aNxiqro3wnYfkqIr1nuBXtih0kVbQyP3l7JteVwzlatCmx5nLSo4hQl%2FOAbXeeFrSd4%2BLdILXK%2BAby8feXS3WDtq3rlKcPbEGUHFRgcSM%2BsryKcptg1hT0%2FvuAwg%2B3qnbxbk5sMZ4BIIcG96CDjPKx4Hu%2BrB%2Bm11DLqcUBD%2BK7uszB%2FbjwXrFHSlK86ZKdxOIryvOLlZz%2FvLYRLv3Ry0vlIgBtUolANyx%2FLCYWc6SyiZg7G4elwbozj%2F4UgQEiNyoDEGeN3RAqvAgJohOQ2qHYPABTwUDauHG64mzPvyK2j4nPOqoLcJWMH6ASLvjXUQlTdnJtdTwaib3j3spj2QHvBkb%2Bt3QgSynXAlzpKZEQsaYXlkSUANOJW4nEHYcyfuOqyhb2UdF9dYHaK%2BIscPpVnbpMad%2BR1bQt5fcac%2BJvpXNJAVrUBTkJVvxzZppDKtQJXPbZ%2FIz9MNOfps8GOqUBAezu%2B47UHSdg74IQP8dzuFaq61ys4D8xmAqoPoY1wRhmuLy76zQ521BXZfQfmop4RAZSfHliIAtWEzErIXQE6b9iE468RHiAsCC0i%2FEnu0RzLfgMjrvYfrqf%2F%2FblRtN6Mi8xIW1yOL1of6l5Sl3cpNc5Q7%2BPIvrJE13ytOHGJmqBgbsPKo4AmDAMGE34PiVIAKQMh4YskOIGbhFJDvr56uyBABqN&X-Amz-Signature=921cd608e42d6b1705e9b287f88a26b771eeee98d448f9a1642a6bf61bf3ec91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



