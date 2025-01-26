from ollama import chat
from config import messages

model: str = "deepseek-r1"

def main() -> None:

    msg_content: str = messages["instruction"]
    msg_content += messages["data"]
    msg_content += messages["pre_mail"]

    with open("mail.txt") as f:
        msg_content += f.read()

    msg_content += messages["answer_format"]

    msg = [
    {
        "role": "user",
        "content": msg_content,
    },
    ]

    response = chat(model, messages=msg)
    print(response["message"]["content"])

if __name__ == "__main__":
    main()