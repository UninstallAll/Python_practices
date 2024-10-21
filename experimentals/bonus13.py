feet2inches = input("Enter feet and inches: ")

def parse(feet2inches):
    parts = feet2inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet, 'inches':inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # return f'{feet} feet and {inches} inches is equal to {meter} meters'
    return meters


parsed = parse(feet2inches)
result = convert(parsed['feet'], parsed['inches'])

print(f'{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters')


print(result)


if result < 1:
    print('Kid is too small')

else:
    print('Kid is OK')
