# About Quanta Agent

This is a tool to automate querying AIs (LLMs) about your codebase. That is, if you're a software developer and you want to be able to ask AI (like OpenAI's ChatGPT for example) questions about very specific parts of your code this tool helps do that.

This app will scan your project and extract named snippets (or sections) of code called `blocks` (i.e. fragments of files, that you identify using structured comments, described below) which can be injected into prompts by using an assigned name you give to each fragment. 

# Simple LLM Prompt Example

Suppose you have a Java file that contains the following:

    // --block.begin Adding_Numbers
    int total = a + b;
    // --block.end

You can run run LLM Prompts/Queries like this:

    What is happening in the following code:

    ${Adding_Numbers}

So you can see you're basically labeling (or naming) arbitrary sections of your code (or other text files) in such a way that this tool can build queries out of templates that refrence the named blocks of code.

# Background and Inspiration

There are other coding assistants like Github's Copilot for example, which let you ask arbitrary questions about your codebase, and those tools are very useful. However `Quanta Agent` lets you ask AI questions (i.e. build prompts) in a more flexible, targeted, specific, and repeatable way, and automatically saves the history of all your query outputs into markdown text files. `Quanta Agent` can solve more complex and difficult questions, in a repeatable way that doesn't require lots of developer time spent in building the same (or similar) prompts over and over again.

For example, let's say you have some SQL in your project and some Java Entity beans that go along with your database tables. You might want to be able to alter or add SQL tables and/or automatically create the associated Java Entity beans. To get AI to do this for you, in a way that "fits into" your application architecture perfectly, you would want to create prompts that show examples of how you're doing each of these types of artifacts (the SQL and the Java), and then ask the AI to generate new code following that pattern. `Quanta Agent` helps you build these kinds of complex prompts, and keeps developers from having to construct these prompts manually.

# How it Works (Identifying Blocks)

In summary `Quanta Agent` allows you to define named blocks inside any of you files like this:

```sql
-- block.begin SQL_Scripts
...all the scripts
-- block.end 
```

--or--

```java
// block.begin My_Java
...all the code
// block.end 
```

and then use the named blocks in AI prompts, to insert the entire content of the block from the file. The text that comes after the `block.begin` is considered the `Block Name` and, as shown in the example above, the `Block Names` are usable in prompts. So `${SQL_Scripts}` and `${My_Java}` when used in a prompt will be replaced with the block content in the final prompt sent to the LLM.

Note: If only `block.begin` exists and `block.end` doesn't exist, the block will end at the end of the file.

Note: The relative filename is also a valid "block name" and will insert the entire content of the specified file into the prompt. So you can simply put `${/path/to/my/file.md}` in a prompt, and it will inject the entire content of the file into the prompt. Note that the configured `source_folder` is the assumed prefix (base folder) for all of these kinds of file names.

So, in summary, The tool will scan all your source files (inside `source_folder`) and collect all these "Named Blocks" of code, and then you can just use the names themselvels in your prompts templates, to inject the block content.



# Use Cases

## New Employee Training

If you decorate specific sections (or blocks) of your company's codebase with these kinds of named blocks, then you can write prompts that are constructed to ask a question about a set of `blocks` that will be super inforformative to new employees learning the codebase, and able to be very specific questions about architecture that really cannot be replicated with tools like Github Copilot.

## Adding new Features or Altering Code

The hard part about adding new features to most codebases is remembering all the different locations in the codebase that might need to be altered in order to get the new feature working, and because every app is a little bit different, a tool like this is really the only way to have prompts that are good enough to make complex changes, that would otherwise require a true AGI. For example, if you need to add a new feature, it might require a new Button on the GUI, new POJOs, new SQL, new API calls, etc. So with a tool like `Quanta Agent` you can sort of package up a prompt that grabs from all these various parts of a codebase to perhaps show an example of how one feature is done, just including precisely only the relevent chunks of code, and then do a prompt like "Using all the example code as your architectural example to follow, create a new feature that does ${feature_description}." So the context for all the aforementioned example code would just be build using the code chunks from various snippets all around the codebase.

## Code Reviews

Developer teams could theoretically use a standard where (perhaps only temporarily) specific block names are required to be put in the code around all changes or specific types of changes. Then you can use AI to run various kinds of automated code reviews (security audits, code correctness audits, AI suggestions for improvements) that specifically look at all the parts of the code involved in any but fix or new feature.


# Configuration and Usage Flow

To run this tool, you should create some data folder and then point the `/config/config.yaml data_folder` to that folder location. This folder will be where the input (the LLM Prompt) is read from and also where the output (AI Generated Responses) are written to. For ease of use in this prototype app we just always expect the prompt itself to be in `${data_folder}\question.md`. So when you run this app it assumes that you have created a file named `question.md` that contains your prompt. As you edit your `question.md` file and then run the tool to generate answers you don't need to worry about maintaining a history of the questions, becasue they're all stored as part of the output. So you can just resave your next question.md file before you run the tool, and it's a fairly good user experience. This app will eventually have a GUI and/or an HTTP API, but for now feeding in prompts via question.md file is idea..

When you run this app, first all your source is scanned (i.e. `source_folder` config property), to build up your named blocks of code. Then your `question.md` file is read, and all the template substitutions are made in it (leaving the `question.md` itself as is), and then the call to OpenAI is made to generate the response. The response file is then written into the output folder, in a timestamped file, so you will have your entire history of questions & answers saved permanently in your `data_folder`.

An example `data_folder` (named `data` in the project root) is included in this project so you can see examples, to get a better more undersanding of how this tool works.


# Project Setup Tips (Development Environment)

## Create a conda environment

    We recommend 'conda' but that's optional of course. All that's really required is Python.

    conda create -n quanta_agent python=3.11.5
    conda activate quanta_agent

    Don't forget to activate your "quanta_agent" environment in your IDE. IDE's, like VSCode, require you to choose the
    Python interpreter, so simply running 'conda activate quanta_agent' won't be enough.

## Install langchain

    conda install langchain -c conda-forge
    pip install langchain-openai

## Install Libraries

    pip install ConfigArgParse


# Configs

The current `config.py` will automatically find the API keys from `..\secrets\secrets.yaml`, and it's not recommended to put them directly into config.yaml itself, because of risk of accidental commits to github


# NOTES:

* This project is being developed on Python 3.11.5, and on Linux, but afaik it will run on any other platform with Python.


# Resources

https://python.langchain.com/docs/get_started/introduction/

https://python.langchain.com/docs/integrations/chat/openai/

