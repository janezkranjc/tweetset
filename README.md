# TweetSet #

Manage supervisor jobs that collect tweets to a database using a web interface.

# About TweetSet #

I developed TweetSet because I needed some tweets for research. It was made available on [http://www.tweetset.com](http://www.tweetset.com) however I quickly ran out of disk space and had to shut the website down. I'm gonna put up a limited version very soon just to demonstrate the usability of this app. The full version is however quite available here and you can run it locally on your machine or even deploy it to a server.

If you're finding this app usefull please provide me with some beer money. I'll be forever grateful.

[![Support tweetset via gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/janezkranjc/)

# How it works #

TweetSet is a Django website that connects to a supervisor daemon and dynamically adds and removes supervisor tasks based on what the user wants to collect. It requires a valid twitter api application key. The user key is generated automatically after approval. If you want you can use the provided key, but for maximum performance and availability create your own application and replace the keys in the settings. You can generate API keys here: https://apps.twitter.com/

It's a bit more complicated to setup than my other project [Twitter Tap](https://github.com/janezkranjc/twitter-tap), but it's way easier to use and maintain in the long run.

# Installing and running local #

First clone the repo:

```bash
git clone git://github.com/janezkranjc/tweetset.git
```

Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages tweetset-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages tweetset-env
cd tweetset-env
source bin/activate
```

### Install requirements ###
```bash
cd tweetset
pip install -r requirements.txt
```

### Copy and edit passwords file ###
```bash
cp tweetset/tweetset/tweetset/settings/__passwords.py tweetset/tweetset/tweetset/settings/passwords.py
vi tweetset/tweetset/tweetset/settings/passwords.py
```


### Sync database ###
```bash
cd tweetset
python manage.py migrate
```

## Run the supervisor daemon ##

Navigate to the top of the repository (where supervisord.conf is located)

```bash
supervisord
```

## Run the webapp ##

Navigate to the directory where manage.py is located

```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

This should work. I will be putting up a demo version soon live @ http://www.tweetset.com in the meantime if you have any questions don't hesitate to contact me.

# Contributing #

Contributions are very welcome. Just issue a pull request, I'll check it out and merge it if it's ok!

