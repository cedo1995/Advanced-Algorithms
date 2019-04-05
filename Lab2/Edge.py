class Edge:
    def __init__(self, departure_time, arrival_time, run_id, id_line, id_departure_station, id_arrival_station):
        """
        :param departure_time: quando parte
        :param arrival_time: quando il bus arriva
        :param run_id: 01031
        :param id_line: AVL
        :param id_departure_station: stazione di partenza del bus
        :param id_arrival_station: stazione in cui il bus arriva
        """
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.run_id = run_id
        self.id_line = id_line
        self.id_departure_station = id_departure_station
        self.id_arrival_station = id_arrival_station
