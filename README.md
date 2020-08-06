
# Description
very simple twitter api. This package can be done without OAuth.
It consists of the standard library of python3.

# usage

```python
import gracula

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

g = gracula.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_secret_key=ACCESS_SECRET
)

items = g.get_follow_user_list()

for item in items['users']:
    print(item['screen_name'])
```