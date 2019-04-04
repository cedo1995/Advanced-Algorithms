import sys
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

    def extractTime(self, orario):
        return orario[0:2], orario[2:]

    def minutesCounter(self, departure_time, arrival_time):
        # print("orario partenza ",departure_time, " orario arrivo ", arrival_time )
        minutes = sys.maxsize
        arrival_hours, arrival_minutes = self.extractTime(arrival_time[1:])
        departure_hours, departure_minutes = self.extractTime(departure_time[1:])
        arrival_minutes = int(arrival_hours) * 60 + int(arrival_minutes)
        departure_minutes = int(departure_hours) * 60 + int(departure_minutes)

        if departure_minutes <= arrival_minutes:
            minutes = arrival_minutes - departure_minutes

        return minutes