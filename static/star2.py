from bottle import route, run, template
import feedparser
import ssl
import json

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
print(feed)


@route("/")
def page():
    return template("star2.html")


@route('/Articles')
def function_first():
    list_of_posts = []
    for x in range(20):
        entry = {
            'title': feed['entries'][x]['title'],
            'link': feed['entries'][x]['link']
        }
        list_of_posts.append(entry)
    return json.dumps(list_of_posts)


def main():
    run(host="localhost", port=7001)


if __name__ == "_main_":
    main()

main()
