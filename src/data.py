import csv, os
from underground import SubwayFeed
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MTA_API_KEY")


def stop_name(stopID):
    name = ""
    with open("stops.csv", "r") as stops:
        reader = csv.reader(stops)
        for row in reader:
            if row[0] == stopID:
                name += row[1]
                if stopID.endswith("N"):
                    name += " Uptown"
                elif stopID.endswith("S"):
                    name += " Downtown"
                return name


def data(line):
    feed = SubwayFeed.get(line, api_key=API_KEY)
    data = feed.extract_stop_dict()
    result = []

    for route, stops_data in data.items():
        if route == line:
            route_info = []
            route_info.append(route)
            stations_info = []

            for stop, arrival_times in stops_data.items():
                formatted_times = [time.strftime("%I:%M %p") for time in arrival_times]
                stations_info.append(
                    {"stop": stop_name(stop), "arrival_times": formatted_times}
                )

            route_info.append(stations_info)
            result.append(route_info)

    return result
