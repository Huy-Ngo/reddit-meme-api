from json import load
from random import choice

from praw import Reddit
from flask import Flask, Blueprint

with open('config.json', 'r') as f:
    data = load(f)
    client_id = data['client_id']
    client_secret = data['client_secret']
    user_agent = data['user_agent']

app = Flask(__name__)

reddit = Reddit(client_id=client_id, client_secret=client_secret,
                user_agent=user_agent)

bp = Blueprint('memes', __name__, url_prefix='/memes')


@bp.route('/<sub>')
def memes(sub):
    meme_list = {}
    for submission in reddit.subreddit(sub).hot(limit=10):
        if submission.selftext == '' and 'redd.it' in submission.url:
            meme_list[submission.id] = {
                "permalink": submission.permalink,
                "url": submission.url,
                "author": submission.author.name,
                "score": submission.score
            }
    return meme_list


@bp.route('/random')
def random_memes():
    meme_list = {}
    subs = ['memes', 'dankmemes', 'meme', 'me_irl']
    for sub in subs:
        for submission in reddit.subreddit(sub).hot(limit=10):
            if submission.selftext == '' and 'redd.it' in submission.url:
                meme_list[submission.id] = {
                    "permalink": submission.permalink,
                    "url": submission.url,
                    "author": submission.author.name,
                    "score": submission.score
                }
    chosen = choice(list(meme_list.keys()))
    return {'chosen': meme_list[chosen]}


@bp.route('/new')
def new_memes():
    meme_list = {}
    subs = ['memes', 'dankmemes', 'meme', 'me_irl']
    for sub in subs:
        for submission in reddit.subreddit(sub).new(limit=10):
            if submission.selftext == '' and 'redd.it' in submission.url:
                meme_list[submission.id] = {
                    "permalink": submission.permalink,
                    "url": submission.url,
                    "author": submission.author.name,
                    "score": submission.score
                }
    chosen = choice(list(meme_list.keys()))
    return {'chosen': meme_list[chosen]}


app.register_blueprint(bp)
