---
title: Ubuntu安装监控系统可视化模块
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
tags:
- Linux
- Ubuntu
categories:
- DevOps
---

Prometheus是一个开放性的监控解决方案，用户可以非常方便的安装和使用Prometheus并且能够非常方便的对其进行扩展。为了能够更加直观的了解Prometheus Server，接下来我们将在本地部署并运行一个Prometheus Server实例，通过Node Exporter采集当前主机的系统资源使用情况。 并通过Grafana创建一个简单的可视化仪表盘。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/daebfb90-2a3b-47c1-95ce-3e1e8b208b83/%E7%9B%91%E6%8E%A7-1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=22209f26f38dac087397b7a60da8c7f690c155cea3579614eadda70fe3ba7096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> Prometheus是什么？

### 下载Prometheus

- 下载链接
### 安装Prometheus

- 解压
### 修改Prometheus配置

- 进入文件目标, 并修改配置
- 将以下内容放置在配置文件内
- 启动服务
### 在web浏览器查看

- localhost:9090
---

> Monitoring Linux host metrics with the Node Exporter

### 下载Node Exporter

- 下载地址
### 安装 & RUN

```shell
tar xvfz node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
./node_exporter
```

### 在web浏览器查看

- http://localhost:9100/
---

> What is Grafana

### 安装Grafana

### Ubuntu安装流程

```shell
# 更新apt-getsudo apt-get install -y adduser libfontconfig1 musl
# 下载软件wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.0.0_amd64.deb
# 安装sudo dpkg -i grafana-enterprise_10.0.0_amd64.deb
```

- 操作系统不是Ubuntu则查看上面的链接, 根据自身系统进行安装
### RUN Grafana

- 运行Grafana可视化服务
```shell
sudo /bin/systemctl start grafana-server
```

### 在web浏览器查看

- http://localhost:3000/
- 设置流程如下:
step-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/19c196f7-552f-4d8d-b491-6ceeee1bb2a7/%E7%9B%91%E6%8E%A7-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=843a483091f21ec18fb156e7c03f85cb09bbb906338d6f4c973e88197d513771&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/07ae8937-e8e8-4d89-a54d-680f40d408ed/%E7%9B%91%E6%8E%A7-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=f8a413f90797d88eb93e97feb11a2f2a61e94307fbbd04629b154400631d03fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-3

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2763c119-8749-49d0-b97c-75667347b7b9/%E7%9B%91%E6%8E%A7-4.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=5d74792e4eefb29f9d57c9a1638f8f547d6d42897aa4bf2ce164d098403daf6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-4

- 之后新建Dashboards, 选择上面新增的 DataSrouce, 按需选择可视化的Query即可
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3ac7ab14-6c65-4ecd-bcb8-262c9732fba0/%E7%9B%91%E6%8E%A7-5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=b7e1a2e4f8f5e6e21db0074df4be1cbf7c2e9f55964c055dc120dd66b62ca57f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

step-5

### 导入仪表盘

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fdafea45-3615-4b74-b303-664ee8e5348c/%E7%9B%91%E6%8E%A7-7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=463313c474e4db5e1b556a57a937e4e6cc5de254e98fdf4e4cad11e3051d2c4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

链接

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4552e150-7d7d-4cb1-807e-4bd1e70323d6/%E7%9B%91%E6%8E%A7-8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC72SBZY%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEOOh2NcZ%2BHVi0fy26KlSFcD9R982RKTxgh%2BXFH1XTQAiEAmg%2FR7seqbOLeIFERuQXel0T0%2Fb1BI9e1xFDgk5ZiXaMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEWmTx2c0uJUfcY7gSrcA%2FdKkg4VhL%2BaZNyK35EvRQ8cYCaTtBOKY58GZsVt3KNJMfzH2BGwqWrLKOt%2BDD0fSlmO39fPBtYLccwj5WTCCH40zxqPaw5TZxvz%2FFVRmAcmPvpqYzf70Ar5RwDz%2BxJW9VDxfK71CPqNKNDDu0q9ku6HEJPY9e1NaN4vmMROqqrFyJXtfhoZnMAmw3kLNssqQECriOyfuHbRLjZNl9Uf6ZR%2FJ7vOxVX6fM4xiAqHhT%2B2oAXT6M2Ew7X1jUmXLTjpb0YTQp84GhZir%2BcoEC2VQx8zQIgy1%2F6chm4Uh1eyL6eYc3HfvODKbGRYkzay%2Bn3S5IM3bNOTLkWgLBSlac7hW5YmmjxaTrvxMz%2FIWUvZ%2FeTasu9ckZ9dZHdxLw0F7pPOJ4lF3MOn8nX0hJf54%2FtB%2FknyvF25gQ13AWku3UfGQWdTpSzGPEm2DQMIkIwbIkERMVY1ZMa%2BqPE1WuJHnbAjtAfWYqNQ%2BQMYzDGXS%2BVLYzN26IU%2B%2FsKS75MIIEzrvNBRiZiqtDnlhhjB6ycTc7FBTfTy%2FgpIg4DP358ycaLilB%2BBG%2BbxPowIdeHInfLzIW3O1qUAn634xonPKnGXyZvEiXGfvzg62gHWoJ3xrh5ko6ah9T3NjtGp69EFPup0MKXkgs4GOqUBH62vbRUSwJ2mBip7qOJmutE9r6GHp08a4a1C3DcQPrU4Fv1zzvWmfqhYbPKsRIc9QkLdOWHlINvVSqqPp%2B5I%2FFu9Ajolp90Ay99zggFiRauCcQNWm8aclRgu9FvPi9rvMISnzHIByFWmJwWxz7B%2BZYBM49R6iV%2Bu%2Fu9Gea%2FQDHF%2FBYGbJ58%2BjvyyOF0eLk7g121Yj%2BIo4vo8DN1YxI7AHp3eAzd4&X-Amz-Signature=4a577cce6a8e1be9a09d73b1379de17387660c9d0c350a5ff1423ebbffb525ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 参考链接

### 拓展代码

- 安装Prometheus
```shell
# 下载export VERSION=2.13.0
curl -LO  https://github.com/prometheus/prometheus/releases/download/v$VERSION/prometheus-$VERSION.darwin-amd64.tar.gz
# 解压tar -xzf prometheus-${VERSION}.darwin-amd64.tar.gz
cd prometheus-${VERSION}.darwin-amd64
# 配置promethes.ymlvim promethes.yml
# 运行./prometheus
```

- 安装Node Exporter
```shell
# 下载curl -OL https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
# 解压tar -xzf node_exporter-0.17.0.linux-amd64.tar.gz
# 将 node_exporter 工具安装到系统中，使其可以被全局访问和使用。cd node_exporter-0.17.0.linux-amd64/
mv node_exporter /usr/local/bin/
# 运行service node_exporter start
```

