from urllib.request import urlopen
import json
import sentiment

data = urlopen('https://api.github.com/events').read().decode('utf8')
response = json.loads(data)


for event in response:
    if event['type'] == 'PushEvent':
        commits = event['payload']['commits']
        if len(commits) > 0:
            for commit in commits:
                msg = commit['message']
                if sentiment.analyze(msg)['score'] < 0:
                    print('========================================================')
                    print(msg)

print('========================================================')
