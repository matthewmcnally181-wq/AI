import json
from ai_parser import parse_command
from executor import execute

def main():
    print("🧠 AI Automation Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        try:
            command = parse_command(user_input)
            print("\nParsed Command:", json.dumps(command, indent=2))

            result = execute(command)
            print("Result:", result, "\n")

        except Exception as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()