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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FQV4GYB%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNqDK6uFvo8QMWz3Bj9od83VcIIHro49%2BA2asiCyRpkwIhAI6DmahTUv%2BZwg6CwX01kq%2BGMsyFuj%2BrXmvzqSlGdjAyKv8DCGwQABoMNjM3NDIzMTgzODA1IgyX0ocVTYtKLBoXUX4q3AMMsx9nG%2FqwhmTev8haZ%2Fn23fHdU%2Bo%2FM9yM2DvU3aEoHKxOSBuZwGBlQBA9Fw6qUYRFATMoOVKksFKWINi6F2dj2GyNO41xYlHp0KCQqZK9hia7Hq3krJQv2B%2FFthlxlaAwcTkQL0PyZfkg8eaIP5%2FLMzSMfYB122CWoCcHvl0UFC24nLW%2FwPBNWn005Vwjj9A5LNRuM2OZZk9lup3ak2aPmq6TkRFTN8BCr%2BfcBSu7hVnDgmhfSacnDldHY2iFePKIPBpqgKlMBhQjd8yOem6Y55FbkRQBmQ9DuRn0l1nv3q9PDpBLyhmV42uYtzp0Dca4pERV1rawpSB88tyQqEDwP4S7C4MWBlFrv5XJrtzZy9M9eqdyvcrgEtuot4Igfhd4SY4AMIcsGxwDORuUW%2Bh6W9WOgBeLsQ002BJyttpeerP9swy%2FG6izfnKb551PC4yzKJ0HdzpvEz1P0RQWLg1TpBXNMJAZW6hApdhbEwMsRKqzdnX%2ByqWqdOvWRF2w6qFaMatem4foArX4VxwxX66ayuSSn5VlJ8qVo4BC%2FnfqFJyeub%2FzyfDOLgKspA6cqzq9F2ftwE8BZIxCL%2FNKMiUGZ2Mz1ywzsCsp%2FdMijFP8E5RGpvjl1R0Y%2FJfRATD0jffKBjqkAdswJct%2FIq9jPIXENYnpoGrtwiKGJN9%2FAenyYybnSnVKW7a0dE5SMDowawSszrbTegJ7OcHNN7UxLwMzzTvB6Zbx0geuD5tSEc8gBTd4yk7sTbW0iM186iEfWS99tJ0lEYbewG%2BO2gmX4mnLFHnpXYCw0pxxhRNiWeCR2WzKgVwdCYZiqw8vjEChzVujpLdlGuYJmN6odokC0K6XGpMKCEQvxjyB&X-Amz-Signature=f98d9cb76206d8a7bc5b6cbcdc97fba7f469f0d06b5c4c656b5f137e5bb2ca37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FQV4GYB%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNqDK6uFvo8QMWz3Bj9od83VcIIHro49%2BA2asiCyRpkwIhAI6DmahTUv%2BZwg6CwX01kq%2BGMsyFuj%2BrXmvzqSlGdjAyKv8DCGwQABoMNjM3NDIzMTgzODA1IgyX0ocVTYtKLBoXUX4q3AMMsx9nG%2FqwhmTev8haZ%2Fn23fHdU%2Bo%2FM9yM2DvU3aEoHKxOSBuZwGBlQBA9Fw6qUYRFATMoOVKksFKWINi6F2dj2GyNO41xYlHp0KCQqZK9hia7Hq3krJQv2B%2FFthlxlaAwcTkQL0PyZfkg8eaIP5%2FLMzSMfYB122CWoCcHvl0UFC24nLW%2FwPBNWn005Vwjj9A5LNRuM2OZZk9lup3ak2aPmq6TkRFTN8BCr%2BfcBSu7hVnDgmhfSacnDldHY2iFePKIPBpqgKlMBhQjd8yOem6Y55FbkRQBmQ9DuRn0l1nv3q9PDpBLyhmV42uYtzp0Dca4pERV1rawpSB88tyQqEDwP4S7C4MWBlFrv5XJrtzZy9M9eqdyvcrgEtuot4Igfhd4SY4AMIcsGxwDORuUW%2Bh6W9WOgBeLsQ002BJyttpeerP9swy%2FG6izfnKb551PC4yzKJ0HdzpvEz1P0RQWLg1TpBXNMJAZW6hApdhbEwMsRKqzdnX%2ByqWqdOvWRF2w6qFaMatem4foArX4VxwxX66ayuSSn5VlJ8qVo4BC%2FnfqFJyeub%2FzyfDOLgKspA6cqzq9F2ftwE8BZIxCL%2FNKMiUGZ2Mz1ywzsCsp%2FdMijFP8E5RGpvjl1R0Y%2FJfRATD0jffKBjqkAdswJct%2FIq9jPIXENYnpoGrtwiKGJN9%2FAenyYybnSnVKW7a0dE5SMDowawSszrbTegJ7OcHNN7UxLwMzzTvB6Zbx0geuD5tSEc8gBTd4yk7sTbW0iM186iEfWS99tJ0lEYbewG%2BO2gmX4mnLFHnpXYCw0pxxhRNiWeCR2WzKgVwdCYZiqw8vjEChzVujpLdlGuYJmN6odokC0K6XGpMKCEQvxjyB&X-Amz-Signature=3bcda034c84b4e41d54bec74543e6599acf787f369a6716facfc17c2e8cee1fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









