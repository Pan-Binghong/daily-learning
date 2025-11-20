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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636WUCYZZ%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC1sNCQehaoJxXByd8DgHExtgjowsQqFqUuwTiNOpJkHwIgRMYqjfdC788ceFYOOKg43MPP5e1udA5PvaaylYThJDkqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7Bc0kHUJx4sQy0kCrcAwrgvKYCS%2FCcz8fb4eanY2fuhTnR13HfyPxP0Kbn%2FcE1uVOurLOUb7l6jJNlmeF%2BRXzHsCQG3r1gg5vNqR8v%2FjxOVCf3FUGQ2x%2BT3tyqdYW3Q9Vjlh%2Bg9RrnrVgza84uQIAGlOFfAZwo0MkBWkdjsovreSE77cUnI1QkCtjUxxNVLigw3ychUVu9Kw%2BzziNEyB1b7dAx4XFNFTjr3ATEm57cuWAUxYerJ4O4I33mSLD5QAKOI4R1U7SXJZKjaiSN%2BzOyimaHCVvZUV0qEeBzKmZ7H2z8WtspkwWSg25VQTktCRFTsGj95kv1Hw%2FOCTjjiBF2thHDuzVl3qbKD1OXqmy0Mqua1AJOo7KwN5t4t%2FXqm%2FoWaPCJ5%2FTv2SIvbw6%2BN7XO%2BB%2Bq2fxstXhnaEC9gsrHLZ766NuyO6vaLRLS%2Fp42V4IFAS8XMiwFNSObguPMBYXizlgpsZMRK0Mhcvg4TTvtHUrJMHDrBKa2qiyRaa0sZB49pU%2FAG%2FVHqMMoHhQSNRdnCOBsN29Dmus%2F1LyxBYRyamf%2FPRVvFPDCgvwY2%2Fqf7Ix9cvS4pN33TJLueF8suxBOefiM4Y0Pe%2FkN5X7SyAbyeMDtg6W73QyG8jL1mAUDk54mmezviEl1otuoMJbp%2BcgGOqUBBP6KuMd%2FkOL1gH%2BGIxCnAoBfT69TQU7CTZavvsz0Y4QQi2JDPyOXVwqxhPN%2Fq4Q6YX5MvOb%2FakXlGIjHo6mSK5BpeeMjLzXIZo%2BA%2F4CG0xlMRRGYZ6S%2BrJaZxO%2FTonF22X2VBExMFuvWI0h64eFaA9eRPiMyn5%2FgX%2BCL%2BRiPIlXXf0dzNaM5U5ckawquZVc5UQ1Gf%2BGthBggtpFmyLa21d5uDQvr&X-Amz-Signature=93f1685a2d8865b0e2c31682f27ad60de661c85156c8063edc39a219e4ed2a87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636WUCYZZ%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC1sNCQehaoJxXByd8DgHExtgjowsQqFqUuwTiNOpJkHwIgRMYqjfdC788ceFYOOKg43MPP5e1udA5PvaaylYThJDkqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7Bc0kHUJx4sQy0kCrcAwrgvKYCS%2FCcz8fb4eanY2fuhTnR13HfyPxP0Kbn%2FcE1uVOurLOUb7l6jJNlmeF%2BRXzHsCQG3r1gg5vNqR8v%2FjxOVCf3FUGQ2x%2BT3tyqdYW3Q9Vjlh%2Bg9RrnrVgza84uQIAGlOFfAZwo0MkBWkdjsovreSE77cUnI1QkCtjUxxNVLigw3ychUVu9Kw%2BzziNEyB1b7dAx4XFNFTjr3ATEm57cuWAUxYerJ4O4I33mSLD5QAKOI4R1U7SXJZKjaiSN%2BzOyimaHCVvZUV0qEeBzKmZ7H2z8WtspkwWSg25VQTktCRFTsGj95kv1Hw%2FOCTjjiBF2thHDuzVl3qbKD1OXqmy0Mqua1AJOo7KwN5t4t%2FXqm%2FoWaPCJ5%2FTv2SIvbw6%2BN7XO%2BB%2Bq2fxstXhnaEC9gsrHLZ766NuyO6vaLRLS%2Fp42V4IFAS8XMiwFNSObguPMBYXizlgpsZMRK0Mhcvg4TTvtHUrJMHDrBKa2qiyRaa0sZB49pU%2FAG%2FVHqMMoHhQSNRdnCOBsN29Dmus%2F1LyxBYRyamf%2FPRVvFPDCgvwY2%2Fqf7Ix9cvS4pN33TJLueF8suxBOefiM4Y0Pe%2FkN5X7SyAbyeMDtg6W73QyG8jL1mAUDk54mmezviEl1otuoMJbp%2BcgGOqUBBP6KuMd%2FkOL1gH%2BGIxCnAoBfT69TQU7CTZavvsz0Y4QQi2JDPyOXVwqxhPN%2Fq4Q6YX5MvOb%2FakXlGIjHo6mSK5BpeeMjLzXIZo%2BA%2F4CG0xlMRRGYZ6S%2BrJaZxO%2FTonF22X2VBExMFuvWI0h64eFaA9eRPiMyn5%2FgX%2BCL%2BRiPIlXXf0dzNaM5U5ckawquZVc5UQ1Gf%2BGthBggtpFmyLa21d5uDQvr&X-Amz-Signature=aa5de5bba06eedbee0b3f0270660fc89a0555082ea0eccb98c8cdd0d387cc616&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









