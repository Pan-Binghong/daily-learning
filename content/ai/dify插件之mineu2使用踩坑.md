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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGTHK2PK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOwXCVzAJ5YNWMJ8uiDnpqc0sr9CZZjH9YqTehIrLMJgIhAP5numJRxyqZ1QliVFZe5dYDN2IuL8IAPefE48ZJbQpoKv8DCGwQABoMNjM3NDIzMTgzODA1IgwvKrksez867DOj6r8q3AMBDBcN36ZxuQOwZNaNhdNMc%2FZBWcuQevswuGS7IkGqBsoygUWKxHb6C%2FGyuKKxycGM7LQ6%2BfvuSrYK7HXa%2B%2FrLIJbq7BdzXrxJ45Gn3qlfO5TJX61jflgoM10eCA0lzHqXQVn7EozX7%2B%2FpnY%2B3YTH1C0tToOgBzk7KwKMP3vClHnJ21E8MPvQTf%2FZqntXLsFqJFXaxKN7dHz7rURDZalWJW%2FP8IXpeYh12IyNWPw6eOQLyIAuI3Wd43dV3%2BpJgN9UmqJUx%2FvmWkREAjDMuamC4MPYiBkRJ7OS8KToSbjKV%2FQ7GFQvlgDZncLEuDvo61tJKRtcc2aLEgs0t3XnkkLdI9GS3PWUXzJoouZe4yDPAcE%2F%2BGMjRE%2BIqNk2IVft0m1GW%2Fbk9ZVQwg2aoE%2B7labkuhhihnT0jg4RVSCNHN8fzaHVjTDv6ddHtQsVMX%2BWQyNlGKBQYBjmQfNerbzuhZ4BSw03bWFd65wRpV%2BArm1Qd3VVzExziWuIaGrdsxWg31v6J8WM2ze8lilDl3r%2FbroCebDG4SEM75WtAZBNb3EGAVnI9sC7x2rfX99CtD%2Fsk4ueUQm7ElyNKCN95PtpJT4Cxy6YjSRvvmWma04KsQIY8HbTXfEva2zHs897f7DDGj%2FfKBjqkAVikIxeVCuhoSpgzguvA3s7eaHz9AZeVfOaHOre8YF%2Fd%2FxFxtj57yUA2OsKhgpwfqDkqv2kwfeKjPtfoDDRCISBROT9%2BCd1nj2bQ%2ByY7LYDK%2BOHvMNCCjEcdZzR6FcyvImB7A4qpJJJA0zd6oKpVN5fNig8U6TqkshNH0P4EK7G1Ytr46z7f4mg7K0mkyiFHgWB6RgK21aI6k1800ivUBcHohWcA&X-Amz-Signature=0389ceea69c6a58bd083d9db8c94215ff83a5025b5da2bb06022d557b071d57f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGTHK2PK%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOwXCVzAJ5YNWMJ8uiDnpqc0sr9CZZjH9YqTehIrLMJgIhAP5numJRxyqZ1QliVFZe5dYDN2IuL8IAPefE48ZJbQpoKv8DCGwQABoMNjM3NDIzMTgzODA1IgwvKrksez867DOj6r8q3AMBDBcN36ZxuQOwZNaNhdNMc%2FZBWcuQevswuGS7IkGqBsoygUWKxHb6C%2FGyuKKxycGM7LQ6%2BfvuSrYK7HXa%2B%2FrLIJbq7BdzXrxJ45Gn3qlfO5TJX61jflgoM10eCA0lzHqXQVn7EozX7%2B%2FpnY%2B3YTH1C0tToOgBzk7KwKMP3vClHnJ21E8MPvQTf%2FZqntXLsFqJFXaxKN7dHz7rURDZalWJW%2FP8IXpeYh12IyNWPw6eOQLyIAuI3Wd43dV3%2BpJgN9UmqJUx%2FvmWkREAjDMuamC4MPYiBkRJ7OS8KToSbjKV%2FQ7GFQvlgDZncLEuDvo61tJKRtcc2aLEgs0t3XnkkLdI9GS3PWUXzJoouZe4yDPAcE%2F%2BGMjRE%2BIqNk2IVft0m1GW%2Fbk9ZVQwg2aoE%2B7labkuhhihnT0jg4RVSCNHN8fzaHVjTDv6ddHtQsVMX%2BWQyNlGKBQYBjmQfNerbzuhZ4BSw03bWFd65wRpV%2BArm1Qd3VVzExziWuIaGrdsxWg31v6J8WM2ze8lilDl3r%2FbroCebDG4SEM75WtAZBNb3EGAVnI9sC7x2rfX99CtD%2Fsk4ueUQm7ElyNKCN95PtpJT4Cxy6YjSRvvmWma04KsQIY8HbTXfEva2zHs897f7DDGj%2FfKBjqkAVikIxeVCuhoSpgzguvA3s7eaHz9AZeVfOaHOre8YF%2Fd%2FxFxtj57yUA2OsKhgpwfqDkqv2kwfeKjPtfoDDRCISBROT9%2BCd1nj2bQ%2ByY7LYDK%2BOHvMNCCjEcdZzR6FcyvImB7A4qpJJJA0zd6oKpVN5fNig8U6TqkshNH0P4EK7G1Ytr46z7f4mg7K0mkyiFHgWB6RgK21aI6k1800ivUBcHohWcA&X-Amz-Signature=d273f39484c4ed5b724c7007e435b52c11e3ba0269e279ac46fdc6f37efc9d78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



