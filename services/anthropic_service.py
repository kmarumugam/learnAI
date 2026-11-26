import os

from dotenv import load_dotenv
from anthropic import Anthropic

# Load .env before reading ANTHROPIC_API_KEY (it is not loaded automatically).
load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-5-5")


def invoke_claude(prompt: str):

    response = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # The response may contain non-text blocks (e.g. "thinking") before the
    # text block, so collect only the text blocks instead of content[0].
    text = "".join(
        block.text
        for block in response.content
        if block.type == "text"
    )

    return text.strip()