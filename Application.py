from libs.bottle import route, static_file, run
import json

from services.activities.ActivityService import allActivities

@route('/api/activities')
def activities():
    activities = allActivities()
    return json.dumps(activities)

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

run(host='localhost', port=8080)
