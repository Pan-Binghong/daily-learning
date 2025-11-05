---
title: 基于联通云AI算力平台训练Llama2-13B任务测试
date: '2024-11-26T07:43:00.000Z'
lastmod: '2025-05-15T06:39:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 自己记录一下。

---

## 一、准备环境

### 1. 创建Notebook1.创建Notebook

在创建Notebook时，根据以下选项进行配置：

- 付费类型：按量计费
- 名称：llama2
- 云区域：[保密]
- 算力规格：[保密]
- 镜像：公共镜像 jupyter:pytorch2.1.0-cann7
- 存储卷：AI原生存储
确认配置后点击“创建”，一段时间后Notebook创建完成，点击“打开”进入。

---

### 2. 安装依赖

### 2.1 下载代码和数据

- 打开终端，在当前用户根目录下执行以下命令来下载代码、权重和数据集：
1. 下载 git-lfs：
1. 安装 git-lfs：
在终端中执行以下命令安装所需依赖：

```shell
cd AscendSpeed
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
cd ..
cd ModelLink
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### 3. 创建Conda环境

将base环境拷贝为新的conda环境：

```shell
conda create -n test1 --clone bas
```

---

### 4. 打包新环境

- 进入新环境并激活：
- 安装 conda-pack：
- 打包新环境到文件夹：
---

### 5. 返回base环境并安装依赖

- 返回base环境并安装必要的依赖：
---

### 6. 处理数据集

- 进入 ModelLink 目录并编辑 dataset.sh 文件：
- 在文件中添加以下内容：
- 执行数据处理命令：
---

### 7. 创建训练脚本

- 在 examples/llama2/ 目录下创建训练脚本 pretrain_llama2_13B_ptd_8p_2.sh，内容如下：
- 创建 train_1.sh 脚本，内容如下：
---

## 二、创建训练任务

在提交任务时，选择以下配置：

- 任务名称：test
- 训练环境：预置镜像 PyTorch2.1.0 pytorch2.1.0-cann7
- 存储挂载：AI原生存储
- 云区域：[保密]
- 存储路径：[保密]
- 启动命令：
- 算力池：公共算力池
- 付费类型：按量计费
- 算力规格：[保密]
- 节点数量：2
确认配置后点击“提交”，等待任务创建完成。

