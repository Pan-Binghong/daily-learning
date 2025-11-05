---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
标签:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UBGMKHJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE2sGmN3q%2F0xtuvhWxov49s%2B%2BCxlXEwyrMXUQgits7zBAiBWxPTqtqbaHE%2FhFq8ilQNndfD5MYtaFxzg1chFxMGlGSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH6%2FzitBiHcbPp7FHKtwDjlmGSwx4dcHKv42GzM6Ro9YHfqTfztGP83v7hlOScuhu5lRZBnVfYbsVBywlX6OKTMH39tRLaKXe49tzmSBb8u6ofgWH1M6K1vdt5xCrBNQNdu23slqMkINb87pGB3ipnld1RCPCflI8vcSlvHDAtAuOkz9pC%2Fi%2FgwiTbpoyxBBuBlEbWU7dZEDf6M0fvhx4iIKQJstgS0cs4KnssJsJP6rHnE37tvdnVn2ngdXrOvpK%2BJqoiiZGbWFqhJ%2BC%2FeIi7hiczUXBINkCM6RMI2FJw8sPoxLENAchDkFYXRJoey7MnhRqI2hxzJ0SmCYZSjK3EMk4sPZPwzkhVdOr8ucXPD8BB4BistiY%2FvIL63Lp9YnJDsCeVlmWr%2BJU%2FBHc10H3JnN0KXBmu%2BLjO4pTRZ%2BcLETA%2Fvv%2Br856NnGmlqlGg%2Fj2Xjv4lB4spWtNAUGX82G7NIDOVSUqtqlE2ExPy5QAKqy%2FwxalfH6WilxSYF4wPVckbE9fTLso2J%2F4j8mXx%2FdEVzeTPGz536R4t4L%2FPb6i1dBTVji0A6wpY8%2Bo7VQkaeEyepbp3H9EtqbBaTZg3BCJeqXaQ2sd%2BdkZBXfh0vlJ8DDuW0optbdMXNY8EwOJsBXG0xY55F8J4qIopfcwxZ%2BsyAY6pgGThqVE5Vyj0NDUICFjBrbWMJhtLF7VGaLIw1yvaOAHZZyhmrlhw1OQ%2BhF08H13G4MUyQIXGpIlEGHjtAyjfyIo6WGikG2Phlj%2FLlz6kkeAaj4WjKMZ6g%2BlYSnSClrzrrfqsbONAS063jgGDnJ36icbawRetsDeXMcYyqosoyD1DgS9wnes4rRU4qO881r7rEohwUWm0EneasaA2KZSG5gg8UrMByc0&X-Amz-Signature=bbb4fb1d442d985ef99d88e3dded62290ff1c9daa3e3383b9b7d5e03b84d7612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UBGMKHJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE2sGmN3q%2F0xtuvhWxov49s%2B%2BCxlXEwyrMXUQgits7zBAiBWxPTqtqbaHE%2FhFq8ilQNndfD5MYtaFxzg1chFxMGlGSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH6%2FzitBiHcbPp7FHKtwDjlmGSwx4dcHKv42GzM6Ro9YHfqTfztGP83v7hlOScuhu5lRZBnVfYbsVBywlX6OKTMH39tRLaKXe49tzmSBb8u6ofgWH1M6K1vdt5xCrBNQNdu23slqMkINb87pGB3ipnld1RCPCflI8vcSlvHDAtAuOkz9pC%2Fi%2FgwiTbpoyxBBuBlEbWU7dZEDf6M0fvhx4iIKQJstgS0cs4KnssJsJP6rHnE37tvdnVn2ngdXrOvpK%2BJqoiiZGbWFqhJ%2BC%2FeIi7hiczUXBINkCM6RMI2FJw8sPoxLENAchDkFYXRJoey7MnhRqI2hxzJ0SmCYZSjK3EMk4sPZPwzkhVdOr8ucXPD8BB4BistiY%2FvIL63Lp9YnJDsCeVlmWr%2BJU%2FBHc10H3JnN0KXBmu%2BLjO4pTRZ%2BcLETA%2Fvv%2Br856NnGmlqlGg%2Fj2Xjv4lB4spWtNAUGX82G7NIDOVSUqtqlE2ExPy5QAKqy%2FwxalfH6WilxSYF4wPVckbE9fTLso2J%2F4j8mXx%2FdEVzeTPGz536R4t4L%2FPb6i1dBTVji0A6wpY8%2Bo7VQkaeEyepbp3H9EtqbBaTZg3BCJeqXaQ2sd%2BdkZBXfh0vlJ8DDuW0optbdMXNY8EwOJsBXG0xY55F8J4qIopfcwxZ%2BsyAY6pgGThqVE5Vyj0NDUICFjBrbWMJhtLF7VGaLIw1yvaOAHZZyhmrlhw1OQ%2BhF08H13G4MUyQIXGpIlEGHjtAyjfyIo6WGikG2Phlj%2FLlz6kkeAaj4WjKMZ6g%2BlYSnSClrzrrfqsbONAS063jgGDnJ36icbawRetsDeXMcYyqosoyD1DgS9wnes4rRU4qO881r7rEohwUWm0EneasaA2KZSG5gg8UrMByc0&X-Amz-Signature=fb5e66c3d4be60580e3c95b8e1fe371c6a4e71cc974da88a97d3b5c2edbd2329&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









