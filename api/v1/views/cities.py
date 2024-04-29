from flask import jsonify, abort, request
from models.city import City
from api.v1.views  import app_views, storage


@app_views.route('/states/<state_id>/cities', method=['GET'],
                strict_slashes=False)
def CityByState(state_id):
    """retrives all cities in a state"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    
    # Get the list of cities associated with the state
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', method=['GET'],
                strict_slashes=False)
def get_city(city_id):
    """To Retrive cities"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route('cities/<city_id>', method=['POST'],
                strict_slashes=False)
def create_city(city_id):
    """This is used to create non existing cities"""
    Cities = request.get_json(silent=True)
    if not Cities:
        abort(400, description="NOT a JSON")
        
    if not storage.get("State", str(state_id)):
        abort(404)
    
    if "name" not in Cities:
        abort(404, description="Missing name")
    
    Cities["state_id"] = state_id
    
    new_city = City(**Cities)
    new_city.save()
    res = jsonify(new_city.to_json())
    res.status_code = 201
    
    return res

@app_views.route("cities/<city_id>",  methods=["PUT"], strict_slashes=False)
def city_put(city_id):
    """
    updates specific City object by ID
    :param city_id: city object ID
    :return: city object and 200 on success, or 400 or 404 on failure
    """
    city_json = request.get_json(silent=True)
    if city_json is None:
        abort(400, 'Not a JSON')
    fetched_obj = storage.get("City", str(city_id))
    if fetched_obj is None:
        abort(404)
    for key, val in city_json.items():
        if key not in ["id", "created_at", "updated_at", "state_id"]:
            setattr(fetched_obj, key, val)
    fetched_obj.save()
    return jsonify(fetched_obj.to_json())
@app_views.route('cities/<city_id>', method=['DELETE'],
                strict_slashes=False)
def del_cities(city_id):
    """To delete cities"""
    get_cit = storage.get(City, city_id)
    if not get_cit:
        abort(404)
    
    storage.delete(get_cit)
    storage.save()
    
    return jsonify({})