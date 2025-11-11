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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBXBS3L%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHdn0%2BZC1zYI8J1HhGCTUDj0Lp34BRiHPBlxJJyKNlP6AiBdgsFGDIC0mzsivV%2FH9VFg9JMi0gBmT7j2WFMRf8yYKSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMAd3n%2FCKusgT68rQ%2BKtwDW4J4cmnzZ8FDkHyAj6pYR1PrI4mvqME4aw2VE9txByQuOrhHuSJeZ%2BWl5j%2Bb6siBTGw%2FPTKsM3gHDJM799iFX9hLXFs2HZzjlyjOdbJBRLAmjR6Kt4d46UQ%2FO%2FRCne4kZGx1XFUUn2fJV91tmgJwGzOz3fjPROghGQy%2BFw6H3t%2BU0QsI5%2BhF8%2BahdLRRcLrS90q7WTBpCAs1ulY%2BzqJVmbJ1RBsiektCIFJsJII2oxlHtI8Dzs4P4orBNRf%2BpkxI%2F9PmM4A%2FQxYCidvOJTsefVkj%2FEw0bXxwoVfCdUOheZR1byFa7Fh9n6%2Fsx22kRiPUlFgIOx6vBc%2Bs7YEawbZT1Z5y9oEigayV4qxUsM%2Fm0BL64gpoJ%2BKK%2BbKGyFvxGfyIw733FNIuPY%2BdZ2E3L%2BDCwu7f0ew4Lb7ujhXHs2RRRjqkMKobfkRBMuU7vLAK5iiXsT4n%2FeS16vEqQjuUofhDe6mKHl%2FUbBaRk4nP65ixJxG%2By%2Baw398nTAjQbGnGcdOpu67dsXph%2Bn8AAo1w1oPmIPtL50ZFDaOXE9TS3Q3DIPuw4c77HCXfGgiopeYW0HRdj%2FtghVUlVI4olans92M39kRbDpaZq61KcTqkkisFc7cE9%2FP1mfs053K7374wrr3KyAY6pgFQk9ujC09Xf2UbxO5bH2uLYaexWiH3sk0GCKPx%2BOR3xkE%2FHzjjmHmtrdm8sd5phveKUFvsw%2FTbyR9e4CIc7QgiW7gzAEmLJsjAO0H3DcB9TaFUPbepun4QyhdpMfEiyour8OCj8IORG7UGbdHoCxSiYAKyIYYYB5waxIaYn4sAIoH0jOaVdQaN%2FNn5ndGAaGfDtuG%2FzNltu5A6sceMCkI96X50vM3X&X-Amz-Signature=551a3d90e89a373825f9e1a8fcfe24f416689d25e4b65b7a44f62bb0806f45f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBXBS3L%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHdn0%2BZC1zYI8J1HhGCTUDj0Lp34BRiHPBlxJJyKNlP6AiBdgsFGDIC0mzsivV%2FH9VFg9JMi0gBmT7j2WFMRf8yYKSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMAd3n%2FCKusgT68rQ%2BKtwDW4J4cmnzZ8FDkHyAj6pYR1PrI4mvqME4aw2VE9txByQuOrhHuSJeZ%2BWl5j%2Bb6siBTGw%2FPTKsM3gHDJM799iFX9hLXFs2HZzjlyjOdbJBRLAmjR6Kt4d46UQ%2FO%2FRCne4kZGx1XFUUn2fJV91tmgJwGzOz3fjPROghGQy%2BFw6H3t%2BU0QsI5%2BhF8%2BahdLRRcLrS90q7WTBpCAs1ulY%2BzqJVmbJ1RBsiektCIFJsJII2oxlHtI8Dzs4P4orBNRf%2BpkxI%2F9PmM4A%2FQxYCidvOJTsefVkj%2FEw0bXxwoVfCdUOheZR1byFa7Fh9n6%2Fsx22kRiPUlFgIOx6vBc%2Bs7YEawbZT1Z5y9oEigayV4qxUsM%2Fm0BL64gpoJ%2BKK%2BbKGyFvxGfyIw733FNIuPY%2BdZ2E3L%2BDCwu7f0ew4Lb7ujhXHs2RRRjqkMKobfkRBMuU7vLAK5iiXsT4n%2FeS16vEqQjuUofhDe6mKHl%2FUbBaRk4nP65ixJxG%2By%2Baw398nTAjQbGnGcdOpu67dsXph%2Bn8AAo1w1oPmIPtL50ZFDaOXE9TS3Q3DIPuw4c77HCXfGgiopeYW0HRdj%2FtghVUlVI4olans92M39kRbDpaZq61KcTqkkisFc7cE9%2FP1mfs053K7374wrr3KyAY6pgFQk9ujC09Xf2UbxO5bH2uLYaexWiH3sk0GCKPx%2BOR3xkE%2FHzjjmHmtrdm8sd5phveKUFvsw%2FTbyR9e4CIc7QgiW7gzAEmLJsjAO0H3DcB9TaFUPbepun4QyhdpMfEiyour8OCj8IORG7UGbdHoCxSiYAKyIYYYB5waxIaYn4sAIoH0jOaVdQaN%2FNn5ndGAaGfDtuG%2FzNltu5A6sceMCkI96X50vM3X&X-Amz-Signature=c10036c370c17c3c081ad66904ae9a77afe101ef7669562ffdf2f9a464a6cc8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEBXBS3L%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIHdn0%2BZC1zYI8J1HhGCTUDj0Lp34BRiHPBlxJJyKNlP6AiBdgsFGDIC0mzsivV%2FH9VFg9JMi0gBmT7j2WFMRf8yYKSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMAd3n%2FCKusgT68rQ%2BKtwDW4J4cmnzZ8FDkHyAj6pYR1PrI4mvqME4aw2VE9txByQuOrhHuSJeZ%2BWl5j%2Bb6siBTGw%2FPTKsM3gHDJM799iFX9hLXFs2HZzjlyjOdbJBRLAmjR6Kt4d46UQ%2FO%2FRCne4kZGx1XFUUn2fJV91tmgJwGzOz3fjPROghGQy%2BFw6H3t%2BU0QsI5%2BhF8%2BahdLRRcLrS90q7WTBpCAs1ulY%2BzqJVmbJ1RBsiektCIFJsJII2oxlHtI8Dzs4P4orBNRf%2BpkxI%2F9PmM4A%2FQxYCidvOJTsefVkj%2FEw0bXxwoVfCdUOheZR1byFa7Fh9n6%2Fsx22kRiPUlFgIOx6vBc%2Bs7YEawbZT1Z5y9oEigayV4qxUsM%2Fm0BL64gpoJ%2BKK%2BbKGyFvxGfyIw733FNIuPY%2BdZ2E3L%2BDCwu7f0ew4Lb7ujhXHs2RRRjqkMKobfkRBMuU7vLAK5iiXsT4n%2FeS16vEqQjuUofhDe6mKHl%2FUbBaRk4nP65ixJxG%2By%2Baw398nTAjQbGnGcdOpu67dsXph%2Bn8AAo1w1oPmIPtL50ZFDaOXE9TS3Q3DIPuw4c77HCXfGgiopeYW0HRdj%2FtghVUlVI4olans92M39kRbDpaZq61KcTqkkisFc7cE9%2FP1mfs053K7374wrr3KyAY6pgFQk9ujC09Xf2UbxO5bH2uLYaexWiH3sk0GCKPx%2BOR3xkE%2FHzjjmHmtrdm8sd5phveKUFvsw%2FTbyR9e4CIc7QgiW7gzAEmLJsjAO0H3DcB9TaFUPbepun4QyhdpMfEiyour8OCj8IORG7UGbdHoCxSiYAKyIYYYB5waxIaYn4sAIoH0jOaVdQaN%2FNn5ndGAaGfDtuG%2FzNltu5A6sceMCkI96X50vM3X&X-Amz-Signature=d3d8b8510001b013a14818be56c27b9c08d5bc320f2757d0ed820815b8fa1b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

