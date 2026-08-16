from pydantic import BaseModel, Field, ValidationError, NaiveDatetime
import json


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: NaiveDatetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def display_stations_infos(station: dict[str, object]) -> None:
    try:
        print("======================================\n")

        space_station = SpaceStation.model_validate(station)

        print("Valid station created:")
        print(f"ID: {space_station.station_id}")
        print(f"Name: {space_station.name}")
        print(f"Crew: {space_station.crew_size} people")
        print(f"Power: {space_station.power_level}%")
        print(f"Oxygen: {space_station.oxygen_level}%")
        print(f"Status: {space_station.is_operational}")
        print(f"Last maintenance: {space_station.last_maintenance}")
        if space_station.notes:
            print(f"Notes: {space_station.notes}")

    except ValidationError as error:
        for error in error.errors():
            print(error['msg'])


def main() -> None:
    print("Space Station Data Validation")

    try:
        with open("../data_generator/generated_data/space_stations.json", "r") as file:
            stations = json.load(file)

        for station in stations:
            display_stations_infos(station)

    except OSError as error:
        print(f"File error: {error}")


if __name__ == '__main__':
    main()
