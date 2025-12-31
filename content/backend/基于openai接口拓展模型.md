---
title: 基于Openai接口拓展模型
date: '2024-11-18T07:55:00.000Z'
lastmod: '2024-11-20T03:24:00.000Z'
draft: false
tags:
- Python
- API
categories:
- 后端
---

> 💡 记录一下，基于Openai API进行接口移植的过程，从引用api、测试、最后转接口部署。

---

### GPT-4o接口

```python
client = OpenAI(
    api_key=#这里就放入刚刚购买到的key就可以啦)
from opneai import OpenAI
def gpt_generate_text(prompt, messages_list):
    messages = ''    if messages_list:
        messages = '以下是你和用户的当前会话消息：\n\n' + '\n'.join(messages_list)
    stream = client.chat.completions.create(
        # model="gpt-4-turbo-preview",        model="gpt-4o",
        messages=[
            {"role": "system", "content": messages},
            {"role": "user", "content": prompt},
        ],
        stream=True    )
    text = ''    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            text += chunk.choices[0].delta.content
    return text
```

- 路由函数
---

## Whisper-1接口

- whisper-1模型(进行音频转文本)
```python
def transcribe_audio(audio_file):
    audio=open(audio_file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1",file=audio)
    text = transcription.text
    return text
```

- 路由函数
```python
@app.route("/transcribe", methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400    if audio_file:
        # 保存文件到临时位置        temp_file_path = os.path.join("temp", audio_file.filename)
        audio_file.save(temp_file_path)
        # 调用转录函数        transcription_text = transcribe_audio(temp_file_path)
        # 删除临时文件        os.remove(temp_file_path)
        return jsonify({"text": transcription_text})
```

> 首先我们要确定返回的请求中是否包含文件和文件名，如果没有，则返回错误信息和400，其次，我们需要保存文件到临时位置，然后调用我们写好的转录函数进行转录，最后删除临时文件。最后返回转录后的文本给客户端 供使用。

---

## TTS-1接口

- TTS-1(文本转换为语音)
```python
def text_to_speech(text, vocie, model, path):

    response = client.audio.speech.create(
        model=model,
        voice=vocie,
        input=text
    )
    speech_file_path = Path(path)
    with open(speech_file_path, 'wb') as file:
        file.write(response.content)

    print(f'文件已保存到: {speech_file_path}')
    return speech_file_path
```

