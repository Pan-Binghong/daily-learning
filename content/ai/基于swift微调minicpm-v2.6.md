---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCRL5C%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDgBq%2BDmfsCMw6l2K2LJDu%2FSl574UD5bswFFiOzR03ouAiBy8cWKb8rcUSEGhj0uckL0Tm0gBzpD%2BKbwmdhlkAwEPCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMDOQ1Wr%2FbsceDEWCoKtwDJsTKxz5sVH5T6m8JvvQGOLWle%2BX9uZjwVzohZtHZPexrioE%2FqpVel8Futp%2BNlls1EFEbCbj%2FSPu%2B49kZXQqIv4Z27Y5NTWGdfvuchw5ohwEdidyo83zstlgzf%2Fju7euLDYBioXomUDyPedjGTh4xqbJgzUsv%2F57j26pr6QacSY3MQ3T0JRcLnTpxzFw8qmooK%2FheWupL%2Fx3%2BufZMHRKO6SZh1T8sh61u7ZbumHF66qyhCfDzRvpuuNjUdNJbUV2RN7vk26vto5N%2FgrLA5buVrwAcMXilqRZPZPZzsfdG%2B7usShGpYNiyEsBviTRPsn70JaL6vfYsdSZw9PKtcz20OOubVgwiF1mTU2gEI2%2BNdpP26qSWUy0EHMZw654RjbbOEu%2F2GH9ttCwqFmRnrhggwUZZZfahwr3XQq8VfBtc4iSQLYvkKU2dq4WCXBFV7pQINLcf8A3ZVYJU7JlkfIl2YTgILuN6u9x30%2BXJU2E69eWbKLPxFG8hxObc3fgFagXUMolMiLdja810c08l4zPI64f8WTi3OUMheAalp7sVu1cp5vrhxzWm14e2o3a2MgkIKaeFUBmcG99qd3etTSdTD8fibgx%2BKui%2FbivUvQiy%2F7y%2B73RgWUzXuwEvjn8wwsbtzQY6pgFFEk8Je6%2B8i6WG4MJeWpoXRamAjIPItTZOM%2B9dGdzSgDSSZR9Ukfc%2F4fobsVfjy5gXq6TiGucHsStMSUbV8nzcvxDl5TIx83AXbYN3y22s%2BMvlBJNtzFNrcJajA0ImK2c9pbJSMtZ9penwjZgqpa28u41Nnf4%2Bz%2Fw6xIWCtqf9siErHJD4CZ10USSC4pufOxYzWjrblJUcjOX6aPqsPZry8ap9wtf4&X-Amz-Signature=14703110448bab8afbf85e5eb7f80e7b603b74cae77c99aa7c31740875eb7a03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCRL5C%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDgBq%2BDmfsCMw6l2K2LJDu%2FSl574UD5bswFFiOzR03ouAiBy8cWKb8rcUSEGhj0uckL0Tm0gBzpD%2BKbwmdhlkAwEPCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMDOQ1Wr%2FbsceDEWCoKtwDJsTKxz5sVH5T6m8JvvQGOLWle%2BX9uZjwVzohZtHZPexrioE%2FqpVel8Futp%2BNlls1EFEbCbj%2FSPu%2B49kZXQqIv4Z27Y5NTWGdfvuchw5ohwEdidyo83zstlgzf%2Fju7euLDYBioXomUDyPedjGTh4xqbJgzUsv%2F57j26pr6QacSY3MQ3T0JRcLnTpxzFw8qmooK%2FheWupL%2Fx3%2BufZMHRKO6SZh1T8sh61u7ZbumHF66qyhCfDzRvpuuNjUdNJbUV2RN7vk26vto5N%2FgrLA5buVrwAcMXilqRZPZPZzsfdG%2B7usShGpYNiyEsBviTRPsn70JaL6vfYsdSZw9PKtcz20OOubVgwiF1mTU2gEI2%2BNdpP26qSWUy0EHMZw654RjbbOEu%2F2GH9ttCwqFmRnrhggwUZZZfahwr3XQq8VfBtc4iSQLYvkKU2dq4WCXBFV7pQINLcf8A3ZVYJU7JlkfIl2YTgILuN6u9x30%2BXJU2E69eWbKLPxFG8hxObc3fgFagXUMolMiLdja810c08l4zPI64f8WTi3OUMheAalp7sVu1cp5vrhxzWm14e2o3a2MgkIKaeFUBmcG99qd3etTSdTD8fibgx%2BKui%2FbivUvQiy%2F7y%2B73RgWUzXuwEvjn8wwsbtzQY6pgFFEk8Je6%2B8i6WG4MJeWpoXRamAjIPItTZOM%2B9dGdzSgDSSZR9Ukfc%2F4fobsVfjy5gXq6TiGucHsStMSUbV8nzcvxDl5TIx83AXbYN3y22s%2BMvlBJNtzFNrcJajA0ImK2c9pbJSMtZ9penwjZgqpa28u41Nnf4%2Bz%2Fw6xIWCtqf9siErHJD4CZ10USSC4pufOxYzWjrblJUcjOX6aPqsPZry8ap9wtf4&X-Amz-Signature=2daccc962ed8bcb4b8175fbfee9cc371a8e13fad8416e6474b71684194d5d6ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GCRL5C%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDgBq%2BDmfsCMw6l2K2LJDu%2FSl574UD5bswFFiOzR03ouAiBy8cWKb8rcUSEGhj0uckL0Tm0gBzpD%2BKbwmdhlkAwEPCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMDOQ1Wr%2FbsceDEWCoKtwDJsTKxz5sVH5T6m8JvvQGOLWle%2BX9uZjwVzohZtHZPexrioE%2FqpVel8Futp%2BNlls1EFEbCbj%2FSPu%2B49kZXQqIv4Z27Y5NTWGdfvuchw5ohwEdidyo83zstlgzf%2Fju7euLDYBioXomUDyPedjGTh4xqbJgzUsv%2F57j26pr6QacSY3MQ3T0JRcLnTpxzFw8qmooK%2FheWupL%2Fx3%2BufZMHRKO6SZh1T8sh61u7ZbumHF66qyhCfDzRvpuuNjUdNJbUV2RN7vk26vto5N%2FgrLA5buVrwAcMXilqRZPZPZzsfdG%2B7usShGpYNiyEsBviTRPsn70JaL6vfYsdSZw9PKtcz20OOubVgwiF1mTU2gEI2%2BNdpP26qSWUy0EHMZw654RjbbOEu%2F2GH9ttCwqFmRnrhggwUZZZfahwr3XQq8VfBtc4iSQLYvkKU2dq4WCXBFV7pQINLcf8A3ZVYJU7JlkfIl2YTgILuN6u9x30%2BXJU2E69eWbKLPxFG8hxObc3fgFagXUMolMiLdja810c08l4zPI64f8WTi3OUMheAalp7sVu1cp5vrhxzWm14e2o3a2MgkIKaeFUBmcG99qd3etTSdTD8fibgx%2BKui%2FbivUvQiy%2F7y%2B73RgWUzXuwEvjn8wwsbtzQY6pgFFEk8Je6%2B8i6WG4MJeWpoXRamAjIPItTZOM%2B9dGdzSgDSSZR9Ukfc%2F4fobsVfjy5gXq6TiGucHsStMSUbV8nzcvxDl5TIx83AXbYN3y22s%2BMvlBJNtzFNrcJajA0ImK2c9pbJSMtZ9penwjZgqpa28u41Nnf4%2Bz%2Fw6xIWCtqf9siErHJD4CZ10USSC4pufOxYzWjrblJUcjOX6aPqsPZry8ap9wtf4&X-Amz-Signature=24558e6a9c02d940bf6a41c2db286ea24b5512f69ef7cf3212d6e4bedc0328f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

