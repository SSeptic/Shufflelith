import inquirer, json, random

##beginning dialogue, selecting biome categories to shuffle by
print('select with space, progress with enter, navigate with arrows')
questions = [
  inquirer.Checkbox('categories',
                    message = "Select categories to classify by",
                    choices = ['Beaches', 'Mountains', 'Deserts (does not touch badland biomes)', 'Mesas', 'Replace All Remaining Biomes', 'Skylands (Can only replace with Skylands)', 'Oceans (Can only replace with oceans)','Rivers'],
                    ),
]
##I convert a list (answers['categories']) to another list purely for the ease of typing
answers = inquirer.prompt(questions)
lst = answers['categories']

##the following series of functions groups biomes based on type and replaces all mentions of biome with a keyphrase

def replace_biomes_with_beach(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_beach(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_beach(elem) for elem in obj]
    elif obj in ['terralith:gravel_beach', 'minecraft:beach', 'minecraft:snowy_beach', 'minecraft:stony_shore']:
        return "Beach"
    else:
        return obj

def replace_biomes_with_mountain(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_mountain(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_mountain(elem) for elem in obj]
    elif obj in ['terralith:basalt_cliffs', 'terralith:blooming_plateau', 'terralith:caldera', 'terralith:emerald_peaks', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:haze_mountain', 'terralith:jungle_mountains', 'terralith:painted_mountains', 'terralith:rocky_mountains', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:stony_spires', 'terralith:volcanic_peaks', 'terralith:white_cliffs', 'terralith:windswept_spires', 'terralith:yosemite_cliffs', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks']:
        return "Mountain"
    else:
        return obj

def replace_biomes_with_desert(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_desert(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_desert(elem) for elem in obj]
    elif obj in ['minecraft:desert', 'terralith:desert_canyon', 'terralith:lush_desert', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:lush_valley', 'terralith:red_oasis', 'terralith:sandstone_valley', 'terralith:ancient_sands', 'terralith:gravel_desert', 'minecraft:snowy_beach']:
        return "Desert"
    else:
        return obj

def replace_biomes_with_mesa(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_mesa(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_mesa(elem) for elem in obj]
    elif obj in ['minecraft:badlands', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'terralith:fractured_savanna', 'terralith:savanna_badlands', 'terralith:snowy_badlands', 'terralith:warped_mesa', 'terralith:white_mesa']:
        return "Mesa"
    else:
        return obj

##this function is a bit of a misnomer, you can only select other skylands biomes or ocean biomes to replace skylands biomes
def replace_biomes_with_skylands(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_skylands(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_skylands(elem) for elem in obj]
    elif obj in ['terralith:skylands_spring', 'terralith:skylands_summer', 'terralith:skylands_autumn', 'terralith:skylands_winter']:
        return "Skylands"
    else:
        return obj

def replace_all_remaining_biomes(obj):
    if isinstance(obj, dict):
        return {k: replace_all_remaining_biomes(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_all_remaining_biomes(elem) for elem in obj]
    elif obj in ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:badlands', 'minecraft:snowy_beach', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands']:
        return "Remaining"
    else:
        return obj

##same as skylands, you can only replace ocean biomes with other ocean biomes or skylands
def replace_biomes_with_ocean(obj):
    if isinstance(obj, dict):
        return {k: replace_biomes_with_ocean(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_ocean(elem) for elem in obj]
    elif obj in ['minecraft:warm_ocean', 'minecraft:lukewarm_ocean', 'minecraft:deep_lukewarm_ocean', 'minecraft:ocean', 'minecraft:deep_ocean', 'minecraft:cold_ocean', 'minecraft:deep_cold_ocean', 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean']:
        return "Ocean"
    else:
        return obj
    
def replace_biomes_with_river(obj):
    if isinstance(obj, dict):
        return {k:replace_biomes_with_river(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_biomes_with_river(elem) for elem in obj]
    elif obj in ['minecraft:river', 'minecraft:frozen_river', 'terralith:warm_river']:
        return "River"
    else:
        return obj

##The following series of functions prompts the user to choose which biomes they want to randomly replace the keyphrase from above

def beachPrompt():
    print('select with space, progress with enter, navigate with arrows')
    beachQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for beaches",
                        choices = ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:lush_caves', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands'],
                        ),
    ]

    answerBeach = inquirer.prompt(beachQuestion)
    beachList = answerBeach['biomes']
    return(beachList)

def mountainPrompt():
    print('select with space, progress with enter, navigate with arrows')
    mountainQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for mountains",
                        choices = ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:lush_caves', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands'],
                        ),
    ]

    answerMountain = inquirer.prompt(mountainQuestion)
    mountainList = answerMountain['biomes']
    return(mountainList)

def desertPrompt():
    print('select with space, progress with enter, navigate with arrows')
    desertQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for deserts",
                        choices = ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:lush_caves', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands'],
                        ),
    ]

    answerDesert = inquirer.prompt(desertQuestion)
    desertList = answerDesert['biomes']
    return(desertList)

def mesaPrompt():
    print('select with space, progress with enter, navigate with arrows')
    mesaQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for mesas",
                        choices = ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:lush_caves', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands'],
                        ),
    ]

    answerMesa = inquirer.prompt(mesaQuestion)
    mesaList = answerMesa['biomes']
    return(mesaList)

