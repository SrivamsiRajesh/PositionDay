from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",  # Replace with your actual API key
)

# System message
system_prompt = "You are a career advisor. Your role is to provide advice on improving skills for various job roles. Be professional, helpful, and provide actionable advice."

# Conversation history
conversation_history = []

def improve_skills(role):
    global conversation_history

    # Format messages
    messages = [
        {"role": "system", "content": system_prompt},
        *conversation_history,
        {"role": "user", "content": f"What skills should I improve for the role of {role}?"},
    ]

    try:
        completion = client.chat.completions.create(
          extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Replace with your site URL.
            "X-Title": "<YOUR_SITE_NAME>",    # Optional. Replace with your site name.
          },
          model="openchat/openchat-7b:free",
          messages=messages
        )

        response_text = completion.choices[0].message.content

        # Update conversation history
        conversation_history.append({"role": "assistant", "content": response_text})

        # Split the response into a list of skills
        skills = [skill.strip() for skill in response_text.split('\n') if skill.strip()]
        return skills

    except Exception as e:
        print(f"An error occurred: {e}")
        return ["Failed to retrieve response."]
