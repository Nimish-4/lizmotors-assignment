from huggingface_hub import InferenceClient


API_TOKEN="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"

def query_response(query):

        client = InferenceClient(
        "mistralai/Mistral-7B-Instruct-v0.1",
        token=API_TOKEN,
        )

        response = client.chat_completion(
                messages=[{"role": "user", "content": query}],
                max_tokens=200,
                stream=False,
        )

        return response.choices[0].message.content
