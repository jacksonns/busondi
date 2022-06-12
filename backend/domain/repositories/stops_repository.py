from backend.adapters.stops_repository_impl import StopsRepositoryImpl

class StopsRepository:
    
    def return_all_stops():
        return StopsRepositoryImpl.return_all_stops_impl()

    def return_stop_by_id(stop_id):
        return StopsRepositoryImpl.return_stop_by_id_impl(stop_id)

    def return_all_stops_in_list(stops_list):
        return StopsRepositoryImpl.return_all_stops_in_list_impl(stops_list)