def allBiomePrompt():
    print('select with space, progress with enter, navigate with arrows')
    allBiomeQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for all remaining biomes",
                        choices = ['minecraft:plains', 'minecraft:sunflower_plains', 'minecraft:snowy_plains', 'minecraft:ice_spikes', 'minecraft:desert', 'minecraft:swamp', 'minecraft:mangrove_swamp', 'minecraft:forest', 'minecraft:flower_forest', 'minecraft:birch_forest', 'minecraft:dark_forest', 'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:taiga', 'minecraft:snowy_taiga', 'minecraft:savanna', 'minecraft:savanna_plateau', 'minecraft:windswept_hills', 'minecraft:windswept_gravelly_hills', 'minecraft:windswept_forest', 'minecraft:windswept_savanna', 'minecraft:jungle', 'minecraft:sparse_jungle', 'minecraft:bamboo_jungle', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands', 'minecraft:meadow', 'minecraft:cherry_grove', 'minecraft:grove', 'minecraft:snowy_slopes', 'minecraft:frozen_peaks', 'minecraft:jagged_peaks', 'minecraft:stony_peaks', 'minecraft:beach', 'minecraft:lush_caves', 'minecraft:stony_shore', 'minecraft:mushroom_fields', 'terralith:alpha_islands', 'terralith:alpha_islands_winter', 'terralith:alpine_grove', 'terralith:alpine_highlands', 'terralith:amethyst_canyon', 'terralith:amethyst_rainforest', 'terralith:ancient_sands', 'terralith:arid_highlands', 'terralith:ashen_savanna', 'terralith:basalt_cliffs', 'terralith:birch_taiga', 'terralith:blooming_plateau', 'terralith:blooming_valley', 'terralith:brushland', 'terralith:bryce_canyon', 'terralith:caldera', 'terralith:cloud_forest', 'terralith:cold_shrubland', 'terralith:desert_canyon', 'terralith:desert_oasis', 'terralith:desert_spires', 'terralith:emerald_peaks', 'terralith:forested_highlands', 'terralith:fractured_savanna', 'terralith:frozen_cliffs', 'terralith:glacial_chasm', 'terralith:granite_cliffs', 'terralith:gravel_beach', 'terralith:gravel_desert', 'terralith:haze_mountain', 'terralith:highlands', 'terralith:hot_shrubland', 'terralith:ice_marsh', 'terralith:jungle_mountains', 'terralith:lavender_forest', 'terralith:lavender_valley', 'terralith:lush_desert', 'terralith:lush_valley', 'terralith:mirage_isles', 'terralith:moonlight_grove', 'terralith:moonlight_valley', 'terralith:orchid_swamp', 'terralith:painted_mountains', 'terralith:red_oasis', 'terralith:rocky_jungle', 'terralith:rocky_mountains', 'terralith:rocky_shrubland', 'terralith:sakura_grove', 'terralith:sakura_valley', 'terralith:sandstone_valley', 'terralith:savanna_badlands', 'terralith:savanna_slopes', 'terralith:scarlet_mountains', 'terralith:shield_clearing', 'terralith:shield', 'terralith:shrubland', 'terralith:siberian_grove', 'terralith:siberian_taiga', 'terralith:snowy_badlands', 'terralith:snowy_cherry_grove', 'terralith:snowy_maple_forest', 'terralith:snowy_shield', 'terralith:steppe', 'terralith:stony_spires', 'terralith:temperate_highlands', 'terralith:tropical_jungle', 'terralith:valley_clearing', 'terralith:volcanic_crater', 'terralith:volcanic_peaks', 'terralith:warped_mesa', 'terralith:white_cliffs', 'terralith:white_mesa', 'terralith:windswept_spires', 'terralith:wintry_forest', 'terralith:wintry_lowlands', 'terralith:yellowstone', 'terralith:yosemite_cliffs', 'terralith:yosemite_lowlands'],
                        ),
    ]

    answerAllBiome = inquirer.prompt(allBiomeQuestion)
    allBiomeList = answerAllBiome['biomes']
    return(allBiomeList)

