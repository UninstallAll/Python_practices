def parse(feet2inches):
    parts = feet2inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {'feet':feet, 'inches':inches}
