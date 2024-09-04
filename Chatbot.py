import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

def chat(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024, #max no of characters in your prompt
    n=1,
    stop=None,
    temperature=0.5, #randomness,creativity
  )

  return response.choices[0].text

while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  else:
    response = chat(user_input)
    print("AI:", response)