- 路由函数
```python
app = Flask(__name__)
server_ip = ""  # 替换为你的服务器IP@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_endpoint():
    data = request.json
    text = data.get('text')
    voice = data.get('voice')
    model = data.get('model')
    output_path = './output.mp3'    if not text or not voice or not model:
        return {'error': 'Missing required parameters'}, 400    try:
        # Define the directory where you want to save the files        output_dir = Path('./audio_files')
        output_dir.mkdir(exist_ok=True)
        # Generate a unique filename using UUID        unique_filename = f"{uuid.uuid4()}.mp3"        output_path = output_dir / unique_filename
        # Generate the speech and save the file        speech_file_path = text_to_speech(text, voice, model, output_path)
        # Create the file URL        file_url = f"http://{server_ip}/root/xxx/{speech_file_path}"        # Return the file URL as a response        return jsonify({'file_url': file_url}), 200    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

> 首先我们要在后端代码中写入 我们的服务器ip地址我们要确保我们的json数据存在 四个键 text ， voice ， model ， output_path ，其次我们调用text_to_speech函数，传入text，voice，model，output_path，然后我们生成一个唯一的filename，保存到output_dir目录下最后我们生成一个file_url，然后返回给客户端。

---

## 测试截图

### gpt4o

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMYW5IXC%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZA8Zs2SUs%2Bcjlw2YdnnsCWHiJKiruUkse69bZ73KhFQIhALsZR2%2F0DQ6QsOrDdz%2B4LvvJFbD%2BbAwdGwQmDZxKIr%2F4KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwAUftbFTh2LYq8B8q3AM9hcQq7p3jcNk%2BrfK3LgwuJ%2FYG%2BJsLwrU9NcyB2FEq%2BM2C4snYfQPM4%2Bf7jjd6Iil4jS%2Fgr80j%2FrFWMjAM7f%2BLTYCIwWZus7zZeq5omqTTJDCB%2BjdlZ6JdJmOk4R2Zoe0tnQe0kHzK9pyIehWZO2DqTvJq871%2F1jZ2XKgQXVOmoje05hRcvGhv0sVS9Z%2BAt%2FIQD18xlGtIVqFDvzRy4hjY5CGlmN1EvPM%2FIa22bbnKYckIRIrQX4GDfSB3W0jRRlWyrXjG4OsUvxGfSS4NtMBcIWEC1tLijdNIoj02QyQjp1%2FzfUYa5k82K44Orvq0QyAwMxL8kUr3TAwl67Vy%2FJawpd6Suw%2BqnipTfvYB4FFSekoNt3SXhE90jZWeSrbWSsBJ6EiH9SxtC%2F3TO0ERpulXLvpTAilCef37U%2FSMDmXy0yW5mUkrhx6iQp0RKGBz8FTopLM7rv9Q3D7h3zvumZHGvtf0UIbOfz37N45LjuS66NfvTuhO4usRnEBFyS1ldcL4CJd%2ByX7SZBEUpnDVCaT%2B3HbNJY%2Ba%2B0QM0tsbGg7H9KZVBx06OlGSui4rNEOwShrC5%2FqYPN2V152vzWe77nihETfWIoSLBUlnc%2B22R84Hr8eI6VS5%2Bv7vincUQDDF79HKBjqkASUse%2Fxatb2n%2BMjggsQQRiN1H4dBX6beVsM3sQz0IcZwMm2fndFHozp3nvoTR5Yg8X3lyCL79e5Cq3feQZvOANf09gebgkwfexFxM2PKgl0g0jK2AU0%2BVM7FmzzSTLNHpelWz8DBy3qqd4teX6XAnn7qAFtD6o9o3amglwxeGg001Oy4bT2YftUdjzcJBTXsF86iYvjkin9KoYiwqg2vO%2BfQclDO&X-Amz-Signature=2f1b20c5baf7ed2ff14699b17c442977a7feb27d2fe1189b58c6522bd94ee667&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMYW5IXC%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZA8Zs2SUs%2Bcjlw2YdnnsCWHiJKiruUkse69bZ73KhFQIhALsZR2%2F0DQ6QsOrDdz%2B4LvvJFbD%2BbAwdGwQmDZxKIr%2F4KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwAUftbFTh2LYq8B8q3AM9hcQq7p3jcNk%2BrfK3LgwuJ%2FYG%2BJsLwrU9NcyB2FEq%2BM2C4snYfQPM4%2Bf7jjd6Iil4jS%2Fgr80j%2FrFWMjAM7f%2BLTYCIwWZus7zZeq5omqTTJDCB%2BjdlZ6JdJmOk4R2Zoe0tnQe0kHzK9pyIehWZO2DqTvJq871%2F1jZ2XKgQXVOmoje05hRcvGhv0sVS9Z%2BAt%2FIQD18xlGtIVqFDvzRy4hjY5CGlmN1EvPM%2FIa22bbnKYckIRIrQX4GDfSB3W0jRRlWyrXjG4OsUvxGfSS4NtMBcIWEC1tLijdNIoj02QyQjp1%2FzfUYa5k82K44Orvq0QyAwMxL8kUr3TAwl67Vy%2FJawpd6Suw%2BqnipTfvYB4FFSekoNt3SXhE90jZWeSrbWSsBJ6EiH9SxtC%2F3TO0ERpulXLvpTAilCef37U%2FSMDmXy0yW5mUkrhx6iQp0RKGBz8FTopLM7rv9Q3D7h3zvumZHGvtf0UIbOfz37N45LjuS66NfvTuhO4usRnEBFyS1ldcL4CJd%2ByX7SZBEUpnDVCaT%2B3HbNJY%2Ba%2B0QM0tsbGg7H9KZVBx06OlGSui4rNEOwShrC5%2FqYPN2V152vzWe77nihETfWIoSLBUlnc%2B22R84Hr8eI6VS5%2Bv7vincUQDDF79HKBjqkASUse%2Fxatb2n%2BMjggsQQRiN1H4dBX6beVsM3sQz0IcZwMm2fndFHozp3nvoTR5Yg8X3lyCL79e5Cq3feQZvOANf09gebgkwfexFxM2PKgl0g0jK2AU0%2BVM7FmzzSTLNHpelWz8DBy3qqd4teX6XAnn7qAFtD6o9o3amglwxeGg001Oy4bT2YftUdjzcJBTXsF86iYvjkin9KoYiwqg2vO%2BfQclDO&X-Amz-Signature=f7688e69d4bef53a7f60f12693c8f26a3b68c68c2d341d47837dd63e18b71a04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMYW5IXC%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZA8Zs2SUs%2Bcjlw2YdnnsCWHiJKiruUkse69bZ73KhFQIhALsZR2%2F0DQ6QsOrDdz%2B4LvvJFbD%2BbAwdGwQmDZxKIr%2F4KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwAUftbFTh2LYq8B8q3AM9hcQq7p3jcNk%2BrfK3LgwuJ%2FYG%2BJsLwrU9NcyB2FEq%2BM2C4snYfQPM4%2Bf7jjd6Iil4jS%2Fgr80j%2FrFWMjAM7f%2BLTYCIwWZus7zZeq5omqTTJDCB%2BjdlZ6JdJmOk4R2Zoe0tnQe0kHzK9pyIehWZO2DqTvJq871%2F1jZ2XKgQXVOmoje05hRcvGhv0sVS9Z%2BAt%2FIQD18xlGtIVqFDvzRy4hjY5CGlmN1EvPM%2FIa22bbnKYckIRIrQX4GDfSB3W0jRRlWyrXjG4OsUvxGfSS4NtMBcIWEC1tLijdNIoj02QyQjp1%2FzfUYa5k82K44Orvq0QyAwMxL8kUr3TAwl67Vy%2FJawpd6Suw%2BqnipTfvYB4FFSekoNt3SXhE90jZWeSrbWSsBJ6EiH9SxtC%2F3TO0ERpulXLvpTAilCef37U%2FSMDmXy0yW5mUkrhx6iQp0RKGBz8FTopLM7rv9Q3D7h3zvumZHGvtf0UIbOfz37N45LjuS66NfvTuhO4usRnEBFyS1ldcL4CJd%2ByX7SZBEUpnDVCaT%2B3HbNJY%2Ba%2B0QM0tsbGg7H9KZVBx06OlGSui4rNEOwShrC5%2FqYPN2V152vzWe77nihETfWIoSLBUlnc%2B22R84Hr8eI6VS5%2Bv7vincUQDDF79HKBjqkASUse%2Fxatb2n%2BMjggsQQRiN1H4dBX6beVsM3sQz0IcZwMm2fndFHozp3nvoTR5Yg8X3lyCL79e5Cq3feQZvOANf09gebgkwfexFxM2PKgl0g0jK2AU0%2BVM7FmzzSTLNHpelWz8DBy3qqd4teX6XAnn7qAFtD6o9o3amglwxeGg001Oy4bT2YftUdjzcJBTXsF86iYvjkin9KoYiwqg2vO%2BfQclDO&X-Amz-Signature=c976bd773c6ad5331e03c946a02a0617f9d03d85608640ca17aa29b6ea3e4520&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

