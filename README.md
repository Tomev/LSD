# LSD --- LLM Spam Detector

**L**LM **S**pam **D**etector is a proof of concept
showing if and how an out-of-the-box LLM can be used
as an additional layer of phishing / spam detection. Turns out that after some tweaks it might work pretty well.

## Methodology and results

I downloaded `ollama` and the `deepseek-r1` model and started
building upon the `ollama` chat API tutorial. When I was done,
I looked through my e-mails and:

- Selected one phishing e-mail from my work inbox and 
translated it to English. See [phishing.txt](phishing.txt).

- Selected one spam mail from my work inbox. See [spam.txt](spam.txt).

- I generated a generic conference invitation e-mail, which was meant to offer something (conference attendance), but be related to the prompted field of work. See [safe.txt](safe.txt).

I checked initial results and tweaked with the prompt a little bit (2h, watching the
show on TV). Then, for each e-mail type, I queried the model 100 times. The results are as follows. LSD was able to recognize safe mail with 100% accuracy. Spam mail was classified as either spam or phishing in 48 and 43 of the queries respectively. There was also one mislabeling as *spambot*. Phishing attempts were recognized 63 times, two of which were mislabelled, and otherwise considered safe. Analysis of the model chain-of-though led me to believe that the model considered 'From: "random.capital.com" <techcare98@gmail.com>' as sender-receiver rather than alias-address, which made a huge difference in its reasoning. Overall, as an **additional** spam filter, LLMs seem a promising tool. I'd, however, advise more tweaks and experimental verification.

## Code

I present the tested version of the code below. 

```python
from ollama import chat


with open("spam.txt", "r") as f:
    msg_content: str = f"I work at Random Capital, a company reasearching LLM capabilities. Our e-mail domain is @random.capital.com. We have internal support department, using the same domain.\n\n Knowing about me and my work, I want you to be an e-mail filter, targeting spam and phishing attempts. Be sceptical and classify the following e-mail as either safe, spam or phishing.\n\nHere's the mail from my inbox. Start of the e-mail:\n\n{f.read()}\n\n\nThat's the end of the mail. I'd like you to answer in one word. Either: safe, spam or phishing."

msg = { "role": "user", "content": msg_content}

response = chat("deepseek-r1", messages=[msg])
print(response["message"]["content"])
```
