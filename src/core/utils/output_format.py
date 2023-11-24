import json


def isOutputFormat(response, format_name):
    format_functions = {
        'json': to_json,
        'txt': to_txt,
        'vtt': to_vtt,
        'srt': to_srt,
        'tsv': to_tsv
    }
    return format_functions[format_name](response)


def to_json(response):
    # Convert the response to json format {text: "text", language: "language", segments: [{start: 0.0,end: 0.0}]}
    return json.dumps(response)


def to_txt(response):
    # Convert the response to txt format
    return response


def to_vtt(response):
    # Convert the response to vtt format {start} --> {end} {text} \n
    return response


def to_srt(response):
    # Convert the response to srt format {index} \n {start} --> {end} \n {text} \n
    return response


def to_tsv(response):
    # Convert the response to tsv format {start} \t {end} \t {text} \n
    return response
