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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTFG6MB%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIHUc9qb7%2B3qTqywh6xfLSKmr8ddtSnstpRWjAPV6IwWGAiEAhFGV1tzgRfJsTB1vcHDEDZwWKAU2eHlCTxXtYagocq0qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoP4kLLGq7oCu%2FwFyrcA7%2BJ4W0k8VRIH2JoIpJNpPdUizJW51w3faE3fSrwFEo8bxA7hIYjC1vQQzvumpEm%2BD4dNXoyPcGycVDBuKVon4za1q5BSw6UBr8KbQG8NK0to45A1C%2FJFZGkuraiImJixJwjOo1TVmpysPIy%2BJSvoa64G%2FKEiLWuzoE5SVzSm%2B%2FWqGRct0KYHCoEbnRCUkWvw6p8zpK4z1izBgZuc1DNpz8MTBW1y8upaPutCLm2XlKfr%2BwdECY2gZib7qr9zwYlQGFbyzLvoxwyfBw1jdQ6lI7Dk6BFIgE4s5FD4E7RQtad%2BhaykdriNSKxWEvV1N102T4JIBrag6fIVNWXIgNAJ8zH%2BCSUQcP7jp7p%2FLKOM4bEYas84UeEWnwRlQnIP%2BVfKXhVDWaq2vTs9kkBrLb65HVWuXOEi3rezHmqHH%2Fdzh3Ll5UWKJQaFixYnSlDFfTw6RLGDR93uACzgzR%2FiHxP2Nv2MZyY2STxik3qEx%2FMWduvqWtlLn0xEn0PYwiBkqRG1%2Fnvnu4d0aR%2Fu7y21v61sWW5xFmE8hvoDxkeCaoC%2FYexTq0ClNRjgfIH%2BZZqsxzHOk1ZG7f29u%2BzIeqrN9k6%2BfMpDKBm1yWocT0Yz7K4HogAgCl3%2Biky2fNcWfQcMMb2sskGOqUByszWIM1lM9O1vdln1Bn5LE8Sq591yPixXAjjoxnLnGwE%2FGe9T1Rb5Uxeq3EhGAm5q7WFmazjelakjb3At2lw1J5%2FOcGlh%2B%2BIg%2F488uC%2FsCmuqT%2B%2FGoFNO5wBjVW4DzFhkCOJrwO0dgcWthYE2wfISWK7LFZvolh%2FS%2B%2FGUFjepfJ44MRJ%2FxhlVTj9biJ%2BNrRVX0lzBGNjAx8AVCpksL%2BoIGBM7ojc&X-Amz-Signature=6359c5475ed8e4201e13339cc7c28e18954b5a74c595ea4552504223a5930197&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTFG6MB%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIHUc9qb7%2B3qTqywh6xfLSKmr8ddtSnstpRWjAPV6IwWGAiEAhFGV1tzgRfJsTB1vcHDEDZwWKAU2eHlCTxXtYagocq0qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBoP4kLLGq7oCu%2FwFyrcA7%2BJ4W0k8VRIH2JoIpJNpPdUizJW51w3faE3fSrwFEo8bxA7hIYjC1vQQzvumpEm%2BD4dNXoyPcGycVDBuKVon4za1q5BSw6UBr8KbQG8NK0to45A1C%2FJFZGkuraiImJixJwjOo1TVmpysPIy%2BJSvoa64G%2FKEiLWuzoE5SVzSm%2B%2FWqGRct0KYHCoEbnRCUkWvw6p8zpK4z1izBgZuc1DNpz8MTBW1y8upaPutCLm2XlKfr%2BwdECY2gZib7qr9zwYlQGFbyzLvoxwyfBw1jdQ6lI7Dk6BFIgE4s5FD4E7RQtad%2BhaykdriNSKxWEvV1N102T4JIBrag6fIVNWXIgNAJ8zH%2BCSUQcP7jp7p%2FLKOM4bEYas84UeEWnwRlQnIP%2BVfKXhVDWaq2vTs9kkBrLb65HVWuXOEi3rezHmqHH%2Fdzh3Ll5UWKJQaFixYnSlDFfTw6RLGDR93uACzgzR%2FiHxP2Nv2MZyY2STxik3qEx%2FMWduvqWtlLn0xEn0PYwiBkqRG1%2Fnvnu4d0aR%2Fu7y21v61sWW5xFmE8hvoDxkeCaoC%2FYexTq0ClNRjgfIH%2BZZqsxzHOk1ZG7f29u%2BzIeqrN9k6%2BfMpDKBm1yWocT0Yz7K4HogAgCl3%2Biky2fNcWfQcMMb2sskGOqUByszWIM1lM9O1vdln1Bn5LE8Sq591yPixXAjjoxnLnGwE%2FGe9T1Rb5Uxeq3EhGAm5q7WFmazjelakjb3At2lw1J5%2FOcGlh%2B%2BIg%2F488uC%2FsCmuqT%2B%2FGoFNO5wBjVW4DzFhkCOJrwO0dgcWthYE2wfISWK7LFZvolh%2FS%2B%2FGUFjepfJ44MRJ%2FxhlVTj9biJ%2BNrRVX0lzBGNjAx8AVCpksL%2BoIGBM7ojc&X-Amz-Signature=4eac466e655a410eeb67a071c33da6ce46ca3d69236f2079bb75783c7d1a8a5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

