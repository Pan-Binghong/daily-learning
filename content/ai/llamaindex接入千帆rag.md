---
title: LlamaIndex接入千帆RAG
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- RAG
categories:
- AI
---

记录从使用Llama-index框架, 基于在线文心千帆大模型ERNIE-4.0, 构建实现本地知识检索.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EJ7NXFT%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfVaDbLleF%2BrMecMczt7UcFk%2FjjYC%2Fvv04Q6UqpAEQXAiEA%2FXyZ2itK4cx8w82svzTn2%2FLl%2BsmQfkdKClEvVG99WK8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BhD11B2qPBzSpb5yrcA5Wq%2BIMXn935oYwKa8lY%2BJSFF6ca8Roe1tyzC3rXUwGToJqp8urtcOdYCHwpE4f6qxguZzhJokZMoQvbrw9tsPIL8ESQXR9vBeoAA9yMFSy2IuFCxfoVlYgnS5w9bY0eEM88q7QC1gEtpCWcm%2BrB%2F4lPbJB8%2BPmzZicPL3OU5n9Q0rS01EWltvvQT7P33Olx%2FpU%2FgdiVs9ej0MKcY51GV1GqJqSRiDs%2BUqFkdzhOKbqfzXZ7a%2FzGs9rpJbLshubyQZzAUPNZluEqy2C4AV59zpx2sHfAHOBzOysoLDhz7OXGlpQzCw4%2FuhNiPl0Fuj4sfptkFkqXVjlDaA9mvlrBDim5ycdx0fztOZKte4MvF3Z0NtacWGsrpaUR%2F3DiQMVQJFxq2rKa8grivKvsge%2BMGxPbIYd%2BAjjSfb%2FQ0R1P%2BylACy3QEAbhmHAIoVsL654ibxpBkn7mQSVyEMoj7%2F4hkEuUfqPhQ9SUw8Hdf6TsmJv357BCW%2BkN0WxT8IVO%2FB0j1SXoR8SQNOwHycdrS4la3cW%2FU6TGN6F6qxv9jTiAgEmkgAiLleosT58BGdWM5La2KTmq5axoq5Qe%2BglK%2BEo9D94G48NIbfoii6%2FVALWDrBfYp64lB%2FQcY4Bt7eQPMMH5hssGOqUBBB77EREGKEXSvjWkG64q%2BUQbrkExBoOziLKO%2B1VzVsVdBD1YUtVH6ICw8QQJmEKxu%2F0QlkN%2BfFU55RcOqdNXo42QO3wYcyqLvCK%2Bii%2FdHlBQN0l09to2jqzTaAANA8Kgvuj318LUn0cd%2FnQas6FhgQ58ORpBk7mu3Yvg99phwBvY3yflL9xlqowBBFk5ufPay%2BbOot493MHTX%2F1R2mPuoxRmmFCT&X-Amz-Signature=44f21dc077e2c81e45a430445147e96684a521ec9617cbb9e85ab5f89403ae74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EJ7NXFT%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfVaDbLleF%2BrMecMczt7UcFk%2FjjYC%2Fvv04Q6UqpAEQXAiEA%2FXyZ2itK4cx8w82svzTn2%2FLl%2BsmQfkdKClEvVG99WK8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BhD11B2qPBzSpb5yrcA5Wq%2BIMXn935oYwKa8lY%2BJSFF6ca8Roe1tyzC3rXUwGToJqp8urtcOdYCHwpE4f6qxguZzhJokZMoQvbrw9tsPIL8ESQXR9vBeoAA9yMFSy2IuFCxfoVlYgnS5w9bY0eEM88q7QC1gEtpCWcm%2BrB%2F4lPbJB8%2BPmzZicPL3OU5n9Q0rS01EWltvvQT7P33Olx%2FpU%2FgdiVs9ej0MKcY51GV1GqJqSRiDs%2BUqFkdzhOKbqfzXZ7a%2FzGs9rpJbLshubyQZzAUPNZluEqy2C4AV59zpx2sHfAHOBzOysoLDhz7OXGlpQzCw4%2FuhNiPl0Fuj4sfptkFkqXVjlDaA9mvlrBDim5ycdx0fztOZKte4MvF3Z0NtacWGsrpaUR%2F3DiQMVQJFxq2rKa8grivKvsge%2BMGxPbIYd%2BAjjSfb%2FQ0R1P%2BylACy3QEAbhmHAIoVsL654ibxpBkn7mQSVyEMoj7%2F4hkEuUfqPhQ9SUw8Hdf6TsmJv357BCW%2BkN0WxT8IVO%2FB0j1SXoR8SQNOwHycdrS4la3cW%2FU6TGN6F6qxv9jTiAgEmkgAiLleosT58BGdWM5La2KTmq5axoq5Qe%2BglK%2BEo9D94G48NIbfoii6%2FVALWDrBfYp64lB%2FQcY4Bt7eQPMMH5hssGOqUBBB77EREGKEXSvjWkG64q%2BUQbrkExBoOziLKO%2B1VzVsVdBD1YUtVH6ICw8QQJmEKxu%2F0QlkN%2BfFU55RcOqdNXo42QO3wYcyqLvCK%2Bii%2FdHlBQN0l09to2jqzTaAANA8Kgvuj318LUn0cd%2FnQas6FhgQ58ORpBk7mu3Yvg99phwBvY3yflL9xlqowBBFk5ufPay%2BbOot493MHTX%2F1R2mPuoxRmmFCT&X-Amz-Signature=b08ec1a5a92a29a0e1307b9498ec295a3a2ae25b7805a42cd8771822c0fd3ddc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 导入本地Embedding

