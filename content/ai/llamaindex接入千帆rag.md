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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZQGJOQJ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIBoDnKvqgGAp6gv983T389zHvTbukLWK8Cde%2ByMJlwxAAiEAhON75IqwoDLGqKjiidvnG7Q8lbn6gpnSosfX6oegnJ8q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDKmtqSpj6zSoUnu%2FmSrcA%2F0DZDyK9vLWXbVE9wfOTctS5K%2FbI86MH2hkJSkRRIyV6bEnS2mbjVfITUWiKEsSzHp7x0Zqd5r6TaL8NQfWKQ1xHBK0lMhsRIwzDCvwYN7gyTLBjWCUTgr2zWKauBX3jz9Hs%2F9CtnZNPRj7Xgrydz8LHi5aqisY5quIcRJ2PrR9C4bgcPhxZzNSyQHd%2FaE7d0Spr%2BdLJHyt%2BYLXQUIOO%2BhyNy2yt75Rqude6Jt4BtyJ6TGYzRHrX5YeobigaW3n0KFtg7vfPk9cyMGCbOFAli5AWMnooC962Txv8x9ieDXu2qtm1vIoHsZU82rWFcJuBqBJ0IaxqjkjglrdQOlvMeytNTT6cRO4hkRXyNGzzcJlMn6GJRlVi%2Biv5NPkw3Z9lWWaRYXOvfbKok%2Bu8aV%2BEEkZfBv%2Bputl5QgQeL7TgtOWYpHEEh3cFZiVXaDnaZX955F84ISiEb13ou%2BWhSg2X8qKKzkl7bjfKs3BfsKDdIJ4fGNY%2BzRKmXMq0fpAqMqQwdHhScn8GBmshklBPAEcthHVbgmlirNwi6oIwnEfEnbroxVaBpKsCYRBYFPoGVUwqB3828duQg15QhzfpzGwaQ5%2BZD5p5ovvaEP%2F8FqarKpGuAgozTY7hGFi7Ad1MIeTkMwGOqUBwddrRxhT4iI%2BIFeItmu%2FhiI1mOdGbZ1gwOxbpEn8YAv6B1xVRVz1NAN5R%2B7hrz0Mkfb9Hj296mM01rZhjkgd0iZrol6AfQyDZeK%2FQI4A1LNCID8liWpE3SrPSOEAJ0QnUBncTwQDgXX4W1A0gHHzvv9loUGR%2Bq%2BLhXi%2BeF33TFqOuFCL%2FLZWX%2FGsydP80iG0khoo4Xt9B%2F%2B2pFjP%2B5UKlI%2BjwkNn&X-Amz-Signature=cfde04ae3aafc1581fe96c024296a47d568bf7be922cede4a6e5bdd5d5a666b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZQGJOQJ%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIBoDnKvqgGAp6gv983T389zHvTbukLWK8Cde%2ByMJlwxAAiEAhON75IqwoDLGqKjiidvnG7Q8lbn6gpnSosfX6oegnJ8q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDKmtqSpj6zSoUnu%2FmSrcA%2F0DZDyK9vLWXbVE9wfOTctS5K%2FbI86MH2hkJSkRRIyV6bEnS2mbjVfITUWiKEsSzHp7x0Zqd5r6TaL8NQfWKQ1xHBK0lMhsRIwzDCvwYN7gyTLBjWCUTgr2zWKauBX3jz9Hs%2F9CtnZNPRj7Xgrydz8LHi5aqisY5quIcRJ2PrR9C4bgcPhxZzNSyQHd%2FaE7d0Spr%2BdLJHyt%2BYLXQUIOO%2BhyNy2yt75Rqude6Jt4BtyJ6TGYzRHrX5YeobigaW3n0KFtg7vfPk9cyMGCbOFAli5AWMnooC962Txv8x9ieDXu2qtm1vIoHsZU82rWFcJuBqBJ0IaxqjkjglrdQOlvMeytNTT6cRO4hkRXyNGzzcJlMn6GJRlVi%2Biv5NPkw3Z9lWWaRYXOvfbKok%2Bu8aV%2BEEkZfBv%2Bputl5QgQeL7TgtOWYpHEEh3cFZiVXaDnaZX955F84ISiEb13ou%2BWhSg2X8qKKzkl7bjfKs3BfsKDdIJ4fGNY%2BzRKmXMq0fpAqMqQwdHhScn8GBmshklBPAEcthHVbgmlirNwi6oIwnEfEnbroxVaBpKsCYRBYFPoGVUwqB3828duQg15QhzfpzGwaQ5%2BZD5p5ovvaEP%2F8FqarKpGuAgozTY7hGFi7Ad1MIeTkMwGOqUBwddrRxhT4iI%2BIFeItmu%2FhiI1mOdGbZ1gwOxbpEn8YAv6B1xVRVz1NAN5R%2B7hrz0Mkfb9Hj296mM01rZhjkgd0iZrol6AfQyDZeK%2FQI4A1LNCID8liWpE3SrPSOEAJ0QnUBncTwQDgXX4W1A0gHHzvv9loUGR%2Bq%2BLhXi%2BeF33TFqOuFCL%2FLZWX%2FGsydP80iG0khoo4Xt9B%2F%2B2pFjP%2B5UKlI%2BjwkNn&X-Amz-Signature=716d60a0484014edb1a5a1d40318b862df717b5405f24ce29cdb1358869432bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

