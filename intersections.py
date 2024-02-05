from math import pi
import numpy as np
        

def countIntersections(radians, identifiers):

    chords = dict()
    #Fill the chords dictionary with ids and respective angles of start and end
    for radian, point in zip(radians, identifiers):
        id = point[1:]
        if id in chords:
            val = radian%(2*pi)
            if val>chords[id][0]:
                chords[id].append(radian % (2 * pi))
            else:
                chords[id] = [val,chords[id][0]]
        else:
            chords[id] = [radian % (2 * pi)]
    
    chordAngles = np.array(list(chords.values()))
    
    # Main idea: Two chords intersect if either the starting or ending angle (exclusive) of one chord lies within the range 
    #defined by the starting and ending angles of the other chord.

    
    # As the order is not consitent we have to calculate with both rows and columns
    condition1 = np.logical_and( chordAngles[:, 0] < chordAngles[:, 0, None] , chordAngles[:, 0, None] < chordAngles[:, 1])
    condition2 = np.logical_and( chordAngles[:, 0] < chordAngles[:, 1, None] , chordAngles[:, 1, None] < chordAngles[:, 1])


    xor_conditions = np.logical_xor(condition1, condition2)

    # Total number of intersections per each chord
    numIntersections = xor_conditions.sum()

    #divide by 2 to avoid duplicates
    return numIntersections//2


