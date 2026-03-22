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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WE7WBXY%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRm%2F6G%2BpojyJlFEUldU9W9IkRz4yJirh5qPOMijRnYQAiEA0FcUErt%2Bj86FiOh67M%2Bo1S6g8Ph18%2F8doYn99uV%2B9ycq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDBmq%2BslMXdhO8pXBDyrcAxN7ptsyo3kk27GJz%2F28kvAkm4qkdm7ReEVjw%2FoFUaPGJ8Fy3Jaf%2BCpouAnSPtn0Vpw9k7q5DwlvXKnC1QsNzU6%2Fa27YRR2jfkzq%2FZV7Gwz6gOdrmNu2iPV1PVALgkbBChgYpxSOTW6YQgY1vCr8wBMxviyVidmvrE41nt%2BUmyLV5bho2Pv9f4rgjvVw3BeuMH4jWwjHKqZT%2BUuBo3fAvEWWlCRjjIE2ftnPnRF2gqFGJgMl82kgEkOwbImHZh2PMWLT60etoRMAog2xOIOnYAXWlcQvQp8Xgr7zJ34TYwPcB0XyHhASciSUwFaCUqgMXuPo8bmemXqObjiMjr%2B1PLG5whM9tOm8lONJmmxwui3AF6qcLUYN0VPvz70l7rPFLVNWRAycaRMXS030pdmxS4z5K%2BD0BMG9IXLxI0%2FsIY0qQtjlEwvzSfC5Yhdzp4EI5AoX3Tx%2Fzn5YrIiiCr%2BoPTxHOWgUly8PVsXZ3%2FZ0SEIIyKOiiMrFDyQ4dsjo%2BqqDcz6Xm20%2F%2F5ybrJbWszvM93nL9NcPv2%2BW5lfFtC96Pej638kD9gUiNi7Ax5xfJsbbiOCLynaqPE9zL0HBB7SQzSCj9fhuQTuWX7Q2JwvSvb6NwOPOZal7Nq2JO41qMPKs%2Fc0GOqUBeTl%2BINJOwvlXCq94c9potXgCo1eIMqOzhObOsMlRpoR9lo7xoNd61yQed4BhOCVkXbNxobxCf3W%2F5PpwKOda%2FR9PYQ%2F26KSJ3pY6WXFWoS3mMxFMZsILkz0pL13XyWjAjCDBWWqAzGUpOB0j3gAqbvUMqMyRmIiaXMiow2QqYlEFDynv1ZQlsbG8rdYh%2FQexzWZiKB4bgVGlfR4GiWcpuOJ0ccwp&X-Amz-Signature=2bc3f87b8ab1e7f10f4bc4a2af00fb58f552cb4a419802303a4e5638ba2f0c67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WE7WBXY%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRm%2F6G%2BpojyJlFEUldU9W9IkRz4yJirh5qPOMijRnYQAiEA0FcUErt%2Bj86FiOh67M%2Bo1S6g8Ph18%2F8doYn99uV%2B9ycq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDBmq%2BslMXdhO8pXBDyrcAxN7ptsyo3kk27GJz%2F28kvAkm4qkdm7ReEVjw%2FoFUaPGJ8Fy3Jaf%2BCpouAnSPtn0Vpw9k7q5DwlvXKnC1QsNzU6%2Fa27YRR2jfkzq%2FZV7Gwz6gOdrmNu2iPV1PVALgkbBChgYpxSOTW6YQgY1vCr8wBMxviyVidmvrE41nt%2BUmyLV5bho2Pv9f4rgjvVw3BeuMH4jWwjHKqZT%2BUuBo3fAvEWWlCRjjIE2ftnPnRF2gqFGJgMl82kgEkOwbImHZh2PMWLT60etoRMAog2xOIOnYAXWlcQvQp8Xgr7zJ34TYwPcB0XyHhASciSUwFaCUqgMXuPo8bmemXqObjiMjr%2B1PLG5whM9tOm8lONJmmxwui3AF6qcLUYN0VPvz70l7rPFLVNWRAycaRMXS030pdmxS4z5K%2BD0BMG9IXLxI0%2FsIY0qQtjlEwvzSfC5Yhdzp4EI5AoX3Tx%2Fzn5YrIiiCr%2BoPTxHOWgUly8PVsXZ3%2FZ0SEIIyKOiiMrFDyQ4dsjo%2BqqDcz6Xm20%2F%2F5ybrJbWszvM93nL9NcPv2%2BW5lfFtC96Pej638kD9gUiNi7Ax5xfJsbbiOCLynaqPE9zL0HBB7SQzSCj9fhuQTuWX7Q2JwvSvb6NwOPOZal7Nq2JO41qMPKs%2Fc0GOqUBeTl%2BINJOwvlXCq94c9potXgCo1eIMqOzhObOsMlRpoR9lo7xoNd61yQed4BhOCVkXbNxobxCf3W%2F5PpwKOda%2FR9PYQ%2F26KSJ3pY6WXFWoS3mMxFMZsILkz0pL13XyWjAjCDBWWqAzGUpOB0j3gAqbvUMqMyRmIiaXMiow2QqYlEFDynv1ZQlsbG8rdYh%2FQexzWZiKB4bgVGlfR4GiWcpuOJ0ccwp&X-Amz-Signature=23a8ac28dee817ed5b76a581e7553dca6d38d33a50dbe604887a3aaa8aee589f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



