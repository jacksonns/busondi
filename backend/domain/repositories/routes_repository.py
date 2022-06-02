from backend.adapters.routes_repository_impl import RoutesRepositoryImpl

class RoutesRepository:

    def return_all_routes_from_stop(stop_id):
        return RoutesRepositoryImpl.return_all_routes_from_stop_impl(stop_id)
      
    def return_route_stop_by_id(stop_id, route_id):
        return RoutesRepositoryImpl.return_route_stop_by_id_impl(stop_id, route_id)
    
    def return_trips_from_route(route_id):
        return RoutesRepositoryImpl.return_trips_from_route_impl(route_id)
    
    def return_one_route_by_id(route_id):
        return RoutesRepositoryImpl.return_one_route_by_id_impl(route_id)