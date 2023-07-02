import requests
import math
from datetime import datetime
import config


class HospitalFinder:
    def __init__(self):
        self.api_key = config.API_KEYS.get("API_KEY2")

    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        # Calculate the distance between two coordinates using the Haversine formula
        R = 6371  # Radius of the Earth in kilometers

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = (dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * (dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance

    def get_nearby_hospitals(self, latitude, longitude):
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=hospital&keyword=devlet%20hastanesi,%20özel%20hastane&key={self.api_key}"
        response = requests.get(url).json()

        hospitals = []

        for result in response["results"]:
            hospital_name = result["name"]
            hospital_address = result["vicinity"]
            hospital_location = result["geometry"]["location"]
            place_id = result["place_id"]
            hospitals.append(
                {
                    "name": hospital_name,
                    "address": hospital_address,
                    "location": hospital_location,
                    "place_id": place_id,
                }
            )

        # Sort the hospitals based on their distances from the user's location
        hospitals = sorted(
            hospitals,
            key=lambda x: self.calculate_distance(
                latitude, longitude, x["location"]["lat"], x["location"]["lng"]
            ),
        )

        return hospitals

    def get_opening_hours(self, place_id):
        url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=opening_hours&key={self.api_key}"
        response = requests.get(url).json()

        if "opening_hours" in response["result"]:
            opening_hours = response["result"]["opening_hours"]["periods"]
            return opening_hours
        return None

    def find_nearest_open_hospital(self, latitude, longitude):
        current_time = datetime.now()

        hospitals = self.get_nearby_hospitals(latitude, longitude)

        nearest_hospital_data = []
        nearest_hospital = None
        nearest_distance = float("inf")
        nearest_open_24h = False

        for hospital in hospitals:
            place_id = hospital["place_id"]
            hospital_name = hospital["name"]
            hospital_location = hospital["location"]
            hospital_address = hospital["address"]

            opening_hours = self.get_opening_hours(place_id)

            if opening_hours:
                all_days_open_24h = True
                for period in opening_hours:
                    if not period.get("open", {}).get("time") == "0000":
                        all_days_open_24h = False
                        break

                if all_days_open_24h:
                    distance = self.calculate_distance(
                        latitude,
                        longitude,
                        hospital_location["lat"],
                        hospital_location["lng"],
                    )
                    if distance < nearest_distance:
                        nearest_hospital = hospital_name
                        nearest_distance = distance
                        nearest_open_24h = True
                else:
                    for period in opening_hours:
                        if period.get("open", {}).get("day") == current_time.weekday():
                            opening_time = datetime.strptime(
                                period["open"]["time"], "%H%M"
                            ).strftime("%H:%M")
                            if "close" in period:
                                closing_time = datetime.strptime(
                                    period["close"]["time"], "%H%M"
                                ).strftime("%H:%M")
                                if (
                                    opening_time
                                    <= current_time.strftime("%H:%M")
                                    <= closing_time
                                ):
                                    distance = self.calculate_distance(
                                        latitude,
                                        longitude,
                                        hospital_location["lat"],
                                        hospital_location["lng"],
                                    )
                                    if distance < nearest_distance:
                                        nearest_hospital = hospital_name
                                        nearest_distance = distance
                                        nearest_open_24h = False

        if nearest_open_24h:
            if hospitals:
                nearest_hospital_data.append(
                    {
                        "name": hospitals[0]["name"],
                        "address": hospitals[0]["address"],
                        "open_24h": nearest_open_24h,
                        "location": hospitals[0]["location"],
                    }
                )
                return nearest_hospital_data
            else:
                return None

    def get_nearby_pharmacy(self, latitude, longitude):
        try:
            url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=pharmacy&keyword=eczane&language=tr&key={self.api_key}"
            response = requests.get(url).json()

            pharmacies = []

            for result in response["results"]:
                pharmacy_name = result["name"]
                pharmacy_address = result["vicinity"]
                pharmacy_location = result["geometry"]["location"]
                pharmacy = result["place_id"]
                pharmacies.append(
                    {
                        "name": pharmacy_name,
                        "address": pharmacy_address,
                        "location": pharmacy_location,
                        "place_id": pharmacy,
                    }
                )

            # Sort the hospitals based on their distances from the user's location
            pharmacies = sorted(
                pharmacies,
                key=lambda x: self.calculate_distance(
                    latitude, longitude, x["location"]["lat"], x["location"]["lng"]
                ),
            )

            return pharmacies
        except Exception as e:
            print(f"Error is here {e}")

    def find_the_nearest_pharmacy(self, latitude, longitude):
        pharmacies = self.get_nearby_pharmacy(latitude, longitude)

        if pharmacies:
            nearest_pharmacy = pharmacies[0]
            nearest_pharmacy_data = {
                "name": nearest_pharmacy["name"],
                "address": nearest_pharmacy["address"],
                "location": nearest_pharmacy["location"],
            }
            return nearest_pharmacy_data
        else:
            return None
