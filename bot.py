import os
from slack import WebClient
from slack.errors import SlackApiError
import feedparser

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

# define a variable for Eastern District Court of Pennsylvania RSS feed
ecpa = feedparser.parse('https://ecf.paed.uscourts.gov/cgi-bin/rss_outside.pl')

# Create a list of court RSS feeds
# This bot currently uses the U.S. district courts in Pennsylvania. The feed for the middle district currently yields a blank page.
courts = ['https://ecf.paed.uscourts.gov/cgi-bin/rss_outside.pl',
          'https://ecf.pamd.uscourts.gov/cgi-bin/rss_outside.pl',
          'https://ecf.pawd.uscourts.gov/cgi-bin/rss_outside.pl'
         ]
# Create a for loop that will iterate over each court's RSS feed
for court in courts:
    feed = feedparser.parse(court)
    # Parse the feed and return useful information in a Slack message
    for entry in feed.entries:
        ed = entry.description.split(']')[0]
        ed = ed.strip("[")
        if 'SCHOOL DISTRICT' in entry.title:
            try:
              response = client.chat_postMessage(
                channel="slack-bots",
                text=f"Update in {entry.title}\n Docket sheet: {entry.link}\n Description: {ed}\n -------------------------------------"
              )

            except SlackApiError as e:
              assert e.response["ok"] is False
              assert e.response["error"]
              print(f"Got an error: {e.response['error']}")
        else:
            print("No new results")
