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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657VYMCHQ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFe5Kzj15hUTogRdR9NSInALry3BbP2ADdpud03qeFCUAiBY%2BCFP%2BdcyEvaJyIVTQIAKtEPTMEZ19py5qKQO0838jir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMBhQ3XSwgqSwptmpJKtwDicrByPeFRy6RpMiw8UzLmECpFB2c%2BC62YGl0O8Fh69b2HPmocSqU2UlvU6BZ558MYIt6%2BeHY0zC5GOTMr6%2FPxywYlmzWiVDDITjHD64qoTZsJybZTMkVCuCdX198rXL6k0MLPWhLd0nfyc1eOCS4GdPIXHI4ZnSA%2Bt0%2FjlekmO30GKyS%2Fnc7cFkeSyWt2JPHKBHI%2FnY%2F1VbkmL9vvaKDAI4QL82tk6n28JrcxtWxRhZLJWX6iZ61fj3EMkPB8yUF5HtKj7UXphR2iD%2F4rbnm2UoyUeiAyCeA3FmP5bLut5LB%2Fmefs0KiAAlwV5c56D%2F%2BKtQzRo4SjrGn32b6twlko2kI4HOhvOsZ906KZwoQPXWGBF23rpfZCFnzIYMZ2aZ51TPbHpF42zsB5k4T08FyoooxU2nCQQ4O9yj4LI%2F3%2F7IB50vDwy3aMziyg2m%2FwX95%2FIE%2FW2F6qrxVB10CAzOOt%2FaIH5U87X9z20%2FP7Yy6XJaz5dnac9CBnsNwzcEB1XK6Ug%2BL2emJAewCQR%2BnsPNMLOvHe2qjot1Hz2JzqN7DV%2Bzy3rzJaBNfyvauKjT3unG%2FP0V5wcPcQd00QkZghpZSh1C8BOThYeclgvWRoLnXTYJXtmK8cBD4tDPxxe4ws9v8yQY6pgHhk6Lt3mFl3phtjniR%2FyAYg35vnuVsgT%2BR2s%2FdTeu3V6E6849hxKo%2BIZmPvxM1iX4Xh5PInANkjVjEmzRlesdxFgoe8xew8J3VqSLx86KlwSzVQCONMuH3Rk1GPAUwcrUGm4BiGZViDQXGvRCscQKA09euBE5Vg%2BGoXGbimGwsmrFtoy75KzP163AlgTc4sxbnO2yM8NG7e9MhGIst2wrkkxDqpjRp&X-Amz-Signature=da2d33fbd40f4c794eddc39749fdec5a785d9bdb0edfbb885eac01f9a928b47f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657VYMCHQ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFe5Kzj15hUTogRdR9NSInALry3BbP2ADdpud03qeFCUAiBY%2BCFP%2BdcyEvaJyIVTQIAKtEPTMEZ19py5qKQO0838jir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMBhQ3XSwgqSwptmpJKtwDicrByPeFRy6RpMiw8UzLmECpFB2c%2BC62YGl0O8Fh69b2HPmocSqU2UlvU6BZ558MYIt6%2BeHY0zC5GOTMr6%2FPxywYlmzWiVDDITjHD64qoTZsJybZTMkVCuCdX198rXL6k0MLPWhLd0nfyc1eOCS4GdPIXHI4ZnSA%2Bt0%2FjlekmO30GKyS%2Fnc7cFkeSyWt2JPHKBHI%2FnY%2F1VbkmL9vvaKDAI4QL82tk6n28JrcxtWxRhZLJWX6iZ61fj3EMkPB8yUF5HtKj7UXphR2iD%2F4rbnm2UoyUeiAyCeA3FmP5bLut5LB%2Fmefs0KiAAlwV5c56D%2F%2BKtQzRo4SjrGn32b6twlko2kI4HOhvOsZ906KZwoQPXWGBF23rpfZCFnzIYMZ2aZ51TPbHpF42zsB5k4T08FyoooxU2nCQQ4O9yj4LI%2F3%2F7IB50vDwy3aMziyg2m%2FwX95%2FIE%2FW2F6qrxVB10CAzOOt%2FaIH5U87X9z20%2FP7Yy6XJaz5dnac9CBnsNwzcEB1XK6Ug%2BL2emJAewCQR%2BnsPNMLOvHe2qjot1Hz2JzqN7DV%2Bzy3rzJaBNfyvauKjT3unG%2FP0V5wcPcQd00QkZghpZSh1C8BOThYeclgvWRoLnXTYJXtmK8cBD4tDPxxe4ws9v8yQY6pgHhk6Lt3mFl3phtjniR%2FyAYg35vnuVsgT%2BR2s%2FdTeu3V6E6849hxKo%2BIZmPvxM1iX4Xh5PInANkjVjEmzRlesdxFgoe8xew8J3VqSLx86KlwSzVQCONMuH3Rk1GPAUwcrUGm4BiGZViDQXGvRCscQKA09euBE5Vg%2BGoXGbimGwsmrFtoy75KzP163AlgTc4sxbnO2yM8NG7e9MhGIst2wrkkxDqpjRp&X-Amz-Signature=c78e8645e9108ddb986bbea0fd3294294ea846aa305d8cf2c4c3533cf5343db3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657VYMCHQ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIFe5Kzj15hUTogRdR9NSInALry3BbP2ADdpud03qeFCUAiBY%2BCFP%2BdcyEvaJyIVTQIAKtEPTMEZ19py5qKQO0838jir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMBhQ3XSwgqSwptmpJKtwDicrByPeFRy6RpMiw8UzLmECpFB2c%2BC62YGl0O8Fh69b2HPmocSqU2UlvU6BZ558MYIt6%2BeHY0zC5GOTMr6%2FPxywYlmzWiVDDITjHD64qoTZsJybZTMkVCuCdX198rXL6k0MLPWhLd0nfyc1eOCS4GdPIXHI4ZnSA%2Bt0%2FjlekmO30GKyS%2Fnc7cFkeSyWt2JPHKBHI%2FnY%2F1VbkmL9vvaKDAI4QL82tk6n28JrcxtWxRhZLJWX6iZ61fj3EMkPB8yUF5HtKj7UXphR2iD%2F4rbnm2UoyUeiAyCeA3FmP5bLut5LB%2Fmefs0KiAAlwV5c56D%2F%2BKtQzRo4SjrGn32b6twlko2kI4HOhvOsZ906KZwoQPXWGBF23rpfZCFnzIYMZ2aZ51TPbHpF42zsB5k4T08FyoooxU2nCQQ4O9yj4LI%2F3%2F7IB50vDwy3aMziyg2m%2FwX95%2FIE%2FW2F6qrxVB10CAzOOt%2FaIH5U87X9z20%2FP7Yy6XJaz5dnac9CBnsNwzcEB1XK6Ug%2BL2emJAewCQR%2BnsPNMLOvHe2qjot1Hz2JzqN7DV%2Bzy3rzJaBNfyvauKjT3unG%2FP0V5wcPcQd00QkZghpZSh1C8BOThYeclgvWRoLnXTYJXtmK8cBD4tDPxxe4ws9v8yQY6pgHhk6Lt3mFl3phtjniR%2FyAYg35vnuVsgT%2BR2s%2FdTeu3V6E6849hxKo%2BIZmPvxM1iX4Xh5PInANkjVjEmzRlesdxFgoe8xew8J3VqSLx86KlwSzVQCONMuH3Rk1GPAUwcrUGm4BiGZViDQXGvRCscQKA09euBE5Vg%2BGoXGbimGwsmrFtoy75KzP163AlgTc4sxbnO2yM8NG7e9MhGIst2wrkkxDqpjRp&X-Amz-Signature=da66284470e486952b05e88921659d0630ab95f4b2668f9b382a18e7bbd33b20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

