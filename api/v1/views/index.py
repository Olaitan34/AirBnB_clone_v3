from api.v1.views import app_views
from models.engine.db_storage import count as cnt
# Importing the app_views module from api.v1.views

# Define a route /status on the app_views object
@app_views.route('/status')
def status():
    # Return a JSON response with status "OK"
    return Jsonify({'status':'ok'})

@app_views.route('/api/v1/stats')
def stats():
    # Return a cnt which is the representative of count
    return cnt