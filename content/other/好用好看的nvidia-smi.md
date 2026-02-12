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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVS7BYJQ%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCICVay%2BNQ9KKbb3%2B940nhuW%2BvJephVLK7mKMbGdb3%2BhUaAiBz9lVXfo%2BnmqepUJ8IKl39VNcSN%2F%2Ffy93fMl0ZOkaktCqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF7laYrcdXvihQV%2FvKtwDGY3VXiJxFyS%2BPUCoBjKIEULwHBgrclJ54hPtKRoEEcF1TLlvvVyuyuxd%2FFx6Mhd6AMHzqgg3icKJTW9BvV08FBI77wp42ou%2Bp6lkSSp4XpxGN4gH%2BYQ6id%2Fhf%2BYKYjQsB8ueMcBMFVSP4Q6%2B3nYw7oBW8HcUvtmx8ZX3IF7uXfOF2K3qQZ7QzuZUocoVa%2F317WgsICPaKdqizYcuTIZU0hQ7dYUdnQAkW9VbJp9yKUieSL3FwYEogkvFlRuiyHxlo4VIGt9dIIPwoibkBpLgtKKj09fcjNVmgBI3%2F4jyW0i2qLEApHdquqhN%2FC3SNXkzbKg15UD1VwqkrBg1Hd2imFbR0BtHOitPR3kmBu2BmwwMNXIJZ8TxXwFBWV7H9iaSCxyayc2rvYZYPbaSylLmKKYpt3rBfrx4S1wh77ANLbYpwt35K2ePfUdeUK3Oq71Bi6oXPYAxjBu4MEjJEuCeY%2FWp4whblK3WgfyHQzZBh1pv7p%2B%2BnsUeOw4bYTudoQKC5efh1x9XzgTupoChSx9440cDjTE%2BraK7pHwuTWwb00k3lfqnGlvzZyO9u3D65RGfNTAn2gh2s0%2Fj1naOb03sWSRFGH0Tjmid%2F7yHADfXX9BQTh7zlNBohB4kGakw%2B5G1zAY6pgH8TKgnoqCpcYOxTBqDo4uz%2BPhkAiOfCTnMIG0%2Fr8AofcgEpJsd3LY%2F0entTEvPP4Ah0m4IG4tomh78s5Cf9afrUPVy0y9cCHquDvBjp3lFUwVPKjR22nW%2F%2Bh8HNxGJFsFHeo8UhBJDxUwVmoyyd%2BPtsFVxp94j%2Bw0NEacZWdvWOTTrUqt4z00XTeqGepKEG6AKfeszf1lt8oDJm4N%2ByilteE9Qe%2Fx5&X-Amz-Signature=01f27c73a9d6bd31a6a130ebf9405edc57925d324e7b295923df3770b6eb21d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVS7BYJQ%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCICVay%2BNQ9KKbb3%2B940nhuW%2BvJephVLK7mKMbGdb3%2BhUaAiBz9lVXfo%2BnmqepUJ8IKl39VNcSN%2F%2Ffy93fMl0ZOkaktCqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF7laYrcdXvihQV%2FvKtwDGY3VXiJxFyS%2BPUCoBjKIEULwHBgrclJ54hPtKRoEEcF1TLlvvVyuyuxd%2FFx6Mhd6AMHzqgg3icKJTW9BvV08FBI77wp42ou%2Bp6lkSSp4XpxGN4gH%2BYQ6id%2Fhf%2BYKYjQsB8ueMcBMFVSP4Q6%2B3nYw7oBW8HcUvtmx8ZX3IF7uXfOF2K3qQZ7QzuZUocoVa%2F317WgsICPaKdqizYcuTIZU0hQ7dYUdnQAkW9VbJp9yKUieSL3FwYEogkvFlRuiyHxlo4VIGt9dIIPwoibkBpLgtKKj09fcjNVmgBI3%2F4jyW0i2qLEApHdquqhN%2FC3SNXkzbKg15UD1VwqkrBg1Hd2imFbR0BtHOitPR3kmBu2BmwwMNXIJZ8TxXwFBWV7H9iaSCxyayc2rvYZYPbaSylLmKKYpt3rBfrx4S1wh77ANLbYpwt35K2ePfUdeUK3Oq71Bi6oXPYAxjBu4MEjJEuCeY%2FWp4whblK3WgfyHQzZBh1pv7p%2B%2BnsUeOw4bYTudoQKC5efh1x9XzgTupoChSx9440cDjTE%2BraK7pHwuTWwb00k3lfqnGlvzZyO9u3D65RGfNTAn2gh2s0%2Fj1naOb03sWSRFGH0Tjmid%2F7yHADfXX9BQTh7zlNBohB4kGakw%2B5G1zAY6pgH8TKgnoqCpcYOxTBqDo4uz%2BPhkAiOfCTnMIG0%2Fr8AofcgEpJsd3LY%2F0entTEvPP4Ah0m4IG4tomh78s5Cf9afrUPVy0y9cCHquDvBjp3lFUwVPKjR22nW%2F%2Bh8HNxGJFsFHeo8UhBJDxUwVmoyyd%2BPtsFVxp94j%2Bw0NEacZWdvWOTTrUqt4z00XTeqGepKEG6AKfeszf1lt8oDJm4N%2ByilteE9Qe%2Fx5&X-Amz-Signature=c38ebef200c42800d80e4c2ebeb8b57c595f197a71d8b334abc910de392bd37a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









