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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXJ3KSA%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuqKaxKyL%2FyaqshAvMuSx1u4%2F9EhB4QIouGbHd7iBrqQIhAJT%2BSgkKQE7gnOZq6PbAgVp%2B%2BBUdcZh3d6H39rvMT%2BfZKv8DCHMQABoMNjM3NDIzMTgzODA1IgyDTusKA2Drnb5YAaUq3ANNTcH44LiagwufFECx4CW5MrLGnzX5%2FkvLM3oqkhBn5wJKhzDvlkhDu4GpyHwKGO582%2B688WBPoPrijqAwKSML5dGFCbHN3NT%2BbdMby5Q%2BC76cszDohNaYWn2%2BmYrNGC%2FF2U7wO5yYRqFyqLp2svdQ8aqH%2B0%2Bjd6JMnVKgj8ZDF85%2BcX1YfpjJYH9DsB1YzrbW%2Fg7lpgfYLo3tBfA1Fcn2G8yvXxBHm7eZ5tX6zhJfpBU9H2LI5H7%2FdZFfTnZsH9tX37PenGM5zI8DWp1arRT7xMbdw8Mn346WQCwfwRGv%2BSYLjN3SWjaab%2B8VEm3cMN0Lld5S7oW%2Bo5NCk58iEE3dI8vabHHx6MBXqKMdJF%2B%2FMHpmSil9fefSuDHFO8Wj%2BOmJQ%2FUCtu%2BYFhgU5Vor3YLIytkYXvJbfmbcgN4CjXLbqKoROYnDJudKiSJjmWsGQ%2FiJ6S6cyNUM46ipZoqOmlGTzuYxZmi4CYENSCjrwGmQ7NAlFhq3aI3umlocbsPpWdyQhKjTiVwdyr8vkVRLBEobuZG9yVc0N5PK6hcVrAMn6iAfFJAtBQnkuwzYKBakMyYffTEf%2BftWj%2FfONAdKm1Z59Xq88HEDM6ZcaeQ0AB%2BWx19FvwHfNfGEYMdZrjCkgrHLBjqkAddj%2FWlxvo9I3lxR78hnifp9jwCimVusUzuAsjnATVQGu%2FAT67do1nOhFDFAv5OLiIgGkZz2NPdmwEUOv4ojoaPgVL2NKpNb1gDlJnnEgJIkKBt4rJB0RthhYgkcNHRkiTDXLSWwlZp7y0lCtbig4WnKumlgB4InGW3shaISkpCB1eGF3V6PpSk96AiZ4H4rMav%2FQVPgHg5%2BC6IR%2Fo%2Fm5HMo5XcN&X-Amz-Signature=e4b1c68765a33dc12887058e0b183cdf5eaf7a3043f225829788b3df2b1aa50f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXJ3KSA%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuqKaxKyL%2FyaqshAvMuSx1u4%2F9EhB4QIouGbHd7iBrqQIhAJT%2BSgkKQE7gnOZq6PbAgVp%2B%2BBUdcZh3d6H39rvMT%2BfZKv8DCHMQABoMNjM3NDIzMTgzODA1IgyDTusKA2Drnb5YAaUq3ANNTcH44LiagwufFECx4CW5MrLGnzX5%2FkvLM3oqkhBn5wJKhzDvlkhDu4GpyHwKGO582%2B688WBPoPrijqAwKSML5dGFCbHN3NT%2BbdMby5Q%2BC76cszDohNaYWn2%2BmYrNGC%2FF2U7wO5yYRqFyqLp2svdQ8aqH%2B0%2Bjd6JMnVKgj8ZDF85%2BcX1YfpjJYH9DsB1YzrbW%2Fg7lpgfYLo3tBfA1Fcn2G8yvXxBHm7eZ5tX6zhJfpBU9H2LI5H7%2FdZFfTnZsH9tX37PenGM5zI8DWp1arRT7xMbdw8Mn346WQCwfwRGv%2BSYLjN3SWjaab%2B8VEm3cMN0Lld5S7oW%2Bo5NCk58iEE3dI8vabHHx6MBXqKMdJF%2B%2FMHpmSil9fefSuDHFO8Wj%2BOmJQ%2FUCtu%2BYFhgU5Vor3YLIytkYXvJbfmbcgN4CjXLbqKoROYnDJudKiSJjmWsGQ%2FiJ6S6cyNUM46ipZoqOmlGTzuYxZmi4CYENSCjrwGmQ7NAlFhq3aI3umlocbsPpWdyQhKjTiVwdyr8vkVRLBEobuZG9yVc0N5PK6hcVrAMn6iAfFJAtBQnkuwzYKBakMyYffTEf%2BftWj%2FfONAdKm1Z59Xq88HEDM6ZcaeQ0AB%2BWx19FvwHfNfGEYMdZrjCkgrHLBjqkAddj%2FWlxvo9I3lxR78hnifp9jwCimVusUzuAsjnATVQGu%2FAT67do1nOhFDFAv5OLiIgGkZz2NPdmwEUOv4ojoaPgVL2NKpNb1gDlJnnEgJIkKBt4rJB0RthhYgkcNHRkiTDXLSWwlZp7y0lCtbig4WnKumlgB4InGW3shaISkpCB1eGF3V6PpSk96AiZ4H4rMav%2FQVPgHg5%2BC6IR%2Fo%2Fm5HMo5XcN&X-Amz-Signature=4f6e63b096d113d2ba4c41d93de1da9cbb2b93cd7e066107af7c52be33575a9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