def skylandPrompt():
    print('select with space, progress with enter, navigate with arrows')
    skylandQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for skylands",
                        choices = ['minecraft:warm_ocean', 'minecraft:lukewarm_ocean', 'minecraft:deep_lukewarm_ocean', 'minecraft:ocean', 'minecraft:deep_ocean', 'minecraft:cold_ocean', 'minecraft:deep_cold_ocean', 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean', 'terralith:skylands_spring', 'terralith:skylands_summer', 'terralith:skylands_autumn', 'terralith:skylands_winter'],
                        ),
    ]

    answerSkyland = inquirer.prompt(skylandQuestion)
    skylandList = answerSkyland['biomes']
    return(skylandList)

def oceanPrompt():
    print('select with space, progress with enter, navigate with arrows')
    oceanQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for oceans",
                        choices = ['minecraft:warm_ocean', 'minecraft:lukewarm_ocean', 'minecraft:deep_lukewarm_ocean', 'minecraft:ocean', 'minecraft:deep_ocean', 'minecraft:cold_ocean', 'minecraft:deep_cold_ocean', 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean', 'terralith:skylands_spring', 'terralith:skylands_summer', 'terralith:skylands_autumn', 'terralith:skylands_winter'],
                        ),
    ]

    answerOcean = inquirer.prompt(oceanQuestion)
    oceanList = answerOcean['biomes']
    return(oceanList)

def riverPrompt():
    print('select with space, progress with enter, navigate with arrows')
    riverQuestion = [
    inquirer.Checkbox('biomes',
                        message = "Select biomes to be shuffled in for rivers", 
                        choices = ['minecraft:river', 'minecraft:frozen_river', 'terralith:warm_river'],
                      ),
    ]

    answerRiver = inquirer.prompt(riverQuestion)
    riverList = answerRiver['biomes']
    return(riverList)

def finalReplace(obj, bList, mList, dList, meList, sList, oList, rList):
    if isinstance(obj, dict):
        return {k: finalReplace(v, bList, mList, dList, meList, sList, oList, rList) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [finalReplace(elem, bList, mList, dList, meList, sList, oList, rList) for elem in obj]
    else:
        if obj == 'Beach':
            return random.choice(bList)
        elif obj == 'Mountain':
            return random.choice(mList)
        elif obj == 'Desert':
            return random.choice(dList)
        elif obj == 'Mesa':
            return random.choice(meList)
        elif obj == 'Skylands':
            return random.choice(sList)
        elif obj == 'Ocean':
            return random.choice(oList)
        elif obj == 'River':
            return random.choice(rList)
        else:
            return obj

def finalBiomeReplace(obj, biomeList):
    if isinstance(obj, dict):
        return {k: finalBiomeReplace(v, biomeList) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [finalBiomeReplace(elem, biomeList) for elem in obj]
    else:
        if obj == 'Remaining':
            return random.choice(biomeList)
        else:
            return obj




def replace_in_json(input_file, output_file):
    beachList = []
    mountainList = []
    desertList = []
    mesaList = []
    allBiomeList = []
    skylandList = []
    oceanList = []
    riverList = []
    with open(input_file, 'r') as f:
        data = json.load(f)
        for item in lst:

            if item == 'Beaches':
                data = replace_biomes_with_beach(data)
                beachList = beachPrompt()
            elif item == 'Mountains':
                data = replace_biomes_with_mountain(data)
                mountainList = mountainPrompt()
            elif item == 'Deserts (does not touch badland biomes)':
                data = replace_biomes_with_desert(data)
                desertList = desertPrompt()
            elif item == 'Mesas':
                data = replace_biomes_with_mesa(data)
                mesaList = mesaPrompt()
            elif item == 'Replace All Remaining Biomes':
                data = replace_all_remaining_biomes(data)
                allBiomeList = allBiomePrompt()
            elif item == 'Skylands (Can only replace with Skylands)':
                data = replace_biomes_with_skylands(data)
                skylandList = skylandPrompt()
            elif item == 'Oceans (Can only replace with oceans)':
                data = replace_biomes_with_ocean(data)
                oceanList = oceanPrompt()
            elif item == 'Rivers':
                data = replace_biomes_with_river(data)
                riverList = riverPrompt()

        if allBiomeList:
            data = finalBiomeReplace(data, allBiomeList)
        if beachList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if mountainList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if desertList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if mesaList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if skylandList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if oceanList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)
        if riverList:
            data = finalReplace(data, beachList, mountainList, desertList, mesaList, skylandList, oceanList, riverList)


    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)




##I'm so goated.
##with the sauce
replace_in_json('overworld.json', 'RENAME.json')