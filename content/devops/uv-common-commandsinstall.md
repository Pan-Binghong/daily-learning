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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKXNHDGE%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJvq81WQLhflQj%2BIQZwZftoR8EwfaMg8GEzigQEp9deAiEA%2Bw%2BNJ3R4fjYwo79IcUvk18%2BoHOuJ%2BoqOanrWX0XObLgq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO1yu1Sv7vAR9JuQIyrcA61wlZZQLrCQUZ01OpD6nJfdYATgrTDsrYQgQVaAIi8%2FXH2VEkf0toLq8uKZF3Lw3vtx0iIAaT259XbaYUPSsQ0rEy3deTjbcLxbiweNaUjB%2FxYjAociMPXxjjXS%2FOSjk4Ye9XNt%2FqYddN9VrJIo1%2BRyNBYcyPmeeAjEm3a2ZYWZPhC2WEwd6AX0uIWE28JOe7aXT9XHBS9Ib9MOXg1%2BbetzmjwpLXKevQ5iOK68nvfxiqVIeuIsiI4%2BAeag0ovuiYJTaI%2BeCNvNEvaJVQ%2F46zMJ4PDBhyvbqOm%2BkYDUQCP1pu%2BnxoR5Nj5Y7Ep1RE47svGcckr77tHVHe2C%2Bf%2Fh9ny%2FwVxrba9nk9NCJTB1cG8GuA9YBWnxErcd%2FmP6dvRg%2BqVyIcHrRc%2Biw1XdLlyz1mv2SkI8k3KnQ6cMy%2F8IekEcwJKHJz3aQ8btfl1CJdW3uPZb465zOIvDaYfHGXatotCk11yXaGBkE%2ByIvJOaxhU0YA6JjiEsJVAZWwR7Jo1NxjhLvRenL3rf9iIEepPITFXVuzHSEGcgcnihT8UFKV5rmFC39oFo9LmLqQcWGdLdB31r6oGaRYfgqkGoGE0KOyQC5UGHr95DxjZb3JQ8neJPLWHsWOtcOd0AnO7BMIyNg8oGOqUBYq0Fi80rsOtCItVVKotgUZ4rQNH9lM7T6rnsKHQGTaKxchlejlsc%2BQKzyAZcYwzkf23QQSaKJZ3kF2LX9j3NGz7aom9NC50ShxG6pXYcUAWm%2Bx9%2BbCPX7%2F2iL5nTL8%2BMb4P8JvOHuQz09RQOL3g%2FpaN%2FktTAGHw1XXgDtg0oD2SXPOOQhYJRg4k5A8QBKOe%2BCY8I45eom%2B%2BG%2BDFtWnxpCCpGcXUK&X-Amz-Signature=d0d90ae4d709d54c8c841cf6bccc3a01a43ae67f1644947815106a6542e6c80e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKXNHDGE%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJvq81WQLhflQj%2BIQZwZftoR8EwfaMg8GEzigQEp9deAiEA%2Bw%2BNJ3R4fjYwo79IcUvk18%2BoHOuJ%2BoqOanrWX0XObLgq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO1yu1Sv7vAR9JuQIyrcA61wlZZQLrCQUZ01OpD6nJfdYATgrTDsrYQgQVaAIi8%2FXH2VEkf0toLq8uKZF3Lw3vtx0iIAaT259XbaYUPSsQ0rEy3deTjbcLxbiweNaUjB%2FxYjAociMPXxjjXS%2FOSjk4Ye9XNt%2FqYddN9VrJIo1%2BRyNBYcyPmeeAjEm3a2ZYWZPhC2WEwd6AX0uIWE28JOe7aXT9XHBS9Ib9MOXg1%2BbetzmjwpLXKevQ5iOK68nvfxiqVIeuIsiI4%2BAeag0ovuiYJTaI%2BeCNvNEvaJVQ%2F46zMJ4PDBhyvbqOm%2BkYDUQCP1pu%2BnxoR5Nj5Y7Ep1RE47svGcckr77tHVHe2C%2Bf%2Fh9ny%2FwVxrba9nk9NCJTB1cG8GuA9YBWnxErcd%2FmP6dvRg%2BqVyIcHrRc%2Biw1XdLlyz1mv2SkI8k3KnQ6cMy%2F8IekEcwJKHJz3aQ8btfl1CJdW3uPZb465zOIvDaYfHGXatotCk11yXaGBkE%2ByIvJOaxhU0YA6JjiEsJVAZWwR7Jo1NxjhLvRenL3rf9iIEepPITFXVuzHSEGcgcnihT8UFKV5rmFC39oFo9LmLqQcWGdLdB31r6oGaRYfgqkGoGE0KOyQC5UGHr95DxjZb3JQ8neJPLWHsWOtcOd0AnO7BMIyNg8oGOqUBYq0Fi80rsOtCItVVKotgUZ4rQNH9lM7T6rnsKHQGTaKxchlejlsc%2BQKzyAZcYwzkf23QQSaKJZ3kF2LX9j3NGz7aom9NC50ShxG6pXYcUAWm%2Bx9%2BbCPX7%2F2iL5nTL8%2BMb4P8JvOHuQz09RQOL3g%2FpaN%2FktTAGHw1XXgDtg0oD2SXPOOQhYJRg4k5A8QBKOe%2BCY8I45eom%2B%2BG%2BDFtWnxpCCpGcXUK&X-Amz-Signature=121f22e81f6fd1f0a29fb0e83a296004c9db58adfb53cb62725cf4237a5eb0ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKXNHDGE%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICJvq81WQLhflQj%2BIQZwZftoR8EwfaMg8GEzigQEp9deAiEA%2Bw%2BNJ3R4fjYwo79IcUvk18%2BoHOuJ%2BoqOanrWX0XObLgq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDO1yu1Sv7vAR9JuQIyrcA61wlZZQLrCQUZ01OpD6nJfdYATgrTDsrYQgQVaAIi8%2FXH2VEkf0toLq8uKZF3Lw3vtx0iIAaT259XbaYUPSsQ0rEy3deTjbcLxbiweNaUjB%2FxYjAociMPXxjjXS%2FOSjk4Ye9XNt%2FqYddN9VrJIo1%2BRyNBYcyPmeeAjEm3a2ZYWZPhC2WEwd6AX0uIWE28JOe7aXT9XHBS9Ib9MOXg1%2BbetzmjwpLXKevQ5iOK68nvfxiqVIeuIsiI4%2BAeag0ovuiYJTaI%2BeCNvNEvaJVQ%2F46zMJ4PDBhyvbqOm%2BkYDUQCP1pu%2BnxoR5Nj5Y7Ep1RE47svGcckr77tHVHe2C%2Bf%2Fh9ny%2FwVxrba9nk9NCJTB1cG8GuA9YBWnxErcd%2FmP6dvRg%2BqVyIcHrRc%2Biw1XdLlyz1mv2SkI8k3KnQ6cMy%2F8IekEcwJKHJz3aQ8btfl1CJdW3uPZb465zOIvDaYfHGXatotCk11yXaGBkE%2ByIvJOaxhU0YA6JjiEsJVAZWwR7Jo1NxjhLvRenL3rf9iIEepPITFXVuzHSEGcgcnihT8UFKV5rmFC39oFo9LmLqQcWGdLdB31r6oGaRYfgqkGoGE0KOyQC5UGHr95DxjZb3JQ8neJPLWHsWOtcOd0AnO7BMIyNg8oGOqUBYq0Fi80rsOtCItVVKotgUZ4rQNH9lM7T6rnsKHQGTaKxchlejlsc%2BQKzyAZcYwzkf23QQSaKJZ3kF2LX9j3NGz7aom9NC50ShxG6pXYcUAWm%2Bx9%2BbCPX7%2F2iL5nTL8%2BMb4P8JvOHuQz09RQOL3g%2FpaN%2FktTAGHw1XXgDtg0oD2SXPOOQhYJRg4k5A8QBKOe%2BCY8I45eom%2B%2BG%2BDFtWnxpCCpGcXUK&X-Amz-Signature=71a6a7e85b96dfec776d16a90ddd7f95d4c66e29c984fbcec06f4e0d1db7c4a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

