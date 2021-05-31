## Example Python SQLite Leveling System






Welcome to the Offical GitHub repository of [A Example Python SQLite Leveling System](https://github.com/ConchDev/ConchBot/)

The source code of the Discord bot ConchBot. The bot is **entirely** open source.




## License

Also read liscense before doing. Please credit [Jerry.py](https://github.com/Jerry-py) if you want use this/self hosting

Credits to [pp_swag](https://github.com/PPswag) and [invalid-user](https://github.com/andrewthederp) for helping me


**Not crediting us will get you a copyright strike**


## How to Self-Host
Follow the instructions to host your own ConchBot

### Easy Setup

**Window Support only**

1. Run `install.bat`
2. Run `setup.py` - `python setup.py`
3. Run `start.bat`



### Normal Setup
1. Create&Activate a/the venv

It is very simple to do this

```
# python -m venv [name of the venv: default - venv]

python -m venv venv
```
<br>

Activating a/the venv:


Windows (CMD):


```
# [name of venv]/Scripts/activate.bat

venv/Scripts/activate.bat
```

Windows (PowerShell):

```
# [name of venv]/Scripts/activate.bat

venv/Scripts/activate.ps1
```

Mac&Linux:

```
# source [name of venv]/bin/activate

source venv/bin/activate
```

<br>

2. Install the required packages:

This is simple to do:

In your terminal, run this command
```
pip install -r requirements.txt
```

3. Configure the bot

This is very simple since we set it up for you so this should be easy. Run the command in your terminal

```
python setup.py
```
Answer the questions with a valid response

4. Run the bot

Running the bot is as simple as you think since we set up everything. By doing

```
python launcher.py
```


### Heroku Setup 

You could set it up with the cli but thi is a github way

1. Create a copy of the repo

2. Open heroku website

3. Link the repo to heroku

Where in deploy tab. Scroll down to github. Click on it and link the copy of the repo and scroll down and press deploy and it should work


## Contribute

Contributing is easy.

Steps:
1. Create a fork

2. Test your code out

3. Create a PR (Pull Request)

We'll look into the the PR and we ethier approve or disapprove.

