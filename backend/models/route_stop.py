from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, ForeignKey, Integer

db_route_stop = SQLAlchemy()

class RouteStop(db_route_stop.Model):

    __tablename__ = 'route_stop'

    route_stop_id = Column(Integer, primary_key = True)
    route_id = Column(String, ForeignKey('routes.route_id'))
    stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    stop_sequence = Column(Integer)

    def __init__(self, route_stop_id, route_id, stop_id, stop_sequence):
        self.route_stop_id = route_stop_id
        self.route_id = route_id
        self.stop_id = stop_id
        self.stop_sequence = stop_sequence