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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNZE5J67%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAc54UwDJrtbgFKfJJg4ex8roLOyemUUQDDE1XJdrsywIhAOhvq8sw7u5BDXOfvaAj4vIc7Jne0zYXNgY30nlpJVhXKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUv%2Fc11Kz3OHZLm%2Fcq3APRjFwSdkQDcUzn8Ob8YkZJAVFodqaYVB3cNRR3C7bMLmdrnTjD1sgVTAVtaqyfJrIkMn7FueydhCOJIX9cz%2FiJ2dq3nPXLRjagakcwGd6ssarNTsgrv31RUmxt4Mtnu2k1wjpp0Mh2MC7R9Wjv2ews%2BFmsvY7Sd0T6LilJB0xPV5whbE1dwZ5YWcmwGKhs9%2FrPbAR3aiWib8q%2BdcrmL0TaOxr22KCaZswt5izQNj2W4%2FQMvJqZdjdzXPtOYToGN6c6lYy0k3MCJjtaR5zbIUeyY61%2FmeUtZxgPAYPfusyXQTj2oPd7vD%2BNW%2BeC%2B5c1HpsUFyK5DnUUn7MmKkk6tJeSH4VQtMx3L8OQ%2B7dIN3wbcsuXTXkHXifwTsbwQrn92%2BC%2Bs2qmBOHG0XQ8xvaSBgDL6Q2ie7myuq0TWJPZ%2B8P%2F1nj0KcQkqANLofduC8Pb2fMM%2BKe%2BtkgdUL9PORb7gwdpAKYSRPrgNRE6Wa%2FaVFx%2BVjI0gjTeaNlooZ1AFx2TR7ZgvRQQrjGBjyKPD0njNCNsSsD85jMFpbG4QxPGaxE0%2BSXkbA%2BNeTYqp33WLNVIKxqrKXWuNucO%2B3HYrf2UX16RUzXNB2Sm7d6DMj3mRozzH8mca2jY%2FfOkw35EDzDzkLbPBjqkAa%2B7BaADu%2F6V0i3yFc1KBMVxWW3bnJ%2Fu9Yu4F%2BBM%2FQ6FXn%2FUiDWZtWwFS%2FlAvfWrl3KtUE6f6P5pPbRPeCBPcUcjcEK%2BeQUfhFZJP55As%2BoNU6yv%2BEtROSsZNdU7jRykkzybNIZdYSfi55vZnjhGGJvTuYyURxKxWVXpyoA4DifIOwsoNFN8K4Rnf16HMYpdU0YgiZpOzFn3kGpBeIxIqYwQ7XVU&X-Amz-Signature=69523b0586b10b6fe529b086289c44dd7d85fa3eeb1d9dbf6a46a1066053f591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNZE5J67%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAc54UwDJrtbgFKfJJg4ex8roLOyemUUQDDE1XJdrsywIhAOhvq8sw7u5BDXOfvaAj4vIc7Jne0zYXNgY30nlpJVhXKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUv%2Fc11Kz3OHZLm%2Fcq3APRjFwSdkQDcUzn8Ob8YkZJAVFodqaYVB3cNRR3C7bMLmdrnTjD1sgVTAVtaqyfJrIkMn7FueydhCOJIX9cz%2FiJ2dq3nPXLRjagakcwGd6ssarNTsgrv31RUmxt4Mtnu2k1wjpp0Mh2MC7R9Wjv2ews%2BFmsvY7Sd0T6LilJB0xPV5whbE1dwZ5YWcmwGKhs9%2FrPbAR3aiWib8q%2BdcrmL0TaOxr22KCaZswt5izQNj2W4%2FQMvJqZdjdzXPtOYToGN6c6lYy0k3MCJjtaR5zbIUeyY61%2FmeUtZxgPAYPfusyXQTj2oPd7vD%2BNW%2BeC%2B5c1HpsUFyK5DnUUn7MmKkk6tJeSH4VQtMx3L8OQ%2B7dIN3wbcsuXTXkHXifwTsbwQrn92%2BC%2Bs2qmBOHG0XQ8xvaSBgDL6Q2ie7myuq0TWJPZ%2B8P%2F1nj0KcQkqANLofduC8Pb2fMM%2BKe%2BtkgdUL9PORb7gwdpAKYSRPrgNRE6Wa%2FaVFx%2BVjI0gjTeaNlooZ1AFx2TR7ZgvRQQrjGBjyKPD0njNCNsSsD85jMFpbG4QxPGaxE0%2BSXkbA%2BNeTYqp33WLNVIKxqrKXWuNucO%2B3HYrf2UX16RUzXNB2Sm7d6DMj3mRozzH8mca2jY%2FfOkw35EDzDzkLbPBjqkAa%2B7BaADu%2F6V0i3yFc1KBMVxWW3bnJ%2Fu9Yu4F%2BBM%2FQ6FXn%2FUiDWZtWwFS%2FlAvfWrl3KtUE6f6P5pPbRPeCBPcUcjcEK%2BeQUfhFZJP55As%2BoNU6yv%2BEtROSsZNdU7jRykkzybNIZdYSfi55vZnjhGGJvTuYyURxKxWVXpyoA4DifIOwsoNFN8K4Rnf16HMYpdU0YgiZpOzFn3kGpBeIxIqYwQ7XVU&X-Amz-Signature=75f0a40ca5094e1739939d8c7eb057fd46f3a4ba72da158fc3db0587fe17d5e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









