from fastapi import FastAPI
from enum import Enum


app = FastAPI()


# Basic FastAPI endpoint:
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


# Endpoint that requires an int as a path parameter:
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # If the item_id param can't be parsed as an int, this route
    # will respond with 422 and { detail: [ {errorObject} ] }
    return {"item_id": item_id}

# Can define an Enum class if there's a use case for a path parameter
# needing to be validated against limited/predefined values/datatypes:
class GrandTour(str, Enum):
    giro = "giro"
    tour = "tour"
    vuelta = "vuelta"

# Endpoint that requires one of three specific strings as a path parameter:
    # If the tour_name param is not a member of the GrandTour enum,
	# this route will respond with 422 and { detail: [ {errorObject} ] }
@app.get("/grand_tours/{tour_name}")
async def get_grand_tour(tour_name: GrandTour):
    # Value of tour_name parameter will be an enum member, so
    # can compare against the GrandTour.giro enum member:
    if tour_name is GrandTour.giro: # Python reminder: "is" checks for reference equality
		# The tour_name enum member gets converted to its actual value:
        return {"tour_name": tour_name, "2023_winner": "Primož Roglič! 🇸🇮"}
    
    # Can also use the enum member's value for comparison:
    if tour_name.value == "tour":
        return {"tour_name": tour_name, "2023_winner": "Jonas Vingegaard! 🇩🇰"}
    
    return {"tour_name": tour_name, "2023_winner": "Sepp Kuss! 🇺🇸"}
