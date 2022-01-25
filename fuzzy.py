import numpy as np
import pandas as pd
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def transformAge(df):
    df['age'] = df['age'].map({
            "Under 18": 1, 
            "18 - 24": 21, 
            "25 - 34": 29, 
            "35 - 44": 40, 
            "45 - 54": 48, 
            "Above 55": 55,
        })
    return df

def fuzzification():
    # age
    age = np.arange(1, 90)
    age_young = fuzz.trapmf(age, [1, 1, 18, 34])
    age_mid = fuzz.trapmf(age, [18, 35, 44, 54])
    age_old = fuzz.trapmf(age, [44, 54, 90, 90])


    # bluegrass
    bluegrass = np.arange(1, 8)
    bluegrass_lo = fuzz.trapmf(bluegrass, [1, 1, 2, 4])
    bluegrass_mid = fuzz.trimf(bluegrass, [2, 4, 6])
    bluegrass_hi = fuzz.trapmf(bluegrass, [4, 6, 7, 7])

    # Blues
    blues = np.arange(1, 8)
    blues_lo = fuzz.trapmf(blues, [1, 1, 2, 4])
    blues_mid = fuzz.trimf(blues, [2, 4, 6])
    blues_hi = fuzz.trapmf(blues, [4, 6, 7, 7])

    # Classical
    classical = np.arange(1, 8)
    classical_lo = fuzz.trapmf(classical, [1, 1, 2, 4])
    classical_mid = fuzz.trimf(classical, [2, 4, 6])
    classical_hi = fuzz.trapmf(classical, [4, 6, 7, 7])

    # Country
    country = np.arange(1, 8)
    country_lo = fuzz.trapmf(country, [1, 1, 2, 4])
    country_mid = fuzz.trimf(country, [2, 4, 6])
    country_hi = fuzz.trapmf(country, [4, 6, 7, 7])

    # Dance/Electronica
    edm = np.arange(1, 8)
    edm_lo = fuzz.trapmf(edm, [1, 1, 2, 4])
    edm_mid = fuzz.trimf(edm, [2, 4, 6])
    edm_hi = fuzz.trapmf(edm, [4, 6, 7, 7])

    # Folk
    folk = np.arange(1, 8)
    folk_lo = fuzz.trapmf(folk, [1, 1, 2, 4])
    folk_mid = fuzz.trimf(folk, [2, 4, 6])
    folk_hi = fuzz.trapmf(folk, [4, 6, 7, 7])

    # Funk
    funk = np.arange(1, 8)
    funk_lo = fuzz.trapmf(funk, [1, 1, 2, 4])
    funk_mid = fuzz.trimf(funk, [2, 4, 6])
    funk_hi = fuzz.trapmf(funk, [4, 6, 7, 7])

    # Gospel
    gospel = np.arange(1, 8)
    gospel_lo = fuzz.trapmf(gospel, [1, 1, 2, 4])
    gospel_mid = fuzz.trimf(gospel, [2, 4, 6])
    gospel_hi = fuzz.trapmf(gospel, [4, 6, 7, 7])

    # Heavy Metal
    metal = np.arange(1, 8)
    metal_lo = fuzz.trapmf(metal, [1, 1, 2, 4])
    metal_mid = fuzz.trimf(metal, [2, 4, 6])
    metal_hi = fuzz.trapmf(metal, [4, 6, 7, 7])

    # World
    world = np.arange(1, 8)
    world_lo = fuzz.trapmf(world, [1, 1, 2, 4])
    world_mid = fuzz.trimf(world, [2, 4, 6])
    world_hi = fuzz.trapmf(world, [4, 6, 7, 7])

    # Jazz
    jazz = np.arange(1, 8)
    jazz_lo = fuzz.trapmf(jazz, [1, 1, 2, 4])
    jazz_mid = fuzz.trimf(jazz, [2, 4, 6])
    jazz_hi = fuzz.trapmf(jazz, [4, 6, 7, 7])

    # New Age
    new = np.arange(1, 8)
    new_lo = fuzz.trapmf(new, [1, 1, 2, 4])
    new_mid = fuzz.trimf(new, [2, 4, 6])
    new_hi = fuzz.trapmf(new, [4, 6, 7, 7])

    # Oldies
    oldies = np.arange(1, 8)
    oldies_lo = fuzz.trapmf(oldies, [1, 1, 2, 4])
    oldies_mid = fuzz.trimf(oldies, [2, 4, 6])
    oldies_hi = fuzz.trapmf(oldies, [4, 6, 7, 7])

    # Opera
    opera = np.arange(1, 8)
    opera_lo = fuzz.trapmf(opera, [1, 1, 2, 4])
    opera_mid = fuzz.trimf(opera, [2, 4, 6])
    opera_hi = fuzz.trapmf(opera, [4, 6, 7, 7])

    # Pop
    pop = np.arange(1, 8)
    pop_lo = fuzz.trapmf(pop, [1, 1, 2, 4])
    pop_mid = fuzz.trimf(pop, [2, 4, 6])
    pop_hi = fuzz.trapmf(pop, [4, 6, 7, 7])

    # Punk
    punk = np.arange(1, 8)
    punk_lo = fuzz.trapmf(punk, [1, 1, 2, 4])
    punk_mid = fuzz.trimf(punk, [2, 4, 6])
    punk_hi =  fuzz.trapmf(punk, [4, 6, 7, 7])

    # Rap/Hip Hop
    rap = np.arange(1, 8)
    rap_lo = fuzz.trapmf(rap, [1, 1, 2, 4])
    rap_mid = fuzz.trimf(rap, [2, 4, 6])
    rap_hi = fuzz.trapmf(rap, [4, 6, 7, 7])

    # Reggae
    reggae = np.arange(1, 8)
    reggae_lo = fuzz.trapmf(reggae, [1, 1, 2, 4])
    reggae_mid = fuzz.trimf(reggae, [2, 4, 6])
    reggae_hi = fuzz.trapmf(reggae, [4, 6, 7, 7])
    fig, ax = plt.subplots(nrows=1, figsize=(6, 3))

    # Religious
    religious = np.arange(1, 8)
    religious_lo = fuzz.trapmf(religious, [1, 1, 2, 4])
    religious_mid = fuzz.trimf(religious, [2, 4, 6])
    religious_hi = fuzz.trapmf(religious, [4, 6, 7, 7])

    # Rock
    rock = np.arange(1, 8)
    rock_lo = fuzz.trapmf(rock, [1, 1, 2, 4])
    rock_mid = fuzz.trimf(rock, [2, 4, 6])
    rock_hi = fuzz.trapmf(rock, [4, 6, 7, 7])

    # Soul/R&B
    rnb = np.arange(1, 8)
    rnb_lo = fuzz.trapmf(rnb, [1, 1, 2, 4])
    rnb_mid = fuzz.trimf(rnb, [2, 4, 6])
    rnb_hi = fuzz.trapmf(rnb, [4, 6, 7, 7])

    # Soundtracks/Theme Song
    soundtracks = np.arange(1, 8)
    soundtracks_lo = fuzz.trapmf(soundtracks, [1, 1, 2, 4])
    soundtracks_mid = fuzz.trimf(soundtracks, [2, 4, 6])
    soundtracks_hi = fuzz.trapmf(soundtracks, [4, 6, 7, 7])

    # Mellow
    mellow = np.arange(1, 8)
    mellow_lo = fuzz.trapmf(mellow, [1, 1, 2, 4])
    mellow_mid = fuzz.trimf(mellow, [2, 4, 6])
    mellow_hi = fuzz.trapmf(mellow, [4, 6, 7, 7])

    # Mellow
    mellow = np.arange(1, 8)
    mellow_lo = fuzz.trapmf(mellow, [1, 1, 2, 4])
    mellow_mid = fuzz.trimf(mellow, [2, 4, 6])
    mellow_hi = fuzz.trapmf(mellow, [4, 6, 7, 7])

    # Unpretentious
    unpretentious = np.arange(1, 8)
    unpretentious_lo = fuzz.trapmf(unpretentious, [1, 1, 2, 4])
    unpretentious_mid = fuzz.trimf(unpretentious, [2, 4, 6])
    unpretentious_hi = fuzz.trapmf(unpretentious, [4, 6, 7, 7])

    # Sophisticated
    sophisticated = np.arange(1, 8)
    sophisticated_lo = fuzz.trapmf(sophisticated, [1, 1, 2, 4])
    sophisticated_mid = fuzz.trimf(sophisticated, [2, 4, 6])
    sophisticated_hi = fuzz.trapmf(sophisticated, [4, 6, 7, 7])

    # Intense
    intense = np.arange(1, 8)
    intense_lo = fuzz.trapmf(intense, [1, 1, 2, 4])
    intense_mid = fuzz.trimf(intense, [2, 4, 6])
    intense_hi = fuzz.trapmf(intense, [4, 6, 7, 7])

    # Contemporary
    contemporary = np.arange(1, 8)
    contemporary_lo = fuzz.trapmf(contemporary, [1, 1, 2, 4])
    contemporary_mid = fuzz.trimf(contemporary, [2, 4, 6])
    contemporary_hi = fuzz.trapmf(contemporary, [4, 6, 7, 7])


