---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WML7D4M7%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuUP%2FptWoXH%2FRIj3EDy0ZKTiWmJBYM3HL0NKD9cZXneAiEAjiL4njLeigwAYuYKWufOYrFMn%2BX2kNwbh30INmLafwsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGPOfYyk%2BCLny30HVCrcA%2B3%2Fu%2FxilEHR3OUPk7O9RNm4xeXquQbUOAMa%2Blg%2Fi3qJ%2BrqOWJp7BW1dmt11hwYao7F1uuk9Ipp%2BywlpuktcYZWYMcqserDcG5L%2BcvaB2ccixCEeAivkNZhkfN8jNtvVkII%2BMGal%2BClaLASsXUVvRGzfUEp1%2FCr2kNb%2FAjS%2FGK7FVS3ziWKS1B%2F8fTdLDfK%2BuuXDQxQhKtzCzQi0tSZU5ryuWa7GT7q5H%2FHApiRCBcCf%2Fwtq1IcsWHwWK6XrbQ2V5L5iK5JmkHQMhk3VHmUGTMJ2c9rETweCuPawDgK%2FGjbA9DgldyguPIlEaRspskQetJGzFATguOQQ6Lu9%2Bgf6cEccPT0j%2BG9s7PNlxn0l34u2JrJ5XTwVCbIYqlMYTqSFPjW8l8FmcKY1fZxaGlPU7yY3Nuyiz8KUTDmE97yboLEyiKK9WQJGOScra6cwA5yZtuRtrUuNsdJFytTUCBbjMZwREjw4K9HVhHpum9uFY3BE8rikkyZ6SzT64ZQvlf8W9Y7lbahuX0NmMWRV53dAAhyxLdlFMl7xU2DovGAl6sY2j%2F55xTAOkr1lnTiD1YgtO%2B5HfQIXmg9V8%2BdMFv%2Fm42paePynk%2B5U3chNIYshwzsObdKgOpo%2FcuBicEWLMM2yiMoGOqUBY0AJUEw7LJNT4EBTd%2FjGLlFiTMYgKXDRZ9BFRFhMqz3sdd34kLF9PfPSLEd8tmLSSeIJI%2BBsLbs%2F0DsJHj%2FMFCGvXB97sQFV3oUoT52C1eqnpAChfkTOWsP01o0WDfCqYE%2BnwRVtacFrFwbWh4vRXKOwmTJU1d0QzZFxGDQeTNhTS8NAi1tnSLr65t6EZ%2FdOjiPmLJ9IVO5AX9C%2BpdTHTxrTC9bk&X-Amz-Signature=3fef5b0f0d101ba4997cdec4450ce611fbf5941e9eb5983a575cf31d3f6e4a3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WML7D4M7%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuUP%2FptWoXH%2FRIj3EDy0ZKTiWmJBYM3HL0NKD9cZXneAiEAjiL4njLeigwAYuYKWufOYrFMn%2BX2kNwbh30INmLafwsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGPOfYyk%2BCLny30HVCrcA%2B3%2Fu%2FxilEHR3OUPk7O9RNm4xeXquQbUOAMa%2Blg%2Fi3qJ%2BrqOWJp7BW1dmt11hwYao7F1uuk9Ipp%2BywlpuktcYZWYMcqserDcG5L%2BcvaB2ccixCEeAivkNZhkfN8jNtvVkII%2BMGal%2BClaLASsXUVvRGzfUEp1%2FCr2kNb%2FAjS%2FGK7FVS3ziWKS1B%2F8fTdLDfK%2BuuXDQxQhKtzCzQi0tSZU5ryuWa7GT7q5H%2FHApiRCBcCf%2Fwtq1IcsWHwWK6XrbQ2V5L5iK5JmkHQMhk3VHmUGTMJ2c9rETweCuPawDgK%2FGjbA9DgldyguPIlEaRspskQetJGzFATguOQQ6Lu9%2Bgf6cEccPT0j%2BG9s7PNlxn0l34u2JrJ5XTwVCbIYqlMYTqSFPjW8l8FmcKY1fZxaGlPU7yY3Nuyiz8KUTDmE97yboLEyiKK9WQJGOScra6cwA5yZtuRtrUuNsdJFytTUCBbjMZwREjw4K9HVhHpum9uFY3BE8rikkyZ6SzT64ZQvlf8W9Y7lbahuX0NmMWRV53dAAhyxLdlFMl7xU2DovGAl6sY2j%2F55xTAOkr1lnTiD1YgtO%2B5HfQIXmg9V8%2BdMFv%2Fm42paePynk%2B5U3chNIYshwzsObdKgOpo%2FcuBicEWLMM2yiMoGOqUBY0AJUEw7LJNT4EBTd%2FjGLlFiTMYgKXDRZ9BFRFhMqz3sdd34kLF9PfPSLEd8tmLSSeIJI%2BBsLbs%2F0DsJHj%2FMFCGvXB97sQFV3oUoT52C1eqnpAChfkTOWsP01o0WDfCqYE%2BnwRVtacFrFwbWh4vRXKOwmTJU1d0QzZFxGDQeTNhTS8NAi1tnSLr65t6EZ%2FdOjiPmLJ9IVO5AX9C%2BpdTHTxrTC9bk&X-Amz-Signature=4fd1f1c21e0c542897553233a510dbf6f31f3a9e3a8c89a40801015a5ab7738c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WML7D4M7%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuUP%2FptWoXH%2FRIj3EDy0ZKTiWmJBYM3HL0NKD9cZXneAiEAjiL4njLeigwAYuYKWufOYrFMn%2BX2kNwbh30INmLafwsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGPOfYyk%2BCLny30HVCrcA%2B3%2Fu%2FxilEHR3OUPk7O9RNm4xeXquQbUOAMa%2Blg%2Fi3qJ%2BrqOWJp7BW1dmt11hwYao7F1uuk9Ipp%2BywlpuktcYZWYMcqserDcG5L%2BcvaB2ccixCEeAivkNZhkfN8jNtvVkII%2BMGal%2BClaLASsXUVvRGzfUEp1%2FCr2kNb%2FAjS%2FGK7FVS3ziWKS1B%2F8fTdLDfK%2BuuXDQxQhKtzCzQi0tSZU5ryuWa7GT7q5H%2FHApiRCBcCf%2Fwtq1IcsWHwWK6XrbQ2V5L5iK5JmkHQMhk3VHmUGTMJ2c9rETweCuPawDgK%2FGjbA9DgldyguPIlEaRspskQetJGzFATguOQQ6Lu9%2Bgf6cEccPT0j%2BG9s7PNlxn0l34u2JrJ5XTwVCbIYqlMYTqSFPjW8l8FmcKY1fZxaGlPU7yY3Nuyiz8KUTDmE97yboLEyiKK9WQJGOScra6cwA5yZtuRtrUuNsdJFytTUCBbjMZwREjw4K9HVhHpum9uFY3BE8rikkyZ6SzT64ZQvlf8W9Y7lbahuX0NmMWRV53dAAhyxLdlFMl7xU2DovGAl6sY2j%2F55xTAOkr1lnTiD1YgtO%2B5HfQIXmg9V8%2BdMFv%2Fm42paePynk%2B5U3chNIYshwzsObdKgOpo%2FcuBicEWLMM2yiMoGOqUBY0AJUEw7LJNT4EBTd%2FjGLlFiTMYgKXDRZ9BFRFhMqz3sdd34kLF9PfPSLEd8tmLSSeIJI%2BBsLbs%2F0DsJHj%2FMFCGvXB97sQFV3oUoT52C1eqnpAChfkTOWsP01o0WDfCqYE%2BnwRVtacFrFwbWh4vRXKOwmTJU1d0QzZFxGDQeTNhTS8NAi1tnSLr65t6EZ%2FdOjiPmLJ9IVO5AX9C%2BpdTHTxrTC9bk&X-Amz-Signature=fa4e589b96d485d455bee78402efb532863f61bc8b4978248dec73cd3cdad021&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

