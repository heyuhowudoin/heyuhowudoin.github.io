import praw, login_info, json, datatime
reddit = login_info.reddit

url = "https://www.reddit.com/r/teenagersbutpog/comments/pjg3lj/coddit_20_but_on_a_reddit_post_cause_im_stupid/"
post = reddit.submission(url = url)
data = {}

with open("data.json") as data_file:
	data = json.load(data_file)
	
	for user in data:
		for time in data.get(user)[4]:
			data.get(user)[2] = 0
			if (time > datetime.datetime.utcnow() - 3600):
				data.get(user)[2] = data.get(user)[2] + 1
			if (time > datetime.datetime.utcnow() - 86400):
				data.get(user)[3] = data.get(user)[3] + 1
