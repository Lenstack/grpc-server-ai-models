import json


def isOutputFormat(response, info, format_name):
    format_functions = {
        'json': to_json,
        'txt': to_txt,
        'vtt': to_vtt,
        'srt': to_srt,
        'tsv': to_tsv
    }
    return format_functions[format_name](response, info)


def to_json(response, info):
    # Convert the response to json format {text: "text", language: "language", segments: {id: "id", seek: "seek",
    # start: "start", end: "end", text: "text", tokens: "tokens", temperature: "temperature", avg_logprob:
    # "avg_logprob", compression_ratio: "compression_ratio", no_speech_prob: "no_speech_prob", words: [{start:
    # "start", end: "end", word: "word", probability: "probability"}]}}
    json_response = {}
    for segment in response:
        print(info)
        json_response = {
            'text': segment.text,
            'language': info.language,
            'segments': {
                'id': segment.id,
                'seek': segment.seek,
                'start': segment.start,
                'end': segment.end,
                'text': segment.text,
                'tokens': segment.tokens,
                'temperature': segment.temperature,
                'avg_logprob': segment.avg_logprob,
                'compression_ratio': segment.compression_ratio,
                'no_speech_prob': segment.no_speech_prob,
                'words': [
                    {
                        'start': word.start,
                        'end': word.end,
                        'word': word.word,
                        'probability': word.probability
                    }
                    for word in segment.words
                ]
            }
        }

    return json.dumps(json_response)


def to_txt(response):
    # Convert the response to txt format
    return '\n'.join(segment.text for segment in response)


def to_vtt(response):
    # Convert the response to vtt format {start} --> {end} {text} \n
    vtt = ''
    for segment in response:
        vtt += f"{segment.start} --> {segment.end}\n{segment.text}\n\n"
    return vtt


def to_srt(response):
    # Convert the response to srt format {index} \n {start} --> {end} \n {text} \n
    srt = ''
    index = 1
    for segment in response:
        srt += f"{index}\n{segment.start} --> {segment.end}\n{segment.text}\n\n"
        index += 1
    return srt


def to_tsv(response):
    # Convert the response to tsv format {start} \t {end} \t {text} \n
    tsv = ''
    for segment in response:
        tsv += f"{segment.start}\t{segment.end}\t{segment.text}\n"
    return tsv
