import openai
import os

# Set up OpenAI API key
openai.api_key = "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"

# Get the diff of changes made to the files
diff = os.popen('git diff').read()

# Use OpenAI's GPT-3 to generate a commit message based on the diff
prompt = f"Please generate a commit message based on the following diff:\n{diff}"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the generated commit message
commit_message = response.choices[0].text.strip()

# Commit the changes with the generated commit message
os.system(f'git commit -m "{commit_message}"')