# def fuzzy_system(row):
    age_level_young = fuzz.interp_membership(age, age_young, row[0])
    age_level_mid = fuzz.interp_membership(age, age_mid, row[0])
    age_level_old = fuzz.interp_membership(age, age_old, row[0])

    bluegrass_level_lo = fuzz.interp_membership(bluegrass, bluegrass_lo, row[1])
    bluegrass_level_mid = fuzz.interp_membership(bluegrass, bluegrass_mid, row[1])
    bluegrass_level_hi = fuzz.interp_membership(bluegrass, bluegrass_hi, row[1])

    blues_level_lo = fuzz.interp_membership(blues, blues_lo, row[2])
    blues_level_mid = fuzz.interp_membership(blues, blues_mid, row[2])
    blues_level_hi = fuzz.interp_membership(blues, blues_hi, row[2])

    classical_level_lo = fuzz.interp_membership(classical, classical_lo, row[3])
    classical_level_mid = fuzz.interp_membership(classical, classical_mid, row[3])
    classical_level_hi = fuzz.interp_membership(classical, classical_hi, row[3])

    country_level_lo = fuzz.interp_membership(country, country_lo, row[4])
    country_level_mid = fuzz.interp_membership(country, country_mid, row[4])
    country_level_hi = fuzz.interp_membership(country, country_hi, row[4])

    edm_level_lo = fuzz.interp_membership(edm, edm_lo, row[5])
    edm_level_mid = fuzz.interp_membership(edm, edm_mid, row[5])
    edm_level_hi = fuzz.interp_membership(edm, edm_hi, row[5])

    folk_level_lo = fuzz.interp_membership(folk, folk_lo, row[6])
    folk_level_mid = fuzz.interp_membership(folk, folk_mid, row[6])
    folk_level_hi = fuzz.interp_membership(folk, folk_hi, row[6])

    funk_level_lo = fuzz.interp_membership(funk, funk_lo, row[7])
    funk_level_mid = fuzz.interp_membership(funk, funk_mid, row[7])
    funk_level_hi = fuzz.interp_membership(funk, funk_hi, row[7])

    gospel_level_lo = fuzz.interp_membership(gospel, gospel_lo, row[8])
    gospel_level_mid = fuzz.interp_membership(gospel, gospel_mid, row[8])
    gospel_level_hi = fuzz.interp_membership(gospel, gospel_hi, row[8])

    metal_level_lo = fuzz.interp_membership(metal, metal_lo, row[9])
    metal_level_mid = fuzz.interp_membership(metal, metal_mid, row[9])
    metal_level_hi = fuzz.interp_membership(metal, metal_hi, row[9])

    world_level_lo = fuzz.interp_membership(world, world_lo, row[10])
    world_level_mid = fuzz.interp_membership(world, world_mid, row[10])
    world_level_hi = fuzz.interp_membership(world, world_hi, row[10])

    jazz_level_lo = fuzz.interp_membership(jazz, jazz_lo, row[11])
    jazz_level_mid = fuzz.interp_membership(jazz, jazz_mid, row[11])
    jazz_level_hi = fuzz.interp_membership(jazz, jazz_hi, row[11])

    new_level_lo = fuzz.interp_membership(new, new_lo, row[12])
    new_level_mid = fuzz.interp_membership(new, new_mid, row[12])
    new_level_hi = fuzz.interp_membership(new, new_hi, row[12])

    oldies_level_lo = fuzz.interp_membership(oldies, oldies_lo, row[13])
    oldies_level_mid = fuzz.interp_membership(oldies, oldies_mid, row[13])
    oldies_level_hi = fuzz.interp_membership(oldies, oldies_hi, row[13])

    opera_level_lo = fuzz.interp_membership(opera, opera_lo, row[14])
    opera_level_mid = fuzz.interp_membership(opera, opera_mid, row[14])
    opera_level_hi = fuzz.interp_membership(opera, opera_hi, row[14])

    pop_level_lo = fuzz.interp_membership(pop, pop_lo, row[15])
    pop_level_mid = fuzz.interp_membership(pop, pop_mid, row[15])
    pop_level_hi = fuzz.interp_membership(pop, pop_hi, row[15])

    punk_level_lo = fuzz.interp_membership(punk, punk_lo, row[16])
    punk_level_mid = fuzz.interp_membership(punk, punk_mid, row[16])
    punk_level_hi = fuzz.interp_membership(punk, punk_hi, row[16])

    rap_level_lo = fuzz.interp_membership(rap, rap_lo, row[17])
    rap_level_mid = fuzz.interp_membership(rap, rap_mid, row[17])
    rap_level_hi = fuzz.interp_membership(rap, rap_hi, row[17])

    reggae_level_lo = fuzz.interp_membership(reggae, reggae_lo, row[18])
    reggae_level_mid = fuzz.interp_membership(reggae, reggae_mid, row[18])
    reggae_level_hi = fuzz.interp_membership(reggae, reggae_hi, row[18])

    religious_level_lo = fuzz.interp_membership(religious, religious_lo, row[19])
    religious_level_mid = fuzz.interp_membership(religious, religious_mid, row[19])
    religious_level_hi = fuzz.interp_membership(religious, religious_hi, row[19])

    rock_level_lo = fuzz.interp_membership(rock, rock_lo, row[20])
    rock_level_mid = fuzz.interp_membership(rock, rock_mid, row[20])
    rock_level_hi = fuzz.interp_membership(rock, rock_hi, row[20])

    rnb_level_lo = fuzz.interp_membership(rnb, rnb_lo, row[21])
    rnb_level_mid = fuzz.interp_membership(rnb, rnb_mid, row[21])
    rnb_level_hi = fuzz.interp_membership(rnb, rnb_hi, row[21])

    soundtracks_level_lo = fuzz.interp_membership(soundtracks, soundtracks_lo, row[22])
    soundtracks_level_mid = fuzz.interp_membership(soundtracks, soundtracks_mid, row[22])
    soundtracks_level_hi = fuzz.interp_membership(soundtracks, soundtracks_hi, row[22])


    # Mellow (edm, new age, world)
    fire_rule_1a = np.fmax(edm_level_hi, new_level_hi)
    fire_rule_1b = np.fmax(fire_rule_1a, world_level_hi)
    fire_rule_mellow_a = np.fmin(fire_rule_1b, mellow_hi)

    fire_rule_2a = np.fmax(edm_level_mid, new_level_mid)
    fire_rule_2b = np.fmax(fire_rule_2a, world_level_mid)
    fire_rule_mellow_b = np.fmin(fire_rule_2b, mellow_mid)

    fire_rule_3a = np.fmax(edm_level_lo, new_level_lo)
    fire_rule_3b = np.fmax(fire_rule_3a, world_level_lo)
    fire_rule_mellow_c = np.fmin(fire_rule_3b, mellow_lo)

    fire_rule_mellow_clip = np.fmax(fire_rule_mellow_a, fire_rule_mellow_b)
    fire_rule_mellow = np.fmax(fire_rule_mellow_clip, fire_rule_mellow_c)

    # Unpretentious (pop, country, religious)
    fire_rule_3a = np.fmax(pop_level_hi, country_level_hi)
    fire_rule_3b = np.fmax(fire_rule_3a, religious_level_hi)
    fire_rule_un_a = np.fmin(fire_rule_3b, unpretentious_hi)

    fire_rule_4a = np.fmax(pop_level_mid, country_level_mid)
    fire_rule_4b = np.fmax(fire_rule_4a, religious_level_mid)
    fire_rule_un_b = np.fmin(fire_rule_4b, unpretentious_mid)

    fire_rule_5a = np.fmax(pop_level_lo, country_level_lo)
    fire_rule_5b = np.fmax(fire_rule_5a, religious_level_lo)
    fire_rule_un_c = np.fmin(fire_rule_5b, unpretentious_lo)

    fire_rule_un_clip = np.fmax(fire_rule_un_a, fire_rule_un_b)
    fire_rule_un = np.fmax(fire_rule_un_clip, fire_rule_un_c)

    # Sophisticated (blues, jazz, bluegrass, folk, classical, gospel, opera)
    fire_rule_6a = np.fmax(blues_level_hi, jazz_level_hi)
    fire_rule_6b = np.fmax(fire_rule_6a, bluegrass_level_hi)
    fire_rule_6c = np.fmax(fire_rule_6b, folk_level_hi)
    fire_rule_6d = np.fmax(fire_rule_6c, classical_level_hi)
    fire_rule_6e = np.fmax(fire_rule_6d, gospel_level_hi)
    fire_rule_6f = np.fmax(fire_rule_6e, opera_level_hi)
    fire_rule_sop_a = np.fmin(fire_rule_6f, sophisticated_hi)

    fire_rule_7a = np.fmax(blues_level_mid, jazz_level_mid)
    fire_rule_7b = np.fmax(fire_rule_7a, bluegrass_level_mid)
    fire_rule_7c = np.fmax(fire_rule_7b, folk_level_mid)
    fire_rule_7d = np.fmax(fire_rule_7c, classical_level_mid)
    fire_rule_7e = np.fmax(fire_rule_7d, gospel_level_mid)
    fire_rule_7f = np.fmax(fire_rule_7e, opera_level_mid)
    fire_rule_sop_b = np.fmin(fire_rule_7f, sophisticated_mid)

    fire_rule_8a = np.fmax(blues_level_hi, jazz_level_hi)
    fire_rule_8b = np.fmax(fire_rule_8a, bluegrass_level_hi)
    fire_rule_8c = np.fmax(fire_rule_8b, folk_level_hi)
    fire_rule_8d = np.fmax(fire_rule_8c, classical_level_hi)
    fire_rule_8e = np.fmax(fire_rule_8d, gospel_level_hi)
    fire_rule_8f = np.fmax(fire_rule_8e, opera_level_hi)
    fire_rule_sop_c = np.fmin(fire_rule_8f, sophisticated_hi)

    fire_rule_sop_clip = np.fmax(fire_rule_sop_a, fire_rule_sop_b)
    fire_rule_sop = np.fmax(fire_rule_sop_clip, fire_rule_sop_c)

    # Intense (rock, punk, heavy metal)
    fire_rule_9a = np.fmax(rock_level_hi, punk_level_hi)
    fire_rule_9b = np.fmax(fire_rule_9a, metal_level_hi)
    fire_rule_int_a = np.fmin(fire_rule_9b, intense_hi)

    fire_rule_10a = np.fmax(rock_level_mid, punk_level_mid)
    fire_rule_10b = np.fmax(fire_rule_10a, metal_level_mid)
    fire_rule_int_b = np.fmin(fire_rule_10b, intense_mid)

    fire_rule_11a = np.fmax(rock_level_lo, punk_level_lo)
    fire_rule_11b = np.fmax(fire_rule_11a, metal_level_lo)
    fire_rule_int_c = np.fmin(fire_rule_11b, intense_lo)

    fire_rule_int_clip = np.fmax(fire_rule_int_a, fire_rule_int_b)
    fire_rule_int = np.fmax(fire_rule_int_clip, fire_rule_int_c)

    # Contemporary (rap, rnb, funk, reggae)
    fire_rule_11a = np.fmax(rap_level_hi, rnb_level_hi)
    fire_rule_11b = np.fmax(fire_rule_11a, funk_level_hi)
    fire_rule_11c = np.fmax(fire_rule_11b, reggae_level_hi)
    fire_rule_cont_a = np.fmin(fire_rule_11c, intense_hi)

    fire_rule_12a = np.fmax(rock_level_mid, punk_level_mid)
    fire_rule_12b = np.fmax(fire_rule_12a, metal_level_mid)
    fire_rule_12c = np.fmax(fire_rule_12b, reggae_level_mid)
    fire_rule_cont_b = np.fmin(fire_rule_12c, intense_mid)

    fire_rule_13a = np.fmax(rock_level_lo, punk_level_lo)
    fire_rule_13b = np.fmax(fire_rule_13a, metal_level_lo)
    fire_rule_13c = np.fmax(fire_rule_13b, reggae_level_lo)
    fire_rule_cont_c = np.fmin(fire_rule_13c, intense_lo)

    fire_rule_cont_clip = np.fmax(fire_rule_cont_a, fire_rule_cont_b)
    fire_rule_cont = np.fmax(fire_rule_cont_clip, fire_rule_cont_c)

    final_out = []
    fuzzy_output_dict = {}
    defuzz_mellow = fuzz.defuzz(mellow, fire_rule_mellow, 'centroid')
    fuzzy_output_dict['mellow_fuzz'] = defuzz_mellow


    defuzz_un = fuzz.defuzz(unpretentious, fire_rule_un, 'centroid')
    fuzzy_output_dict['Unpretentious'] = defuzz_un

    defuzz_sop = fuzz.defuzz(sophisticated, fire_rule_sop, 'mom')
    fuzzy_output_dict['Sophisticated'] = defuzz_sop

    defuzz_int = fuzz.defuzz(intense, fire_rule_int, 'centroid')
    fuzzy_output_dict['Intense'] = defuzz_int

    defuzz_cont = fuzz.defuzz(contemporary, fire_rule_cont, 'centroid')
    fuzzy_output_dict['Contemporary'] = defuzz_cont

    row['Mellow'] = fuzzy_output_dict['Mellow'] 
    row['Unpretentious'] = fuzzy_output_dict['Unpretentious'] 
    row['Sophisticated'] = fuzzy_output_dict['Sophisticated'] 
    row['Intense'] = fuzzy_output_dict['Intense'] 
    row['Contemporary'] = fuzzy_output_dict['Contemporary'] 

    # display(pd.DataFrame(row))
    return row
