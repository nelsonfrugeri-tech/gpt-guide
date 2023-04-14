# fine_tuning

> In this session you will learn more about Fine Tuning

Fine-tuning is a process used to adjust a pre-trained deep learning model to the specific needs of an application, improving its performance on specific tasks.

## Prerequisites
OpenAI command-line interface (CLI)
An OpenAI API key

## Installation
```sh
pip3 install --upgrade openai
```

## Prepare training data
* File: data.jsonl

## Configuration
To make it easier to set the environment variables you can create an .env file in the project root with the following content:
```sh
OPENAI_API_KEY=<YOUR_KEY_OPENAI>
OPENAI_MODEL=<YOUR_MODEL_OPENAI>
```

## CLI data preparation tool
A tool which validates, gives suggestions and reformats your data:
```sh
openai tools fine_tunes.prepare_data -f /fine_tuning/data.jsonl
```

## Create a fine-tuned model
Start your fine-tuning job using the OpenAI CLI:
```sh
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
```

## Check the fine-tuning process
```sh
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```

## Run the test
When the process is in successful status, run the chat_completion create

[To learn more about how to run chat_completion create](https://github.com/nelsonfrugeri/gpt-manual/blob/main/chat_completion) 

#### Reference
https://platform.openai.com/docs/guides/fine-tuning