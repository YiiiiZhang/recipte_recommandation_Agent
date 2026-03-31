from app.llm.transformers_qwen import LocalQwenLLM


def main():
    llm = LocalQwenLLM()
    messages = [
        {"role": "system", "content": "You are a concise assistant."},
        {"role": "user", "content": "Say hello in one short sentence."},
    ]
    print(llm.chat(messages))


if __name__ == "__main__":
    main()