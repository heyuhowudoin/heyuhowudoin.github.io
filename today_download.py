import praw, login_info, json, time as time_
reddit = login_info.reddit

submission_stream = reddit.subreddit("teenagersbutpog").stream.submissions(pause_after = -1, skip_existing = True)
comment_stream = reddit.subreddit("teenagersbutpog").stream.comments(pause_after = -1, skip_existing = True)
data = {}
old_times = []

def store_total(author, contribution_type):
	with open('data.json') as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1


		elif (author not in data):
			data[author] = [0, 0]
			data[author][contribution_type] += 1

def store_daily(author, created_time, contribution_type):
	with open("today.json") as data_file:
		data = json.load(data_file)

		if (author in data):
			data[author][contribution_type] += 1
			data[author][contribution_type + 2].append(created_time)

		elif (author not in data):
			data[author] = [0, 0, [], []]
			data[author][contribution_type] += 1
			data[author][contribution_type + 2].append(created_time)

	with open("today.json", "w") as data_file:
		json.dump(data, data_file, indent = 3)

while True:
	for post in submission_stream:
		if post is None:
			break
		store_daily(str(post.author), post.created_utc, 0)
		store_total(str(post.author), 0)

	for comment in comment_stream:
		if comment is None:
			break
		store_daily(str(comment.author), comment.created_utc, 1)
		store_total(str(comment.author), 0)

	with open("today.json") as data_file:
		data = json.load(data_file)
		
		for user in data:
			for time in data.get(user)[2]:
				if (time < time_.time() - 84600):
					data.get(user)[0] = data.get(user)[0] - 1
					old_times.append(time)

				for i in old_times:
					data.get(user)[2].remove(i)
				old_times = []

			for time in data.get(user)[3]:
				if (time < time_.time() - 84600):
					data.get(user)[1] = data.get(user)[1] - 1
					old_times.append(time)

				for i in old_times:
					data.get(user)[3].remove(i)
				old_times = []