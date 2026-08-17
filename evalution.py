import os
import lm_eval

# Make sure Groq API key exists
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is not set!")

# Model arguments
model_args = {
    "model": "llama-3.3-70b-versatile",
    "base_url": "https://api.groq.com/openai/v1/chat/completions",
    "tokenizer": "meta-llama/Llama-3.3-70B-Instruct",
}

# Run evaluation
results = lm_eval.simple_evaluate(
    model="local-chat-completions",
    model_args=model_args,
    tasks=["gsm8k"],
    num_fewshot=5,
    limit=100,
)

# Print results
print("\n========== RESULTS ==========")

for task, result in results["results"].items():
    print(f"\nTask: {task}")

    for metric, value in result.items():
        if isinstance(value, (int, float)):
            print(f"{metric}: {value}")


