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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGXG4FOE%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaApZ9RJS2S1QoRd673vokNpD8pY%2Fhg1M2ennFngKhSgIgTnoDxcEugzdFR61mRZI1AI51jdaUOyg9sV9H0Cwu1lgq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDD95w1XphXehyke5YircA%2FsUXhb%2B3g1S8A7JkHXNjcevjMtKnW1ww7jE6VgvUzXjmNfxnAEpnDYRaFkErdEPK6ITiMoTAG8IfoxkTwNW8asWNbOyqW2MoLnIlnc0n2VyGJjBA0ggWsVY1mbbW7wVOp7261N0cPsBwtfpsO5FaBfyfABDrWHJfQBQPPAw6LMlMq8eukm1PzRKUx%2FFoRThuCMoLczH%2FMwHpLi%2B0LVKRkg9W9yQJg3wzW5TSo8%2FYxk9JFbj5%2FPit0AroDvmA0s8%2BMuTmWQJLQ%2BacFABO0DgFR74EquQnxsl8i84BF0F8G%2BQ%2BoEHvQ997%2FI6dexxux8C2qQDt84ELxzsZQ03%2B%2FkDIurDuhVSICo3xfljDytJiOMx224zELYihEQgU%2F1sq0kjfpzcSSioVSxXSVesHYEu1tMuLeu54NJ%2Bap9gXLm3YaRP21vBybpdUKmI8byue0ZP2e1h5sIZJbeuOexa8UFjjWLaY2EIu%2F4%2FigPIrC4OGIJMMWFvBnrk3kRn%2FlpPOAIeaeGoDJdsyIuR2FSg3%2B%2BknFDgPMqJTNZCdWMvrcmNAKC8YjzjpYwY6IpASrOWNLgHPLDSkCCOtbWzbjIvuVDOnFQkZy8PtaozO%2B5HNYPuLahRlCw02RxgyFUbQlVbMJSCscsGOqUB78yPJ9zGFxcRLy5lZDOqN7fNuFgggFHNRB3kSoVZs7DXEmyJ2vYIaaUubgRL5%2FRylnA%2F3dEHay2Sr7iCtfKcf1rTW82JEVBtQvo86LAYb2cu1yt3PENli0TEUwJrzk351p%2FVlmFQiVDa2TUViG%2Ff6Xc55Rq3v63eINEMtdx%2BgzUYTXmKMtLxPv0rpDOUtGXWFatpM5nD%2FCaGg%2B8VsNbk97LGhaTq&X-Amz-Signature=3722ccf0ca0ce66de6d0c40ad72d5247636fad8f937be89dcfc7453c5785e703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGXG4FOE%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaApZ9RJS2S1QoRd673vokNpD8pY%2Fhg1M2ennFngKhSgIgTnoDxcEugzdFR61mRZI1AI51jdaUOyg9sV9H0Cwu1lgq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDD95w1XphXehyke5YircA%2FsUXhb%2B3g1S8A7JkHXNjcevjMtKnW1ww7jE6VgvUzXjmNfxnAEpnDYRaFkErdEPK6ITiMoTAG8IfoxkTwNW8asWNbOyqW2MoLnIlnc0n2VyGJjBA0ggWsVY1mbbW7wVOp7261N0cPsBwtfpsO5FaBfyfABDrWHJfQBQPPAw6LMlMq8eukm1PzRKUx%2FFoRThuCMoLczH%2FMwHpLi%2B0LVKRkg9W9yQJg3wzW5TSo8%2FYxk9JFbj5%2FPit0AroDvmA0s8%2BMuTmWQJLQ%2BacFABO0DgFR74EquQnxsl8i84BF0F8G%2BQ%2BoEHvQ997%2FI6dexxux8C2qQDt84ELxzsZQ03%2B%2FkDIurDuhVSICo3xfljDytJiOMx224zELYihEQgU%2F1sq0kjfpzcSSioVSxXSVesHYEu1tMuLeu54NJ%2Bap9gXLm3YaRP21vBybpdUKmI8byue0ZP2e1h5sIZJbeuOexa8UFjjWLaY2EIu%2F4%2FigPIrC4OGIJMMWFvBnrk3kRn%2FlpPOAIeaeGoDJdsyIuR2FSg3%2B%2BknFDgPMqJTNZCdWMvrcmNAKC8YjzjpYwY6IpASrOWNLgHPLDSkCCOtbWzbjIvuVDOnFQkZy8PtaozO%2B5HNYPuLahRlCw02RxgyFUbQlVbMJSCscsGOqUB78yPJ9zGFxcRLy5lZDOqN7fNuFgggFHNRB3kSoVZs7DXEmyJ2vYIaaUubgRL5%2FRylnA%2F3dEHay2Sr7iCtfKcf1rTW82JEVBtQvo86LAYb2cu1yt3PENli0TEUwJrzk351p%2FVlmFQiVDa2TUViG%2Ff6Xc55Rq3v63eINEMtdx%2BgzUYTXmKMtLxPv0rpDOUtGXWFatpM5nD%2FCaGg%2B8VsNbk97LGhaTq&X-Amz-Signature=9dd25893afd3f62f514dd799994e5ad2dcef84cf27cf980f1f9e982cf9e7f081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









