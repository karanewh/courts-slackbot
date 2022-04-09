import os
from slack import WebClient
from slack.errors import SlackApiError
import feedparser
import re

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

# define a variable for Eastern District Court of Pennsylvania RSS feed
ecpa = feedparser.parse('https://ecf.paed.uscourts.gov/cgi-bin/rss_outside.pl')

# Create a list of court RSS feeds
courts = ['https://ecf.paed.uscourts.gov/cgi-bin/rss_outside.pl',
          'https://ecf.pamd.uscourts.gov/cgi-bin/rss_outside.pl',
          'https://ecf.pawd.uscourts.gov/cgi-bin/rss_outside.pl'
         ]
#not sure about the middle district of PA feed - the one from Big Cases bot yields a blank page. I found a different set of rss feeds via gov.info, but those aren't daily updates.

# Create a for loop that will iterate over each court's RSS feed
for court in courts:
    feed = feedparser.parse(court)
    # Parse the feed and return useful information in a Slack message
    for entry in feed.entries:
        ed = entry.description.split(']')
        ed = re.sub('[','', ed)
        if 'SCHOOL DISTRICT' in entry.title:

            try:
              response = client.chat_postMessage(
                channel="slack-bots",
                text=f"Update in {entry.title} \n Docket sheet: {entry.link} \n Description: {ed}"
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

#
