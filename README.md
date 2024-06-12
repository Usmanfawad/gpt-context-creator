# gpt-context-creator

## Overview

Isn't it a PAIN IN THE A** writing down the whole context for GPT and then explaining what you WANT from it? Well...
`gpt-context-creator` is a simple yet powerful script designed to help developers and content creators who frequently work with GPT models. This tool automates the process of gathering text from specified project files and consolidating it into a single output file. This file can then be used as context for GPT models, eliminating the need to manually copy and paste text each time.

# GPT Context Creator

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Project Description

**GPT Context Creator** is a utility script designed to streamline text aggregation from multiple project files into a single context file. This is particularly useful for seamlessly using the aggregated content with GPT models. Save time by automating the collection of context across multiple files.

## Features

- Aggregates text content from multiple files.
- Allows exclusion of specific directories.
- Easily configurable through CSV files.
- Supports Python 3.12+.

## Installation

To get started with GPT Context Creator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gpt-context-creator.git
   cd gpt-context-creator

2. **Install Dependencies**:
   ```bash
   poetry install

3. **Usage (RUN THE main.py)**:
   ```bash
   poetry run python main.py


**Sample Output**
   ```text
   --- Content of /path/to/project/pyproject.toml ---
   
   [tool.poetry]
   name = "gpt-context-creator"
   version = "0.1.0"
   description = "A utility script to streamline text aggregation from multiple project files into a single context file for seamless use with GPT models."
   authors = ["Your Name <email@example.com>"]
   license = "MIT"
   
   [tool.poetry.dependencies]
   python = "^3.12"
   black = "^24.4.2"
   
   --- End of content ---
   ```

**Contributing**
Contributions are welcome! Please fork this repository and submit a pull request for any feature requests or bug fixes.