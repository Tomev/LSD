from typing import Dict

messages: Dict[str, str] = {
    "instruction": "I'll send you an e-mail I've received. Using the data I provide about my work and my company, try to classify the e-mail as either safe, spam or phishing.\n\n",
    "data": "My company is Random Company. We're a small start-up reasearching LLM capabilities. Our e-mail domain is random.company.com. We have internal IT support, using mails in the same domain.\n\n",
    "pre_mail": "Here's the mail:\n\n",
    "answer_format": "\n\n\nThat's the end of the mail. I'd like you to answer in one word. Either: safe, spam or phishing.",
}