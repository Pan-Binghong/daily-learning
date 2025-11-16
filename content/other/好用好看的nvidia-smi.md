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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEOOMUSG%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdL5xJeklIGlDcjPK7%2BfF5qgsTMcjX%2Bk%2FShsw6IZjWIwIhALj8bp7VfcPWuwL05FEsNU4iYRQx1xoaQG77%2F8rgn8pjKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FU%2B6dlkbfEUh5ti8q3AOptTFmovePyUeSYyvqlQ5Q4nZlp58kkD7NwR5ZaJCTZYfNjwXYo10SilMVMv5knVcszcSJSxv7KF22qbjEYhdQB11ihJBxVy2P21%2BQLllYegtuIudfseRH32uMB8cl43teCr3Uml9JWztlz6uf8mTTw713bkZPVx%2FLycGKY96GtJmyMTK8IgVYKc34uJC5gYQhgPZXo%2FAGW4k39dlmr55MpwWESW0WdW0id4Rp0tzhVEvNPJrfmCQpxq4%2BS%2FENY4Afmdz6p%2BU9vVV3GIYaT3gbTzCuloxlTBL%2F9s3D8nTVTOc2P2ez7gBP3ukv0UBlgi%2ByN3%2FXwzIZX5oWognTCvs4XaWeaiV8NUQB%2B3ecwLsG3o5hzQBvdE%2FJbC5muQhI96GNYFluRdwfTvU4T2L%2Brec1wGXiY974O8tXCHAC%2BoOUoYzp4FacnL4PjYVG4AEFOrNTk%2FnjiTmFzFex6TZFL4CFgzeoTGrLXjkYOaknAs7zsHo4EsRo3p7P0pNxEw3nfgAZY47DpFadxL3pafmpyNmPOw2cBwOf1jYDh1J8tS0TZJPEkALphYHTagohdEfoJDibyxTa4rE%2FJiKpRBvsET7OTfTyTc%2FNkg473HAYa67dw2G44aEheuf2kLWLyDDZ4OTIBjqkAcN7w42P17dDXUvfIxkb5X%2FMCbdcQypTpGV0nZZcnWCujHqsw4E1EKd4mMONCjAYCrbflwr0pgtGnXgOFardGTORiNHMG9RIyzxsYsxlEoSO%2Fcin6PwbEY42z61yoeJx3El30TT0i0qWrLKSAx5cLBcUANClU3Rk50pBNKI%2BUReOf0YiWfzv0CZzdFBm0IfIlAO9Y4gyrs%2BuEfAVnf0VZEmSMIma&X-Amz-Signature=8aa89be14eaa2e509e10f28b15b978344a01c3a48be35ed3aba24ec412874ea9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEOOMUSG%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCdL5xJeklIGlDcjPK7%2BfF5qgsTMcjX%2Bk%2FShsw6IZjWIwIhALj8bp7VfcPWuwL05FEsNU4iYRQx1xoaQG77%2F8rgn8pjKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2FU%2B6dlkbfEUh5ti8q3AOptTFmovePyUeSYyvqlQ5Q4nZlp58kkD7NwR5ZaJCTZYfNjwXYo10SilMVMv5knVcszcSJSxv7KF22qbjEYhdQB11ihJBxVy2P21%2BQLllYegtuIudfseRH32uMB8cl43teCr3Uml9JWztlz6uf8mTTw713bkZPVx%2FLycGKY96GtJmyMTK8IgVYKc34uJC5gYQhgPZXo%2FAGW4k39dlmr55MpwWESW0WdW0id4Rp0tzhVEvNPJrfmCQpxq4%2BS%2FENY4Afmdz6p%2BU9vVV3GIYaT3gbTzCuloxlTBL%2F9s3D8nTVTOc2P2ez7gBP3ukv0UBlgi%2ByN3%2FXwzIZX5oWognTCvs4XaWeaiV8NUQB%2B3ecwLsG3o5hzQBvdE%2FJbC5muQhI96GNYFluRdwfTvU4T2L%2Brec1wGXiY974O8tXCHAC%2BoOUoYzp4FacnL4PjYVG4AEFOrNTk%2FnjiTmFzFex6TZFL4CFgzeoTGrLXjkYOaknAs7zsHo4EsRo3p7P0pNxEw3nfgAZY47DpFadxL3pafmpyNmPOw2cBwOf1jYDh1J8tS0TZJPEkALphYHTagohdEfoJDibyxTa4rE%2FJiKpRBvsET7OTfTyTc%2FNkg473HAYa67dw2G44aEheuf2kLWLyDDZ4OTIBjqkAcN7w42P17dDXUvfIxkb5X%2FMCbdcQypTpGV0nZZcnWCujHqsw4E1EKd4mMONCjAYCrbflwr0pgtGnXgOFardGTORiNHMG9RIyzxsYsxlEoSO%2Fcin6PwbEY42z61yoeJx3El30TT0i0qWrLKSAx5cLBcUANClU3Rk50pBNKI%2BUReOf0YiWfzv0CZzdFBm0IfIlAO9Y4gyrs%2BuEfAVnf0VZEmSMIma&X-Amz-Signature=087071372887f39b37fffc62fd9da66413cb890ee538194d66a4772a181e8ec0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









