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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GEDZCCI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpHiDxB9T2rpaJL5rLoU0%2BdxE249pPvlFdTeU6qdms4QIhAJaL6dUNN8V4fYyKqATEyJ2PIqfItF0u4kaXG8Qy%2B0vHKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ2bN4qKT9RYcGUOYq3ANeOwgyTb%2Fpx4V6lAck1TkrVsr%2F1%2BeE75LqkDfhAdlSoGCkFzQ4%2F8Ogr0jjeO4lhxl1z7htMEiaxbBH3o4gX9z%2BrTsyu1BfXCyDBljz0OMbM2ccmYtlH1%2BPDT8ZFWqVXkWieqgpUPH2nzJxFPUFZYCacI319OIgs8y0meE23vCV74yo3Ro9FYiJW39k3PaIbFETOQ4gYrib6PJkqWXqv8TVM3BSYBqZYE%2B2RYdJHJE3AMP7y78s9JMpGela8fjFJUZbQUc9BwQht24xi6vHmkX75XHk0EWmmwS58j5KrezdGs%2BsbqLmlvtLnAPLbh7mCE%2BQ0K6sRxco3bMb5%2BZV6rKjEFg6%2BIattKZvQi2bwhKMdluEO%2F4aTLSHjHDwixZaSPGqmE%2F2ZGDUXU3oPZvnDNVxj6YlYxwp5nsG1XZidoXVbMbsNAyM3rOBKCFdxCOqJowlbQb%2Fh7ZHZ3hB6iwXtrIZSXx%2Fbs%2FBmmHOiPzYmKyseNB9mQLt2M8joofhm3wFB%2FEIp7WHVCgHxCCZxrVhF82mkUMoo2ICpGG0JfpYUZ1pLoVuQiMlvK%2Big9XNKGbn2zbZtuAHz2Nk3C5Zk4hkACfon8vbCrx%2FZuP7C3V7pMGsJgdg%2BEHckVobzl7y9zDq0L3OBjqkAQLVcTIc7nXat%2BXrT%2Bbtx9t5HKqKzyWy%2FRms47lXrLw%2F1S0L1igd5WGKpPuVlC0gHF3cPaOY5935jjLg4WT26sp4UB8OQ7VdX3zLMt%2BIni1KPjql8WmdMTlhpWDJR%2B6G3%2FJj%2Fw5BXKG0YHmtjl7q%2BtyxLVyLfcndLO%2BNhKSGdLmPeMylM3jJIovu5nEH7xPDX9oL5sbJZoRNvd0SkvkWpH5HGZ0A&X-Amz-Signature=d5fbe76a4184fc56bfea86ac091b47686245c2871514445562da7741114fc9ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GEDZCCI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpHiDxB9T2rpaJL5rLoU0%2BdxE249pPvlFdTeU6qdms4QIhAJaL6dUNN8V4fYyKqATEyJ2PIqfItF0u4kaXG8Qy%2B0vHKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQ2bN4qKT9RYcGUOYq3ANeOwgyTb%2Fpx4V6lAck1TkrVsr%2F1%2BeE75LqkDfhAdlSoGCkFzQ4%2F8Ogr0jjeO4lhxl1z7htMEiaxbBH3o4gX9z%2BrTsyu1BfXCyDBljz0OMbM2ccmYtlH1%2BPDT8ZFWqVXkWieqgpUPH2nzJxFPUFZYCacI319OIgs8y0meE23vCV74yo3Ro9FYiJW39k3PaIbFETOQ4gYrib6PJkqWXqv8TVM3BSYBqZYE%2B2RYdJHJE3AMP7y78s9JMpGela8fjFJUZbQUc9BwQht24xi6vHmkX75XHk0EWmmwS58j5KrezdGs%2BsbqLmlvtLnAPLbh7mCE%2BQ0K6sRxco3bMb5%2BZV6rKjEFg6%2BIattKZvQi2bwhKMdluEO%2F4aTLSHjHDwixZaSPGqmE%2F2ZGDUXU3oPZvnDNVxj6YlYxwp5nsG1XZidoXVbMbsNAyM3rOBKCFdxCOqJowlbQb%2Fh7ZHZ3hB6iwXtrIZSXx%2Fbs%2FBmmHOiPzYmKyseNB9mQLt2M8joofhm3wFB%2FEIp7WHVCgHxCCZxrVhF82mkUMoo2ICpGG0JfpYUZ1pLoVuQiMlvK%2Big9XNKGbn2zbZtuAHz2Nk3C5Zk4hkACfon8vbCrx%2FZuP7C3V7pMGsJgdg%2BEHckVobzl7y9zDq0L3OBjqkAQLVcTIc7nXat%2BXrT%2Bbtx9t5HKqKzyWy%2FRms47lXrLw%2F1S0L1igd5WGKpPuVlC0gHF3cPaOY5935jjLg4WT26sp4UB8OQ7VdX3zLMt%2BIni1KPjql8WmdMTlhpWDJR%2B6G3%2FJj%2Fw5BXKG0YHmtjl7q%2BtyxLVyLfcndLO%2BNhKSGdLmPeMylM3jJIovu5nEH7xPDX9oL5sbJZoRNvd0SkvkWpH5HGZ0A&X-Amz-Signature=2a21b0d95bfc91a89942f2b3e7e3dec22a28dc4dbf8b705fabe48e18c10f7488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

