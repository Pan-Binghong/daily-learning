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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ3KEU4S%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQC%2Fohqj7MX1I0WI3ObYV6UMo8KknCIbqUK03rUrlpyIiQIhAJyCPkq%2Fm3vddZif9%2FqQbF9Sih3becJLE3rL%2By2uSCPKKv8DCB8QABoMNjM3NDIzMTgzODA1Igw62ltyBv0nlYO6S6oq3ANEFYZOaKcyrh1HMtLvRY7%2BUgP8fn8Qzbfnt3tysHjaXiINy83tmmW%2B0f%2BDT4QAERdjYGKAYSeTad5srY8%2BHdN6EkK%2BbdYLRQw2IHs8%2FPjBJngQpU8D02ycG7azu12EflF2WKmwtxB1LJlaDW0VcfzM4%2BpECpzGYkKlICp318z%2FOBIhOUXMOShJPrg5RmcTH0Rrx4F6HcYAGQZXqvcLGA%2BIQZ3mSRX5OuNiRtwEdag5tpwhSvxd4Vgi81X2RCpyiQ4MRCMnZiP4b4mnrUebQkrOYIn3UcoTSAwptxb3xHaslTbpBOUvKudLiqaE1Rbv%2FegA45dfwaFviRi0kJeIaTMBopWDneRiikxxmAdojCJAavwAxZ%2FGDHTnoMD8TnL7dtzAZHy8eKIytyjVCc9U9XJp5BhvshIR0YYIBFZyvLAHCiZs8avkmY%2BcEaaAcNE7OaWSFMJe7PzT6GTbTlK8G3HrVwqguXEBD85KQWi9jiZVnN7NTMZzflXqvhV8sqddb7fw%2F%2FxwZX18Uz6fn4AlzKKJ9gQlSKeI2HtXM2wPHTQWrVlti1n94CWjcbA43%2Fb1lSzegNbdPCEiJ0HvLsaPQql%2BBltJA8wNJm1pt07KKvAVm%2BR279UUR5EnP0yLfjCXoebKBjqkAV%2FcU4jOs1o6TQImUZkLl56LdvnBr8WIAFUDKSoBhkJ43UwOzzaAP%2FUUQ0csvN1xE8F5FFo0JUM97LKAV%2FmwXcwowiLqgyTgoly66WKSgv3MIYNqlCS0IJ4Yx2nHuWH9H9irdRMqRQYObd8VUNfHW2%2Fagbble%2FxTU%2BWpfjsWUzsoux6UJTpLhi7Ah2wpFHqQVlRAko8ndJ1OhSYxCO4hKKvPbEy9&X-Amz-Signature=3beb1d0f8b92a34a33e4f52968bab8820e1c9cd7b659a4dc0857a06f5cd5b242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ3KEU4S%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQC%2Fohqj7MX1I0WI3ObYV6UMo8KknCIbqUK03rUrlpyIiQIhAJyCPkq%2Fm3vddZif9%2FqQbF9Sih3becJLE3rL%2By2uSCPKKv8DCB8QABoMNjM3NDIzMTgzODA1Igw62ltyBv0nlYO6S6oq3ANEFYZOaKcyrh1HMtLvRY7%2BUgP8fn8Qzbfnt3tysHjaXiINy83tmmW%2B0f%2BDT4QAERdjYGKAYSeTad5srY8%2BHdN6EkK%2BbdYLRQw2IHs8%2FPjBJngQpU8D02ycG7azu12EflF2WKmwtxB1LJlaDW0VcfzM4%2BpECpzGYkKlICp318z%2FOBIhOUXMOShJPrg5RmcTH0Rrx4F6HcYAGQZXqvcLGA%2BIQZ3mSRX5OuNiRtwEdag5tpwhSvxd4Vgi81X2RCpyiQ4MRCMnZiP4b4mnrUebQkrOYIn3UcoTSAwptxb3xHaslTbpBOUvKudLiqaE1Rbv%2FegA45dfwaFviRi0kJeIaTMBopWDneRiikxxmAdojCJAavwAxZ%2FGDHTnoMD8TnL7dtzAZHy8eKIytyjVCc9U9XJp5BhvshIR0YYIBFZyvLAHCiZs8avkmY%2BcEaaAcNE7OaWSFMJe7PzT6GTbTlK8G3HrVwqguXEBD85KQWi9jiZVnN7NTMZzflXqvhV8sqddb7fw%2F%2FxwZX18Uz6fn4AlzKKJ9gQlSKeI2HtXM2wPHTQWrVlti1n94CWjcbA43%2Fb1lSzegNbdPCEiJ0HvLsaPQql%2BBltJA8wNJm1pt07KKvAVm%2BR279UUR5EnP0yLfjCXoebKBjqkAV%2FcU4jOs1o6TQImUZkLl56LdvnBr8WIAFUDKSoBhkJ43UwOzzaAP%2FUUQ0csvN1xE8F5FFo0JUM97LKAV%2FmwXcwowiLqgyTgoly66WKSgv3MIYNqlCS0IJ4Yx2nHuWH9H9irdRMqRQYObd8VUNfHW2%2Fagbble%2FxTU%2BWpfjsWUzsoux6UJTpLhi7Ah2wpFHqQVlRAko8ndJ1OhSYxCO4hKKvPbEy9&X-Amz-Signature=b43698297c7c843e992fdd4952d20611b6e890186675d89498dd9ee04b32e0cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









