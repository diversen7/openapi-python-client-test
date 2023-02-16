from swagger_petstore_open_api_3_0_client import Client, AuthenticatedClient
from swagger_petstore_open_api_3_0_client.models.pet import Pet
from swagger_petstore_open_api_3_0_client.api.pet import get_pet_by_id, add_pet, update_pet

import sys 




client = AuthenticatedClient( base_url="https://petstore3.swagger.io/api/v3", token="special-key", raise_on_unexpected_status=True)
# Client.raise_on_unexpected_status = True

def get_pet(id) -> Pet:
    pet: Pet = get_pet_by_id.sync(pet_id=id, client=client)
    return pet


pet = get_pet(1000)
print(pet)

sys.exit()
pet.id = 100
pet.name = 'Dennis The Dish Fish'

add_pet.sync(client=client, form_data=pet, json_body=pet)

pet.id = 101
update_pet.sync(client=client, form_data=pet, json_body=pet)



