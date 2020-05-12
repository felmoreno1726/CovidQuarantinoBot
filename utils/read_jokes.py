import json, random

def read_random_joke():
    with open('./assets/reddit_jokes.json', 'r') as jokes_file:
        jokes = json.load(jokes_file)
    num_jokes = len(jokes)
    joke_id = random.randint(0, num_jokes)
    #get joke id
    joke = jokes[joke_id]
    joke_text = joke['title'] + ' ' + joke['body']
    return joke_text
