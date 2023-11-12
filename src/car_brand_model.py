from typing import Union

car_brand_model = {
	'SEAT': [
		'LEON III'
	],
	'Mazda': [
		'CX-3'
	]
}

def get_brand(subject: str) -> Union[str, None]:
	for brand in car_brand_model:
		if brand in subject:
			return brand
	else:
		return None
	
def get_model(subject: str, brand: str) -> Union[str, None]:
	try:
		models = car_brand_model[brand]
	except:
		return None
	for model in models:
		if model in subject:
			return model
	return None	
	