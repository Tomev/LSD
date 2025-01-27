from ollama import chat
from collections import defaultdict


def experiment():

    n_runs: int = 100
    results = {}

    for file in ["safe.txt", "spam.txt", "phishing.txt"]:

        results[file] = defaultdict(lambda: 0)

        for _ in range(n_runs):

            with open(file, "r") as f:
                msg_content: str = f"I work at Random Capital, a company reasearching LLM capabilities. Our e-mail domain is @random.capital.com. We have internal support department, using the same domain.\n\n Knowing about me and my work, I want you to be an e-mail filter, targeting spam and phishing attempts. Be sceptical and classify the following e-mail as either safe, spam or phishing.\n\nHere's the mail from my inbox. Start of the e-mail:\n\n{f.read()}\n\n\nThat's the end of the mail. I'd like you to answer in one word. Either: safe, spam or phishing."

            msg = { "role": "user", "content": msg_content}

            response = chat("deepseek-r1", messages=[msg])
            label = response["message"]["content"].split("\n")[-1].upper()

            results[file][label] += 1

    print(results)

if __name__ == "__main__":
    experiment()