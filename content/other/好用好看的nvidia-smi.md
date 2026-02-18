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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCNHYR4P%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICiB5f0R7%2Fw9r1ROU8zPPEIBtKfg5x3ACYtw8WwFZe1hAiBcO6y8WW%2FNnGvE6YDlFAoYmoAsNJpB59esbYwQk49jJir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMMHMB0i38%2FyyjeeWeKtwD%2F98wdDyI9U8FKA2%2BmHmoEBQGKpbYFGl5yzZlysuyVBtV2JiZwvzAxKMo3W%2FfxvqvzDwvF6QgCintF8QHPMGWxUv8T7uwJMU21E7Iaj5yCd9ukS%2BXP83WD%2B0nhTzBwlNUjLpwJ6qnNtmo1%2FgjxfcVTkKzvwshzx%2Bs6Gmvdvp15iXAGoJ3Y5F3aBlJC%2BrgbVavVuwW9siLv741OMv5d4JC9hP0IZqn0WFTo2OnwyHo9lPRVVEWbeDZQEYb4H9iA%2B%2F7IBoogqi%2BHqj5pwZhTPbOYRT0sAGR9bz10Pd6Pvk2oVtO%2BBabyEdEu858YMNdURIsKvooGPJDHjyKnEta1dO59C%2BOiiMJYw2SeZ6uRhZNcb2%2F7jKii0o%2F0PUYZtwSQbFhv5g%2BbDzcn1CgwprgzstcLvCrDTLHfL3dvunSN8UqImLBuJhN1J7oypRPhkmH6XmD5JxChpTWPFGO%2FgzfpvSyOcFKNFT0WWajtMIDSQfmJd10FaT3mrPtCQPoMBHkkNN%2B6pjthu5ub6rIAVYAP13Ibf9OCA0pfqT8HqEyfYp8vyi0%2FNsDIGqNgmVDwUbcBwhllC3ujMCR9YImHkTYA%2BCCpRy5xOfuh%2FEjoAciYsSCsZF3dnxFX2keEzQnVxww%2Fp7UzAY6pgFQs%2F5Q9JYgODh%2FRf1LBNIt5Sr4pwEMA6AGTQQgWEv40WxBbxoWeY9ePJjyvD9%2FF2hAfrOrk7wHTQJ%2FpomQhQ3dhnw7qhmALBHEBWUZNhWwsqusLATswysVIC3VLhDrMMFgcpxGUemzQ5DaQhAqNNNFwhi%2FWgB0WIdYGmg7xGBzzjRaBPqNd51NLlNMuOwoFyMHAMSm7JIRnACpTFTTrnMDlptBgBW7&X-Amz-Signature=c2a0bbe4b5ab7deda20eff4595a0796c0e2bce7a7bda5a1ca085a8ca2371eb16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCNHYR4P%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICiB5f0R7%2Fw9r1ROU8zPPEIBtKfg5x3ACYtw8WwFZe1hAiBcO6y8WW%2FNnGvE6YDlFAoYmoAsNJpB59esbYwQk49jJir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMMHMB0i38%2FyyjeeWeKtwD%2F98wdDyI9U8FKA2%2BmHmoEBQGKpbYFGl5yzZlysuyVBtV2JiZwvzAxKMo3W%2FfxvqvzDwvF6QgCintF8QHPMGWxUv8T7uwJMU21E7Iaj5yCd9ukS%2BXP83WD%2B0nhTzBwlNUjLpwJ6qnNtmo1%2FgjxfcVTkKzvwshzx%2Bs6Gmvdvp15iXAGoJ3Y5F3aBlJC%2BrgbVavVuwW9siLv741OMv5d4JC9hP0IZqn0WFTo2OnwyHo9lPRVVEWbeDZQEYb4H9iA%2B%2F7IBoogqi%2BHqj5pwZhTPbOYRT0sAGR9bz10Pd6Pvk2oVtO%2BBabyEdEu858YMNdURIsKvooGPJDHjyKnEta1dO59C%2BOiiMJYw2SeZ6uRhZNcb2%2F7jKii0o%2F0PUYZtwSQbFhv5g%2BbDzcn1CgwprgzstcLvCrDTLHfL3dvunSN8UqImLBuJhN1J7oypRPhkmH6XmD5JxChpTWPFGO%2FgzfpvSyOcFKNFT0WWajtMIDSQfmJd10FaT3mrPtCQPoMBHkkNN%2B6pjthu5ub6rIAVYAP13Ibf9OCA0pfqT8HqEyfYp8vyi0%2FNsDIGqNgmVDwUbcBwhllC3ujMCR9YImHkTYA%2BCCpRy5xOfuh%2FEjoAciYsSCsZF3dnxFX2keEzQnVxww%2Fp7UzAY6pgFQs%2F5Q9JYgODh%2FRf1LBNIt5Sr4pwEMA6AGTQQgWEv40WxBbxoWeY9ePJjyvD9%2FF2hAfrOrk7wHTQJ%2FpomQhQ3dhnw7qhmALBHEBWUZNhWwsqusLATswysVIC3VLhDrMMFgcpxGUemzQ5DaQhAqNNNFwhi%2FWgB0WIdYGmg7xGBzzjRaBPqNd51NLlNMuOwoFyMHAMSm7JIRnACpTFTTrnMDlptBgBW7&X-Amz-Signature=e842646d0bbd57829241fbb31ad231be046ca324e4857bf1d0a560f24e3bf533&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