- 下载Embedding模型
```python
from modelscope import snapshot_download
model_dir = snapshot_download('Xorbits/bge-m3', cache_dir='/data/LLMs')
```

- 加载本地Embedding模型
```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
cache_folder = r"embed_model/m3e-large"embed_model = HuggingFaceEmbedding(cache_folder=cache_folder)
```

---

### 构建本地知识库

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
directory = "/data/documents" #文档路径vector_index = VectorStoreIndex.from_documents(documents)
```

---

### 构建查询引擎

```python
query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
```

> similarity_top_k可根据经验自行调整, 推荐设置3, 5.

---

### 构建RAG Agent

- 构建工具
```python
import os
def get_tool(name, full_name, documents=None):
    if not os.path.exists(f"./data/{name}"):
        # build vector index        vector_index = VectorStoreIndex.from_documents(documents)
        vector_index.storage_context.persist(persist_dir=f"./data/{name}")
    else:
        vector_index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=f"./data/{name}"),
        )
    query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=llm)
    query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name=name,
            description=(
                "Provides information about Uber quarterly financials ending"                f" {full_name}"            ),
        ),
    )
    return query_engine_tool
```

- 设置Agent
```python
from llama_index.core.agent import AgentRunner, ReActAgent
agent = ReActAgent.from_tools(
    query_engine_tools, llm=agent_llm, verbose=True, max_iterations=20)
```

- 运行
```python
response = agent.chat("您的问题")
```

### 整体代码

```python
from llama_index.core import Settings
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.qianfan import Qianfan
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# 初始化Qianfan模型class Rag:
    def __init__(self):
        self.access_key = ""        self.secret_key = ""        self.model_name = "ERNIE-4.0-8K-Latest"        self.url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"        self.llm = Qianfan(self.access_key, self.secret_key, self.model_name, self.url, context_window=8192)
        self.cache_folder = r"embed_model/m3e-large"        self.directory = r"/data/documents"  # 数据目录路径    def get_tool(self, name, full_name, documents=None):
        embed_model = HuggingFaceEmbedding(cache_folder=self.cache_folder)
        Settings.embed_model = embed_model
        vector_index = VectorStoreIndex.from_documents(documents)
        persist_path = f"{self.directory}/{name}"        if not os.path.exists(persist_path):
            vector_index.storage_context.persist(persist_dir=persist_path)
        query_engine = vector_index.as_query_engine(similarity_top_k=3, llm=self.llm)
        query_engine_tool = QueryEngineTool(query_engine=query_engine, metadata=ToolMetadata(name=name, description=f"Provides information from document {full_name}"))
        return query_engine_tool
    def parse_args(self):
        query_engine_tools = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.directory, filename)
                documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
                tool_name = filename[:-4]  # 去除'.txt'得到工具名称                tool = self.get_tool(tool_name, tool_name, documents=documents)
                query_engine_tools.append(tool)
        return query_engine_tools
    def query_engine(self, query):
        from llama_index.core.agent import ReActAgent
        tools = self.parse_args()
        agent = ReActAgent.from_tools(tools, llm=self.llm, verbose=True, max_iterations=20)
        response = agent.chat(query)
        return response
# 创建 Rag 实例并执行查询if __name__ == "__main__":
    rag = Rag()
    print(rag.query_engine(query="问题"))
```

> 参考链接

