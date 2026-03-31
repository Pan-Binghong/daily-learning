---
title: 使用 langchain-aws 调用 AWS Bedrock 模型完整指南
date: '2026-03-30T08:27:00.000Z'
lastmod: '2026-03-31T01:39:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

# 1. 核心概念：按量付费 vs 推理配置文件

在写代码之前，必须先搞清楚这两种调用方式的区别，这是导致模型 ID 写法不同的根本原因。

## 1.1 按量付费（On-Demand）

> 💡 直接使用模型，按实际 Token 数量计费，无需预约容量。

- 模型 ID 格式：短 ID，如 anthropic.claude-3-5-sonnet-20240620-v1:0
- 调用的是单一固定区域的模型
- 适合：开发测试、低频调用、不确定用量时
```plain text
# 按量付费模型 ID 举例
anthropic.claude-3-5-sonnet-20240620-v1:0
anthropic.claude-3-haiku-20240307-v1:0
amazon.nova-pro-v1:0
deepseek.r1-v1:0
```

## 1.2 推理配置文件（Inference Profile）

推理配置文件分两种，这是很多人混淦的地方：

### (A) 系统定义推理配置文件（System-defined Inference Profile）

> 💡 AWS 官方预设，自动跨区域路由，提高可用性。

- 模型 ID 格式：在短 ID 前加区域前缀，如 us.、eu.、ap.
- AWS 帮你在多个区域之间自动负载均衡，不需要 Account ID，不是 ARN
- 适合：生产环境首选、需要高可用、怕单区域限速时
```plain text
# 系统定义推理配置文件 ID
us.anthropic.claude-3-5-sonnet-20241022-v2:0    # 美区跨 region 路由
eu.anthropic.claude-3-5-sonnet-20241022-v2:0    # 欧区
us.deepseek.r1-v1:0
us.amazon.nova-pro-v1:0
```

### (B) 应用推理配置文件（Application Inference Profile）

> 💡 用户在 AWS 控制台自己创建的，可以自定义路由规则。

- 模型 ID 格式：完整 ARN，包含你的 Account ID（这就是你现在 .env 里写的那种长 ARN）
```plain text
# 应用推理配置文件 ARN
arn:aws:bedrock:us-east-1:871720422414:inference-profile/us.deepseek.r1-v1:0
arn:aws:bedrock:us-east-1:871720422414:inference-profile/us.anthropic.claude-sonnet-4-5-20250929-v1:0
```

## 1.3 三种方式对比

---

