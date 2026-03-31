from app.llm.transformers_qwen import LocalQwenLLM


def main():
    llm = LocalQwenLLM()

    print("Local Qwen CLI")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]

        try:
            reply = llm.chat(messages)
            print(f"\n{reply}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()