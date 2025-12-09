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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BQZBEDU%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO%2FLvbbzdF2ANiy9xMtY4ULoGpKradUZv3JE2PTwIkqAIhANa8IqNB1x6KVtBpOcKuHIgtUfoxlf1xdzCo6s%2FQdkPoKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz4lTXSXMqthgwfWoq3AO7nq%2FIh4Z8A68mGsJB1EHqjj1pOIp%2BGe40R6wI68%2FP%2FPT7WVoiHMFbb6FrT2JBfkjqhBHEi4E1lwnnLl%2FK8e41S7RSVNCKj4dqVLbN7da6I2jjRDGQO%2BuzFJoLZZ177WrcSXDNayNqdmFX2njymEI4a%2B%2FBkNAjwhClOnbcjTeFnGrlcQ53kryPfSer5v2V%2BhCAf1T%2FEzS7Iq3os1G2qK3GU%2BoHdMNFFUi%2BLDhAUkzoZCcJe3hPIbVJGFxn%2BkRdVpTg%2Fj9KxZhsD5vwXSRAtMt%2FB50617vjQ97%2FBieOl%2F0YOLg2ZD9%2BcVl04%2F4jlZsNjyt4rXmYNXzYANifjT0ywU1YKXEd%2BiRyfmiL%2Bl60b7fZav%2FI2rrXR8ln5tXWKOtyBCL1gm%2Bf03kvE%2BYBK6B0iTgdasOgQwAYtgbqZAAbPrf4nCXTl9EoWEsK3%2F%2BGCiQL8cjMbPvgTQKjBkmPq82Q0O6PbOnK7tr3eCBjEZNQAA6%2F9CUffWFr6ddfduCdjcXvKhAMxjLbNC64oLgCV1KXyg8qReeiHX%2Fm52uAgGN%2BsYJvEXzc4qk1nsL3F4XPPVM1Uq3AaU4XGiSTPXolmsob%2FhMK3XOoHenc4vWtPYXT3KhXTSE7roG0eZGtLf0ZQjC%2FkN7JBjqkAQ%2Bc9CBhsNtiVVXwJ%2FAZJsfkR9u6FNWCo%2BBranUwpChoyJvDhi0LyesO0JYNLhI0bzrHQ6iu3%2BePpdQhfyDyUZhLd4FymI6qGrbyviJ5J3xWy%2FFm%2BGlU7Af5JWoTGUYVH16FE3UP%2FwSK071rk8aBG6%2FbjE5IpfYo1lYnNv8LHT3BHy6MWMGk%2BIElb7VGkIG4dO%2FUyRCuRkOpnTfMf5JGJCzkxVoC&X-Amz-Signature=f7a7d5c3526c54c9f827a7e023058341f8008c80b482e1294c3c3074b20f99ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BQZBEDU%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO%2FLvbbzdF2ANiy9xMtY4ULoGpKradUZv3JE2PTwIkqAIhANa8IqNB1x6KVtBpOcKuHIgtUfoxlf1xdzCo6s%2FQdkPoKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyz4lTXSXMqthgwfWoq3AO7nq%2FIh4Z8A68mGsJB1EHqjj1pOIp%2BGe40R6wI68%2FP%2FPT7WVoiHMFbb6FrT2JBfkjqhBHEi4E1lwnnLl%2FK8e41S7RSVNCKj4dqVLbN7da6I2jjRDGQO%2BuzFJoLZZ177WrcSXDNayNqdmFX2njymEI4a%2B%2FBkNAjwhClOnbcjTeFnGrlcQ53kryPfSer5v2V%2BhCAf1T%2FEzS7Iq3os1G2qK3GU%2BoHdMNFFUi%2BLDhAUkzoZCcJe3hPIbVJGFxn%2BkRdVpTg%2Fj9KxZhsD5vwXSRAtMt%2FB50617vjQ97%2FBieOl%2F0YOLg2ZD9%2BcVl04%2F4jlZsNjyt4rXmYNXzYANifjT0ywU1YKXEd%2BiRyfmiL%2Bl60b7fZav%2FI2rrXR8ln5tXWKOtyBCL1gm%2Bf03kvE%2BYBK6B0iTgdasOgQwAYtgbqZAAbPrf4nCXTl9EoWEsK3%2F%2BGCiQL8cjMbPvgTQKjBkmPq82Q0O6PbOnK7tr3eCBjEZNQAA6%2F9CUffWFr6ddfduCdjcXvKhAMxjLbNC64oLgCV1KXyg8qReeiHX%2Fm52uAgGN%2BsYJvEXzc4qk1nsL3F4XPPVM1Uq3AaU4XGiSTPXolmsob%2FhMK3XOoHenc4vWtPYXT3KhXTSE7roG0eZGtLf0ZQjC%2FkN7JBjqkAQ%2Bc9CBhsNtiVVXwJ%2FAZJsfkR9u6FNWCo%2BBranUwpChoyJvDhi0LyesO0JYNLhI0bzrHQ6iu3%2BePpdQhfyDyUZhLd4FymI6qGrbyviJ5J3xWy%2FFm%2BGlU7Af5JWoTGUYVH16FE3UP%2FwSK071rk8aBG6%2FbjE5IpfYo1lYnNv8LHT3BHy6MWMGk%2BIElb7VGkIG4dO%2FUyRCuRkOpnTfMf5JGJCzkxVoC&X-Amz-Signature=2c4e1e80483adc4d7656b96e1c53c97bd0c84112842326d3daf4476193546f81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









