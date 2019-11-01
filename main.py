import gitlab
import simplejson as json

from quart import Quart, request


LGTM_SUBMATCHES = ("lgtm", "looks good to me", "+1", "+2")
gl = gitlab.Gitlab('http://172.17.0.1', private_token='eyWKr-udMh6rsXNkbnfv')

app = Quart(__name__)

def read_config():
    pass

def handle_merge_request(merge_request_data):
    print("GOT A NEW MERGE REQUEST")

def handle_comment(merge_request_data):
    print("GOT A NEW lgtm COMMENT")

@app.route('/', methods=['POST'])
async def index():
    raw_event_data = await request.get_data()
    event_data = json.loads(raw_event_data)
    if event_data['object_kind'] == 'merge_request' and event_data['user']['username'] != 'gitlab_lgtm_bot'
        handle_merge_request(event_data)
    elif event_data['object_kind'] == "note" and event_data['object_attributes']['noteable_type'] == 'MergeRequest' and any(s in event_data['object_attributes']['note'].lower() for s in LGTM_SUBMATCHES):
        handle_comment(event_data)
    #mr = project.mergerequests.get(mr_id)
    print(event_data)
    return event_data
