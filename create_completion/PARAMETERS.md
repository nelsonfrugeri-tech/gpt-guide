
### CREATE COMPLETION
| **Field** | **What's it?** | **Examples** | 
| --- | --- | -- |
| engine | The "engine" parameter in the create method of the OpenAI Chat Completion API is used to specify which language model should be used to generate the response for the user input provided. Each language model is trained on a different set of data and can be specialized for specific tasks. | "davinci": This model is considered the most advanced and generally produces more accurate and coherent responses. It is trained on a wide variety of data and is useful for general text generation tasks. "curie": This model is specialized in text generation tasks for specific purposes, such as summaries, translations, and product descriptions. "babbage": This model is less accurate than the others, but it is faster and can be used for tasks that require less precision, such as simple chatbots. | 
| prompt | It's the parameter in the OpenAI Chat Completion API is used to specify the input text or prompt for which the API should generate a response. It is the text that is used to seed the AI model's response. | Here are some examples of prompts that could be used with the API:

- "Can you write me a short story about a haunted house?"
- "Can you provide a summary of the latest research on climate change?"
- "Can you generate a list of potential names for a new restaurant?"
- "Can you translate the phrase 'hello, how are you?' from English to French?"
- "Can you write a product description for a new smartphone?"

The API will then use the provided prompt to generate a response that is relevant to the given task. |
| max_tokens | It's max_tokens | |
| temperature | It's temperature | |
| top_p | It's top_p | |
| n | It's n | |
| stop | It's stop | |
| best_of | success/failure | |
| suffix | success/failure | |
| echo | success/failure | |