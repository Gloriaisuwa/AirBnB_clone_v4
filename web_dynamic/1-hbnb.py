#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template, url_for
from models import storage
import uuidi

# flask setup
app = Flask(_name_)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# start flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after the request, the current SQLAlchemy Session is terminated
    by invoking the .close() method (also known as .remove())
    """
    storage.close()


@app.route('/1-hbnb')
def hbnb_filters(the_id=None):
    """
    handles request for template containing states, cities & amentities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('1-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)


if _name_ == "_main_":
    """ MAIN Flask App"""
    app.run(host=host, port=port)
