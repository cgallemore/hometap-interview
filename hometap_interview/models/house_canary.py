from pydantic import BaseModel


# I'm only modeling the basic pieces, this could be expanded over time to add
# additional data that would be required, since the requirements specified
# sewer, that's all that I'm adding, with the basic assessment piece.
# Note, I chose to return the raw string value (e.g. municipal, septic, etc) from
# the API vs doing something like has_septic and returning a bool.  I'd probably
# want to clarify this with product what we truly want here.
class Property(BaseModel):
    sewer: str

class PropertyAssessment(BaseModel):
    tax_amount: float

class PropertyDetail(BaseModel):
    property: Property
    assessment: PropertyAssessment