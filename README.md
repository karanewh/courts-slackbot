# ⚖️ Courts Slackbot: Get alerts about updates or new cases of interest
This is a code repository for a bot that sends Slack messages about new or updated court cases based on court RSS feeds and selected criteria.

I created Courts Slackbot to solve a problem I experienced as a local education reporter in Pennsylvania: keeping track of lawsuits against school districts I covered. Sometimes I learned about lawsuits from advocacy groups or at board meetings, but daily checks of court dockets were not part of my routine. This bot automates that process.

## How it works
Courts Slackbot uses a Python script to parse entries from a list of RSS feeds for court dockets. It searches the title of each entry in each feed for key words. If those key words appear in an entry, it sends a Slack message containing the case title, a link to its docket sheet in Pacer and the description of the latest activity.

For my purposes, **bot.py** searches for the term "SCHOOL DISTRICT"; however, the script could be modified to use different key words that consistently appear in the titles of cases of interest, such as a specific agency name. It could also be set to search for a specific case number.

Using Github Actions, I have scheduled bot.py to run daily at 6 a.m. Eastern Time.

## Acknowledgements
In developing Courts Slackbot, I drew inspiration from Brad Heath's [Big Cases Twitter bot](https://github.com/bdheath/Big-Cases).
