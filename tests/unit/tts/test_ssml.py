from paddlespeech.t2s.frontend.ssml.xml_processor import MixTextProcessor

if __name__ == '__main__':
    text = "你好吗，<speak>我们的声学模型使用了 Fast Speech Two。前浪<say-as pinyin='dao3'>倒</say-as>在沙滩上,沙滩上倒了一堆<say-as pinyin='tu3'>土</say-as>。 想象<say-as pinyin='gan1 gan1'>干干</say-as>的树干<say-as pinyin='dao3'>倒</say-as>了, 里面有个干尸，不知是被谁<say-as pinyin='gan4'>干</say-as>死的。</speak>thank you."

    # SSML: 13
    # 0 ['你好吗，', []]
    # 1 ['我们的声学模型使用了FastSpeechTwo。前浪', []]
    # 2 ['倒', ['dao3']]
    # 3 ['在沙滩上,沙滩上倒了一堆', []]
    # 4 ['土', ['tu3']]
    # 5 ['。想象', []]
    # 6 ['干干', ['gan1', 'gan1']]
    # 7 ['的树干', []]
    # 8 ['倒', ['dao3']]
    # 9 ['了,里面有个干尸，不知是被谁', []]
    # 10 ['干', ['gan4']]
    # 11 ['死的。', []]
    # 12 ['thank you.', []]
    inputs = MixTextProcessor.get_pinyin_split(text)
    print(f"SSML get_pinyin_split: {len(inputs)}")
    for i, sub in enumerate(inputs):
        print(i, sub)
    print()

    # SSML get_dom_split: 13
    # 0 你好吗，
    # 1 我们的声学模型使用了 Fast Speech Two。前浪
    # 2 <say-as pinyin="dao3">倒</say-as>
    # 3 在沙滩上,沙滩上倒了一堆
    # 4 <say-as pinyin="tu3">土</say-as>
    # 5 。 想象
    # 6 <say-as pinyin="gan1 gan1">干干</say-as>
    # 7 的树干
    # 8 <say-as pinyin="dao3">倒</say-as>
    # 9 了, 里面有个干尸，不知是被谁
    # 10 <say-as pinyin="gan4">干</say-as>
    # 11 死的。
    # 12 thank you.
    inputs = MixTextProcessor.get_dom_split(text)
    print(f"SSML get_dom_split: {len(inputs)}")
    for i, sub in enumerate(inputs):
        print(i, sub)
    print()

    # SSML object.get_pinyin_split: 246
    # <speak>我们的声学模型使用了 Fast Speech Two。前浪<say-as pinyin='dao3'>倒</say-as>在沙滩上,沙滩上倒了一堆<say-as pinyin='tu3'>土</say-as>。 想象<say-as pinyin='gan1 gan1'>干干</say-as>的树干<say-as pinyin='dao3'>倒</say-as>了, 里面有个干尸，不知是被谁<say-as pinyin='gan4'>干</say-as>死的。</speak>
    outs = MixTextProcessor().get_xml_content(text)
    print(f"SSML object.get_pinyin_split: {len(outs)}")
    print(outs)
    print()

    # SSML object.get_content_split: 30 你好吗，
    # 1 <speak>我们的声学模型使用了 Fast Speech Two。前浪<say-as pinyin='dao3'>倒</say-as>在沙滩上,沙滩上倒了一堆<say-as pinyin='tu3'>土</say-as>。 想象<say-as pinyin='gan1 gan1'>干干</say-as>的树干<say-as pinyin='dao3'>
    # 倒</say-as>了, 里面有个干尸，不知是被谁<say-as pinyin='gan4'>干</say-as>死的。</speak>
    # 2 thank you.
    outs = MixTextProcessor().get_content_split(text)
    print(f"SSML object.get_content_split: {len(outs)}")
    for i, sub in enumerate(outs):
        print(i, sub)
    print()
