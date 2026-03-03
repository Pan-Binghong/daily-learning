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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGPGTVZX%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsNJ3luium54ZQnf7RQLXr%2FMBmwz86vB12HEaYEBKg1wIgLUPX1JmAyA4TA%2FWAOmIBAI21Ig8ZfBiHm13VwsZ9EDUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBQPGAxMosI7%2BcJdzCrcA1SwfM9s7RCUv5HlWMUeij6kYneq7%2BH2cdWUZVHqp0caHyfthkGaBmSDgIwdyNNTIloM9hVUlW%2BHQdVjWgS9OoM4uXxQVgmYUJtC6to5M0PPNyl%2BGLmmhmW%2FnDFGACia3LNBRc99MwNkESclaUnrmJMNQmdp%2Bcph3TAkf6UDnGmAJIuoZJoznq%2BAcBeI40wnU6H7JQxraBWN4iOV3JulTpCeKvuh12yZtJscVWigNH980bocoW%2BV%2B0N4JQGsjQ66MDk8AtxEAJscClL3QZJO86pG6Lo1AdpDxuNVQyTD3WhTPDpbYzblsKKmfU1LQ8Ov8Qp8dB%2FOJ9d2jz0tVQYE%2Baf4aTio25WI62mr03yeh%2BbS4RYP%2FuDyDfGComJRfAbnLWcN8GlizJW8VST15%2BJHRLFHT371uJumqh0dlFZ%2B9hxQeeDPKnlH%2FJrEIBPq7p2QkpZgXaZRnkPzbwdaVSC33g1CIHm4zQV6NFXNw1pJcrutBdSOJ915g%2BlRv4DKAB3O2zT1eQoRj4Sir3NWHq4cBkqVQO2b7nXaHAUa2n95QHv5pzYyCDHu5DzrB66Y8F3gl6og9yU%2F0j59KNPo8Ha6OeBtz70O%2F6hM4Qgew%2Fm5067CCNcD5KjIlx%2Fxog4HMLK1mM0GOqUB0aWWHkrjxVKh5W9lozDCqrJX%2Bfz6pjm36bwcmyLwyon2JgvDH03xS3f9TRQhBPyg0%2FqtG1B5fMpyRFbk0zoawJQ1zQFewIWUtxQ48cEHuvQ1IF0IXSD3nxcjbe%2FIBj7qMn8iMX6tOs9GhLwrBYl%2FoqJWfcDKtHhkWWBTykKjGiY7WAHycC7bFqN8qssDfoXgjyV84JpAjNRKSsMvkkM77Ii2EmLZ&X-Amz-Signature=893f7c8081dd100fd64092e619f4ed801a11e1d2a8dd3666931297ba65b97adf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGPGTVZX%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsNJ3luium54ZQnf7RQLXr%2FMBmwz86vB12HEaYEBKg1wIgLUPX1JmAyA4TA%2FWAOmIBAI21Ig8ZfBiHm13VwsZ9EDUqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBQPGAxMosI7%2BcJdzCrcA1SwfM9s7RCUv5HlWMUeij6kYneq7%2BH2cdWUZVHqp0caHyfthkGaBmSDgIwdyNNTIloM9hVUlW%2BHQdVjWgS9OoM4uXxQVgmYUJtC6to5M0PPNyl%2BGLmmhmW%2FnDFGACia3LNBRc99MwNkESclaUnrmJMNQmdp%2Bcph3TAkf6UDnGmAJIuoZJoznq%2BAcBeI40wnU6H7JQxraBWN4iOV3JulTpCeKvuh12yZtJscVWigNH980bocoW%2BV%2B0N4JQGsjQ66MDk8AtxEAJscClL3QZJO86pG6Lo1AdpDxuNVQyTD3WhTPDpbYzblsKKmfU1LQ8Ov8Qp8dB%2FOJ9d2jz0tVQYE%2Baf4aTio25WI62mr03yeh%2BbS4RYP%2FuDyDfGComJRfAbnLWcN8GlizJW8VST15%2BJHRLFHT371uJumqh0dlFZ%2B9hxQeeDPKnlH%2FJrEIBPq7p2QkpZgXaZRnkPzbwdaVSC33g1CIHm4zQV6NFXNw1pJcrutBdSOJ915g%2BlRv4DKAB3O2zT1eQoRj4Sir3NWHq4cBkqVQO2b7nXaHAUa2n95QHv5pzYyCDHu5DzrB66Y8F3gl6og9yU%2F0j59KNPo8Ha6OeBtz70O%2F6hM4Qgew%2Fm5067CCNcD5KjIlx%2Fxog4HMLK1mM0GOqUB0aWWHkrjxVKh5W9lozDCqrJX%2Bfz6pjm36bwcmyLwyon2JgvDH03xS3f9TRQhBPyg0%2FqtG1B5fMpyRFbk0zoawJQ1zQFewIWUtxQ48cEHuvQ1IF0IXSD3nxcjbe%2FIBj7qMn8iMX6tOs9GhLwrBYl%2FoqJWfcDKtHhkWWBTykKjGiY7WAHycC7bFqN8qssDfoXgjyV84JpAjNRKSsMvkkM77Ii2EmLZ&X-Amz-Signature=d7cbb567f394d4d7bbb8b9d8e0c199dd812efb39dbc37a90904cbeb03a8d5c8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

