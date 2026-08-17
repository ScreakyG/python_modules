from pydantic import BaseModel, Field, ValidationError, NaiveDatetime, model_validator
import json

from enum import Enum

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: NaiveDatetime
    location : str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_id(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID should start with 'AC'")
        return self

    @model_validator(mode="after")
    def validate_physical_reports(self) -> "AlienContact":
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def validate_telepathic_reports(self) -> "AlienContact":
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self


    @model_validator(mode="after")
    def validate_signal_stength(self) -> "AlienContact":
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Signals strength superior to 7.0 should include received messages")
        return self



def display_contact_infos(alien_contact: dict[str, object]) -> None:
    try:
        print("======================================\n")

        contact = AlienContact.model_validate(alien_contact)

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as error:
        print("Expected validation error:")
        for error in error.errors():
            print(error['msg'])


def main() -> None:
    print("Alien Contact Log Validation")

    try:
        with open("../data_generator/generated_data/alien_contacts.json", "r") as file:
            contacts = json.load(file)

        # for contact in contacts:
        #     display_contact_infos(contact)

        display_contact_infos(contacts[0])

    except OSError as error:
        print(f"File error: {error}")


if __name__ == '__main__':
    main()
