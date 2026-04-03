---
title: GitLab CI/CD 入门教程：从零开始自动化你的代码流水线
date: '2026-04-03T05:57:00.000Z'
lastmod: '2026-04-03T06:00:00.000Z'
draft: false
tags:
- Git
- Docker
- CI/CD
categories:
- DevOps
---

当多人协作开发一个项目时，每次提交代码都需要手动跑测试、手动打包、手动部署——这不仅耗时，还容易出错。CI/CD 就是用来解决这个问题的：让这些重复的工作自动化完成。

## 1. 什么是 CI/CD？

CI（Continuous Integration，持续集成）：每次开发者推送代码，自动触发构建和测试，及时发现问题。

CD（Continuous Delivery/Deployment，持续交付/部署）：测试通过后，自动将代码部署到服务器，无需人工干预。

> 💡 一句话总结：你只管写代码 push，剩下的测试、打包、部署全由 GitLab 自动完成。

### CI/CD 的好处

- 减少手动操作失误，部署更可靠
- 问题更早暴露：每次提交就跑测试，不用等集成阶段才发现 Bug
- 发布更快：从提交到上线可以做到分钟级自动化
- 团队协作更顺畅：所有人遵循同一套自动化流程
---

## 2. GitLab CI/CD 核心概念

![](https://about.gitlab.com/images/blogimages/gitlab-flow-duo/The-GitLab-Flow-2023-mr-pushing-code-portion.png)

GitLab CI/CD 由以下几个核心概念组成，理解它们是使用的基础：

### Pipeline（流水线）

Pipeline 是整个自动化流程的总称。每次你 git push 时，GitLab 就会触发一条 Pipeline。你可以把它理解为一条「生产线」，代码在这条线上经历测试、构建、部署等步骤。

### Stage（阶段）

Pipeline 被分成多个 Stage，Stage 按顺序执行。常见的 Stage 包括：test（测试）、build（构建）、deploy（部署）。上一个 Stage 全部成功，才会进入下一个 Stage。

### Job（任务）

Job 是具体执行的单元，每个 Job 属于某个 Stage，定义了要运行的 Shell 命令。同一个 Stage 内的多个 Job 会并行执行。

### Runner（执行者）

Runner 是真正执行 Job 命令的机器（或容器）。GitLab 提供公共的 Shared Runner，你也可以在自己的服务器上注册私有 Runner。

> 💡 关系总结：一条 Pipeline 包含多个 Stage，每个 Stage 包含多个 Job，Job 由 Runner 负责执行。

---

## 3. .gitlab-ci.yml 文件详解

GitLab CI/CD 的一切配置都写在项目根目录的 .gitlab-ci.yml 文件中。当你 push 代码时，GitLab 自动读取这个文件并执行。

### 基本结构

```yaml
stages:         # 定义阶段顺序
  - test
  - build
  - deploy

job名称:        # 自定义 Job 名
  stage: test   # 属于哪个阶段
  image: python:3.11   # 使用哪个 Docker 镜像运行
  before_script:       # 执行命令前的准备工作
    - pip install -r requirements.txt
  script:              # 核心：要执行的命令
    - pytest tests/
  only:                # 触发条件：只在 main 分支时运行
    - main
```

> 💡 注意：缩进必须用空格，不能用 Tab，否则会解析失败。

### 常用关键字速查

```yaml
# 常用关键字速查

stages        # 定义所有阶段及顺序
stage         # 指定 Job 所属阶段
script        # Job 要执行的命令（必填）
image         # 指定运行环境的 Docker 镜像
before_script # 每个 Job 运行前执行的命令
after_script  # 每个 Job 运行后执行的命令
only/except   # 控制触发条件（分支、标签等）
rules         # 更灵活的触发条件控制（推荐替代 only）
variables     # 定义环境变量
artifacts     # 保存 Job 产出的文件（如测试报告）
cache         # 缓存目录，加速构建（如 node_modules）
needs         # 指定 Job 依赖关系，不等 Stage 顺序
```

---

## 4. 实战示例：Python Flask 应用自动测试 + 部署

下面用一个最简单的 Python Flask 应用来演示完整的 CI/CD 流程。场景是：每次推送代码，自动运行单元测试，测试通过后自动部署到服务器。

### 项目结构

```plain text
my-flask-app/
├── app.py              # Flask 应用主文件
├── test_app.py         # 单元测试
├── requirements.txt    # 依赖列表
└── .gitlab-ci.yml      # CI/CD 配置文件
```

### 应用代码（app.py）

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 单元测试（test_app.py）

```python
# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello' in resp.data

def test_add(client):
    resp = client.get('/add/3/4')
    assert resp.data == b'7'
```

### 依赖文件（requirements.txt）

```plain text
flask>=2.0
pytest>=7.0
```

### CI/CD 配置（.gitlab-ci.yml）

```yaml
# .gitlab-ci.yml

stages:
  - test      # 第一阶段：跑测试
  - deploy    # 第二阶段：部署

# ── 阶段一：自动测试 ──────────────────────
run-tests:
  stage: test
  image: python:3.11-slim       # 使用官方 Python 镜像
  before_script:
    - pip install -r requirements.txt   # 安装依赖
  script:
    - pytest test_app.py -v             # 运行测试，-v 显示详细输出
  only:
    - main          # 只在 main 分支触发
    - merge_requests  # 合并请求时也触发

# ── 阶段二：自动部署 ──────────────────────
deploy-production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client    # 安装 SSH 工具
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY" | ssh-add -  # 从变量读取私钥
    - mkdir -p ~/.ssh
    - ssh-keyscan $SERVER_IP >> ~/.ssh/known_hosts
  script:
    # SSH 到服务器，拉取最新代码并重启服务
    - ssh user@$SERVER_IP "
        cd /opt/my-flask-app &&
        git pull origin main &&
        pip install -r requirements.txt &&
        systemctl restart flask-app
      "
  only:
    - main    # 只有 main 分支的提交才触发部署
  when: on_success  # 只有前面的 Stage 全部成功才执行
```

### 流程图解

```plain text
# 完整流程说明：
# 
# 1. 开发者本地修改代码
# 2. git push origin main
# 3. GitLab 检测到 push，读取 .gitlab-ci.yml
# 4. 触发 Pipeline：
#    Stage1: test
#      └─ run-tests Job：
#         - 启动 python:3.11-slim 容器
#         - pip install -r requirements.txt
#         - pytest test_app.py  ← 如果有测试失败，Pipeline 中止！
#    Stage2: deploy（仅测试全部通过才执行）
#      └─ deploy-production Job：
#         - SSH 连接到生产服务器
#         - git pull 拉取最新代码
#         - systemctl restart flask-app 重启服务
# 5. 开发者在 GitLab 界面可以看到每个 Job 的日志
```

> 💡 部署阶段需要 SSH 密钥，切记不要把私钥直接写在 .gitlab-ci.yml 文件里！应该使用 GitLab 的 CI/CD Variables 功能来安全存储。

```yaml
# 在 GitLab 项目设置中配置（Settings → CI/CD → Variables）：
# SSH_PRIVATE_KEY  = 你的 SSH 私钥内容（设为 File 类型）
# SERVER_IP        = 你的服务器 IP 地址
#
# 这样敏感信息不会出现在代码里，安全！
```

---

## 5. 常用配置技巧

### ① 缓存依赖加速构建

```yaml
# 缓存 pip 依赖，避免每次都重新下载（加速构建）
run-tests:
  stage: test
  image: python:3.11-slim
  cache:
    key: "$CI_COMMIT_REF_SLUG"   # 按分支名缓存
    paths:
      - .cache/pip               # 缓存 pip 下载目录
  variables:
    PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  before_script:
    - pip install -r requirements.txt
  script:
    - pytest test_app.py -v
```

### ② 用 rules 精确控制触发条件

```yaml
# 用 rules 替代 only/except，更灵活
deploy-production:
  stage: deploy
  script:
    - echo "deploying..."
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'   # 只在 main 分支
      when: on_success                     # 且上一阶段成功
    - when: never                          # 其他情况不触发
```

### ③ 保存测试报告 artifacts

```yaml
# 保存测试报告，方便在 GitLab 界面查看
run-tests:
  stage: test
  script:
    - pytest test_app.py --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml      # GitLab 会解析并展示测试结果
    expire_in: 1 week        # 7 天后自动删除
```

### ④ 快速调试 Pipeline

- 在 GitLab 项目页面 → CI/CD → Pipelines 可以看到所有流水线记录
- 点进某个 Pipeline 可以看到每个 Job 的实时日志
- 失败的 Job 会标红并显示错误信息，方便定位问题
- 可以点击「重新运行」单独重跑某个 Job，不用全部重来
> 💡 建议：初次配置时先只写 test 阶段，确认 CI 跑通后再加 deploy 阶段。

---

## 6. 总结

配置 GitLab CI/CD 只需三步：

1. 在项目根目录创建 .gitlab-ci.yml 文件
1. 定义 stages 和 jobs，写好 script 命令
1. push 到 GitLab，Pipeline 自动触发
从最简单的自动测试开始，逐步加入构建和部署步骤。一旦 CI/CD 跑通，你会发现开发效率和代码质量都有明显提升。

> 💡 本文示例代码已包含完整可运行的 Flask 应用 + CI/CD 配置，可以直接复制到自己的项目中修改使用。

---

## References

1. [1] GitLab. GitLab CI/CD 官方文档. https://docs.gitlab.com/ee/ci/
1. [2] GitLab. .gitlab-ci.yml 关键字参考. https://docs.gitlab.com/ee/ci/yaml/
1. [3] GitLab. GitLab Runner 安装与注册. https://docs.gitlab.com/runner/install/
1. [4] GitLab. CI/CD Variables 安全变量使用. https://docs.gitlab.com/ee/ci/variables/
[https://docs.gitlab.com/ee/ci/](https://docs.gitlab.com/ee/ci/)

[https://docs.gitlab.com/ee/ci/yaml/](https://docs.gitlab.com/ee/ci/yaml/)

