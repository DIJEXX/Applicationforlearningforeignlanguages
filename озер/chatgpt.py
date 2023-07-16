import openai
openai.api_key = "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"
model_engine = "text-davinci-003"

def question(question):
    response = openai.Completion.create(
        engine=model_engine,
        prompt="",
        max_tokens=2048,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text


result = question(input())
print(result)