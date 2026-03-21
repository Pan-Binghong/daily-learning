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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7OFJGD5%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICuU89pt4J8q54AosrltMrYYMVVQKjFORlZ5QpkovXNpAiEAzi9oZOBa9K28QBalDAtYLlz6XEUc0ILvtu%2BNW%2Bomesoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDCv9YGuOwgUnWotRTircA1zoX%2FS8urlJJKjfB%2F1hk1NZj%2B1yki%2FRgwaAfpCpxYi9f2jB8s8GLIpt%2FodXWT3JEO%2BzSFfaA0EtTZOKAhPx76v8F5rV7A7%2Byr%2FMulm8bGKRDhCoEuhG9TXqOUHGHaT9VgTYacLF6xikdlajWxJRFPSHcVRS46dqXHcVZkc1ax3xCYSecjiNd9vFaGL%2BUkQMV2bID2LiNFXw%2B4bfC0u%2BV7k%2Fm%2BLXU7u9JEbapV9Y4UcdxzfYsIYgONFgCYjymBy9B7UulUJ%2BcP7povPyiKlPYMwU2IVfJil0q%2FIUIXqhYHiFJch%2FUA2HUo2eMf57oIQy6cwidhHs3XSNuafdfuYE2aYxvYNiWHJKskLrwVHJ%2B2WNXCoemCWNjQR5pp0bFkgBQljfm8CCS7Elj1lZEL6mvYZmsQVsVw7YA07fqF6ZAoJaKElWwcQgSh%2Fpncp5CRJfSNWqXhlUllq8%2BOM3c2uVZgJrqwxTXXGPSNN%2BkduilDgI4DJ2wRZJtsWCP68JwE0M9L8eqfBvWDe8xb9nUVHFSF%2BQsSM6OOHIzeJKBf22oXh2MZU5dXAsOhI4%2FYvRvVJ%2BtZr5lSLCQRgzY9fOD6jZEHksW49Onp5aUtJa9R4HdhuyprVv02fzDDBurzbYMLyQ%2BM0GOqUBDDP4xrO3pCy1NsO1xQ78ZJFF%2Bql5DFILIZ%2FrnE1ydLc6Hf5sierokaEtpJ8PPs8co6pNo4gJLiaOkyl3gUDCMNeVNf77hkErPcyG1U1VJ80esMZUUvUb6fA8AzGYWJY5Wamqccd8DLDxxkf6b1W8ahhY32KMsdl5pEp9uOn8LUqNomrIzkgHPP2Lb28YhzK6cK0fVWHwpuacDzbhX50BxOuaqEIB&X-Amz-Signature=d9534b9ae18cc74f48c051efc4212609bf01a6a8578502e7ce43cae8e3f582e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7OFJGD5%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICuU89pt4J8q54AosrltMrYYMVVQKjFORlZ5QpkovXNpAiEAzi9oZOBa9K28QBalDAtYLlz6XEUc0ILvtu%2BNW%2Bomesoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDCv9YGuOwgUnWotRTircA1zoX%2FS8urlJJKjfB%2F1hk1NZj%2B1yki%2FRgwaAfpCpxYi9f2jB8s8GLIpt%2FodXWT3JEO%2BzSFfaA0EtTZOKAhPx76v8F5rV7A7%2Byr%2FMulm8bGKRDhCoEuhG9TXqOUHGHaT9VgTYacLF6xikdlajWxJRFPSHcVRS46dqXHcVZkc1ax3xCYSecjiNd9vFaGL%2BUkQMV2bID2LiNFXw%2B4bfC0u%2BV7k%2Fm%2BLXU7u9JEbapV9Y4UcdxzfYsIYgONFgCYjymBy9B7UulUJ%2BcP7povPyiKlPYMwU2IVfJil0q%2FIUIXqhYHiFJch%2FUA2HUo2eMf57oIQy6cwidhHs3XSNuafdfuYE2aYxvYNiWHJKskLrwVHJ%2B2WNXCoemCWNjQR5pp0bFkgBQljfm8CCS7Elj1lZEL6mvYZmsQVsVw7YA07fqF6ZAoJaKElWwcQgSh%2Fpncp5CRJfSNWqXhlUllq8%2BOM3c2uVZgJrqwxTXXGPSNN%2BkduilDgI4DJ2wRZJtsWCP68JwE0M9L8eqfBvWDe8xb9nUVHFSF%2BQsSM6OOHIzeJKBf22oXh2MZU5dXAsOhI4%2FYvRvVJ%2BtZr5lSLCQRgzY9fOD6jZEHksW49Onp5aUtJa9R4HdhuyprVv02fzDDBurzbYMLyQ%2BM0GOqUBDDP4xrO3pCy1NsO1xQ78ZJFF%2Bql5DFILIZ%2FrnE1ydLc6Hf5sierokaEtpJ8PPs8co6pNo4gJLiaOkyl3gUDCMNeVNf77hkErPcyG1U1VJ80esMZUUvUb6fA8AzGYWJY5Wamqccd8DLDxxkf6b1W8ahhY32KMsdl5pEp9uOn8LUqNomrIzkgHPP2Lb28YhzK6cK0fVWHwpuacDzbhX50BxOuaqEIB&X-Amz-Signature=0be7a48bac9746ffd4a7104110b3a704adda9af9a9100058204f7c6fb752ccd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7OFJGD5%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICuU89pt4J8q54AosrltMrYYMVVQKjFORlZ5QpkovXNpAiEAzi9oZOBa9K28QBalDAtYLlz6XEUc0ILvtu%2BNW%2Bomesoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDCv9YGuOwgUnWotRTircA1zoX%2FS8urlJJKjfB%2F1hk1NZj%2B1yki%2FRgwaAfpCpxYi9f2jB8s8GLIpt%2FodXWT3JEO%2BzSFfaA0EtTZOKAhPx76v8F5rV7A7%2Byr%2FMulm8bGKRDhCoEuhG9TXqOUHGHaT9VgTYacLF6xikdlajWxJRFPSHcVRS46dqXHcVZkc1ax3xCYSecjiNd9vFaGL%2BUkQMV2bID2LiNFXw%2B4bfC0u%2BV7k%2Fm%2BLXU7u9JEbapV9Y4UcdxzfYsIYgONFgCYjymBy9B7UulUJ%2BcP7povPyiKlPYMwU2IVfJil0q%2FIUIXqhYHiFJch%2FUA2HUo2eMf57oIQy6cwidhHs3XSNuafdfuYE2aYxvYNiWHJKskLrwVHJ%2B2WNXCoemCWNjQR5pp0bFkgBQljfm8CCS7Elj1lZEL6mvYZmsQVsVw7YA07fqF6ZAoJaKElWwcQgSh%2Fpncp5CRJfSNWqXhlUllq8%2BOM3c2uVZgJrqwxTXXGPSNN%2BkduilDgI4DJ2wRZJtsWCP68JwE0M9L8eqfBvWDe8xb9nUVHFSF%2BQsSM6OOHIzeJKBf22oXh2MZU5dXAsOhI4%2FYvRvVJ%2BtZr5lSLCQRgzY9fOD6jZEHksW49Onp5aUtJa9R4HdhuyprVv02fzDDBurzbYMLyQ%2BM0GOqUBDDP4xrO3pCy1NsO1xQ78ZJFF%2Bql5DFILIZ%2FrnE1ydLc6Hf5sierokaEtpJ8PPs8co6pNo4gJLiaOkyl3gUDCMNeVNf77hkErPcyG1U1VJ80esMZUUvUb6fA8AzGYWJY5Wamqccd8DLDxxkf6b1W8ahhY32KMsdl5pEp9uOn8LUqNomrIzkgHPP2Lb28YhzK6cK0fVWHwpuacDzbhX50BxOuaqEIB&X-Amz-Signature=88efec4377d6de016987c2b3791522e58a583d9cc1b3b375d06380fd9fce5b60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

