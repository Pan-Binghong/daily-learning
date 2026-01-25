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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2XJC3W6%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIEN9pSaatI8GpJ4oIF32wRWoSfEBjKCnud8QdVki2M8PAiBkWotzeNyyf8jk7a6Kkf7Cxmt2lrbD4hMa0%2Fyhlks13Cr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMtgljSt4o97KiZcIQKtwDPjPYuRwcO3DDFVcJPUDpmtVBqXxTIHGPFGBDjXkH%2BPKGkQDJivulvg%2F6T1OlxejQO1mIQK9l7NCJC3Cl2Tz2azN%2F7y5Taba06FKTkxP97yVpAjlxU%2BsjL%2FzM8hbvPwo0bDERPTzsEsNuNXhfkcKQkWaeziRXdsbk6IkHgjmFreW5Orvd2TEOhcOl1eydPaF1tlaFVne0VPj1gpn8gZlrenBkiybxu%2FK8m5RykME9nKwshlGxk9YA5TB7IGv%2FXd1uPYUNS7rCfbqWapjwFL6CUR8Qbw8l3Y0MNnVmRuCPZjNvTaWuJVu4M3D266mx%2FFw8UhkBGjPfkSxIXWPbxzChaGtixcG2POQdTqoT1AxDzHK0syYxjkj0qNWY1fkI1fPzZHozkd%2F2R9nivL3XMJkjQ57eOVnC6QxictU6J6cmlBF36gnjvSLq6Vz9xp0DgsNm1ghsgi1BxLJHds6dq7R4g8i%2BHBkZfM63eUixc6giHomeGcXNh7nxXpqBgcFhkzJ2lrhjJhMNOLKDuckowUwA8XX4OhFSLqehy8dzE4IUel3gdR5I5lBc54GgC6d8emIApq5hAioT2sjQEQRELOBDU7USkfi7BvusCZyAYe9tCDGxkkiwzdnwlqZC9mwwuoXWywY6pgECIfIOU3yisKwxiblsCkdMX5NOXQwqh9u8yJ%2BBtfFTHJfbbX7s%2FmbyQU3J359Tsz2GAQ4XUG25GE1zx%2FbWj0v2mWyHkYjjqURR2YNV37pEMWu7CWPL2EsEzdc2Ue5vNNYL7Mgbx3SIk3z4zRU73sTojrb9uinTRWWYlqwAeU17vh931%2FVn1yG6Ja36%2BZ0NlPdRQicqWAWub8bEviRXrTpJXywmu4zX&X-Amz-Signature=26d5104f6f7368de7ea2bbbdf2f7bf3393bb894e64809551df055101a2b2854a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2XJC3W6%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIEN9pSaatI8GpJ4oIF32wRWoSfEBjKCnud8QdVki2M8PAiBkWotzeNyyf8jk7a6Kkf7Cxmt2lrbD4hMa0%2Fyhlks13Cr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMtgljSt4o97KiZcIQKtwDPjPYuRwcO3DDFVcJPUDpmtVBqXxTIHGPFGBDjXkH%2BPKGkQDJivulvg%2F6T1OlxejQO1mIQK9l7NCJC3Cl2Tz2azN%2F7y5Taba06FKTkxP97yVpAjlxU%2BsjL%2FzM8hbvPwo0bDERPTzsEsNuNXhfkcKQkWaeziRXdsbk6IkHgjmFreW5Orvd2TEOhcOl1eydPaF1tlaFVne0VPj1gpn8gZlrenBkiybxu%2FK8m5RykME9nKwshlGxk9YA5TB7IGv%2FXd1uPYUNS7rCfbqWapjwFL6CUR8Qbw8l3Y0MNnVmRuCPZjNvTaWuJVu4M3D266mx%2FFw8UhkBGjPfkSxIXWPbxzChaGtixcG2POQdTqoT1AxDzHK0syYxjkj0qNWY1fkI1fPzZHozkd%2F2R9nivL3XMJkjQ57eOVnC6QxictU6J6cmlBF36gnjvSLq6Vz9xp0DgsNm1ghsgi1BxLJHds6dq7R4g8i%2BHBkZfM63eUixc6giHomeGcXNh7nxXpqBgcFhkzJ2lrhjJhMNOLKDuckowUwA8XX4OhFSLqehy8dzE4IUel3gdR5I5lBc54GgC6d8emIApq5hAioT2sjQEQRELOBDU7USkfi7BvusCZyAYe9tCDGxkkiwzdnwlqZC9mwwuoXWywY6pgECIfIOU3yisKwxiblsCkdMX5NOXQwqh9u8yJ%2BBtfFTHJfbbX7s%2FmbyQU3J359Tsz2GAQ4XUG25GE1zx%2FbWj0v2mWyHkYjjqURR2YNV37pEMWu7CWPL2EsEzdc2Ue5vNNYL7Mgbx3SIk3z4zRU73sTojrb9uinTRWWYlqwAeU17vh931%2FVn1yG6Ja36%2BZ0NlPdRQicqWAWub8bEviRXrTpJXywmu4zX&X-Amz-Signature=58d1f70f8589d39a5f8a024ecdc864dd3917adcd6668831f0e1d0b51b91fa55a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









