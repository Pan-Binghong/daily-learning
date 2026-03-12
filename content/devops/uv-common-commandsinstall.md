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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQKYKIAB%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmfS9GgseVSRUb0lcHgga%2BCmzklbKmWyANoFHCqY4MUAiEA%2B5ikimowOA%2BdvsL1%2BLzaeDE6o%2BpwG2cSfYG7xCNSzX0q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDNsVWSomX4kJ6On3ySrcA1DP5c3H%2FWJvQDvYzhS3exq%2FbolTKthhvHOmLmicL1JQZzc0NgXnDr9fjOkqu%2F4GG15dpTyp85CAfwOZY3i6iT9ErwEiwJDZlxM1TdxJaQvWSN0vHB3yYx%2FpUVCu%2FlDu0PIJgbbykpKj4EE547%2B0WKJwtmuf%2BHw6BCSiPOYMYtzj%2BIyQSpm5LGNV5f69KTjIFw%2Bv5X1agDFKHJM%2BIQU%2F1SN7J7t4RgqsdQg%2F2R5rsXyT0GaEZYEeVcg4QcFR5GLVPdGPVKRW3qrlbf0X3Bah95J5BavdlZNMI7CwnTHx3%2Fjte2ELUbWVUTeJP8RKiKVUgQzGmaHqqesorby3yM0juOUr1b4%2BYS8tlKLaYb2QUsjmjRNybo6YPgPFtf2wYG60RqYE1L%2FdVS143kKO%2Bc5cVJGB6DaMY%2BwREM2AadSvIp3S8aiuadS47xgYqAS2ytC7YlLwzTooMvIggx%2FgioNIRkZu11fIHyOQz6%2B9w772lMVf%2BTXyKOc6uMa8gRzBLZVEm%2FCyXaVLjwMvNpXjG9zbgEQ%2Bw2TlbN0fjod9%2BecY8jLszDk0M3Ortqp7akfDpz%2FmMOjmwTTTcdW8Am8LnhEMtP1ytf9%2F4MmzjRJPw27jae2CRXT6Tf1QteqpuM2wMM2yyM0GOqUB3MYeRolDAyZzMfwwSlfcTmagsxSAXzy%2BjmCMWJL6OBsTtCBnE0d9PkLdyEQe%2FHqFrVamwHHpTPkNAAtttMwrIb%2B4xR57HLt2LCS%2BKnSVOUCPbYatY1kyur9TYtIAKBG6FVa8olVzG4vEihzmQD6qn5RaExMXXkzGRWU7DoQqeNamv7aTy3KVv54V34E1VB0ED0R%2FmhV7cT7Itax6UAkmnJcGc3HW&X-Amz-Signature=409e71b646805f9cdbd5655741e71375f5ff61d88598c08c334cc1eb92c44839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQKYKIAB%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmfS9GgseVSRUb0lcHgga%2BCmzklbKmWyANoFHCqY4MUAiEA%2B5ikimowOA%2BdvsL1%2BLzaeDE6o%2BpwG2cSfYG7xCNSzX0q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDNsVWSomX4kJ6On3ySrcA1DP5c3H%2FWJvQDvYzhS3exq%2FbolTKthhvHOmLmicL1JQZzc0NgXnDr9fjOkqu%2F4GG15dpTyp85CAfwOZY3i6iT9ErwEiwJDZlxM1TdxJaQvWSN0vHB3yYx%2FpUVCu%2FlDu0PIJgbbykpKj4EE547%2B0WKJwtmuf%2BHw6BCSiPOYMYtzj%2BIyQSpm5LGNV5f69KTjIFw%2Bv5X1agDFKHJM%2BIQU%2F1SN7J7t4RgqsdQg%2F2R5rsXyT0GaEZYEeVcg4QcFR5GLVPdGPVKRW3qrlbf0X3Bah95J5BavdlZNMI7CwnTHx3%2Fjte2ELUbWVUTeJP8RKiKVUgQzGmaHqqesorby3yM0juOUr1b4%2BYS8tlKLaYb2QUsjmjRNybo6YPgPFtf2wYG60RqYE1L%2FdVS143kKO%2Bc5cVJGB6DaMY%2BwREM2AadSvIp3S8aiuadS47xgYqAS2ytC7YlLwzTooMvIggx%2FgioNIRkZu11fIHyOQz6%2B9w772lMVf%2BTXyKOc6uMa8gRzBLZVEm%2FCyXaVLjwMvNpXjG9zbgEQ%2Bw2TlbN0fjod9%2BecY8jLszDk0M3Ortqp7akfDpz%2FmMOjmwTTTcdW8Am8LnhEMtP1ytf9%2F4MmzjRJPw27jae2CRXT6Tf1QteqpuM2wMM2yyM0GOqUB3MYeRolDAyZzMfwwSlfcTmagsxSAXzy%2BjmCMWJL6OBsTtCBnE0d9PkLdyEQe%2FHqFrVamwHHpTPkNAAtttMwrIb%2B4xR57HLt2LCS%2BKnSVOUCPbYatY1kyur9TYtIAKBG6FVa8olVzG4vEihzmQD6qn5RaExMXXkzGRWU7DoQqeNamv7aTy3KVv54V34E1VB0ED0R%2FmhV7cT7Itax6UAkmnJcGc3HW&X-Amz-Signature=e744cd15d9c2fe0bafbc11d092474a4ebf8da174cc66792b9783775fea211a45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQKYKIAB%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmfS9GgseVSRUb0lcHgga%2BCmzklbKmWyANoFHCqY4MUAiEA%2B5ikimowOA%2BdvsL1%2BLzaeDE6o%2BpwG2cSfYG7xCNSzX0q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDNsVWSomX4kJ6On3ySrcA1DP5c3H%2FWJvQDvYzhS3exq%2FbolTKthhvHOmLmicL1JQZzc0NgXnDr9fjOkqu%2F4GG15dpTyp85CAfwOZY3i6iT9ErwEiwJDZlxM1TdxJaQvWSN0vHB3yYx%2FpUVCu%2FlDu0PIJgbbykpKj4EE547%2B0WKJwtmuf%2BHw6BCSiPOYMYtzj%2BIyQSpm5LGNV5f69KTjIFw%2Bv5X1agDFKHJM%2BIQU%2F1SN7J7t4RgqsdQg%2F2R5rsXyT0GaEZYEeVcg4QcFR5GLVPdGPVKRW3qrlbf0X3Bah95J5BavdlZNMI7CwnTHx3%2Fjte2ELUbWVUTeJP8RKiKVUgQzGmaHqqesorby3yM0juOUr1b4%2BYS8tlKLaYb2QUsjmjRNybo6YPgPFtf2wYG60RqYE1L%2FdVS143kKO%2Bc5cVJGB6DaMY%2BwREM2AadSvIp3S8aiuadS47xgYqAS2ytC7YlLwzTooMvIggx%2FgioNIRkZu11fIHyOQz6%2B9w772lMVf%2BTXyKOc6uMa8gRzBLZVEm%2FCyXaVLjwMvNpXjG9zbgEQ%2Bw2TlbN0fjod9%2BecY8jLszDk0M3Ortqp7akfDpz%2FmMOjmwTTTcdW8Am8LnhEMtP1ytf9%2F4MmzjRJPw27jae2CRXT6Tf1QteqpuM2wMM2yyM0GOqUB3MYeRolDAyZzMfwwSlfcTmagsxSAXzy%2BjmCMWJL6OBsTtCBnE0d9PkLdyEQe%2FHqFrVamwHHpTPkNAAtttMwrIb%2B4xR57HLt2LCS%2BKnSVOUCPbYatY1kyur9TYtIAKBG6FVa8olVzG4vEihzmQD6qn5RaExMXXkzGRWU7DoQqeNamv7aTy3KVv54V34E1VB0ED0R%2FmhV7cT7Itax6UAkmnJcGc3HW&X-Amz-Signature=2a2f3a7013c222c4a746ec41e9683c44d5fb2d435953041637617869f7f46353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