![](https://images.pexels.com/photos/4508751/pexels-photo-4508751.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

# 2. .env 文件应该怎么写

## 2.1 推荐方案：系统定义推理配置文件（短 ID）

不需要自己创建应用推理配置文件，直接用带前缀的短 ID，既有跨区域能力又干净。

```shell
# .env 文件

# AWS 凭证
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=us-east-1

# 模型配置（系统定义推理配置文件，短 ID）
BEDROCK_MODEL_ID=us.anthropic.claude-3-5-sonnet-20241022-v2:0

# 多模型配置
BEDROCK_CLAUDE_MODEL_ID=us.anthropic.claude-3-5-sonnet-20241022-v2:0
BEDROCK_DEEPSEEK_MODEL_ID=us.deepseek.r1-v1:0
BEDROCK_NOVA_MODEL_ID=us.amazon.nova-pro-v1:0
```

## 2.2 你的 .env 可以改成这样（对照）

```shell
# 之前（长 ARN）
DEEPSEEK_INFERENCE_PROFILE_ARN=arn:aws:bedrock:us-east-1:871720422414:inference-profile/us.deepseek.r1-v1:0
CLAUDE_INFERENCE_PROFILE_ARN=arn:aws:bedrock:us-east-1:871720422414:inference-profile/us.anthropic.claude-sonnet-4-5-20250929-v1:0

# 现在（系统定义推理配置文件短 ID，效果完全一样）
BEDROCK_DEEPSEEK_MODEL_ID=us.deepseek.r1-v1:0
BEDROCK_CLAUDE_MODEL_ID=us.anthropic.claude-sonnet-4-5-20250929-v1:0
```

> 💡 ChatBedrock 的 model 参数可以接受短 ID、带前缀的短 ID、完整 ARN，三种都行。

---

# 3. 安装依赖

```shell
pip install langchain-aws python-dotenv
```

---

# 4. 代码示例

## 4.1 基础用法

```python
import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock

load_dotenv()

llm = ChatBedrock(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

response = llm.invoke("你好，请介绍一下你自己")
print(response.content)
```

## 4.2 带参数配置（推荐）

```python
import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatBedrock(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    temperature=0.7,
    max_tokens=2048,
)

messages = [
    SystemMessage(content="你是一个专业的助手。"),
    HumanMessage(content="用 Python 写一个冒泡排序"),
]

response = llm.invoke(messages)
print(response.content)
```

## 4.3 流式输出

```python
import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock

load_dotenv()

llm = ChatBedrock(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    streaming=True,
)

for chunk in llm.stream("请解释一下量子纠缠"):
    print(chunk.content, end="", flush=True)
```

## 4.4 Prompt Template + Chain

```python
import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatBedrock(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}。"),
    ("human", "{question}"),
])

chain = prompt | llm

response = chain.invoke({
    "role": "资深 Python 工程师",
    "question": "什么时候应该用生成器而不是列表？",
})
print(response.content)
```

---

![](https://images.pexels.com/photos/10816120/pexels-photo-10816120.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

# 5. 用 AWS CLI 查询模型 ID

> 💡 所有模型 ID 都可以直接从 CLI 查，不需要去猜或去文档里翻。

## 5.1 查询所有基础模型（按量付费 ID）

```shell
aws bedrock list-foundation-models \
  --region us-east-1 \
  --query "sort_by(modelSummaries[?modelLifecycle.status=='ACTIVE'], &providerName)[*].[providerName,modelId]" \
  --output table
```

只过滤某个厂商（例如 Anthropic）：

```shell
aws bedrock list-foundation-models \
  --region us-east-1 \
  --by-provider Anthropic \
  --query "modelSummaries[?modelLifecycle.status=='ACTIVE'].[modelId,modelName]" \
  --output table
```

## 5.2 查询系统定义推理配置文件（带 us. 前缀的短 ID）

```shell
aws bedrock list-inference-profiles \
  --region us-east-1 \
  --type-equals SYSTEM_DEFINED \
  --query "inferenceProfileSummaries[*].[inferenceProfileId,inferenceProfileName,status]" \
  --output table
```

## 5.3 查询你自己创建的应用推理配置文件（ARN）

```shell
aws bedrock list-inference-profiles \
  --region us-east-1 \
  --type-equals APPLICATION \
  --query "inferenceProfileSummaries[*].[inferenceProfileId,inferenceProfileArn,inferenceProfileName]" \
  --output table
```

## 5.4 查单个模型详细信息

```shell
aws bedrock get-inference-profile \
  --region us-east-1 \
  --inference-profile-identifier us.deepseek.r1-v1:0
```

## 5.5 实用过滤技巧

```shell
# 只查文本模型
aws bedrock list-foundation-models --region us-east-1 \
  --by-output-modality TEXT --by-input-modality TEXT \
  --query "sort_by(modelSummaries[?modelLifecycle.status=='ACTIVE'], &providerName)[*].[providerName,modelId]" \
  --output table

# 过滤关键字（找 claude 的推理配置文件）
aws bedrock list-inference-profiles --region us-east-1 \
  --type-equals SYSTEM_DEFINED \
  --query "inferenceProfileSummaries[*].inferenceProfileId" \
  --output text | tr '\t' '\n' | grep claude
```

---

![](https://images.pexels.com/photos/5480781/pexels-photo-5480781.jpeg?auto=compress&cs=tinysrgb&fit=crop&h=627&w=1200)

# 6. 常用模型 ID 速查表（你的账号实际数据）

## Claude 系列（Anthropic）

## DeepSeek 系列

## Amazon Nova 系列

---

# 7. 常见报错

## AccessDeniedException

模型没有开通访问权限。去 AWS 控制台 → Bedrock → Model Access，申请开通对应模型。

## ValidationException: The provided model identifier is invalid

- 检查模型 ID 拼写是否正确
- 确认模型在 AWS_DEFAULT_REGION 这个区域可用
- 使用系统定义推理配置文件（us. 前缀）时，region_name 必须是 us-east-1 或 us-west-2
## botocore.exceptions.NoCredentialsError

确认 .env 已加载，检查 AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY 是否填写正确。

---

# 8. 推荐项目结构

```plain text
my_project/
├── .env              # 环境变量（不要提交到 git）
├── .env.example      # 示例文件（提交到 git）
├── main.py
└── requirements.txt
```

```shell
# .env.example
AWS_ACCESS_KEY_ID=your_access_key_id_here
AWS_SECRET_ACCESS_KEY=your_secret_access_key_here
AWS_DEFAULT_REGION=us-east-1

# 按量付费：anthropic.claude-3-5-sonnet-20241022-v2:0
# 系统定义推理配置文件（推荐）：us.anthropic.claude-3-5-sonnet-20241022-v2:0
# 应用推理配置文件 ARN：arn:aws:bedrock:us-east-1:123456789012:inference-profile/us.xxx
BEDROCK_MODEL_ID=us.anthropic.claude-3-5-sonnet-20241022-v2:0
```

---

# 参考文献

---

[https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

[https://github.com/langchain-ai/langchain-aws](https://github.com/langchain-ai/langchain-aws)

[https://python.langchain.com/docs/integrations/chat/bedrock/](https://python.langchain.com/docs/integrations/chat/bedrock/)

[https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)

[https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)

[https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)

