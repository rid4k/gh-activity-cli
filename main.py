import requests
from enum import Enum

username = "kadirkattas"  # Replace with the desired GitHub username
github_api_url = f"https://api.github.com/users/{username}/events"

class Event(Enum):
    CommitCommentEvent = "CommitCommentEvent"
    CreateEvent = "CreateEvent"
    DeleteEvent = "DeleteEvent"
    DeploymentEvent = "DeploymentEvent"
    DeploymentStatusEvent = "DeploymentStatusEvent"
    ForkEvent = "ForkEvent"
    GollumEvent = "GollumEvent"
    IssueCommentEvent = "IssueCommentEvent"
    IssuesEvent = "IssuesEvent"
    MemberEvent = "MemberEvent"
    PublicEvent = "PublicEvent"
    PullRequestReviewCommentEvent = "PullRequestReviewCommentEvent"
    PullRequestReviewEvent = "PullRequestReviewEvent"
    PullRequestEvent = "PullRequestEvent"
    PushEvent = "PushEvent"
    ReleaseEvent = "ReleaseEvent"
    StatusEvent = "StatusEvent"
    WatchEvent = "WatchEvent"

response = requests.get(github_api_url)
if response.status_code == 200:
    events = response.json()
    for event in events:
        match event['type']:
            case Event.CommitCommentEvent.value:
                print(f"Commit Comment Event: {event['repo']['name']}")
            case Event.CreateEvent.value:
                print(f"Create Event: {event['repo']['name']}")
            case Event.DeleteEvent.value:
                print(f"Delete Event: {event['repo']['name']}")
            case Event.DeploymentEvent.value:
                print(f"Deployment Event: {event['repo']['name']}")
            case Event.DeploymentStatusEvent.value:
                print(f"Deployment Status Event: {event['repo']['name']}")
            case Event.ForkEvent.value:
                print(f"Fork Event: {event['repo']['name']}")
            case Event.GollumEvent.value:
                print(f"Gollum Event: {event['repo']['name']}")
            case Event.IssueCommentEvent.value:
                print(f"Issue Comment Event: {event['repo']['name']}")
            case Event.IssuesEvent.value:
                print(f"Issues Event: {event['repo']['name']}")
            case Event.MemberEvent.value:
                print(f"Member Event: {event['repo']['name']}")
            case Event.PublicEvent.value:
                print(f"Public Event: {event['repo']['name']}")
            case Event.PullRequestReviewCommentEvent.value:
                print(f"Pull Request Review Comment Event: {event['repo']['name']}")
            case Event.PullRequestReviewEvent.value:
                print(f"Pull Request Review Event: {event['repo']['name']}")
            case Event.PullRequestEvent.value:
                print(f"Pull Request Event: {event['repo']['name']}")
            case Event.PushEvent.value:
                print(f"Push Event: {event['repo']['name']}")
            case Event.ReleaseEvent.value:
                print(f"Release Event: {event['repo']['name']}")
            case Event.StatusEvent.value:
                print(f"Status Event: {event['repo']['name']}")
            case Event.WatchEvent.value:
                print(f"Watch Event: {event['repo']['name']}")
            case _:
                print(f"Unknown Event Type: {event['type']} in repository {event['repo']['name']}")
else:
    print(f"Failed to fetch events for user {username}. Status code: {response.status_code}")