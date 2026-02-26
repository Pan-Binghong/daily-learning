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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJX6OF4B%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDkUM48WZGjW88sAyJWnoHoJ3giatdrElWqhlRdaj%2F2lQIgXFUrbes47J1nmf91zVvESM6SZplH0Q3TL83tQrN6%2B54q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJ40BGaQ9KW2NpjmZircA%2Fx0oboG9uj1EWwsX4OgHMh2hE8E5e%2FZhlEe86E44TiweFA8POaG5pqVUR5%2FePx8E4B4KaMC4HxwKTWd9bm0tUrxJME1kuknllqmX%2BN8jetcdVm7qBgpXK4%2F1e3YlG5qpcAIjUROVGskaCluDPTo8pTU4pUMm9nS4rOttnUhOWSDhtc52UjDspNfrFo68LXCfCxn%2B02Ti%2Be7U0xHTeZ3bafVydD2MvGZpIFpUDjbPRAUC5KPXCEb4R418iVFFjq%2F2pweHxvG%2FHCp%2BD6cHqaqe%2BGGb8dZEfncYjNeLbgPpkfOBsWCh3tPWbsQc%2BIBfhFgSCUGXf4Iivq0y%2BM6g6dHkBw0fnHSifqQczkUbb5D4Jn5AvLPbyLgIHufr8UklXi9KrlmtxlOCzOKBw4XvT36mBao7PYvu4VdWAjXEtJ91O%2FqMSWiKxtR3H58x%2BZiIEA3YoLaSLogP8vfgeJervqNWqaMZxPED%2BPKJgMcOIL5k%2FETUHMLY8TKOPIw08z4nDXGeRtXC5eo69noFa6S2tPs6KHBrNEo6dkAlINHofu3jgD2Uc1VRzo0wKnH%2FbjGDtL5SAskxcr5vvV1z3%2FZT1n2GXBvGgNe2gdZlykyIKN%2F7DqLSTsnj%2Fv2J%2F8QDbDwMIH1%2FswGOqUB6vY%2BY5WTqLa2dL%2BoaEdcIO8MLNkzKDjVYa6RHBh%2BXhzo%2BIeYAthLc%2B%2FonkRdtQ1w3Om%2FKUvBpDPUFvZwSdCHcrGFWTALDqBT9bHCTqrLUQnU%2BdOUbpb55HDqrkSabGnJJqmUUoX2DNPAoYCHPHFKIVZUio6AFZMwO1AU35GpDA1%2FXBY9d8kvLrUoQQ2tDxnyB3EMOeQZxeOh0PpJ0VAXvYnlhJi5&X-Amz-Signature=4e288fa5e687f0441d5dd0badf348bc25b7c6b906089a4730b5d2f53b95e3cd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJX6OF4B%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDkUM48WZGjW88sAyJWnoHoJ3giatdrElWqhlRdaj%2F2lQIgXFUrbes47J1nmf91zVvESM6SZplH0Q3TL83tQrN6%2B54q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJ40BGaQ9KW2NpjmZircA%2Fx0oboG9uj1EWwsX4OgHMh2hE8E5e%2FZhlEe86E44TiweFA8POaG5pqVUR5%2FePx8E4B4KaMC4HxwKTWd9bm0tUrxJME1kuknllqmX%2BN8jetcdVm7qBgpXK4%2F1e3YlG5qpcAIjUROVGskaCluDPTo8pTU4pUMm9nS4rOttnUhOWSDhtc52UjDspNfrFo68LXCfCxn%2B02Ti%2Be7U0xHTeZ3bafVydD2MvGZpIFpUDjbPRAUC5KPXCEb4R418iVFFjq%2F2pweHxvG%2FHCp%2BD6cHqaqe%2BGGb8dZEfncYjNeLbgPpkfOBsWCh3tPWbsQc%2BIBfhFgSCUGXf4Iivq0y%2BM6g6dHkBw0fnHSifqQczkUbb5D4Jn5AvLPbyLgIHufr8UklXi9KrlmtxlOCzOKBw4XvT36mBao7PYvu4VdWAjXEtJ91O%2FqMSWiKxtR3H58x%2BZiIEA3YoLaSLogP8vfgeJervqNWqaMZxPED%2BPKJgMcOIL5k%2FETUHMLY8TKOPIw08z4nDXGeRtXC5eo69noFa6S2tPs6KHBrNEo6dkAlINHofu3jgD2Uc1VRzo0wKnH%2FbjGDtL5SAskxcr5vvV1z3%2FZT1n2GXBvGgNe2gdZlykyIKN%2F7DqLSTsnj%2Fv2J%2F8QDbDwMIH1%2FswGOqUB6vY%2BY5WTqLa2dL%2BoaEdcIO8MLNkzKDjVYa6RHBh%2BXhzo%2BIeYAthLc%2B%2FonkRdtQ1w3Om%2FKUvBpDPUFvZwSdCHcrGFWTALDqBT9bHCTqrLUQnU%2BdOUbpb55HDqrkSabGnJJqmUUoX2DNPAoYCHPHFKIVZUio6AFZMwO1AU35GpDA1%2FXBY9d8kvLrUoQQ2tDxnyB3EMOeQZxeOh0PpJ0VAXvYnlhJi5&X-Amz-Signature=8ed06aef99c671ca8eba536c9c281fc1eb52002bbf6447f94e0748db55b2c1f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









