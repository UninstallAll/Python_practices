feet2inches = input("Enter feet and inches: ")

def convert(feet2inches):
    parts = feet2inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])

    meter = feet * 0.3048 + inches * 0.0254
    # return f'{feet} feet and {inches} inches is equal to {meter} meters'
    return meter

print(convert(feet2inches))
result = convert(feet2inches)

if result < 1:
    print('Kid is too small')
else:
    print('Kid is OK')

