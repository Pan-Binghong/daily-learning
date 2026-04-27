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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2C7MHC2%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1DpU4Zt3DINAt77nfS%2B3vo%2BJY7i07IJYNaaVnEzoKlwIgbUY%2F8LWHH6YBjiKgRUCu9I4o4tSH9mdMDlkT5J5cYFwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2F4eiDseEYfN3I2mCrcA5cObf2lxKMoJ%2BqODUJtUkgZrjBtc7VZjyZz1K1pBVYzr%2BTZdUbEgYZdZOeP%2BjjtOyLCYTFTENjm1P1SGCDcZIDi908WBNdqzWG%2BZJQDv2TzUnFi2bvao7E%2B8yg4HvQO6Tu16qlpEPQKRNSerEBHX8VCGn%2B%2BfUT4QYh8TBWfrXD%2FrlIdZFwpELZ4JAsHQAvH70Se2cP25sWbXRtqZm9XMAvs14T1Uw4uNlcRWbMaOxyldApA1IhQT%2FuqZESEHlmiLOQ58gwnw9YEo3NwiDTdKLyFcE8nP83rsw%2BI8I48Kh7KFCQpARw4CJo7tsIYV%2BRlcrzYKkCNyrt3N4zOV9VyFB4mzBMFN3nO5GNeUpYMBD0QGAHGo4Zs8FtsisYML%2BTGhGgjthe2Z3e6nRpfXUYWJavPizPa5Ax8F9QUZcCtrDJu0HLM4ydBEIRxLJwVEvlxYr14iN3LzhFf133TXSncS79Vk5eZM8xKX7cn%2Fq7Y4DjYFguPcbsYqYjIMTQXvJWqK7tvacKErOXrfCn7aaT%2FJHMgOfEcqDJY%2Fl0cdqgrlo08IMYgVDxK9vTbnocWtCVmYfwfUSD3k1TswPVNr9Fa5gaSejcBiqC4SqbcRoVSS6D3xf2UmCDE2Hzc91A8MPq2u88GOqUB%2B4iYhAcb5E34vI0u8Vjnrw2FQ44Alpu6ilC2Nq6YaPIyC90rv4OfbB54Wz2DeLua7tZ2UWpJOCAYXZ5B4s5zRoIjaRNrN%2Fhisn3voli9LJHjBEZYUpnajtwvS1QxpO7Z5UqQUATTGj%2Fx5agfK%2Fk0c2tn2QjgfnTgsaNlEtJhPY2WPV0r2v%2BdUTCXRuiUKjQtsJS%2Fjr1QnK3QQXEqIx6r2v8%2F9tjY&X-Amz-Signature=edc09155f5b32f44ec936e6148afb27171e3d8acbc008f4a0f3b34fd67500d1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2C7MHC2%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1DpU4Zt3DINAt77nfS%2B3vo%2BJY7i07IJYNaaVnEzoKlwIgbUY%2F8LWHH6YBjiKgRUCu9I4o4tSH9mdMDlkT5J5cYFwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2F4eiDseEYfN3I2mCrcA5cObf2lxKMoJ%2BqODUJtUkgZrjBtc7VZjyZz1K1pBVYzr%2BTZdUbEgYZdZOeP%2BjjtOyLCYTFTENjm1P1SGCDcZIDi908WBNdqzWG%2BZJQDv2TzUnFi2bvao7E%2B8yg4HvQO6Tu16qlpEPQKRNSerEBHX8VCGn%2B%2BfUT4QYh8TBWfrXD%2FrlIdZFwpELZ4JAsHQAvH70Se2cP25sWbXRtqZm9XMAvs14T1Uw4uNlcRWbMaOxyldApA1IhQT%2FuqZESEHlmiLOQ58gwnw9YEo3NwiDTdKLyFcE8nP83rsw%2BI8I48Kh7KFCQpARw4CJo7tsIYV%2BRlcrzYKkCNyrt3N4zOV9VyFB4mzBMFN3nO5GNeUpYMBD0QGAHGo4Zs8FtsisYML%2BTGhGgjthe2Z3e6nRpfXUYWJavPizPa5Ax8F9QUZcCtrDJu0HLM4ydBEIRxLJwVEvlxYr14iN3LzhFf133TXSncS79Vk5eZM8xKX7cn%2Fq7Y4DjYFguPcbsYqYjIMTQXvJWqK7tvacKErOXrfCn7aaT%2FJHMgOfEcqDJY%2Fl0cdqgrlo08IMYgVDxK9vTbnocWtCVmYfwfUSD3k1TswPVNr9Fa5gaSejcBiqC4SqbcRoVSS6D3xf2UmCDE2Hzc91A8MPq2u88GOqUB%2B4iYhAcb5E34vI0u8Vjnrw2FQ44Alpu6ilC2Nq6YaPIyC90rv4OfbB54Wz2DeLua7tZ2UWpJOCAYXZ5B4s5zRoIjaRNrN%2Fhisn3voli9LJHjBEZYUpnajtwvS1QxpO7Z5UqQUATTGj%2Fx5agfK%2Fk0c2tn2QjgfnTgsaNlEtJhPY2WPV0r2v%2BdUTCXRuiUKjQtsJS%2Fjr1QnK3QQXEqIx6r2v8%2F9tjY&X-Amz-Signature=534b3b9aea032ddba2d09d3b94b7b236ea5e9fcfde00acb9c7aeb917ff04bfb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2C7MHC2%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1DpU4Zt3DINAt77nfS%2B3vo%2BJY7i07IJYNaaVnEzoKlwIgbUY%2F8LWHH6YBjiKgRUCu9I4o4tSH9mdMDlkT5J5cYFwqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2F4eiDseEYfN3I2mCrcA5cObf2lxKMoJ%2BqODUJtUkgZrjBtc7VZjyZz1K1pBVYzr%2BTZdUbEgYZdZOeP%2BjjtOyLCYTFTENjm1P1SGCDcZIDi908WBNdqzWG%2BZJQDv2TzUnFi2bvao7E%2B8yg4HvQO6Tu16qlpEPQKRNSerEBHX8VCGn%2B%2BfUT4QYh8TBWfrXD%2FrlIdZFwpELZ4JAsHQAvH70Se2cP25sWbXRtqZm9XMAvs14T1Uw4uNlcRWbMaOxyldApA1IhQT%2FuqZESEHlmiLOQ58gwnw9YEo3NwiDTdKLyFcE8nP83rsw%2BI8I48Kh7KFCQpARw4CJo7tsIYV%2BRlcrzYKkCNyrt3N4zOV9VyFB4mzBMFN3nO5GNeUpYMBD0QGAHGo4Zs8FtsisYML%2BTGhGgjthe2Z3e6nRpfXUYWJavPizPa5Ax8F9QUZcCtrDJu0HLM4ydBEIRxLJwVEvlxYr14iN3LzhFf133TXSncS79Vk5eZM8xKX7cn%2Fq7Y4DjYFguPcbsYqYjIMTQXvJWqK7tvacKErOXrfCn7aaT%2FJHMgOfEcqDJY%2Fl0cdqgrlo08IMYgVDxK9vTbnocWtCVmYfwfUSD3k1TswPVNr9Fa5gaSejcBiqC4SqbcRoVSS6D3xf2UmCDE2Hzc91A8MPq2u88GOqUB%2B4iYhAcb5E34vI0u8Vjnrw2FQ44Alpu6ilC2Nq6YaPIyC90rv4OfbB54Wz2DeLua7tZ2UWpJOCAYXZ5B4s5zRoIjaRNrN%2Fhisn3voli9LJHjBEZYUpnajtwvS1QxpO7Z5UqQUATTGj%2Fx5agfK%2Fk0c2tn2QjgfnTgsaNlEtJhPY2WPV0r2v%2BdUTCXRuiUKjQtsJS%2Fjr1QnK3QQXEqIx6r2v8%2F9tjY&X-Amz-Signature=0cf977787c02ee7d231f6c633ad38df482e01388dc293c5bfb74487b0096f746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

