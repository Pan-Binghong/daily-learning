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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OKJGMIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCqCzcCNT%2B0Di5Oey1%2F39uttZBYIR4TCQTR82ebuaOOnwIgd0PGjZTuGOHishHBsT6ylSUxnPHcInr4ErYE%2Bus52MAqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzkXb%2BEa4q%2B2%2Fah0ircAzsUeBA%2BWtrzNgBFD2eby9kYYv9PC5NLpp5xE6JADbRfwcaXC3rBSbuBOUnO5qe1x7YTH9TT4qtmcsFK0cFopCRHuWC0tmbNc4w9V3gJ78XvPeLOF8PwZJ9%2BO8Rhgg5xQ7S3x3a73zi%2BRdgMaTjj1CHFwAEV2LiRtz2M%2BT1%2B%2BDEjGOuXRl7L2aGa9HuzsxhF1t2obIwUKQMQp44lllRioByzOCFlp9DSZxV%2Fbyr1suz%2BHE13mZglrRN9Bdz5hQ2%2BvCJfTmBhRDrUTO%2FiFWn4qMTL80CSnGC10J4DqHMkZMhl%2B8dcZCQJl4Vz7ti8DLJ9YtiraQq6aL6U7rHjqXhBBuorf5SJtjiUjNqxGGl711wzX8lYWWobcA1Qn6jv2nB5yh6sJh%2BwPQUqpTfYD7Kk2DGAJtW5MJ%2B2ja9uNibLo59RazBtNASFnrq4zLGUvMdJMWBZbucob2EYmCsKIGd8evPRAh%2BLHQ%2FrbOYcjtcqHO264ju0TFV%2BmgLt0vzARo1LlNhPt1Y1QoPqSs%2BhRd8pd2kfnMhypOo4KxuvUUanedem5ySRj4RiYK0qCOkdA2f7Z1MPR9YzSbTlCeTwUfrOlS5FdqfEZdYHglK9cejg6F3Np1Ufe3a7rsgX81xOMLTYhcwGOqUBYWI7xWWPF8aCfbGBPjQP1oixRTWkPfNrFJJFk7%2Bklfnk46BgDBc8lIes%2BceGRzJ8w6%2FupZBYVRzqUOygaS14hML5%2Bv2OmIXzfkFvKJkO2cybO1T2uSDLbVcpBb17uT9CQMS%2FZV%2F9aOs8yS%2B8BdcgAALcpVBSUkR7XJNyOUlEyxb7erdwepMwrkTQIgHhlZqZLcFyOkD9zXv%2Bydga6kEhWI4qDNzZ&X-Amz-Signature=e9ad2abdb0149174088f85f9a36db345d4a8ee4444f027c646a2dd6f08d9d06b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OKJGMIZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCqCzcCNT%2B0Di5Oey1%2F39uttZBYIR4TCQTR82ebuaOOnwIgd0PGjZTuGOHishHBsT6ylSUxnPHcInr4ErYE%2Bus52MAqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzkXb%2BEa4q%2B2%2Fah0ircAzsUeBA%2BWtrzNgBFD2eby9kYYv9PC5NLpp5xE6JADbRfwcaXC3rBSbuBOUnO5qe1x7YTH9TT4qtmcsFK0cFopCRHuWC0tmbNc4w9V3gJ78XvPeLOF8PwZJ9%2BO8Rhgg5xQ7S3x3a73zi%2BRdgMaTjj1CHFwAEV2LiRtz2M%2BT1%2B%2BDEjGOuXRl7L2aGa9HuzsxhF1t2obIwUKQMQp44lllRioByzOCFlp9DSZxV%2Fbyr1suz%2BHE13mZglrRN9Bdz5hQ2%2BvCJfTmBhRDrUTO%2FiFWn4qMTL80CSnGC10J4DqHMkZMhl%2B8dcZCQJl4Vz7ti8DLJ9YtiraQq6aL6U7rHjqXhBBuorf5SJtjiUjNqxGGl711wzX8lYWWobcA1Qn6jv2nB5yh6sJh%2BwPQUqpTfYD7Kk2DGAJtW5MJ%2B2ja9uNibLo59RazBtNASFnrq4zLGUvMdJMWBZbucob2EYmCsKIGd8evPRAh%2BLHQ%2FrbOYcjtcqHO264ju0TFV%2BmgLt0vzARo1LlNhPt1Y1QoPqSs%2BhRd8pd2kfnMhypOo4KxuvUUanedem5ySRj4RiYK0qCOkdA2f7Z1MPR9YzSbTlCeTwUfrOlS5FdqfEZdYHglK9cejg6F3Np1Ufe3a7rsgX81xOMLTYhcwGOqUBYWI7xWWPF8aCfbGBPjQP1oixRTWkPfNrFJJFk7%2Bklfnk46BgDBc8lIes%2BceGRzJ8w6%2FupZBYVRzqUOygaS14hML5%2Bv2OmIXzfkFvKJkO2cybO1T2uSDLbVcpBb17uT9CQMS%2FZV%2F9aOs8yS%2B8BdcgAALcpVBSUkR7XJNyOUlEyxb7erdwepMwrkTQIgHhlZqZLcFyOkD9zXv%2Bydga6kEhWI4qDNzZ&X-Amz-Signature=7b90f6e753fa97be576cb6cdca2adfa1732486662264045815ed09f88539b51c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



