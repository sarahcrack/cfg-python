place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name'], place['post_code'], place['street_number'])
print(place['location']['longitude'])
print(place['location']['latitude'])

location = place['location']
print(location['longitude'])
print(location['latitude'])
