from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
import json

class CrewRank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_id(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode="after")
    def validate_crew_ranks(self) -> "SpaceMission":
        if not any(
            member.rank in {CrewRank.commander, CrewRank.captain}
            for member in self.crew
        ):
            raise ValueError("Mission must have at least one Commander or Captain")

        return self

    @model_validator(mode="after")
    def validate_long_missions(self) -> "SpaceMission":
        if self.duration_days > 365:
            experienced_members = sum(
                member.years_experience >= 5
                for member in self.crew
            )

            if experienced_members * 2 < len(self.crew):
                raise ValueError(f"Long missions need 50% experienced crew (5+ years)")

        return self


    @model_validator(mode="after")
    def validate_crew_activity(self) -> "SpaceMission":
        if not all(
            member.is_active
            for member in self.crew
        ):
            raise ValueError("All crew members must be active")

        return self

def print_details(item: dict[str, object]) -> None:
    print("==============================================")

    try:
        mission = SpaceMission.model_validate(item)

    except ValueError as error:
         print("Expected validation error:")
         for error in error.errors():
            print(error['msg'])



    else:
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for crew_member in mission.crew:
            print(f" - {crew_member.name} ({crew_member.rank.value}) - {crew_member.specialization}")


def main() -> None:
    print("Space Missions Crew Validation")

    try:

        with open("../data_generator/generated_data/space_missions.json", "r") as file:
            inputs: list[dict[str, object]] = json.load(file)

        # print_details(inputs[0])
        for input in inputs:
            print_details(input)
            print()

    except OSError as error:
        print(f"OSError: {error}")


if __name__ == '__main__':
    main()
