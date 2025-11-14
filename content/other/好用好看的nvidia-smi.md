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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RUR2E6F%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk%2FbZKcuMe9r33PY9L8%2FOwYmhv9PCdatMuwdPJe%2BL4cgIgSBHzSiNEJqvRxOcCM4Z%2BH7qo0o33LcBmEuuwsXXYLboq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNQF%2BMbBPRJJ%2B4epByrcAznP8lrKw3jS07syyq2vIsHHebi5MsD10fn%2Fu0S%2BPzymUjehapj2s5fXZSPuejiorkka6fMmcdB8pKozDadnUCFM60R%2FG1MjOu%2B438LLuuIcvjMat0UKXMgm%2BwGOz7QyuD%2FO%2FdxL9vABsVY6%2FcNn9YT4LO0SxpG2ufml4n2we7iqCzSH1oLoWI6vFWDIzJj4HU%2BIzlPJpi3adnlLH%2F8W4XxqTjZpD0L3BawuLoZtI%2FkdXVu20wvzcmLQtvsEsk2ZpAKTlgnPG3qOh7aiRvA8xJsxYUIM8bR5FcFA8IxZw%2F2aPHDg9Xx5dMQB%2FJrFVIsDgJbkQJvmBXcUMWTD%2BW9Ey26jMoYV6k3XmD9MbZ9aLkQQsvQ3V9oNmTBWErhAnxODZpNhsSyBAYRUL6TOtj7ttcvElv%2F7pNEIjVG1N5V%2FHGuJrIip7P2twUHzFZZlvTkaticNZ88MB%2BCYPIteYt3BqPDxW5Dm5hzkVIsPA6E3PJBq%2F1xpQwjlN9MPWrdZkQq6DABiEjV195Wh9RWQRVijecMl13NzJQ%2BlGl0FCaD0ZUaZAxy4nL9aRbUY02h3UC7qrw6Q7Ef%2BeVPSzDR1JTm8wUxM76rqRuBYRG49lxr72b8YYluPS%2Bdaf%2F7UYGhQMMaJ2sgGOqUBkeOfA0fwOB9MG9Qt%2FUZS8yM75baERwwvL2Iu5j499WrUh0d6gf8IHsgplBiZx%2FJjMEU53JidsIrUbOKy81Qj4pJ2kHcucV4qpw02zyiKfvoYUhrhGKomXfkA3A273ouoBKb53wFb%2BuwZT8eFghy2Z28wOzprJtpvEylisn0v4VhJiJxFEaY2O04I2F2c%2FPYHTat5nChZyT2jMHn2YXIfKy1QUKgL&X-Amz-Signature=edd5a543ccddcc754ab5777e2513e86419ecf5de542d794dcb2fadd46b2ac228&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RUR2E6F%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk%2FbZKcuMe9r33PY9L8%2FOwYmhv9PCdatMuwdPJe%2BL4cgIgSBHzSiNEJqvRxOcCM4Z%2BH7qo0o33LcBmEuuwsXXYLboq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDNQF%2BMbBPRJJ%2B4epByrcAznP8lrKw3jS07syyq2vIsHHebi5MsD10fn%2Fu0S%2BPzymUjehapj2s5fXZSPuejiorkka6fMmcdB8pKozDadnUCFM60R%2FG1MjOu%2B438LLuuIcvjMat0UKXMgm%2BwGOz7QyuD%2FO%2FdxL9vABsVY6%2FcNn9YT4LO0SxpG2ufml4n2we7iqCzSH1oLoWI6vFWDIzJj4HU%2BIzlPJpi3adnlLH%2F8W4XxqTjZpD0L3BawuLoZtI%2FkdXVu20wvzcmLQtvsEsk2ZpAKTlgnPG3qOh7aiRvA8xJsxYUIM8bR5FcFA8IxZw%2F2aPHDg9Xx5dMQB%2FJrFVIsDgJbkQJvmBXcUMWTD%2BW9Ey26jMoYV6k3XmD9MbZ9aLkQQsvQ3V9oNmTBWErhAnxODZpNhsSyBAYRUL6TOtj7ttcvElv%2F7pNEIjVG1N5V%2FHGuJrIip7P2twUHzFZZlvTkaticNZ88MB%2BCYPIteYt3BqPDxW5Dm5hzkVIsPA6E3PJBq%2F1xpQwjlN9MPWrdZkQq6DABiEjV195Wh9RWQRVijecMl13NzJQ%2BlGl0FCaD0ZUaZAxy4nL9aRbUY02h3UC7qrw6Q7Ef%2BeVPSzDR1JTm8wUxM76rqRuBYRG49lxr72b8YYluPS%2Bdaf%2F7UYGhQMMaJ2sgGOqUBkeOfA0fwOB9MG9Qt%2FUZS8yM75baERwwvL2Iu5j499WrUh0d6gf8IHsgplBiZx%2FJjMEU53JidsIrUbOKy81Qj4pJ2kHcucV4qpw02zyiKfvoYUhrhGKomXfkA3A273ouoBKb53wFb%2BuwZT8eFghy2Z28wOzprJtpvEylisn0v4VhJiJxFEaY2O04I2F2c%2FPYHTat5nChZyT2jMHn2YXIfKy1QUKgL&X-Amz-Signature=29e4e0f67e862b13811b110ce21da73a98427093461648541d660f640b195541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









