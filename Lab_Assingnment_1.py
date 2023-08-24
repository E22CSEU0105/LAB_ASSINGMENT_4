class FlightTable:
    def __init__(self):
        self.matches = [
            {"location": "Mumbai", "team_01": "India", "team_02": "Sri Lanka", "timing": "DAY"},
            {"location": "Delhi", "team_01": "England", "team_02": "Australia", "timing": "DAY-NIGHT"},
            {"location": "Chennai", "team_01": "India", "team_02": "South Africa", "timing": "DAY"},
            {"location": "Indore", "team_01": "England", "team_02": "Sri Lanka", "timing": "DAY-NIGHT"},
            {"location": "Mohali", "team_01": "Australia", "team_02": "South Africa", "timing": "DAY-NIGHT"},
            {"location": "Delhi", "team_01": "India", "team_02": "Australia", "timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in [match["team_01"], match["team_02"]]:
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location_name):
        location_matches = []
        for match in self.matches:
            if match["location"] == location_name:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing_name):
        timing_matches = []
        for match in self.matches:
            if match["timing"] == timing_name:
                timing_matches.append(match)
        return timing_matches
    
flight_table = FlightTable()

print("Choose a search parameter:")
print("1. List of all the matches of a Team")
print("2. List of Matches on a Location")
print("3. List of Matches based on timing")

choice = int(input("Enter your choice: "))

if choice == 1:
    team_name = input("Enter team name: ")
    matches = flight_table.search_by_team(team_name)
elif choice == 2:
    location_name = input("Enter location name: ")
    matches = flight_table.search_by_location(location_name)
elif choice == 3:
    timing_name = input("Enter timing name: ")
    matches = flight_table.search_by_timing(timing_name)
else:
    print("Invalid choice")
    exit()

print("Match\tLocation\tTeam 01\tTeam 02\tTiming")
for match in matches:
    print(f"{matches.index(match)+1}\t{match['location']}\t{match['team_01']}\t{match['team_02']}\t{match['timing']}")