from pydantic import BaseModel


# I'm only modeling the basic pieces, this could be expanded over time to add
# additional data that would be required, since the requirements specified
# sewer, that's all that I'm adding, with the basic assessment piece.
class Property(BaseModel):
    sewer: str

class PropertyAssessment(BaseModel):
    tax_amount: float

class PropertyDetail(BaseModel):
    property: Property
    assessment: PropertyAssessment