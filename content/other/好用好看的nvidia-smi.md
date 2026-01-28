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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCSTJGA%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6B%2FlxPQ3Yvp88%2FZE5ArQQx%2BdYaGO5WwrYtKZ4Gn5hAIgRM5J1Kf9cDV5KjVRd2EG9d8DMIta17jU94JuJLVTmMIq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDLYcvIJ5JN%2FR5tGsGSrcAyTP%2FuuhwXwvnOEYqxXC7iXH0LuqM4WllW53ksQ8e4Psq4nQscaPpY5l5N%2BIStk8tlFo0cc%2BT0Un%2BlmXR0gpFwxzPROk8xBVdAf773CAKFwVBFUlN1jjevQEq3NIbjlxY%2BJqiw4qei92FWxphc3a%2F0x3Zy1c9CQcL6dbaSfMkULbocPSNDQXMHJpzKRT2WIL4W8h7ymtP35WfcSW3W%2B1lYAZ4t8n6rigl058nvuO9%2Br9rxfpJYMvZSYeQd0Z99ymI6jwBVmKiMmHZykEvLXz0ino8%2FtjtbJjIkZ16C5McAERz45%2FIOs28o9nhx%2FEmtwIvFWjkuY%2BBxPxsL07tJ43mI9s%2FX1GyWF%2F9mYQqY6125VHS1rp6vph%2BcMMZN0SEe8nOYnXWUezV3uhUX%2FDIYK%2BbP4IIjvMAsyBrvMQzUE5CFXrnd%2F0Jk%2FvL36j4BV%2BAkqr2laheqNMzKt66rlnomkdY6DAlSy5MLAYL4uxuKovoJ8MoZzMWTZSo5ja0HpMnn4WAlHhJuoEMZHlJr%2BnJXUr9YZjWr6S4bjinQphxGNpTmNyJjU3ZT3gXTh4pbE6sY%2F22a%2FRdF%2FL8jKcxEjxQil4tlu0v9IIIfNH%2FTqxu62V7g0KFENH9PNM74p23P6oMNaW5csGOqUB%2BXH22l1kf0RHFhIC3uRuJ12Wm%2FJGLOt8W66pKVQRgCVu1AsJ86T%2FvySKdW%2FTfYjUuLxW%2FAhGYOhVFR1jfv6UCDhjbbbjuzLy3Aqjfy7wWAru9CtLCEfMmdA23kDldpkxgQRQRaApj3cuKmRAGeTX7oBqaHbOFGiF7DX7qYnvd38iZWUQbPCj5YbW5lMuqP8%2B9p6Ydvwx4v8zZBg2E0ujBmxyCowh&X-Amz-Signature=b77c52e2e572a87c65ac70537c9f8b8f9d0ca754742943d6b7d26f88731d906d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYCSTJGA%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj6B%2FlxPQ3Yvp88%2FZE5ArQQx%2BdYaGO5WwrYtKZ4Gn5hAIgRM5J1Kf9cDV5KjVRd2EG9d8DMIta17jU94JuJLVTmMIq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDLYcvIJ5JN%2FR5tGsGSrcAyTP%2FuuhwXwvnOEYqxXC7iXH0LuqM4WllW53ksQ8e4Psq4nQscaPpY5l5N%2BIStk8tlFo0cc%2BT0Un%2BlmXR0gpFwxzPROk8xBVdAf773CAKFwVBFUlN1jjevQEq3NIbjlxY%2BJqiw4qei92FWxphc3a%2F0x3Zy1c9CQcL6dbaSfMkULbocPSNDQXMHJpzKRT2WIL4W8h7ymtP35WfcSW3W%2B1lYAZ4t8n6rigl058nvuO9%2Br9rxfpJYMvZSYeQd0Z99ymI6jwBVmKiMmHZykEvLXz0ino8%2FtjtbJjIkZ16C5McAERz45%2FIOs28o9nhx%2FEmtwIvFWjkuY%2BBxPxsL07tJ43mI9s%2FX1GyWF%2F9mYQqY6125VHS1rp6vph%2BcMMZN0SEe8nOYnXWUezV3uhUX%2FDIYK%2BbP4IIjvMAsyBrvMQzUE5CFXrnd%2F0Jk%2FvL36j4BV%2BAkqr2laheqNMzKt66rlnomkdY6DAlSy5MLAYL4uxuKovoJ8MoZzMWTZSo5ja0HpMnn4WAlHhJuoEMZHlJr%2BnJXUr9YZjWr6S4bjinQphxGNpTmNyJjU3ZT3gXTh4pbE6sY%2F22a%2FRdF%2FL8jKcxEjxQil4tlu0v9IIIfNH%2FTqxu62V7g0KFENH9PNM74p23P6oMNaW5csGOqUB%2BXH22l1kf0RHFhIC3uRuJ12Wm%2FJGLOt8W66pKVQRgCVu1AsJ86T%2FvySKdW%2FTfYjUuLxW%2FAhGYOhVFR1jfv6UCDhjbbbjuzLy3Aqjfy7wWAru9CtLCEfMmdA23kDldpkxgQRQRaApj3cuKmRAGeTX7oBqaHbOFGiF7DX7qYnvd38iZWUQbPCj5YbW5lMuqP8%2B9p6Ydvwx4v8zZBg2E0ujBmxyCowh&X-Amz-Signature=d963daaf0b704e793fa1c481e33665163bd7d43cc771ecb3fb593c6ca8a1aef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









