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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL5NNMJB%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDUBXGTOhngabdCDSy6i%2BmG1rU1cF2mCv1ruedATivnAiEA8f9lgy8QQ8G5d1AJpU84CMbzRAHvtqPwG5yeIw4uxToq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJFpapI0B%2BSNtXXcBircA1sXCLa7WfqlY6xYjjFeH%2B4fBHO8vJWBrTrUFTVehNQydFLnOAAqoiggwJ0X%2BcaIgblleOQA1ZMBYbjUTfjdEYYh7b5nvTllfu2QBfqf3A%2Bd%2Bg%2FnLfrbRYHNCotm1mrErvvGqjbe4hZvzfreVNB0HRU91N7hS0UfGQoVTFwcw1fO62H258W0c5pzG8q45KQA%2BUskSSBA%2FtnSka4yuXFxy%2BeTUQ%2FD7poLHqojd823CyP1BS54%2BOYk1gNQc7AljiE0L5bmFZhsMOYP228qwbUxoMtPhpIqbMKmDQRs9O9Xfemr%2Bdzkn7IYxooVo2tRo3%2BIRAY%2FJWSVEvf7RueMdIS4SrNQeIXldPNnKWGMaW1mDmiNRPNfpXz2MFRjGltN%2FJ4XTx1N9aUzYVwUb8q3UPs0hsJELDlZihj1UgOhfDcy0jQ7nAcbYgFoA3pKEzKqScDwFVqWpYL1%2FZJFThpygpaeu5QUfHgA5adgyD9YpZBd5BWB92C7rSkGBeR5tK9Y4vIwxWpCwWR0%2BVfH%2FfhFeOYiPTzvPfcR2adpQexZ9TTnaMrtcUTXDmvXLUFowG5k39PrHCRi%2F%2BWbaD%2F8neS4fq%2FHaWx3AMDu6gDy4l3%2BFX2YIk96J4QMdlIcQBzK%2BphvMLyvvc4GOqUBEDCvColIh6jv%2FQirINbdI6LiVL6FSNh6FF6ghKScE2k5vFJl2%2FKFnbKXCQFxWvsGRW1GJLJCD5Y1RTme43SAwsXzUFOHVkEqxx6k4yje2NmzsK7kpKMoEZ1s1kZDE6yRrhjUsBdpWrkiVz0bqmGRc2j1N2SMD2aXyDqoVOP3XO%2F%2BhRuBIuWY6baij0gYS2UKpiVRFp7kzHWurh0QfT0pe8dBQHsu&X-Amz-Signature=8708ca4dd8cdd2617498bff4ed6829885883f99ecff227b9194e74534ec81594&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UL5NNMJB%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDUBXGTOhngabdCDSy6i%2BmG1rU1cF2mCv1ruedATivnAiEA8f9lgy8QQ8G5d1AJpU84CMbzRAHvtqPwG5yeIw4uxToq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJFpapI0B%2BSNtXXcBircA1sXCLa7WfqlY6xYjjFeH%2B4fBHO8vJWBrTrUFTVehNQydFLnOAAqoiggwJ0X%2BcaIgblleOQA1ZMBYbjUTfjdEYYh7b5nvTllfu2QBfqf3A%2Bd%2Bg%2FnLfrbRYHNCotm1mrErvvGqjbe4hZvzfreVNB0HRU91N7hS0UfGQoVTFwcw1fO62H258W0c5pzG8q45KQA%2BUskSSBA%2FtnSka4yuXFxy%2BeTUQ%2FD7poLHqojd823CyP1BS54%2BOYk1gNQc7AljiE0L5bmFZhsMOYP228qwbUxoMtPhpIqbMKmDQRs9O9Xfemr%2Bdzkn7IYxooVo2tRo3%2BIRAY%2FJWSVEvf7RueMdIS4SrNQeIXldPNnKWGMaW1mDmiNRPNfpXz2MFRjGltN%2FJ4XTx1N9aUzYVwUb8q3UPs0hsJELDlZihj1UgOhfDcy0jQ7nAcbYgFoA3pKEzKqScDwFVqWpYL1%2FZJFThpygpaeu5QUfHgA5adgyD9YpZBd5BWB92C7rSkGBeR5tK9Y4vIwxWpCwWR0%2BVfH%2FfhFeOYiPTzvPfcR2adpQexZ9TTnaMrtcUTXDmvXLUFowG5k39PrHCRi%2F%2BWbaD%2F8neS4fq%2FHaWx3AMDu6gDy4l3%2BFX2YIk96J4QMdlIcQBzK%2BphvMLyvvc4GOqUBEDCvColIh6jv%2FQirINbdI6LiVL6FSNh6FF6ghKScE2k5vFJl2%2FKFnbKXCQFxWvsGRW1GJLJCD5Y1RTme43SAwsXzUFOHVkEqxx6k4yje2NmzsK7kpKMoEZ1s1kZDE6yRrhjUsBdpWrkiVz0bqmGRc2j1N2SMD2aXyDqoVOP3XO%2F%2BhRuBIuWY6baij0gYS2UKpiVRFp7kzHWurh0QfT0pe8dBQHsu&X-Amz-Signature=a356c9b1163bf176a735df6c04354d4145daf21a80ddeb20986b7e8e58174e15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









