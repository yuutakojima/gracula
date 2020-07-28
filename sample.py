import gracula

g = gracula.Api(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_secret_key=''
)

items = g.get_follow_user_list()

for item in items['users']:
    print(item['screen_name'])
