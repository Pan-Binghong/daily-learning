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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJJ7OGTT%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCmGQW%2Fzul5ZDPYrIQ5B9adeMubBunGLCVRBOpzjruV%2BAIgbSwtXfZA2sxQE47kSyyTcPOHSirj%2FuhV6v5dUlQkCl8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFZ8r2F113M%2BKRm31yrcA%2BE4o2WcM4XPr%2F0euxzmbPbg0P8wGCINemBSy2BDCUalTqHkZ1HVhD31432dcHCzCF9zwrTmqV74jmVmL%2B%2BiwYREYpYSiXGXMNfJQhrVVwcG4AgM5K9t8btwpLeKMJpxgn%2BoR6ePmMqEkUJU3SlpLc7J7IYlYqA5YPMM6Cq5d8pg7t4ump6JjZVAY2Hh0LjRIctFaJ%2Fv4H7lfgCfZiY0dy8wtFe%2BQe09X%2B6CSr47%2BXU1BgILHEZTy3ZMXTzixUfUob%2F8H7WkMn8bucRkPVbbivIk3sGbjZBNAsTk2zx88u%2F4DNedFfMNTNfRDZHON5AfVkA%2FCzByAGFg5b9mruhLeI%2BUksCsWCFb2aT%2BaRZirFItiJOPdEiwwVrVAJaq%2F31wIM3o9S6DjAS6RMMSFL4XNuJBdg1EpTwDWAqGwctD2EzgyXPdHrhl77sbyPgd4Ez8wGP73hX6kHXZG%2FYeT%2B0cYJrYJEA15QQiX6IHkPJKEbYS%2FqGgEx5QEBAFdlbfsz0%2B3xvioLZsq7cYjP82LvPQ%2BioWuFZdmbW9guwf4AV1GjaM6RqcgcDjCX2H2F3KrbCVkuIsjKpVa3dhxYyUS5uYxmoe0TjRJHbygoG9BL1%2FVGmodtcKk9lYM%2FLul7HEMKHvm8sGOqUBKzuc%2BRq58rmGHHydos%2BNKcIlZ57mYdnZXOsmk2%2BQ4yRJFuNjC03%2BJbqyxpjO3COrJ8SlNuSkx3Pdbrripfk9N%2Bvaooo%2BzR0tYIqKtwkNL8S1t%2BG%2BRUg70jm3H003hPNtKMg8ZgwC6pgYWbAbhFkrY15P4LUpd2j4EvgOZJjYaEybyIVLpdbglXQg%2FSHjCP1UuOwlPmMXvrnniw9tYZuetA4skWY2&X-Amz-Signature=4d480c55197aa1856ffb3ec5ea7d6a4f8fbc945a3410fd5762c4fd1748d10230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJJ7OGTT%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCmGQW%2Fzul5ZDPYrIQ5B9adeMubBunGLCVRBOpzjruV%2BAIgbSwtXfZA2sxQE47kSyyTcPOHSirj%2FuhV6v5dUlQkCl8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFZ8r2F113M%2BKRm31yrcA%2BE4o2WcM4XPr%2F0euxzmbPbg0P8wGCINemBSy2BDCUalTqHkZ1HVhD31432dcHCzCF9zwrTmqV74jmVmL%2B%2BiwYREYpYSiXGXMNfJQhrVVwcG4AgM5K9t8btwpLeKMJpxgn%2BoR6ePmMqEkUJU3SlpLc7J7IYlYqA5YPMM6Cq5d8pg7t4ump6JjZVAY2Hh0LjRIctFaJ%2Fv4H7lfgCfZiY0dy8wtFe%2BQe09X%2B6CSr47%2BXU1BgILHEZTy3ZMXTzixUfUob%2F8H7WkMn8bucRkPVbbivIk3sGbjZBNAsTk2zx88u%2F4DNedFfMNTNfRDZHON5AfVkA%2FCzByAGFg5b9mruhLeI%2BUksCsWCFb2aT%2BaRZirFItiJOPdEiwwVrVAJaq%2F31wIM3o9S6DjAS6RMMSFL4XNuJBdg1EpTwDWAqGwctD2EzgyXPdHrhl77sbyPgd4Ez8wGP73hX6kHXZG%2FYeT%2B0cYJrYJEA15QQiX6IHkPJKEbYS%2FqGgEx5QEBAFdlbfsz0%2B3xvioLZsq7cYjP82LvPQ%2BioWuFZdmbW9guwf4AV1GjaM6RqcgcDjCX2H2F3KrbCVkuIsjKpVa3dhxYyUS5uYxmoe0TjRJHbygoG9BL1%2FVGmodtcKk9lYM%2FLul7HEMKHvm8sGOqUBKzuc%2BRq58rmGHHydos%2BNKcIlZ57mYdnZXOsmk2%2BQ4yRJFuNjC03%2BJbqyxpjO3COrJ8SlNuSkx3Pdbrripfk9N%2Bvaooo%2BzR0tYIqKtwkNL8S1t%2BG%2BRUg70jm3H003hPNtKMg8ZgwC6pgYWbAbhFkrY15P4LUpd2j4EvgOZJjYaEybyIVLpdbglXQg%2FSHjCP1UuOwlPmMXvrnniw9tYZuetA4skWY2&X-Amz-Signature=2bcbc1614125aca1ac18a441612841eeec6e27cda36fddbd25fac74ccd8a2204&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJJ7OGTT%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCmGQW%2Fzul5ZDPYrIQ5B9adeMubBunGLCVRBOpzjruV%2BAIgbSwtXfZA2sxQE47kSyyTcPOHSirj%2FuhV6v5dUlQkCl8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFZ8r2F113M%2BKRm31yrcA%2BE4o2WcM4XPr%2F0euxzmbPbg0P8wGCINemBSy2BDCUalTqHkZ1HVhD31432dcHCzCF9zwrTmqV74jmVmL%2B%2BiwYREYpYSiXGXMNfJQhrVVwcG4AgM5K9t8btwpLeKMJpxgn%2BoR6ePmMqEkUJU3SlpLc7J7IYlYqA5YPMM6Cq5d8pg7t4ump6JjZVAY2Hh0LjRIctFaJ%2Fv4H7lfgCfZiY0dy8wtFe%2BQe09X%2B6CSr47%2BXU1BgILHEZTy3ZMXTzixUfUob%2F8H7WkMn8bucRkPVbbivIk3sGbjZBNAsTk2zx88u%2F4DNedFfMNTNfRDZHON5AfVkA%2FCzByAGFg5b9mruhLeI%2BUksCsWCFb2aT%2BaRZirFItiJOPdEiwwVrVAJaq%2F31wIM3o9S6DjAS6RMMSFL4XNuJBdg1EpTwDWAqGwctD2EzgyXPdHrhl77sbyPgd4Ez8wGP73hX6kHXZG%2FYeT%2B0cYJrYJEA15QQiX6IHkPJKEbYS%2FqGgEx5QEBAFdlbfsz0%2B3xvioLZsq7cYjP82LvPQ%2BioWuFZdmbW9guwf4AV1GjaM6RqcgcDjCX2H2F3KrbCVkuIsjKpVa3dhxYyUS5uYxmoe0TjRJHbygoG9BL1%2FVGmodtcKk9lYM%2FLul7HEMKHvm8sGOqUBKzuc%2BRq58rmGHHydos%2BNKcIlZ57mYdnZXOsmk2%2BQ4yRJFuNjC03%2BJbqyxpjO3COrJ8SlNuSkx3Pdbrripfk9N%2Bvaooo%2BzR0tYIqKtwkNL8S1t%2BG%2BRUg70jm3H003hPNtKMg8ZgwC6pgYWbAbhFkrY15P4LUpd2j4EvgOZJjYaEybyIVLpdbglXQg%2FSHjCP1UuOwlPmMXvrnniw9tYZuetA4skWY2&X-Amz-Signature=59f9122b3c829c916da423465ff30cb660060ca27755bb61801efd10d5c0b795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

