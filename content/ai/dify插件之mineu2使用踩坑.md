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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTWY7BM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8yKW4drnspJPPpGTc9seI4RZ6IHXBJ%2BMsSAFJ%2By27%2FQIgNuMNuE%2FfCtHmO0%2F7yUkv16ArpWCD8Tt4TurII4AgVRsq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJrkQhiNht3mXVvymircA89RXZdKPABrn3a%2B9uUZcu3gozbCEWxT%2FeMdeKZIyk2zBnKNG7O7%2FXzZAR7SUavrebW8tkzC%2BxHfCDNtgUwmb2mXcf3hMRjmowJKgK8aVu2clqgKXtm1l82gBrmtxu2s5VROuxyPGuZwkHv1AiI%2F%2Bym8lNZPzvp%2FtQJyNvBBgctt4iO87OViydoKlayjBvPhT9MRCXZLGwQaCb50j5jvOpFV13khnZStILv5kPpw6LG%2FJNpluse5l7qm3OgUowCKvcVy7ZJLDZLvIMM2Cd8whYVFWJ0G8TsOUZWlPiyzJ2nByoKwJKPr3KCEmgh%2FXkJUkp3p%2FyfuM4HfrAa0cyytkUkQL8c6ObmRAodGjaTi%2F3DWjvkrVEl6oHRS%2B0oRG2QFxvWspTDfWciMVKYB3kF5KAwIWC%2F4tTu%2FTKPBrOw%2FBU7qyqDqcBgDl6uf5f6HEchSggV2wOdIBd%2B1gvAR%2B3ycu1%2FUO7foNcMxnW3yU895fCm7w9vvGb84rIRObsantehsSP7DLSs3QmUjiE%2FSjna83al2fgxElBhS3oJaTFlMax9CuFTE0yKaSba8%2Fm%2BUiiE1X4dU9ThAPYoPiR2kUNrzt7Gg%2Fisio%2FVbacLhm6dfcgScgsT723h227qLA7CwMNSwt84GOqUBFp%2B7zka2JwB2Yj%2BPfWA5l%2Fbk2iKYNwPyp6K9zPVNPd8uUkFdLw8nilT4Y4Qd%2F49hb5DrH%2F6TiCYMM%2BuAVHeViRfNlMhoQXX076N3OZ2Vi%2BoIHC3u04Z6tz5DPq477Ed8DyOpXYwT43Np1KvWNE1aa2vCpFQ1%2Fbv00QziQrD%2BKV7YzLw6bGnNKLN0t4MIYNutcBoaUtmeR2Br9jCwAC3ROTgh9nt4&X-Amz-Signature=61a95e549a034b1518ecbaf7648286d236f22425ca61ecd5361666f3f39baa8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOTWY7BM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8yKW4drnspJPPpGTc9seI4RZ6IHXBJ%2BMsSAFJ%2By27%2FQIgNuMNuE%2FfCtHmO0%2F7yUkv16ArpWCD8Tt4TurII4AgVRsq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJrkQhiNht3mXVvymircA89RXZdKPABrn3a%2B9uUZcu3gozbCEWxT%2FeMdeKZIyk2zBnKNG7O7%2FXzZAR7SUavrebW8tkzC%2BxHfCDNtgUwmb2mXcf3hMRjmowJKgK8aVu2clqgKXtm1l82gBrmtxu2s5VROuxyPGuZwkHv1AiI%2F%2Bym8lNZPzvp%2FtQJyNvBBgctt4iO87OViydoKlayjBvPhT9MRCXZLGwQaCb50j5jvOpFV13khnZStILv5kPpw6LG%2FJNpluse5l7qm3OgUowCKvcVy7ZJLDZLvIMM2Cd8whYVFWJ0G8TsOUZWlPiyzJ2nByoKwJKPr3KCEmgh%2FXkJUkp3p%2FyfuM4HfrAa0cyytkUkQL8c6ObmRAodGjaTi%2F3DWjvkrVEl6oHRS%2B0oRG2QFxvWspTDfWciMVKYB3kF5KAwIWC%2F4tTu%2FTKPBrOw%2FBU7qyqDqcBgDl6uf5f6HEchSggV2wOdIBd%2B1gvAR%2B3ycu1%2FUO7foNcMxnW3yU895fCm7w9vvGb84rIRObsantehsSP7DLSs3QmUjiE%2FSjna83al2fgxElBhS3oJaTFlMax9CuFTE0yKaSba8%2Fm%2BUiiE1X4dU9ThAPYoPiR2kUNrzt7Gg%2Fisio%2FVbacLhm6dfcgScgsT723h227qLA7CwMNSwt84GOqUBFp%2B7zka2JwB2Yj%2BPfWA5l%2Fbk2iKYNwPyp6K9zPVNPd8uUkFdLw8nilT4Y4Qd%2F49hb5DrH%2F6TiCYMM%2BuAVHeViRfNlMhoQXX076N3OZ2Vi%2BoIHC3u04Z6tz5DPq477Ed8DyOpXYwT43Np1KvWNE1aa2vCpFQ1%2Fbv00QziQrD%2BKV7YzLw6bGnNKLN0t4MIYNutcBoaUtmeR2Br9jCwAC3ROTgh9nt4&X-Amz-Signature=c2c35f1e60ccb7b06d2cf583518a45bce09b6a999009239a8ee97a9fcc3c7892&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



