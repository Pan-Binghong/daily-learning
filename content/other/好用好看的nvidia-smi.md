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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XHQPKJ3%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhZmfMmbwenIkCCFkjccc%2FI1KXZlB6%2BhqfYDpMd729DAiEA%2B5gwl0LVuRtWaJu17OHaFaqm0aDUjUYWjRUZuWtyxIQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAJTqus1FCAOmORe3ircA%2Fx2D8l5pQLt%2FeV4Wx5EkWHA48iOtIMQvFKpzkUkwK%2BY3MvkAiWJDhFn53XmOVkllbwzWtvJw511ebcHB9ju0951TlsIzxZJYy0nz%2F73pr%2FQ972BfqIGD6IpPWhnvj%2BlseR9Z0iqpZdV04riqtkhvVLZWOCCpAvQS2tEjFj7H1tPEyARthUaPj5BwRfCJMHMTTwI0aEmX4MAgyk4ZEnp%2F5hWJVJTaenNrM47YGr8keLp0qtx5xE0qzzoeWzYLgiRW96t8vBg8xMsnb8Itb8UP%2FNonj9WXYjpeELELtiSpfvmtUm%2FmBSH9hUi4AgjM9%2FDTmUKf0PkL8vesrSEzNPY8sj0dpjFXPPOardviHJuvxdPteHxvhQj9pPBB1IZ3zU3NYF4SDw7Y1MHwoJOH8udynaqJwA3fp9aJbDk12onBeLdy%2Bcn0dsX%2F6hMPUn7v0CYmT8MUSzbkpQQ11%2Bmy3ADkUMhDhgtXLqgKZ68EsPDB%2BrKk0nMWteCAfm5f2KZl0%2FVvYvL0FWUBiDq7gYiAn906808FBdP3FiW8MOe0JEa59%2BDWt6swASIoMl6LzBBsAR%2BIgwpZpJ5aIG4VkG9a1xo75tKeiyUZDe5o77o5ie8pR5mnPJiEolfYTDChlZtMNuxmckGOqUBdBxMr8tOHgel6lrfM9Pr2NYYi9m2mk5I%2BfT11p2Nh3WrGmnNQvhjiuSEtVcyx0lf%2F1fI%2F1QhtDi9I0ThkHQiYdI5qzhsz3oJ0PxpgHwfytXvOuChDm9FMHNhfQQ1kM1lNonnCvBxgWJ7COf%2BK2sfsr82tQHGx8rOoUNJxoF920hb%2Bq%2FAwY8m5zdEaEAQJzrUd5KwgyBKbS%2BL8cJ38QRK5UIYu6OF&X-Amz-Signature=31d7d8289147681a6de79efe248ba502322b5d555fb16bfb584cd988d0065f86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XHQPKJ3%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAhZmfMmbwenIkCCFkjccc%2FI1KXZlB6%2BhqfYDpMd729DAiEA%2B5gwl0LVuRtWaJu17OHaFaqm0aDUjUYWjRUZuWtyxIQq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDAJTqus1FCAOmORe3ircA%2Fx2D8l5pQLt%2FeV4Wx5EkWHA48iOtIMQvFKpzkUkwK%2BY3MvkAiWJDhFn53XmOVkllbwzWtvJw511ebcHB9ju0951TlsIzxZJYy0nz%2F73pr%2FQ972BfqIGD6IpPWhnvj%2BlseR9Z0iqpZdV04riqtkhvVLZWOCCpAvQS2tEjFj7H1tPEyARthUaPj5BwRfCJMHMTTwI0aEmX4MAgyk4ZEnp%2F5hWJVJTaenNrM47YGr8keLp0qtx5xE0qzzoeWzYLgiRW96t8vBg8xMsnb8Itb8UP%2FNonj9WXYjpeELELtiSpfvmtUm%2FmBSH9hUi4AgjM9%2FDTmUKf0PkL8vesrSEzNPY8sj0dpjFXPPOardviHJuvxdPteHxvhQj9pPBB1IZ3zU3NYF4SDw7Y1MHwoJOH8udynaqJwA3fp9aJbDk12onBeLdy%2Bcn0dsX%2F6hMPUn7v0CYmT8MUSzbkpQQ11%2Bmy3ADkUMhDhgtXLqgKZ68EsPDB%2BrKk0nMWteCAfm5f2KZl0%2FVvYvL0FWUBiDq7gYiAn906808FBdP3FiW8MOe0JEa59%2BDWt6swASIoMl6LzBBsAR%2BIgwpZpJ5aIG4VkG9a1xo75tKeiyUZDe5o77o5ie8pR5mnPJiEolfYTDChlZtMNuxmckGOqUBdBxMr8tOHgel6lrfM9Pr2NYYi9m2mk5I%2BfT11p2Nh3WrGmnNQvhjiuSEtVcyx0lf%2F1fI%2F1QhtDi9I0ThkHQiYdI5qzhsz3oJ0PxpgHwfytXvOuChDm9FMHNhfQQ1kM1lNonnCvBxgWJ7COf%2BK2sfsr82tQHGx8rOoUNJxoF920hb%2Bq%2FAwY8m5zdEaEAQJzrUd5KwgyBKbS%2BL8cJ38QRK5UIYu6OF&X-Amz-Signature=a620dc3e670d5b6ab3e01e5252547161c9ac25da4063b388e6ca98317d6d3213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









