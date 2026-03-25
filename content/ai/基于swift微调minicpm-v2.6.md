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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRJ3IYM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuU4L0v55GZyd2RxxMHztiPChS1EzGAd7%2BKwJUG%2F0QYQIgdstuusVbgZfSYc0T%2BTjZGYLEYMgxyPCePXhB1q%2BPOqEqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPnbgEDdPcBGWzXgCrcA9HbOIwKWP%2Fut584eQ58Zop3gyBdXVJ0%2Fx94jSgoNHKrX6IyaHjrLA1G6%2FFpnOsvIuJslKMpzy17zMGxQ23tUwYcLQlJkMDkUdUD9pQCM%2FAR0Vnnp%2Fi4uI36q3e45O7aN1L11LeUZR109mXnR%2BFW4hRaBKgYSOEbaA7%2FUABmvD3%2F1UgfBR8TGtapsYcQQHOEIpHHnPSiTXXHoLGZ4sjX6Nl9Df3D0GQXw1GAtNhCdnxMBgqIf9FUi%2BY8bUc%2B8hfW5k%2B5Uw4zz0BBZmsSt9UnDEPOxkbbANACMJkRXYBo7VAaHmutAIWujmhgXboEof7cb%2BCGnR%2F8lbRhpuirjaUIf%2FCCujnURURkSgcdrmVufbWDaOXQm%2FeOenW9VbdzGU2pXv9pViIMCvGObLk5X9UIY2UxdjCuvVpx2wSnGt%2FScN9By5Co10CTRPuQArr5JXSwiIVTF2xD5SMOKODRW2SlNsbDhlQZwQuiy2Fo42Dj3pLiuJH1na4HycMuIuJqOWZ%2BZOoM6Szao8Rr38MvMWcjSh3TyECPFJZbWv7atnUq52ML0m36ueWHKv9H3wPQunJ4UZ88AIkLMe9MXJQ3Mokj8hqHbsW%2FkRCT23CiS9P5vmNzE0d5uceKwAEz6aWzMLLWjs4GOqUBJFrEUJSf%2B1uyX8yiqAGS%2BZpef4314h162p8wOvRVQdyvj2w4rgfYNiFg9ysbK5nO88iYriYx%2BCjK58kRBNatUIO3qERBctSy1jIDINj2Lf0kG42Vv4FvlsnDRlGeES30g6DiiAB5gAvn9Zpj6%2Fxn7AgHVLcN8IQVm5PVUGI0v4bxQcSh3exBtxg8dGC89XHnP73EXzM6OcZ5l5REdDGI67cFEFen&X-Amz-Signature=82aa3f18f6774795cae043bf3dd3e4362a6416788a250af0c486fa8dc4c4ebeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRJ3IYM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuU4L0v55GZyd2RxxMHztiPChS1EzGAd7%2BKwJUG%2F0QYQIgdstuusVbgZfSYc0T%2BTjZGYLEYMgxyPCePXhB1q%2BPOqEqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPnbgEDdPcBGWzXgCrcA9HbOIwKWP%2Fut584eQ58Zop3gyBdXVJ0%2Fx94jSgoNHKrX6IyaHjrLA1G6%2FFpnOsvIuJslKMpzy17zMGxQ23tUwYcLQlJkMDkUdUD9pQCM%2FAR0Vnnp%2Fi4uI36q3e45O7aN1L11LeUZR109mXnR%2BFW4hRaBKgYSOEbaA7%2FUABmvD3%2F1UgfBR8TGtapsYcQQHOEIpHHnPSiTXXHoLGZ4sjX6Nl9Df3D0GQXw1GAtNhCdnxMBgqIf9FUi%2BY8bUc%2B8hfW5k%2B5Uw4zz0BBZmsSt9UnDEPOxkbbANACMJkRXYBo7VAaHmutAIWujmhgXboEof7cb%2BCGnR%2F8lbRhpuirjaUIf%2FCCujnURURkSgcdrmVufbWDaOXQm%2FeOenW9VbdzGU2pXv9pViIMCvGObLk5X9UIY2UxdjCuvVpx2wSnGt%2FScN9By5Co10CTRPuQArr5JXSwiIVTF2xD5SMOKODRW2SlNsbDhlQZwQuiy2Fo42Dj3pLiuJH1na4HycMuIuJqOWZ%2BZOoM6Szao8Rr38MvMWcjSh3TyECPFJZbWv7atnUq52ML0m36ueWHKv9H3wPQunJ4UZ88AIkLMe9MXJQ3Mokj8hqHbsW%2FkRCT23CiS9P5vmNzE0d5uceKwAEz6aWzMLLWjs4GOqUBJFrEUJSf%2B1uyX8yiqAGS%2BZpef4314h162p8wOvRVQdyvj2w4rgfYNiFg9ysbK5nO88iYriYx%2BCjK58kRBNatUIO3qERBctSy1jIDINj2Lf0kG42Vv4FvlsnDRlGeES30g6DiiAB5gAvn9Zpj6%2Fxn7AgHVLcN8IQVm5PVUGI0v4bxQcSh3exBtxg8dGC89XHnP73EXzM6OcZ5l5REdDGI67cFEFen&X-Amz-Signature=177fb695d20163896efa870212392008d3680d4e34eafaef1a51b9f9cfbb70e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYRJ3IYM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuU4L0v55GZyd2RxxMHztiPChS1EzGAd7%2BKwJUG%2F0QYQIgdstuusVbgZfSYc0T%2BTjZGYLEYMgxyPCePXhB1q%2BPOqEqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPnbgEDdPcBGWzXgCrcA9HbOIwKWP%2Fut584eQ58Zop3gyBdXVJ0%2Fx94jSgoNHKrX6IyaHjrLA1G6%2FFpnOsvIuJslKMpzy17zMGxQ23tUwYcLQlJkMDkUdUD9pQCM%2FAR0Vnnp%2Fi4uI36q3e45O7aN1L11LeUZR109mXnR%2BFW4hRaBKgYSOEbaA7%2FUABmvD3%2F1UgfBR8TGtapsYcQQHOEIpHHnPSiTXXHoLGZ4sjX6Nl9Df3D0GQXw1GAtNhCdnxMBgqIf9FUi%2BY8bUc%2B8hfW5k%2B5Uw4zz0BBZmsSt9UnDEPOxkbbANACMJkRXYBo7VAaHmutAIWujmhgXboEof7cb%2BCGnR%2F8lbRhpuirjaUIf%2FCCujnURURkSgcdrmVufbWDaOXQm%2FeOenW9VbdzGU2pXv9pViIMCvGObLk5X9UIY2UxdjCuvVpx2wSnGt%2FScN9By5Co10CTRPuQArr5JXSwiIVTF2xD5SMOKODRW2SlNsbDhlQZwQuiy2Fo42Dj3pLiuJH1na4HycMuIuJqOWZ%2BZOoM6Szao8Rr38MvMWcjSh3TyECPFJZbWv7atnUq52ML0m36ueWHKv9H3wPQunJ4UZ88AIkLMe9MXJQ3Mokj8hqHbsW%2FkRCT23CiS9P5vmNzE0d5uceKwAEz6aWzMLLWjs4GOqUBJFrEUJSf%2B1uyX8yiqAGS%2BZpef4314h162p8wOvRVQdyvj2w4rgfYNiFg9ysbK5nO88iYriYx%2BCjK58kRBNatUIO3qERBctSy1jIDINj2Lf0kG42Vv4FvlsnDRlGeES30g6DiiAB5gAvn9Zpj6%2Fxn7AgHVLcN8IQVm5PVUGI0v4bxQcSh3exBtxg8dGC89XHnP73EXzM6OcZ5l5REdDGI67cFEFen&X-Amz-Signature=64a0d742817764f5abaee7a0239d9bdd3aa0c05478416392b3819a87b092df6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

