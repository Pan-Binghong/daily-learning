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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7XY7HBD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBkvEboItM6rEaakCMufZDbme5ZF1PG%2B8eEji5VebVi1AiAt5PGE8l2MZdosvaKonPTbaaoZOO9BZe9y5Ni87eKDgSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMiQy76OaSwZj8bJO%2FKtwD31wF3Te81%2B%2FmxiH13j%2Ffywo7UosLF3bUzAB%2BPyjloAACxcblnb6rCZxq3Ms5ww%2Bp5EAflP4TDpUfFTUPSQLdTXok04IkdJLVWuP5eLhx%2FjDj6ZqLvyixo0mUl%2BIIRg%2BjFE3rVB0gERaP3Nx4YwIWBjARQLlCjCquo7q8d9rLrFfG7jlYYC01P5wX3NHb3WNE2gIfIlNtH%2FL2d0vN69UmnGhUbZapnU91AqTem4pCpXAv%2FPm8xlWz%2BLqJPSiY3QVPL9g107PqDnEXvdUF4kJQ0mOaIsGeCSbU7iwjZUIo%2FxE6sqoP0S%2BvdT3PsT8ojUi4jK9WjFjb5exz5ek64klZ8V%2F4RPHPOZ2bBYUhpk5Z8Z8mMCt0TO4DmqfpEYnYne3SLUG%2FmfXbFcTNI1idqDc%2BesodAja2881yGPUjCXmuLAHYFxcHwjvLs2l48RhEBe8GLD%2BPS7LA1YEfWoH0F0eGHOuVaCG368CASdM%2F4iXJk8U2ucjWXdGwyfaaDpcqucaKbubCXl8wr2tM%2FjcmQoYptTYKBZJV1nAzkZyYkzHWn6bEqecemJ1FVfOAIsu2geeGuQ4ohBUXUtFRYCALUr0vSlNNwfTA%2FC0mGZRvmcDPkVhY5A%2BvkIZFLreTaAwwio3zyQY6pgHZ70Uj%2B0K%2F8uKxHt6BlZpa8sCIoummjwrQOGe2ecbd4Q7hhlhCXiEW0r6hPnteJXphJp%2FFa5YSAYfFAicX7ouilvaP9BzTNIPNhJmjKmGZDIqhE730WuuoSaU8nXy5K%2FhATukvhwPgTVJPPqGKdgiGjaXfVuW%2By0jrgmZEN5DMjNJTebFeor8TTOy7%2BbKSqAjBHnNUYjUscgFU4DgXx5KiNLPOIoHs&X-Amz-Signature=5180f97f723f3d59e36b5dfadb2ef3a10aa922dd0df519f087d8be14373eea05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7XY7HBD%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBkvEboItM6rEaakCMufZDbme5ZF1PG%2B8eEji5VebVi1AiAt5PGE8l2MZdosvaKonPTbaaoZOO9BZe9y5Ni87eKDgSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMiQy76OaSwZj8bJO%2FKtwD31wF3Te81%2B%2FmxiH13j%2Ffywo7UosLF3bUzAB%2BPyjloAACxcblnb6rCZxq3Ms5ww%2Bp5EAflP4TDpUfFTUPSQLdTXok04IkdJLVWuP5eLhx%2FjDj6ZqLvyixo0mUl%2BIIRg%2BjFE3rVB0gERaP3Nx4YwIWBjARQLlCjCquo7q8d9rLrFfG7jlYYC01P5wX3NHb3WNE2gIfIlNtH%2FL2d0vN69UmnGhUbZapnU91AqTem4pCpXAv%2FPm8xlWz%2BLqJPSiY3QVPL9g107PqDnEXvdUF4kJQ0mOaIsGeCSbU7iwjZUIo%2FxE6sqoP0S%2BvdT3PsT8ojUi4jK9WjFjb5exz5ek64klZ8V%2F4RPHPOZ2bBYUhpk5Z8Z8mMCt0TO4DmqfpEYnYne3SLUG%2FmfXbFcTNI1idqDc%2BesodAja2881yGPUjCXmuLAHYFxcHwjvLs2l48RhEBe8GLD%2BPS7LA1YEfWoH0F0eGHOuVaCG368CASdM%2F4iXJk8U2ucjWXdGwyfaaDpcqucaKbubCXl8wr2tM%2FjcmQoYptTYKBZJV1nAzkZyYkzHWn6bEqecemJ1FVfOAIsu2geeGuQ4ohBUXUtFRYCALUr0vSlNNwfTA%2FC0mGZRvmcDPkVhY5A%2BvkIZFLreTaAwwio3zyQY6pgHZ70Uj%2B0K%2F8uKxHt6BlZpa8sCIoummjwrQOGe2ecbd4Q7hhlhCXiEW0r6hPnteJXphJp%2FFa5YSAYfFAicX7ouilvaP9BzTNIPNhJmjKmGZDIqhE730WuuoSaU8nXy5K%2FhATukvhwPgTVJPPqGKdgiGjaXfVuW%2By0jrgmZEN5DMjNJTebFeor8TTOy7%2BbKSqAjBHnNUYjUscgFU4DgXx5KiNLPOIoHs&X-Amz-Signature=b338891cc2809b68f915221989d6520ae9cb4a8a5ef92ac32c9aa31c355e6ee5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









