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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONC64GA%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdgfqF7O%2BsogWX5GlRQ522AKeU27W1OTmBaG6jyF2keAIgYvSGbngjuAiO%2B399BVdhz1XNQYnaSABqKTZG2ihLJeIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDxfxFNliLn22LVoyrcA%2Fj5x9ozsp%2BEiN3pNlaU53PNZgiYou6AAvOdgATzokhoLrWfW%2FemRCtTktf%2BhL38A0FSqRAjQcmZIeKTHgR%2BmbdPFoqwQCtGRgKfr%2FOD%2BznusEXgehoZwVrZ8QhCmivxqLQob%2FLeW2eK6JpztKyoTmguKZbjyGbfEfe85z6Fy47szF3EPaGWGjduZotI32fXSjOLSS5aszCDAQ%2BMd3FvDOxatAoNZ4GpNZ84mvDiFsQzL%2BCeDyf40VJwX4PJBr5MWztdGKG4A7UbM0GAFTwgaI%2BVUu0I%2FSdUgqRDyqAFjNnYMbLwvzazcEPre0skHiGTCx2W5E%2BnewjgEBprC1UInOgfek4MZxGdF2DekZPoEWpvsoEmXL6NUqjGlp6iz1GXW9F8XQ1%2F9UVyQtzyAIG83vk7YmCij26iFs9meJyWqqiYSKfzy6u6yN4ZPS6hGHUZ%2BgrMeVkCAEHSl%2F73iXPMSh4r0CHoLYXlWLBgKAtFBVWB41mpMynAbsuIc9xaj3tyMeT8WFLSFW5zvljpsIQlzCMA6odiy8tPXgMiws6upm%2Bf9WKPEP7JGQAYFalME%2BwZnP2%2B%2BcEbfY%2FXqPzLv1Q6mcRMc120xEAgCTuJn6ZKOTtjXmnmVZ9JtB%2F%2FSAC8MKL90skGOqUBWqJLRpPaybMLU%2FjGxtaMHl%2FOCgQcikkWkfNETICzHqdicOnTJc2EZxSB5GGnzb85Fm5w2fnM%2BpifvH6yARqUV0K4qHq2aoyGTcoTNFg6u1dYGieXH7GWqO3UJiyvGORTGl2VzupHvicZZ5xMVR4KFbbPIA%2Bfxdoi5xtZe2vA%2FSbCCcUT7dtBhh756iHg2RqAv0NPp6g%2BexzNHfohxWgeMJKOu3bn&X-Amz-Signature=33437d4e448c14913d67dd87781656e8320d86464b261d58cc2bd9202ffdd8a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONC64GA%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdgfqF7O%2BsogWX5GlRQ522AKeU27W1OTmBaG6jyF2keAIgYvSGbngjuAiO%2B399BVdhz1XNQYnaSABqKTZG2ihLJeIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJDxfxFNliLn22LVoyrcA%2Fj5x9ozsp%2BEiN3pNlaU53PNZgiYou6AAvOdgATzokhoLrWfW%2FemRCtTktf%2BhL38A0FSqRAjQcmZIeKTHgR%2BmbdPFoqwQCtGRgKfr%2FOD%2BznusEXgehoZwVrZ8QhCmivxqLQob%2FLeW2eK6JpztKyoTmguKZbjyGbfEfe85z6Fy47szF3EPaGWGjduZotI32fXSjOLSS5aszCDAQ%2BMd3FvDOxatAoNZ4GpNZ84mvDiFsQzL%2BCeDyf40VJwX4PJBr5MWztdGKG4A7UbM0GAFTwgaI%2BVUu0I%2FSdUgqRDyqAFjNnYMbLwvzazcEPre0skHiGTCx2W5E%2BnewjgEBprC1UInOgfek4MZxGdF2DekZPoEWpvsoEmXL6NUqjGlp6iz1GXW9F8XQ1%2F9UVyQtzyAIG83vk7YmCij26iFs9meJyWqqiYSKfzy6u6yN4ZPS6hGHUZ%2BgrMeVkCAEHSl%2F73iXPMSh4r0CHoLYXlWLBgKAtFBVWB41mpMynAbsuIc9xaj3tyMeT8WFLSFW5zvljpsIQlzCMA6odiy8tPXgMiws6upm%2Bf9WKPEP7JGQAYFalME%2BwZnP2%2B%2BcEbfY%2FXqPzLv1Q6mcRMc120xEAgCTuJn6ZKOTtjXmnmVZ9JtB%2F%2FSAC8MKL90skGOqUBWqJLRpPaybMLU%2FjGxtaMHl%2FOCgQcikkWkfNETICzHqdicOnTJc2EZxSB5GGnzb85Fm5w2fnM%2BpifvH6yARqUV0K4qHq2aoyGTcoTNFg6u1dYGieXH7GWqO3UJiyvGORTGl2VzupHvicZZ5xMVR4KFbbPIA%2Bfxdoi5xtZe2vA%2FSbCCcUT7dtBhh756iHg2RqAv0NPp6g%2BexzNHfohxWgeMJKOu3bn&X-Amz-Signature=a425aa684bb0300ea41d1653ff33e0afd8f8a7aedc1191f56b2ecf86e132e49e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









