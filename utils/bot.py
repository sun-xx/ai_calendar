import erniebot
import os
import re
import datetime

def extract_info(input_str): 
    erniebot.api_type = 'aistudio'
    erniebot.access_token = os.environ.get('ERNIE_ACCESS_TOKEN')
    # Set your own access_token of baidu in environment variable.

    dt = datetime.datetime.today()
    dt = dt.strftime('%Y-%m-%d')

    model = 'ernie-4.0'
    prompt = "请从以上语句中提取出日期(用年-月-日格式)、时间（用24小时制）、事件、地点，将以上要素按顺序输出，每两个之间空一格。如果时间表述不清，则选择合理的时间，如下午替换为2pm，上午替换为7am。如果有要素缺失，请用暂无替代。请使用中文输出要素。"
    prompt2 = "注意今天是" + dt + "。"
    prompt3 = "输出以上要素时，请用英文括号将四个要素整体括起来，例如：(2024-7-19 14:00 写作 家)"

    messages = [{'role': 'user', 'content': input_str + prompt + prompt2 + prompt3}]
    def main(model, messages):
        response = erniebot.ChatCompletion.create(
            model = model,
            messages = messages,
            top_p = 0.01)
        result = response.get_result()
        return result

    answer = main(model, messages)
    match = re.search(r'\((.*?)\)', answer)
    if match:
        return match.group(1)
    else:
        return None