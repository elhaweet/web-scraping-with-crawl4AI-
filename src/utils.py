import csv
from pydantic import BaseModel

def is_duplicated(record: str, seen_names: set) -> bool:
    return record in seen_names

def save_data_to_csv(records: list, data_struct: BaseModel, filename: str):
    if not records:
        print("No records to save.")
        return

    # Use field names from the PydantiAc data model
    fieldnames = data_struct.model_fields.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Saved {len(records)} records to '{filename}'.")
