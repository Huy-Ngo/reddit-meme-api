# Reddit Meme API

An API for random hot memes from top subreddits.

## Routes & responses

This API searches for image posts on r/meme, r/memes, r/dankmemes, and r/me\_irl
Each meme post is returned in the following format:


```json
{
    "author": "Poster of the meme",
    "permalink: "Path to the post from reddit.com",
    "score": "The number of upvotes minus downvotes",
    "url": "URL to the image"
}

```

- Route: `/memes/<subreddit>`
  - Return: list of up to 10 hot memes
- Route: `/memes/hot`
  - Return: a meme in the hot
- Route: `/memes/new`
  - Return: a meme in the new.

