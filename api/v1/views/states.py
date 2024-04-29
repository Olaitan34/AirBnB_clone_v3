from api.v1.views import app_views
from flask import Flask, jsonify,abort
from models import storage
from models.state import State


@app_views.route('cccc', methods=['GET'])
def get_all_states():
    """
    Retrieves the list of all State objects
    """
    all_states = storage.all(State).values
    
    # Convert each State object to a dictionary using the to_dict() method
    state_dicts = [state.to_dict() for state in all_states]
    
    # Return the list of State objects as a JSON response
    return jsonify(state_dicts), 200

@app_views.route('/api/v1/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """REtrieve a specific state"""
    state = storage.get(state, state_id)
    
    if state is None:
        abort(404)
    return jsonify(state_id)
    
    
@app_views.route('DELETE /api/v1/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """REtrieve a specific state"""
    state = storage.get(state, state_id)
    
    if state is None:
        abort(404)
    state.delete(state)
    state.save()
    
    return make_response(jsonify({}), 200)        

@app_views.route('/api/v1/states', method=['POST'])
def create_object():
    """REtrieve a specific state"""
    
    if not request.get_json:
        abort(400, description="Not a JSON")
        
    if name not in request.get_json():
        abort(400, description="Missing name")
    
    obj = request.get_json()
    instance = State(**obj)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/api/v1/states/<state_id>', method=['PUT'])
def update_object():
    """To update the state"""
    state = storage.get(state, state_id)
    if not state:
        abort(404)
    data = request.get_json
    if not data:
        abort(404, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
        #save the updated state object
        storage.save()
        
        return jsonify(state.to_dict(), 200)