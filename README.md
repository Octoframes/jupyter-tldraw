# Jupyter Tldraw
[![PyPI version](https://img.shields.io/pypi/v/tldraw.svg)](https://pypi.org/project/tldraw/)
<img width="946" alt="image" src="https://github.com/kolibril13/jupyter-tldraw/assets/44469195/8ba7e662-1f35-4e3b-b342-6d9fd3079e22">


Installation:
```
python3.11 -m venv .venv
pip install jupyterlab
pip install tldraw
jupyterlab   (or alternative VS Code Jupyter Lab)
```

## Example
```
from tldraw import TldrawWidget
t = TldrawWidget()
t
```



## MakeReal Example
```
from tldraw import MakeReal
from api_key import api_key

m = MakeReal(width=1002, height = 500, api_key = api_key)
m
```
INFO: To use GPT4-Vision, you need an API key.

### How do I get my API key?

1. Create an OpenAI account at [OpenAI](https://platform.openai.com/)
2.  In your Openai API account, navigate to **[Settings > Billing](https://platform.openai.com/account/billing/overview)** 
3. Click **Add to credit balance**
4. Add at least **$5** to your account
5. Navigate to [API Keys](https://platform.openai.com/api-keys)
6. Click **Create new secret key**
7. Copy the key to your clipboard.
8. Back on your jupyter-tldraw folder, paste the key into the API key into a new file called api_key.py 
9. Add the key in this form: `api_key = "sk-*************************"`.
10. Add  `api_key.py` into your gitignore. WARNING: Don't upload your API KEY on GitHub!

Now you're ready to run!

For transparency, this is how the key is used:  
https://github.com/kolibril13/jupyter-tldraw/blob/main/src/tldraw/prompt.py#L5-L47


 
# Developer Instructions

1. Clone Repo
2. `npm i`
3. Make virutal env `python3.11 -m venv .venv && source .venv/bin/activate`
4. `pip install -e ".[dev]" `
5. `npm run dev`





# Changelog

# 3.0.0

update npm install @tldraw/tldraw@3.0.0



# 2.4.6

update npm install @tldraw/tldraw@2.4.5
TldrawSetImage implementation

## 2.4.5

* fix path
  
## 2.4.4

* better TldrawWidgetCoordinates 

## 2.4.3


* update npm install @tldraw/tldraw@2.4.3
* add ReactiveColorPicker


## 2.2.5

* include  "package.json", "node_config.mjs" to pypi, so that conda works as well.
* update to tldraw 2.2.5
* include jsx files on pypi, so that conda can build more easily.

## 2.2.4

update to tldraw 2.2.4

## 2.0.20

Add debug example

## 2.0.19

Experiment with node_config


### 2.0.17 & 2.0.18

small fixes

### 2.0.16

add TldrawWidgetCoordinates

### 2.0.15

* update tldraw version

### 2.0.14

* update to GPT4o

### 2.0.13

* fix svgAsImage problem
* update makereal to gpt4-turbo
* run_next_cell parameter

### 2.0.12

* fix cell selection bug by autoFocus={false}
* npm i @tldraw/tldraw@2.1.3


### 2.0.11

* updating npm install @tldraw/tldraw@2.1.0

### 2.0.9 & 2.0.10

* Setting up hatch correctly

### 2.0.8

* Update version to @tldraw/tldraw@2.0.2


### 2.0.7

*increase number of output tokens to 4096

### 2.0.6

Tweak prompt parameter.

### 2.0.5

Add requests module
Tweak readme

### 2.0.4

Add experimental SVG/PNG export.  
Add experimental .txt export.  
Add makereal


## 2.0.3

Update to version `2.0.0-alpha.19`


## 2.0.2

Add experimental TldrawImageArray

## 2.0.1

Switch to new version: `@tldraw/tldraw@2.0.0-canary.b9d82466295e` (Version from 6th November2023)

<!-- npm install @tldraw/tldraw@2.0.0-canary.b9d82466295e -->

## 2.0.0

* simplify to minimal template


## 1.0.0

* Rename notebooks, and prepare 2.0.0 release.

## 0.1.5

* add .venv to gitignore, so that it's not uploaded to pypi by hatch build.

## 0.1.4

* Add experimental TldrawSegmentation


## 0.1.3
* format toml

## 0.1.2

* replace ipyreact backend with anywidget backend.
  * this will make this package more reliable, because all js and css is shipped via pip and not anymore via cdn.
* Remove JupyterLite build.
* Remove experimental files.


## 0.1.1

* add update_plot in TldrawMatplotlib

## 0.1.0

* Added TldrawMatplotlib

## 0.0.3

* refactor readme
* add jupyterlite demo
## 0.0.2

* refactor code

## 0.0.1

* init setup
