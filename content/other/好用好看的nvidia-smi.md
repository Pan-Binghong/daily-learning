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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ES7PLYF%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAG7n%2FGOjBp%2FenSCiafqscVI1pV6p9%2BbIXLb17l1koZuAiEAulSCx5LPODRIFoc1uThnbHlf%2BRq2kOi302w%2BrmVWjOAq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDPgz9AVhbc936UylFSrcA9y%2BuMxA0lfoMGuoU%2BCmdLNirpE%2Fg42h%2B0fGUc5%2BnGx3Cm22L%2BTnqbrEEXOyCXCUom3Xqz1YQx%2Bm%2BQ%2BxlcuSxjr9Fs5F06FJN%2B6G3A0iEGnOc5sraUFrR0xF4O1dxYCnSou%2BrVZSr7fO%2BMG3C0iURq%2Bj6w9Ve0ENDgJwAdfd1LaTTXXSe04x%2Bxfh7qLDWwl%2FQ7CYQNKkA1Ud4Fw3yBqPTDJu0s8c6PXn4ifcr7dKvQNtwFd4hRmPH1GzlrWenvjsV9w5iklA9gFknIxi3jawSIW8WBiqblQG3Lw2iW5EUuByaHELEanF%2BjZUFXXpcDVfkNTVbN5ezVRXa6%2BYBcZF0OUaYTt7RIg2rSZDyr2q7ZrhLdx7jzQ9L96yylQqFfJv0RrUs%2FZLlNpWs6PtNhUFvDbkrOyaRVrt6TCovGFmyfua0qgmDq%2BSc1olqfjtdfCOpbLRDOqpo0%2F0NSmk3bq%2BD6PtxQsWwEjWs051l2IWMy5%2B2KC%2F8LhTja3cvYyD%2BlWChnPiLHd6AMRqyWfAVgC4ngHmQ9mYcRmuE%2FSoyUiE3pkxgSFqwIZyDX1Dkyk9BWeitQDqVqS8KnVRfK7c3eHYhdZdMEyMfV8lQEVQlddJaFQkVoIqLuQbPfeI5jkSMITl8coGOqUBxzvPn21tFJKMzkE8QrsxBQoLRIOOnet9eERfuNtoInT5Dja6DEtL7DNOJi2F7cWOGczICad0bt5qGEWZPh0gZwkhD9Eb3K%2FJazU4xgi7G4iXslF2j8S6SGibaHixLNXHsu7e65VYaLcp6M9GaMC0goJzKOd%2FmgCHut9zRjnZ6E3XQrYqTGBOsBy%2BfBwBggbhb25HTflht8lVii%2BEWPVk1obZsHIA&X-Amz-Signature=6909e364b007a03f76f4be033c4b7a55eb8f718768f3abc2f7157e55e63ee0d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ES7PLYF%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAG7n%2FGOjBp%2FenSCiafqscVI1pV6p9%2BbIXLb17l1koZuAiEAulSCx5LPODRIFoc1uThnbHlf%2BRq2kOi302w%2BrmVWjOAq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDPgz9AVhbc936UylFSrcA9y%2BuMxA0lfoMGuoU%2BCmdLNirpE%2Fg42h%2B0fGUc5%2BnGx3Cm22L%2BTnqbrEEXOyCXCUom3Xqz1YQx%2Bm%2BQ%2BxlcuSxjr9Fs5F06FJN%2B6G3A0iEGnOc5sraUFrR0xF4O1dxYCnSou%2BrVZSr7fO%2BMG3C0iURq%2Bj6w9Ve0ENDgJwAdfd1LaTTXXSe04x%2Bxfh7qLDWwl%2FQ7CYQNKkA1Ud4Fw3yBqPTDJu0s8c6PXn4ifcr7dKvQNtwFd4hRmPH1GzlrWenvjsV9w5iklA9gFknIxi3jawSIW8WBiqblQG3Lw2iW5EUuByaHELEanF%2BjZUFXXpcDVfkNTVbN5ezVRXa6%2BYBcZF0OUaYTt7RIg2rSZDyr2q7ZrhLdx7jzQ9L96yylQqFfJv0RrUs%2FZLlNpWs6PtNhUFvDbkrOyaRVrt6TCovGFmyfua0qgmDq%2BSc1olqfjtdfCOpbLRDOqpo0%2F0NSmk3bq%2BD6PtxQsWwEjWs051l2IWMy5%2B2KC%2F8LhTja3cvYyD%2BlWChnPiLHd6AMRqyWfAVgC4ngHmQ9mYcRmuE%2FSoyUiE3pkxgSFqwIZyDX1Dkyk9BWeitQDqVqS8KnVRfK7c3eHYhdZdMEyMfV8lQEVQlddJaFQkVoIqLuQbPfeI5jkSMITl8coGOqUBxzvPn21tFJKMzkE8QrsxBQoLRIOOnet9eERfuNtoInT5Dja6DEtL7DNOJi2F7cWOGczICad0bt5qGEWZPh0gZwkhD9Eb3K%2FJazU4xgi7G4iXslF2j8S6SGibaHixLNXHsu7e65VYaLcp6M9GaMC0goJzKOd%2FmgCHut9zRjnZ6E3XQrYqTGBOsBy%2BfBwBggbhb25HTflht8lVii%2BEWPVk1obZsHIA&X-Amz-Signature=3917229913b83b678356385278594749deaec8f853e0ab73df7125ad5c4d349f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









