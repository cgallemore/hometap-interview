from flask import Blueprint, request

from hometap_interview.clients.house_canary import HouseCanaryClient
from hometap_interview.exceptions import RequiredParametersMissing

property_details_bp = Blueprint('property_details', __name__, url_prefix='/api/property/details')

@property_details_bp.route('', methods=['GET'])
def property_details():
    """
    Retrieve the property details from the HouseCanary Analytics API.  For reference, the API endpoint is
    documented here: https://api-docs.housecanary.com/#property-details
    """
    address = request.args.get('address', type=str)
    zipcode = request.args.get('zipcode', type=str)

    if address and zipcode:
        client = HouseCanaryClient()
        return client.get_property_details(address, zipcode)
    else:
        raise RequiredParametersMissing('The address and zipcode query paramters are required.')