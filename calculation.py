def calculateMUSIC(params):
    location, gender, isMusician, age, \
    qc2, qc3, qc4, qc5, qc6, qc7, qc8, \
    qc9, qc10, qc11, qc12, qc13, qc14, \
    qc15, qc16, qc17, qc18, qc19, qc20,\
    qc21, qc22, qc23 = params
# calculation of big five genre
    # mellow = (int(qc6) + int(qc13) + int(qc11) + int(qc24))/4
    mellow = (int(qc6) + int(qc13) + int(qc11))/3
    unpretentious = (int(qc16) + int(qc5) + int(qc20))/3
    sophisticated = (int(qc3) + int(qc12) + int(qc2) + int(qc7) + int(qc4) + int(qc9) + int(qc15))/7
    # intense = (int(qc21) + int(qc17) + int(qc1) + int(qc10))/4
    intense = (int(qc21) + int(qc17) + int(qc10))/3
    contemporary = (int(qc18) + int(qc22) + int(qc8) + int(qc19))/4
    genres = [mellow, unpretentious, sophisticated, intense, contemporary]

    mellow = round(mellow, 4)
    unpretentious = round(unpretentious, 4)
    sophisticated = round(sophisticated, 4)
    intense = round(intense, 4)
    contemporary = round(contemporary, 4)

    return (mellow, unpretentious, sophisticated, intense, contemporary)