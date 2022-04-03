import os
from slack import WebClient
from slack.errors import SlackApiError
import feedparser

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

# define a variable for Eastern District Court of Pennsylvania RSS feed
ecpa = feedparser.parse('https://ecf.paed.uscourts.gov/cgi-bin/rss_outside.pl')

for entry in ecpa.entries:
    if 'SCHOOL DISTRICT' in entry.title:
        try:
          response = client.chat_postMessage(
            channel="slack-bots",
            text=f"Update in {entry.title} \n Docket sheet: {entry.link} \n {entry.description.split(']')[0]}"
          )
        except SlackApiError as e:
          assert e.response["ok"] is False
          assert e.response["error"]
          print(f"Got an error: {e.response['error']}")
    else:
        print("No new results")




        #except SlackApiError as e:
          # You will get a SlackApiError if "ok" is False
          #assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
