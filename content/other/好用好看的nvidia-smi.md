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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M76F6D4%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQC5PInGbQE295wJtJnuf%2BMukmnRvx5kn6aVinaLEwkK%2FQIgEKE38BCn4tohPt7KuyKO5CWqz3LRq0BW6KpXiGZsKNEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBgPKt5QaVnbCZtqSrcA71UwgE6GDbTQjgKjV2t%2FzIQSigLppD%2FmEJrPU50K9Qm6Dl0%2B240kTmqIrFIdfr7N48KVckxMfgw5rVvLb3tLiUbFPbyUUlQp4%2Bzo9NOyqu90XqiwSKhszSt4sjNeqMmvsOdavZZ5dKaH3KgriwO3c74LQHqdPI9I4IWBJWS%2FG9ltOuij%2FlzIDaryUoKvFgxCEYZUD84gLfwXHHAoDrlWhiLdpDuSJN5MvccSAQJHzZO4yPRWRYmqZqAWA%2FxfUXG6NI9wP0LxV7ifnVLXHxCmUhMxOVz8K48RZrNeZA8%2B6w6xGcv0xZ4RNYJ2I47qVSBYkP0%2FFXYSo0ro7JwmHj14Z4NRf%2FRP6nJ0l%2BXdXz6e1E1LER0y%2BQqLQO5T7iuPFGUnO3Gf6aKdFrOT9VTHLVdvBTfZPM9%2FEmkUIyIMkC27sf2zNaOVbkpkenIlHCv7LQdxiPJJvuIzHm17Fa%2BFdwbqN%2FwlSgI6yULHpJT4WER891ILbkxC6OKGsbDwFow7q7OOi3XhWVhW4L5jcSMQQ8snbxMAskUT3%2BdOYf07OslNO3TGdkcAEKPFBvmQTOwx%2BQUiaG8V1EuPCBDIZYHdq%2BfygmA3vwfgmSi19%2BhATmlwiLWj2OqElEMqk5eGeI8MJfOrckGOqUBEhlxAeHdnk261yVG%2FxmsE4n3O%2FiwsIwjOLKjuc8oue5mtUBUtXYsQQCse%2BFWWbriE%2FgGXemZmGZoOQ5UZZIMULs16r0rei0IsQXCH3uBA0CDNjJjEU6rt%2BLvhT0vzNOFmLU3MowGZG%2FVuWURCZS%2BDTgTh90BS2uuHaEjf4a1HY9pPzcmEiu9k1upIPxCj303KlNO0JzRMwr7H0OP3a%2BLVgfX8k4M&X-Amz-Signature=303bebaa8becf323edf9d1e8521e579071a1fe64b7b592d9066cc0ed8d05065f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M76F6D4%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQC5PInGbQE295wJtJnuf%2BMukmnRvx5kn6aVinaLEwkK%2FQIgEKE38BCn4tohPt7KuyKO5CWqz3LRq0BW6KpXiGZsKNEqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBgPKt5QaVnbCZtqSrcA71UwgE6GDbTQjgKjV2t%2FzIQSigLppD%2FmEJrPU50K9Qm6Dl0%2B240kTmqIrFIdfr7N48KVckxMfgw5rVvLb3tLiUbFPbyUUlQp4%2Bzo9NOyqu90XqiwSKhszSt4sjNeqMmvsOdavZZ5dKaH3KgriwO3c74LQHqdPI9I4IWBJWS%2FG9ltOuij%2FlzIDaryUoKvFgxCEYZUD84gLfwXHHAoDrlWhiLdpDuSJN5MvccSAQJHzZO4yPRWRYmqZqAWA%2FxfUXG6NI9wP0LxV7ifnVLXHxCmUhMxOVz8K48RZrNeZA8%2B6w6xGcv0xZ4RNYJ2I47qVSBYkP0%2FFXYSo0ro7JwmHj14Z4NRf%2FRP6nJ0l%2BXdXz6e1E1LER0y%2BQqLQO5T7iuPFGUnO3Gf6aKdFrOT9VTHLVdvBTfZPM9%2FEmkUIyIMkC27sf2zNaOVbkpkenIlHCv7LQdxiPJJvuIzHm17Fa%2BFdwbqN%2FwlSgI6yULHpJT4WER891ILbkxC6OKGsbDwFow7q7OOi3XhWVhW4L5jcSMQQ8snbxMAskUT3%2BdOYf07OslNO3TGdkcAEKPFBvmQTOwx%2BQUiaG8V1EuPCBDIZYHdq%2BfygmA3vwfgmSi19%2BhATmlwiLWj2OqElEMqk5eGeI8MJfOrckGOqUBEhlxAeHdnk261yVG%2FxmsE4n3O%2FiwsIwjOLKjuc8oue5mtUBUtXYsQQCse%2BFWWbriE%2FgGXemZmGZoOQ5UZZIMULs16r0rei0IsQXCH3uBA0CDNjJjEU6rt%2BLvhT0vzNOFmLU3MowGZG%2FVuWURCZS%2BDTgTh90BS2uuHaEjf4a1HY9pPzcmEiu9k1upIPxCj303KlNO0JzRMwr7H0OP3a%2BLVgfX8k4M&X-Amz-Signature=c782e7e3a3e2a4e6a104115fa23632bfc5451c32cab3cc109014cb32b4e3417b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









