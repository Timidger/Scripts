import time
import praw
import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib.parse as urlparse

# Registration
# Add the github url when I get it
BACKLOG = []
BOT_IDENTIFY_STRING = ("MovieIdentifierBot: indentifies easy movie screen "
                       "caps by /u/Timidger "
                       "@ github.com/timidger/Scripts/MovieBot.py")
LOGIN_FILE = "login_details.txt"
SUBREDDIT = "GuessTheMovie"

HEADERS = {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 "
                         "(KHTML, like Gecko) Chrome/24.0.1312.27 "
                         "Safari/537.17"}

def add_to_backlog(post_title):
    assert isinstance(post_title, str), ("Add the titles to the backlog!"
                                            "was {}".format(type(post_title)))
    if len(BACKLOG) > 10:
        BACKLOG.pop(0)
    BACKLOG.append(post_title)

def compare_to_backlog(posts):
    set_posts = set(post.title for post in posts)
    set_backlog = set(BACKLOG)
    differences = set_posts.difference(set_backlog)
    new_posts = [post for post in posts if post.title in differences]
    return new_posts

def get_login_details(text_file):
    with open(text_file, "r") as login_file:
        user = login_file.readline().strip()
        password = login_file.readline().strip()
    return user, password

def login(username, password):
    user_agent = praw.Reddit(BOT_IDENTIFY_STRING)
    user_agent.login(username, password)
    return user_agent

def get_new_posts(bot, subreddit_name):
    subreddit = bot.get_subreddit(subreddit_name)
    return [post for post in subreddit.get_new(limit=10)]

def is_indentified(post):
    if post.link_flair_text:
        return "identified" in post.link_flair_text.lower()

def is_easy(post):
    if post.link_flair_text:
        return "easy" in post.link_flair_text.lower()

def already_posted(post, bot_name):
    """If I have already commented, don't comment again"""
    names = [str(comment.author).lower() for comment in post.comments]
    return bot_name in names

def get_links(page):
    # Get the html on the page
    text = page.text
    links = SoupStrainer('a')
    links = [tag for tag in BeautifulSoup(text, parse_only=links)]
    return links

def get_search_page(image_url):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17"
                             " (KHTML, like Gecko) Chrome/24.0.1312.27 "
                             "Safari/537.17",
               'connection': 'close'}
    base_url = "https://www.google.com/searchbyimage?&image_url={url}"
    url = base_url.format(url=image_url)
    webpage = requests.get(url, headers=headers)
    return webpage

def post_answer(post, movie_name):
    # Just for fun
    movie_name += "?"
    post.add_comment(movie_name)


if __name__ == "__main__":
    username, password = get_login_details(LOGIN_FILE)
    bot = login(username, password)
    print("Authenticated account: {}".format(username))
    try:
        while True:
            posts = get_new_posts(bot, SUBREDDIT)
            posts = compare_to_backlog(posts)
            for post in posts:
                add_to_backlog(post.title)
                identified = is_indentified(post)
                easy = is_easy(post)
                posted = already_posted(post, str(bot.user).lower())
                if identified or easy or posted:
                    continue
                print("Possible Post found: {}".format(post.title))
                image_url = post.url
                page = get_search_page(image_url)
                # first thing is the doc type, which we don't want
                links = get_links(page)[1:]
                page.close()
                for link in links:
                    if "IMDb" in  link.text:
                        movie = link.text
                        if "(" in movie:
                            partition = movie.find("(") # Year of pub.
                            movie = movie[:partition]
                        else:
                            continue # No year == Not a movie
                        movie = movie.strip() # Annoying extra whitespace

                        print("Found the movie: {}".format(movie))
                        print("Posting movie...")
                        post_answer(post, movie)
                        print("Movie posted!")
                        break
            print("Sleeping...")
            # Every 1/2 minute check the site
            time.sleep(30)
    finally:
        bot.clear_authentication()

