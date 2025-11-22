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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/1f73f1b2-0e9d-4fdf-9a59-00189860a2f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667D5VXUL%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIGjhWLgKapHonGJcreQzvhn7f8g7zxnE56SOyX7JPe0mAiBaKr5ay6xUB1B3EystIVKT%2BZgiIBph0NnuUvn5YE1mtCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIM6vzhykPPN%2BWS5f0JKtwDsaD1wZB3kftABOcARipPsUuBr%2FaJp2ZmL2FNI1%2FxaJNV1DFliF%2B%2BAoWJsDHuTzaVNCtlO4enRbPfWLhQI9Orsse9YkQtb3SogRhydk7%2F5kEBBfcYJVArKUY9QDRzeVvJ2xQEKn3wCcMLMIU%2BczdCwHJ5xc%2BeS1UzZRQz1jEcs4rvy62Kai7JbBSl9O4LwUI1ixlxj%2Bx5W5jahR1TtljCRTOFNlhJ94oVhLqcHlJi9a3IsPjMga3izDw%2F8H1lYdqlkuv9OH6ZIkjgkskJUrlhO5rX3H%2FzWCY5xvqVGcDhhNERSJbyIYgKcjnwl3fjsPemhWKx9rEH40Asiq6DnitnO52%2BQyz6usPOlHGho6%2FCEkHhg2p3mlIse5dFBTR3bW%2BPix3VA4iryAtGHozV3aT0D%2FyVeDkfqWjpVOh%2F%2Bha42LORbUFu%2FbUfkm3uFWfiD%2F3bI7u2i3%2Buho%2FITU2nTdC0M41y96TxYlau5qaxw7c%2BuVubqWktX9gnYbN%2BGJy%2F%2FukQUU4BFPgQ7wSKf0TqFeL2Yx9He%2B9NTf26nvVOtx5V8s1DNnmxK9ANf06gbij%2BaXepAnwu16qhwNhvGvOrq2%2BLRwIT8pr99LOHTcK7kBO%2B0UKeiZpHL1LJmiL4akYwwKGEyQY6pgGckdcLdEf493YW023AOeFRW01SI%2FRDD9pBEMbSycEJNmd8nWmS6hgnKySsZ%2B0G4vbBVZBb1aCS5UPQ%2BLofZ6Q3%2FGh3m7nzSYqqCKY4c41y77XuUOL%2FjXw%2BKtZA4HH%2F8xlSk5SKBTn%2FY7XhkCouTBS%2B33zAxqQIdHMDftshfYZTljPVSk2qdyGbaqZwoID73%2Ffr%2BRy%2BNbsb2YuLL4D%2BKzauA9vNkOCG&X-Amz-Signature=85f9cf4391e97199454dd52e3223e2000685014cda24149f9a4c26deb374c227&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 导入大模型

```python
from llama_index.llms.qianfan import Qianfan
access_key = ""secret_key = ""model_name = "ERNIE-4.0-8K-Latest"url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro"llm = Qianfan(access_key, secret_key, model_name, url, context_window=8192)
```

> model_name可在千帆平台查看, 如下图:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ec53fa42-9c7c-4b3b-b334-810c76b293ae/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667D5VXUL%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIGjhWLgKapHonGJcreQzvhn7f8g7zxnE56SOyX7JPe0mAiBaKr5ay6xUB1B3EystIVKT%2BZgiIBph0NnuUvn5YE1mtCr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIM6vzhykPPN%2BWS5f0JKtwDsaD1wZB3kftABOcARipPsUuBr%2FaJp2ZmL2FNI1%2FxaJNV1DFliF%2B%2BAoWJsDHuTzaVNCtlO4enRbPfWLhQI9Orsse9YkQtb3SogRhydk7%2F5kEBBfcYJVArKUY9QDRzeVvJ2xQEKn3wCcMLMIU%2BczdCwHJ5xc%2BeS1UzZRQz1jEcs4rvy62Kai7JbBSl9O4LwUI1ixlxj%2Bx5W5jahR1TtljCRTOFNlhJ94oVhLqcHlJi9a3IsPjMga3izDw%2F8H1lYdqlkuv9OH6ZIkjgkskJUrlhO5rX3H%2FzWCY5xvqVGcDhhNERSJbyIYgKcjnwl3fjsPemhWKx9rEH40Asiq6DnitnO52%2BQyz6usPOlHGho6%2FCEkHhg2p3mlIse5dFBTR3bW%2BPix3VA4iryAtGHozV3aT0D%2FyVeDkfqWjpVOh%2F%2Bha42LORbUFu%2FbUfkm3uFWfiD%2F3bI7u2i3%2Buho%2FITU2nTdC0M41y96TxYlau5qaxw7c%2BuVubqWktX9gnYbN%2BGJy%2F%2FukQUU4BFPgQ7wSKf0TqFeL2Yx9He%2B9NTf26nvVOtx5V8s1DNnmxK9ANf06gbij%2BaXepAnwu16qhwNhvGvOrq2%2BLRwIT8pr99LOHTcK7kBO%2B0UKeiZpHL1LJmiL4akYwwKGEyQY6pgGckdcLdEf493YW023AOeFRW01SI%2FRDD9pBEMbSycEJNmd8nWmS6hgnKySsZ%2B0G4vbBVZBb1aCS5UPQ%2BLofZ6Q3%2FGh3m7nzSYqqCKY4c41y77XuUOL%2FjXw%2BKtZA4HH%2F8xlSk5SKBTn%2FY7XhkCouTBS%2B33zAxqQIdHMDftshfYZTljPVSk2qdyGbaqZwoID73%2Ffr%2BRy%2BNbsb2YuLL4D%2BKzauA9vNkOCG&X-Amz-Signature=eec78c9749bd57b537e16401f2ebf1667fa76c2abdd205b2a0e4911362204277&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

