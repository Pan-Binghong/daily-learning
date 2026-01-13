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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTPW4MUD%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCID8JH4fBSzoBOug7SfKOHF4ndrNISPskuAlk6b3gnXwnAiB0z6zTYTY3WWwnAkjOqmBLm0KgssCQhC%2FVyN3MmXoY4iqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKU3I6ZPtEGutieQQKtwDl8CgkHsxpq72gZExR%2B0seA5J3bmMw%2BZR%2FOcdV%2Bm9rIWVzvPqYfL2WnAuGa%2FXmbEQlnVZKHnKSwDahpC8Cy3Vm7lt1vvBPpldXfbrcEhuNpr3HWsrXeOpqHbGkiLs9YFrWcrXHlPw%2B360qoxTohsRYQxGiHpvswU9YTRdSZDRkMp0sl6Gewbpzl54%2FXOjDUXnWhdnnSqTGo2j3EaMfM0Piqo0G7MhPkoR45kQtu7E3m%2F9bWwGPqelUbFxyGOKk6ube6tX6j7hGICo2uJEFWbrjJL5f%2BJ16y8hb3I67NBsOzv7ZAHQs4kiU%2BN5Fz3x7lBT6aEGuTQ8JaEEohMNWIAJFApDQVFc7Q4SBFWeKRXZdeZ98XVIS%2Fq4iMauvjOf2aSiuzs525fEScbef96M54%2Fkf3sehvg3M9UagVoF%2BeuQq3%2B5YdyB7LxSi7EtJeUoHvihW4KjHg8FW1HHGNpP%2FjhOxen87jykN0vq%2FK9wgbu3zDWQsV6LsISENne4%2B%2B59tBFrDLd27DzO6NRyiuTqsH8G7cdxYbNqm7ASgQBj0TZx5rJI4W7b39E9jCufI7r6LvoBfNTaMqhpnlfV07TLsE5oXK1uJrmPtiqqyj1s15R9y%2FB6pFq3yFV94rFfEKEw3eWWywY6pgFNhOqAXKj891OQ3q6QUlWBkryX7n1Gl9dVFonbMeqnyTXcHWtYaFUfgfXKgzVfZJ4Junyv5d0jmax3phojgK6phgiyovH5z1cVMeDzWdHobGQO9HF83Vq6iFNuy%2FzVo%2BUbDFmfu5RsaxruQYZ0svO3soNq1h7g8leJ8%2BSg1J1SNEFZgyVNt3ymXln25yzD8vCv1SCEwhG4MgR0oUUGgR8UBRVgP4zR&X-Amz-Signature=ca202527f824a0db2d12814d7bac02142ec1d6fb5df72d90417f0de210c58d93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTPW4MUD%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCID8JH4fBSzoBOug7SfKOHF4ndrNISPskuAlk6b3gnXwnAiB0z6zTYTY3WWwnAkjOqmBLm0KgssCQhC%2FVyN3MmXoY4iqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKU3I6ZPtEGutieQQKtwDl8CgkHsxpq72gZExR%2B0seA5J3bmMw%2BZR%2FOcdV%2Bm9rIWVzvPqYfL2WnAuGa%2FXmbEQlnVZKHnKSwDahpC8Cy3Vm7lt1vvBPpldXfbrcEhuNpr3HWsrXeOpqHbGkiLs9YFrWcrXHlPw%2B360qoxTohsRYQxGiHpvswU9YTRdSZDRkMp0sl6Gewbpzl54%2FXOjDUXnWhdnnSqTGo2j3EaMfM0Piqo0G7MhPkoR45kQtu7E3m%2F9bWwGPqelUbFxyGOKk6ube6tX6j7hGICo2uJEFWbrjJL5f%2BJ16y8hb3I67NBsOzv7ZAHQs4kiU%2BN5Fz3x7lBT6aEGuTQ8JaEEohMNWIAJFApDQVFc7Q4SBFWeKRXZdeZ98XVIS%2Fq4iMauvjOf2aSiuzs525fEScbef96M54%2Fkf3sehvg3M9UagVoF%2BeuQq3%2B5YdyB7LxSi7EtJeUoHvihW4KjHg8FW1HHGNpP%2FjhOxen87jykN0vq%2FK9wgbu3zDWQsV6LsISENne4%2B%2B59tBFrDLd27DzO6NRyiuTqsH8G7cdxYbNqm7ASgQBj0TZx5rJI4W7b39E9jCufI7r6LvoBfNTaMqhpnlfV07TLsE5oXK1uJrmPtiqqyj1s15R9y%2FB6pFq3yFV94rFfEKEw3eWWywY6pgFNhOqAXKj891OQ3q6QUlWBkryX7n1Gl9dVFonbMeqnyTXcHWtYaFUfgfXKgzVfZJ4Junyv5d0jmax3phojgK6phgiyovH5z1cVMeDzWdHobGQO9HF83Vq6iFNuy%2FzVo%2BUbDFmfu5RsaxruQYZ0svO3soNq1h7g8leJ8%2BSg1J1SNEFZgyVNt3ymXln25yzD8vCv1SCEwhG4MgR0oUUGgR8UBRVgP4zR&X-Amz-Signature=31a41b100ac30e45e79c6fc1bc44a0f9ac25300590961da66603196589671a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









