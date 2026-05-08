from fastapi import FastAPI
from pydantic import BaseModel , Field
from openai import OpenAI
from os import getenv

llm = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENAI_API_KEY"),
)

def chatting(message : str):
    response = llm.chat.completions.create(
    model="tencent/hy3-preview:free",
    messages=[
            {
                "role": "user",
                "content": message
            }
            ],
    extra_body={"reasoning": {"enabled": True}}
    )

    response = response.choices[0].message.content

    return response


server = FastAPI()

reqresp = {}

class Chat(BaseModel):
    id : int = Field(gt=0)
    msg : str = Field(min_length=1)

@server.post('/chat')
def chatfunction(chat : Chat):
    if chat.id not in reqresp:
        resp = chatting(chat.msg)
        reqresp[chat.id] = resp
        return { "message" : "SUCCESSFULL", "msg" : f"{resp}"}
    else:
        return { "message" : "UNSUCCESSFULL"}
