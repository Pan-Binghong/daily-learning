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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHHAK6OM%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQD0BG%2FqN3UeMtl8ZeZF2wLWKe8s7zI0LC6m9ATeAtDpQAIhAOXKoq%2B%2FZa6jjYtHn8Q4ib7ijzSwYK%2FQ1l1wqJTTKaCBKv8DCCQQABoMNjM3NDIzMTgzODA1IgwBCfugn3QG3aLBdiwq3AN3lvP4N8wL6rW4j0mk%2FzhB%2BQBgGOWdS1DK%2FB%2FXHm2OgmzPKquvjWiRldLc7OoVTx4X7YhSGQnbQdmbAfE6wuzesRY6AoaBtDR3oTls%2BsIHCA0%2BryX5zT3zHPLhAvMAvvZAxriUA4pUu53nu4%2F9uA9SvUk8paaNy%2FS1kk8isGnq00crj%2F%2FEkexSeAGzizVVB%2FxI02czY3rjurCiINByK2d0XROT7u%2B7cIcYmDUd%2FVXoMhM1MV44Le2qNYkoHoJF2Ef5a2tCXdIc0pUubar27r%2FJgOJBIXvwHIwxbnjWJL3EptSDVQs4cm%2BZtU4YYmzzLI%2B3ECzt4Jb%2BhAcu%2BNXRp6bZQWhp1NGM2iYPFPrwDqQLWyWTzDqkfkBNp%2FYv1yMf24dDw91hMws8x9ZfhcftmPIHjsyPAbGGgozGBTHmzOQtsBK50p5ldd%2BSbaHCtjuX%2FmRK3YH8VaFNMr64S99M2oQ42WC7fQpuFkfH1r8Z7kk%2FSeF0P4F93oFqrJIPmRv0jBmNPf0uq70CLhFJUq0iyDjR2jsuHT7VrQS33gV6UaCr5c4%2FZeayifYIEKxokIzznXJmiwITYpu01xdoX%2B7WS5lIkivGa%2Fv47EoKHX%2FfaKg6yfZIZ0EbslUt6ntvdTD0kpDMBjqkAZDjFI34Yi9wtrIY8l4v%2FR0A77fI04dRZyVE4UNbki3Xl4XAtyQ8xzKu0N5dfBEcRA%2B36EkTo7O6%2Fz9i2CC7asybFaJcUq4k1uDTomQsisCPp3g2LW6xUaFeZbAE7z1a4PdhrfEZk0cM5rUTis2E2mcM1GOXcWvandW%2F0Olf9QY5yqbdFS8Re2h8i0FWUvFWqivisb90ZkWiK%2BMlvOJV8NqqUSXG&X-Amz-Signature=8dc143b4d5a75d15cef26b3d0129fb17ba1d258fe7da7a228e9e9d1d71b183de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHHAK6OM%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQD0BG%2FqN3UeMtl8ZeZF2wLWKe8s7zI0LC6m9ATeAtDpQAIhAOXKoq%2B%2FZa6jjYtHn8Q4ib7ijzSwYK%2FQ1l1wqJTTKaCBKv8DCCQQABoMNjM3NDIzMTgzODA1IgwBCfugn3QG3aLBdiwq3AN3lvP4N8wL6rW4j0mk%2FzhB%2BQBgGOWdS1DK%2FB%2FXHm2OgmzPKquvjWiRldLc7OoVTx4X7YhSGQnbQdmbAfE6wuzesRY6AoaBtDR3oTls%2BsIHCA0%2BryX5zT3zHPLhAvMAvvZAxriUA4pUu53nu4%2F9uA9SvUk8paaNy%2FS1kk8isGnq00crj%2F%2FEkexSeAGzizVVB%2FxI02czY3rjurCiINByK2d0XROT7u%2B7cIcYmDUd%2FVXoMhM1MV44Le2qNYkoHoJF2Ef5a2tCXdIc0pUubar27r%2FJgOJBIXvwHIwxbnjWJL3EptSDVQs4cm%2BZtU4YYmzzLI%2B3ECzt4Jb%2BhAcu%2BNXRp6bZQWhp1NGM2iYPFPrwDqQLWyWTzDqkfkBNp%2FYv1yMf24dDw91hMws8x9ZfhcftmPIHjsyPAbGGgozGBTHmzOQtsBK50p5ldd%2BSbaHCtjuX%2FmRK3YH8VaFNMr64S99M2oQ42WC7fQpuFkfH1r8Z7kk%2FSeF0P4F93oFqrJIPmRv0jBmNPf0uq70CLhFJUq0iyDjR2jsuHT7VrQS33gV6UaCr5c4%2FZeayifYIEKxokIzznXJmiwITYpu01xdoX%2B7WS5lIkivGa%2Fv47EoKHX%2FfaKg6yfZIZ0EbslUt6ntvdTD0kpDMBjqkAZDjFI34Yi9wtrIY8l4v%2FR0A77fI04dRZyVE4UNbki3Xl4XAtyQ8xzKu0N5dfBEcRA%2B36EkTo7O6%2Fz9i2CC7asybFaJcUq4k1uDTomQsisCPp3g2LW6xUaFeZbAE7z1a4PdhrfEZk0cM5rUTis2E2mcM1GOXcWvandW%2F0Olf9QY5yqbdFS8Re2h8i0FWUvFWqivisb90ZkWiK%2BMlvOJV8NqqUSXG&X-Amz-Signature=caadaa8bed466a61e897e1f302ad8c71b9a4bec1da5bfe9df5de75f6dccc470a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









