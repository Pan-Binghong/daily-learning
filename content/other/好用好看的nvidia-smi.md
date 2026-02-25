---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZI4EOKM%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQC2ymWKKpE1An0vs%2BsCMqg2qK8rcjGuYu0wTMqzwbsOMQIhAKtUvDLzJOMkFMqHU1A33%2Fk9m%2FW6WyJ0%2BjXcRTWvTnl1Kv8DCAIQABoMNjM3NDIzMTgzODA1Igx8AXRIvX0nYmOEcLkq3AMVFqM8uOcRJfXvMALcnAogZLH1PDezIyxnJJ7YLfWbVlcpCn6EsDBxRQQk%2BGakStnFXQQ6cRF8Q5%2FZBsS9X31R4FDsqlpgTkpxyurLbIoVsSSz5jpFQT0p%2FCFatUqe5GpdBEPo6mSFwNSZMtBq20OLlJ30dgy2%2BLH4M0QY%2FJRxZxVFB6vpqf7287j%2FYM%2Bi2%2BYQjyTowqtb6hFMJaM8ATFr8aLZgKEVtZ1W4JgV9Voa4yVEfbYmYJ%2FgWd3jhwvcZmVJu4CdG4x6iN1ib9mEcnUXdoWFjAps1%2FfvrAjzXx%2FI8rYaNKJB052OilRYIoFjdc5i5X4f%2FLxiS6A9SDbooD9jknk5dQI%2Fmn%2BNKutMnXHYMZkIrn3Xh3%2F62Pb9nqPJFaVu252PHSIq7yw5kEgFy3adqdc96Wc45RdwWUutsNJsOWNcxndwb%2BBU8ua2SYOxXUzRV5uJxisspWDi2wM%2FByntJQb0eGVsShZ9XhjAISkVLwQd2giMPVS3Rv9xne7OGhhdVoqL07d6cEDDOU4nyE4ZrdR5h7GG%2BFfNfYs6aTsrpNiNk%2BKk%2F535b6wDNqBYi3NpliCOZfPl2LF8EnW4OW7VvP9YFxORm9i2I%2F7sF3KG8PpkXI9aFt79aZv5PDCXhPnMBjqkAZDp0QnJS8ehBdvKAUlJUWrTGVsY6DWvdBDh4Jbto%2BBQI1IJaa7NARQWsi1aPvgH%2BoONYO8B4nLI%2BomiqW3svaH%2B3QIH0DRI2qOI%2BAf7eJA3Ut%2FuS8mUkfaOUUZIxq5hS6zf3m%2FYBWTNakfl3rI1zKTqSNLpX90PKO0tZrcNowCt%2BINhI8NMC9mHFzFejdtIsvUFoK9OTVlPiB2yRGBN178Vq6ac&X-Amz-Signature=25fd7a4c93e027d48e094ca0faa7a0f0ad02bdef1faaa2782e0033e82a9d6817&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZI4EOKM%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQC2ymWKKpE1An0vs%2BsCMqg2qK8rcjGuYu0wTMqzwbsOMQIhAKtUvDLzJOMkFMqHU1A33%2Fk9m%2FW6WyJ0%2BjXcRTWvTnl1Kv8DCAIQABoMNjM3NDIzMTgzODA1Igx8AXRIvX0nYmOEcLkq3AMVFqM8uOcRJfXvMALcnAogZLH1PDezIyxnJJ7YLfWbVlcpCn6EsDBxRQQk%2BGakStnFXQQ6cRF8Q5%2FZBsS9X31R4FDsqlpgTkpxyurLbIoVsSSz5jpFQT0p%2FCFatUqe5GpdBEPo6mSFwNSZMtBq20OLlJ30dgy2%2BLH4M0QY%2FJRxZxVFB6vpqf7287j%2FYM%2Bi2%2BYQjyTowqtb6hFMJaM8ATFr8aLZgKEVtZ1W4JgV9Voa4yVEfbYmYJ%2FgWd3jhwvcZmVJu4CdG4x6iN1ib9mEcnUXdoWFjAps1%2FfvrAjzXx%2FI8rYaNKJB052OilRYIoFjdc5i5X4f%2FLxiS6A9SDbooD9jknk5dQI%2Fmn%2BNKutMnXHYMZkIrn3Xh3%2F62Pb9nqPJFaVu252PHSIq7yw5kEgFy3adqdc96Wc45RdwWUutsNJsOWNcxndwb%2BBU8ua2SYOxXUzRV5uJxisspWDi2wM%2FByntJQb0eGVsShZ9XhjAISkVLwQd2giMPVS3Rv9xne7OGhhdVoqL07d6cEDDOU4nyE4ZrdR5h7GG%2BFfNfYs6aTsrpNiNk%2BKk%2F535b6wDNqBYi3NpliCOZfPl2LF8EnW4OW7VvP9YFxORm9i2I%2F7sF3KG8PpkXI9aFt79aZv5PDCXhPnMBjqkAZDp0QnJS8ehBdvKAUlJUWrTGVsY6DWvdBDh4Jbto%2BBQI1IJaa7NARQWsi1aPvgH%2BoONYO8B4nLI%2BomiqW3svaH%2B3QIH0DRI2qOI%2BAf7eJA3Ut%2FuS8mUkfaOUUZIxq5hS6zf3m%2FYBWTNakfl3rI1zKTqSNLpX90PKO0tZrcNowCt%2BINhI8NMC9mHFzFejdtIsvUFoK9OTVlPiB2yRGBN178Vq6ac&X-Amz-Signature=7a2d37fa4e8fff69088740d7fa3b1911904bd9fa1aad74b708c6f666892f00a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









