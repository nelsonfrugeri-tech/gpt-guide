# chat-completions-manual
> Repository with practical examples and explanations about OpenAI's Chat Completion project

This is a sample project that uses the OpenAI Chat Completions API to automatically generate text responses. The project is developed in Python and uses the python-dotenv library to load environment variables from an .env file.

## Prerequisites
Python 3.x
An OpenAI API key

Next, you need to install the project's dependencies using the pip package manager. To do this, navigate to the root folder of the project and run the following command:

```sh
pip install -r requirements.txt
```

## Configuration
To use the OpenAI Chat Completions API, you need to set the OPENAI_API_KEY and OPENAI_MODEL environment variables. The value of the OPENAI_API_KEY variable must be your OpenAI API key. To get an API key, go to the OpenAI control panel and create a new key.

The value of the variable OPENAI_MODEL should be the ID of the template you want to use to generate the text responses. You can get the template ID from the OpenAI templates page. In this project we are using the text-davinci-002 template.

To make it easier to set the environment variables you can create an .env file in the project root with the following content:

```sh
OPENAI_API_KEY=<sua chave de API da OpenAI>
OPENAI_MODEL=text-davinci-003
```

The .env file will be loaded automatically by the python-dotenv library when you run the project code.

## Example with pipenv

* Install Pipenv:

```sh
pip3 install pipenv
```

* Install dependencies:
```sh
pipenv install
```

* Install additional dependencies listed in requirements.txt:
```sh
pipenv run pip install -r requirements.txt
```

* Run the exemplo request-body:
```sh
pipenv run python3 request-body/hello_my_friend.py
```