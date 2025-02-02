from openai import OpenAI

client = OpenAI()

prompt = "Please generate a blog outline on how a beginner can break into the field of politics."

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
