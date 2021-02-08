import pandas as pd
import re
import numpy as np
import datetime

#read data and combine
data = pd.read_excel('../wildlife_data_clean.xlsx', sheet_name = None, engine='openpyxl')
wildlife_data_clean = pd.concat(data, ignore_index=True)

#remove missing data or fill missing
wildlife_data_clean_clean = wildlife_data_clean[wildlife_data_clean['CALL_DESCRIPTION'].notna()]
wildlife_data_clean_clean.fillna({
    'CALL_REGION': 'Unknown',
    'CALL_SAVED_TIME': 'Unknown',
    'CA_ANIMAL_TYPE': 'Unknown'}, inplace = True)

#call description assigning
#requires HARD coding! and attention for a new data, can be changed if necessary

wildlife_data_clean_clean['CALL_DESCRIPTION'] = wildlife_data_clean_clean['CALL_DESCRIPTION'].str.lower()

key_words = ['broken', 'cut', 'wounded', 'lying', 'neck', 'pup', 'leg', 'flew', 'rescue', 'living', 'panting',
               'wound', 'wing', 'duplicate', 'netting', 'laying', 'new', 'dead', 'paw', 'sleeping', 'sick',
               'bleeding', 'inj', 'res', 'beach', 'fly', 'flightless', 'garden', 'loft', 'catted', 'deceased',
            'fledgling', 'carpark', 'trapped', 'transport', 'RTA', 'stuck', 'pigeon', 'collect', 'sitting',
            'swan', 'enquire', 'police', 'out', 'unwell', 'myxi', 'killed', 'advice', 'unable', 'shooting', 'remove',
            'looking', 'poisoned', 'side', 'hit', 'seen', 'mobile', 'attic', 'afraid', 'pest', 'lame', 'died', 'chimney',
            'fire', 'report', 'river', 'call', 'diarrhoea', 'removal', 'walls', 'nest', 'wrong', 'vet',
            'wall', 'owl', 'seal', 'snh', 'hallway', 'feral', 'wobbly', 'rta', 'fox',
            'license', 'street','stray', 'fawn', 'missing', 'transfer', 'falling','ARO','heron','underneath',
            'adv', 'dup', 'playground','wondering','fledgling', 'area', 'uplift', 'grass',
            'building', 'hatching','know', 'exhausted','run','flat', 'stove', 'tree','house','donation','advice',
            'cygnet','shed','land','grate','vent','balcony','properly','rid','baiting','transfer',
            'ceiling','adv','grounded','pheasant','magpie','window','pavement','trap','found','lone',
            'assistance','query','roof','wild','request','control','robin','flue','chimeny','night','neglected',
             'goose','stranded','neglect','neg','badger','gull','kitchen','startled',
             'curled','stairwell','martin','aldi','handover','lum','close','how','mxy','walking','asking',
             'daed', 'spotted','baby','table','water','puffin','alive','harbour','crossing','road', 'queries',
             'bees','dying','rubbish','woodburner','not\\ moving','cupboard','floorboards','suffered','covered',
             'bedroom','fishcross','cruelty','hand\\ over','field'
             
             ]
key_pattern = r'(' + r'|'.join(key_words) + r')'

wildlife_data_clean_clean['verb_inj']= wildlife_data_clean_clean['CALL_DESCRIPTION'].str.extract(key_pattern)

conditions = [
    (wildlife_data_clean_clean['verb_inj'] == 'inj'), (wildlife_data_clean_clean['verb_inj'] == 'rta'),
    (wildlife_data_clean_clean['verb_inj'] == 'dead'), (wildlife_data_clean_clean['verb_inj'] == 'deceased'),
    (wildlife_data_clean_clean['verb_inj'] == 'catted'), (wildlife_data_clean_clean['verb_inj'] == 'poisoned'),
    (wildlife_data_clean_clean['verb_inj'] == 'rescue'), (wildlife_data_clean_clean['verb_inj'] == 'new'),
    (wildlife_data_clean_clean['verb_inj'] == 'myxi'),(wildlife_data_clean_clean['verb_inj'] == 'hallway'),
    (wildlife_data_clean_clean['verb_inj'] == 'shooting'), (wildlife_data_clean_clean['verb_inj'] == 'sitting'),
    (wildlife_data_clean_clean['verb_inj'] == 'leg'), (wildlife_data_clean_clean['verb_inj'] == 'nest'),
    (wildlife_data_clean_clean['verb_inj'] == 'unwell'), (wildlife_data_clean_clean['verb_inj'] == 'sick'),
    (wildlife_data_clean_clean['verb_inj'] == 'seen'), (wildlife_data_clean_clean['verb_inj'] == 'sleeping'),
    (wildlife_data_clean_clean['verb_inj'] == 'seal'), (wildlife_data_clean_clean['verb_inj'] == 'duplicate'),
    (wildlife_data_clean_clean['verb_inj'] == 'swan'), (wildlife_data_clean_clean['verb_inj'] == 'owl'),
    (wildlife_data_clean_clean['verb_inj'] == 'flightless'), (wildlife_data_clean_clean['verb_inj'] == 'garden'),
    (wildlife_data_clean_clean['verb_inj'] == 'hit'), (wildlife_data_clean_clean['verb_inj'] == 'fire'),
    (wildlife_data_clean_clean['verb_inj'] == 'flew'), (wildlife_data_clean_clean['verb_inj'] == 'trapped'),
    (wildlife_data_clean_clean['verb_inj'] == 'call'), (wildlife_data_clean_clean['verb_inj'] == 'collect'),
    (wildlife_data_clean_clean['verb_inj'] == 'out'), (wildlife_data_clean_clean['verb_inj'] == 'advice'),
    (wildlife_data_clean_clean['verb_inj'] == 'pigeon'), (wildlife_data_clean_clean['verb_inj'] == 'police'),
    (wildlife_data_clean_clean['verb_inj'] == 'report'), (wildlife_data_clean_clean['verb_inj'] == 'mobile'),
    (wildlife_data_clean_clean['verb_inj'] == 'broken'), (wildlife_data_clean_clean['verb_inj'] == 'res'),
    (wildlife_data_clean_clean['verb_inj'] == 'attic'), (wildlife_data_clean_clean['verb_inj'] == 'living'),
    (wildlife_data_clean_clean['verb_inj'].isnull()), (wildlife_data_clean_clean['verb_inj'] == 'beach'),
    (wildlife_data_clean_clean['verb_inj'] == 'wing'), (wildlife_data_clean_clean['verb_inj'] == 'stuck'),
    (wildlife_data_clean_clean['verb_inj'] == 'side'), (wildlife_data_clean_clean['verb_inj'] == 'looking'),
    (wildlife_data_clean_clean['verb_inj'] == 'lame'), (wildlife_data_clean_clean['verb_inj'] == 'pest'),
    (wildlife_data_clean_clean['verb_inj'] == 'loft'), (wildlife_data_clean_clean['verb_inj'] == 'fly'),
    (wildlife_data_clean_clean['verb_inj'] == 'chimney'), (wildlife_data_clean_clean['verb_inj'] == 'lying'),
    (wildlife_data_clean_clean['verb_inj'] == 'diarrhoea'), (wildlife_data_clean_clean['verb_inj'] == 'stray'),
    (wildlife_data_clean_clean['verb_inj'] == 'vet'), (wildlife_data_clean_clean['verb_inj'] == 'fox'),
    (wildlife_data_clean_clean['verb_inj'] == 'aro'), (wildlife_data_clean_clean['verb_inj'] == 'transfer'),
    (wildlife_data_clean_clean['verb_inj'] == 'wall'), (wildlife_data_clean_clean['verb_inj'] == 'neck'),
    (wildlife_data_clean_clean['verb_inj'] == 'cut'), (wildlife_data_clean_clean['verb_inj'] == 'remove'),
    (wildlife_data_clean_clean['verb_inj'] == 'street'), (wildlife_data_clean_clean['verb_inj'] == 'removal'),
    (wildlife_data_clean_clean['verb_inj'] == 'killed'), (wildlife_data_clean_clean['verb_inj'] == 'bleeding'),
    (wildlife_data_clean_clean['verb_inj'] == 'walls'), (wildlife_data_clean_clean['verb_inj'] == 'unable'),
    (wildlife_data_clean_clean['verb_inj'] == 'laying'), (wildlife_data_clean_clean['verb_inj'] == 'license'),
    (wildlife_data_clean_clean['verb_inj'] == 'wrong'), (wildlife_data_clean_clean['verb_inj'] == 'river'),
    (wildlife_data_clean_clean['verb_inj'] == 'paw'), (wildlife_data_clean_clean['verb_inj'] == 'pup'),
    (wildlife_data_clean_clean['verb_inj'] == 'fawn'), (wildlife_data_clean_clean['verb_inj'] == 'wound'),
    (wildlife_data_clean_clean['verb_inj'] == 'missing'), (wildlife_data_clean_clean['verb_inj'] == 'snh'),
    (wildlife_data_clean_clean['verb_inj'] == 'netting'), (wildlife_data_clean_clean['verb_inj'] == 'feral'),
    (wildlife_data_clean_clean['verb_inj'] == 'falling'), (wildlife_data_clean_clean['verb_inj'] == 'afraid'),
    (wildlife_data_clean_clean['verb_inj'] == 'wobbly'), (wildlife_data_clean_clean['verb_inj'] == 'panting'),
    (wildlife_data_clean_clean['verb_inj'] == 'carpark'), (wildlife_data_clean_clean['verb_inj'] == 'fledgling'),
    (wildlife_data_clean_clean['verb_inj'] == 'transport'),(wildlife_data_clean_clean['verb_inj'] == 'feral'),
    (wildlife_data_clean_clean['verb_inj'] == 'ceiling'),(wildlife_data_clean_clean['verb_inj'] == 'hallway'),
    (wildlife_data_clean_clean['verb_inj'] == 'flue'),(wildlife_data_clean_clean['verb_inj'] == 'afraid'),
    (wildlife_data_clean_clean['verb_inj'] == 'stairwell'),(wildlife_data_clean_clean['verb_inj'] == 'handover'),
    (wildlife_data_clean_clean['verb_inj'] == 'died'),(wildlife_data_clean_clean['verb_inj'] == 'puffin'),
    (wildlife_data_clean_clean['verb_inj'] == 'startled'),(wildlife_data_clean_clean['verb_inj'] == 'flat'),
    (wildlife_data_clean_clean['verb_inj'] == 'daed'),(wildlife_data_clean_clean['verb_inj'] == 'underneath'),
    (wildlife_data_clean_clean['verb_inj'] == 'curled'),(wildlife_data_clean_clean['verb_inj'] == 'spotted'),
    (wildlife_data_clean_clean['verb_inj'] == 'dying'),(wildlife_data_clean_clean['verb_inj'] == 'baiting'),
    (wildlife_data_clean_clean['verb_inj'] == 'pavement'),(wildlife_data_clean_clean['verb_inj'] == 'lum'),
    (wildlife_data_clean_clean['verb_inj'] == 'dup'),(wildlife_data_clean_clean['verb_inj'] == 'badger'),
    (wildlife_data_clean_clean['verb_inj'] == 'stranded'),(wildlife_data_clean_clean['verb_inj'] == 'found'),
    (wildlife_data_clean_clean['verb_inj'] == 'cygnet'),(wildlife_data_clean_clean['verb_inj'] == 'alive'),
    (wildlife_data_clean_clean['verb_inj'] == 'land'),(wildlife_data_clean_clean['verb_inj'] == 'goose'),
    (wildlife_data_clean_clean['verb_inj'] == 'adv'),(wildlife_data_clean_clean['verb_inj'] == 'neg'),
    (wildlife_data_clean_clean['verb_inj'] == 'road'),(wildlife_data_clean_clean['verb_inj'] == 'lone'),
    (wildlife_data_clean_clean['verb_inj'] == 'uplift'),(wildlife_data_clean_clean['verb_inj'] == 'cruelty'),
    (wildlife_data_clean_clean['verb_inj'] == 'assistance'),(wildlife_data_clean_clean['verb_inj'] == 'neglect'),
    (wildlife_data_clean_clean['verb_inj'] == 'field'),(wildlife_data_clean_clean['verb_inj'] == 'wild'),
    (wildlife_data_clean_clean['verb_inj'] == 'gull'),(wildlife_data_clean_clean['verb_inj'] == 'grass'),
    (wildlife_data_clean_clean['verb_inj'] == 'bedroom'),(wildlife_data_clean_clean['verb_inj'] == 'heron'),
    (wildlife_data_clean_clean['verb_inj'] == 'request'),(wildlife_data_clean_clean['verb_inj'] == 'walking'),
    (wildlife_data_clean_clean['verb_inj'] == 'exhausted'),(wildlife_data_clean_clean['verb_inj'] == 'area'),
    (wildlife_data_clean_clean['verb_inj'] == 'night'),(wildlife_data_clean_clean['verb_inj'] == 'grounded'),
    (wildlife_data_clean_clean['verb_inj'] == 'run'),(wildlife_data_clean_clean['verb_inj'] == 'tree'),
    (wildlife_data_clean_clean['verb_inj'] == 'query'),(wildlife_data_clean_clean['verb_inj'] == 'playground'),
    (wildlife_data_clean_clean['verb_inj'] == 'robin'),(wildlife_data_clean_clean['verb_inj'] == 'house'),
    (wildlife_data_clean_clean['verb_inj'] == 'donation'),(wildlife_data_clean_clean['verb_inj'] == 'building'),
    (wildlife_data_clean_clean['verb_inj'] == 'wondering'),(wildlife_data_clean_clean['verb_inj'] == 'pheasant'),
    (wildlife_data_clean_clean['verb_inj'] == 'neglected'),(wildlife_data_clean_clean['verb_inj'] == 'fishcross'),
    (wildlife_data_clean_clean['verb_inj'] == 'close'),(wildlife_data_clean_clean['verb_inj'] == 'stove'),
    (wildlife_data_clean_clean['verb_inj'] == 'not moving'),(wildlife_data_clean_clean['verb_inj'] == 'window'),
    (wildlife_data_clean_clean['verb_inj'] == 'trap'),(wildlife_data_clean_clean['verb_inj'] == 'magpie'),
    (wildlife_data_clean_clean['verb_inj'] == 'balcony'),(wildlife_data_clean_clean['verb_inj'] == 'how'),
    (wildlife_data_clean_clean['verb_inj'] == 'vent'),(wildlife_data_clean_clean['verb_inj'] == 'crossing'),
    (wildlife_data_clean_clean['verb_inj'] == 'roof'), (wildlife_data_clean_clean['verb_inj'] == 'mxy'),
    (wildlife_data_clean_clean['verb_inj'] == 'baby'),(wildlife_data_clean_clean['verb_inj'] == 'shed'),
    (wildlife_data_clean_clean['verb_inj'] == 'asking'),(wildlife_data_clean_clean['verb_inj'] == 'grate'),
    (wildlife_data_clean_clean['verb_inj'] == 'hand over'),(wildlife_data_clean_clean['verb_inj'] == 'chimeny'),
    (wildlife_data_clean_clean['verb_inj'] == 'kitchen'),(wildlife_data_clean_clean['verb_inj'] == 'covered'),
    (wildlife_data_clean_clean['verb_inj'] == 'martin'),(wildlife_data_clean_clean['verb_inj'] == 'water'),
    (wildlife_data_clean_clean['verb_inj'] == 'table'), (wildlife_data_clean_clean['verb_inj'] == 'harbour'),
     (wildlife_data_clean_clean['verb_inj'] == 'bees'), (wildlife_data_clean_clean['verb_inj'] == 'know'),
     (wildlife_data_clean_clean['verb_inj'] == 'rid'),(wildlife_data_clean_clean['verb_inj'] == 'rubbish'),
    (wildlife_data_clean_clean['verb_inj'] == 'hatching'),(wildlife_data_clean_clean['verb_inj'] == 'cupboard'),
    (wildlife_data_clean_clean['verb_inj'] == 'floorboards'),(wildlife_data_clean_clean['verb_inj'] == 'woodburner'),
    (wildlife_data_clean_clean['verb_inj'] == 'queries'), (wildlife_data_clean_clean['verb_inj'] == 'suffered')


    ]
choices = ['injury', 'rescue','dead','dead','injury','cruel_behavior', 'rescue', 'unclear', 'disease', 'location_notice',
           'cruel_behavior','location_notice','injury', 'location_notice', 'unwell', 'unwell','location_notice',
           'location_notice','unclear', 'injury','unclear','unclear','injury','location_notice','injury','location_notice',
          'injury', 'rescue', 'unclear','location_notice','unclear','advice','unclear','unclear','unclear','injury',
          'injury','rescue','location_notice','injury','unclear','location_notice','injury','rescue','injury',
          'location_notice','injury','unclear','location_notice','injury','location_notice','dead',
          'unwell','location_notice','advice','unclear','rescue','location_notice','injury','injury','injury',
          'unclear','location_notice','unclear','dead','injury','rescue','injury','injury','cruel_behavior',
          'unclear','location_notice','injury','injury','location_notice','injury','location_notice','advice',
          'rescue','location_notice','injury','unclear','unwell','unwell','location_notice', 'location_notice',
          'location_notice','location_notice','location_notice','location_notice','rescue','location_notice',
          'location_notice','location_notice','dead','unclear','rescue','location_notice','dead',
          'location_notice','rescue','location_notice','dead','cruel_behavior','location_notice','rescue',
          'injury','location_notice','rescue','location_notice','location_notice','rescue',
          'location_notice','rescue','advice','cruel_behavior','rescue','location_notice','location_notice',
          'cruel_behavior','advice','cruel_behavior','location_notice','location_notice','location_notice',
           'location_notice','rescue','location_notice','unclear','location_notice','unwell','location_notice',
           'location_notice','rescue','rescue','location_notice','advice','location_notice','location_notice',
           'rescue','advice','rescue','advice','location_notice','cruel_behavior','location_notice',
           'location_notice','rescue','dead','location_notice','rescue','injury','location_notice','advice',
           'rescue','location_notice','rescue','disease','rescue','location_notice','advice','rescue',
           'location_notice','rescue','rescue','unwell','location_notice','location_notice','rescue',
           'location_notice','unclear','advice','rescue','cruel_behavior','rescue','rescue','rescue','rescue',
           'advice','disease'
]

wildlife_data_clean_clean['reason_for_call'] = np.select(conditions, choices)

#split calls into two categories - advice and report
wildlife_data_clean_clean.loc[:,'type_of_calls']= np.where(wildlife_data_clean_clean['reason_for_call'] == 'advice', 'advice_calls','report_calls')

#-----------------------------------------------------------------------------------------------------------------
#!!! Further cleaning requires to be changed accordingly for a new data !!!
# It will be manually assigned

wildlife_data_clean.loc[59563,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[59563,'CA_ANIMAL_TYPE'] = wildlife_data_clean.loc[59563,'Unnamed: 4']
wildlife_data_clean.loc[59563,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[60430,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[60430,'CA_ANIMAL_TYPE'] = wildlife_data_clean.loc[60430,'Unnamed: 4']
wildlife_data_clean.loc[60430,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[70360,'CALL_REGION'] = wildlife_data_clean.loc[70360,'CA_ANIMAL_TYPE']
wildlife_data_clean.loc[70360,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[70360,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[73945,'CALL_REGION'] = wildlife_data_clean.loc[73945,'CA_ANIMAL_TYPE']
wildlife_data_clean.loc[73945,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[73945,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[80463,'CALL_REGION'] = wildlife_data_clean.loc[80463,'Unnamed: 5']
wildlife_data_clean.loc[80463,'CA_ANIMAL_TYPE'] = wildlife_data_clean.loc[80463,'Unnamed: 7']
wildlife_data_clean.loc[80463,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[80820,'CALL_REGION'] = wildlife_data_clean.loc[80820,'Unnamed: 5']
wildlife_data_clean.loc[80820,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[80820,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[82926,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[82926,'CA_ANIMAL_TYPE'] = 'Swan'
wildlife_data_clean.loc[82926,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[85871,'CALL_REGION'] = 'Inverness'
wildlife_data_clean.loc[85871,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[85871,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[87768,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[87768,'CA_ANIMAL_TYPE'] = 'Deer'
wildlife_data_clean.loc[87768,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[87795,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[87795,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[87795,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[88364,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[88364,'CA_ANIMAL_TYPE'] = 'Fox'
wildlife_data_clean.loc[88364,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[91823,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[91823,'CA_ANIMAL_TYPE'] = 'Owl'
wildlife_data_clean.loc[91823,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[94412,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[94412,'CA_ANIMAL_TYPE'] = 'Deer'
wildlife_data_clean.loc[94412,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[95142,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[95142,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[95142,'CALL_SAVED_TIME'] = '2018-05-18 00:00:00'

wildlife_data_clean.loc[96115,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[96115,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[96115,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[98692,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[98692,'CA_ANIMAL_TYPE'] = 'Rabbit'
wildlife_data_clean.loc[98692,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[101056,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[101056,'CA_ANIMAL_TYPE'] = 'Squirrel'
wildlife_data_clean.loc[101056,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[101501,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[101501,'CA_ANIMAL_TYPE'] = 'Hedgehog'
wildlife_data_clean.loc[101501,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[101802,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[101802,'CA_ANIMAL_TYPE'] = '*Other Wildlife'
wildlife_data_clean.loc[101802,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[102499,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[102499,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[102499,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[105135,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[105135,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[105135,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[108094,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[108094,'CA_ANIMAL_TYPE'] = 'Gull'
wildlife_data_clean.loc[108094,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[111382,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[111382,'CA_ANIMAL_TYPE'] = 'Swan'
wildlife_data_clean.loc[111382,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[115169,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[115169,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[115169,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[122180,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[122180,'CA_ANIMAL_TYPE'] = 'Hedgehog'
wildlife_data_clean.loc[122180,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[127970,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[127970,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[127970,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[132941,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[132941,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[132941,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[133290,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[133290,'CA_ANIMAL_TYPE'] = 'Gull'
wildlife_data_clean.loc[133290,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[135010,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[135010,'CA_ANIMAL_TYPE'] = '*Other Wildlife'
wildlife_data_clean.loc[135010,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[139708,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[139708,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[139708,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[139717,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[139717,'CA_ANIMAL_TYPE'] = 'Rat'
wildlife_data_clean.loc[139717,'CALL_SAVED_TIME'] = 'Unknown'

#drop extra columns 
wildlife_data_clean.drop(columns = ['Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], inplace = True) 


wildlife_data_clean.loc[1358,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[1358,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[1358,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[4163,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[4163,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[4163,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[5878,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[5878,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[5878,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[65134,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[65134,'CA_ANIMAL_TYPE'] = 'Hedgehog'
wildlife_data_clean.loc[65134,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[71459,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[71459,'CA_ANIMAL_TYPE'] = 'Hedgehog'
wildlife_data_clean.loc[71459,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[72388,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[72388,'CA_ANIMAL_TYPE'] = 'Hedgehog'
wildlife_data_clean.loc[72388,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[80218,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[80218,'CA_ANIMAL_TYPE'] = 'Fox'
wildlife_data_clean.loc[80218,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[80765,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[80765,'CA_ANIMAL_TYPE'] = 'Swan'
wildlife_data_clean.loc[80765,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[81865,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[81865,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[81865,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[82612,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[82612,'CA_ANIMAL_TYPE'] = 'Swan'
wildlife_data_clean.loc[82612,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[83043,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[83043,'CA_ANIMAL_TYPE'] = 'Seal'
wildlife_data_clean.loc[83043,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[83970,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[83970,'CA_ANIMAL_TYPE'] = 'Gull'
wildlife_data_clean.loc[83970,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[88721,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[88721,'CA_ANIMAL_TYPE'] = 'Duck'
wildlife_data_clean.loc[88721,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[89628,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[89628,'CA_ANIMAL_TYPE'] = 'Nestling'
wildlife_data_clean.loc[89628,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[95060,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[95060,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[95060,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[97049,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[97049,'CA_ANIMAL_TYPE'] = 'Deer'
wildlife_data_clean.loc[97049,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[97631,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[97631,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[97631,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[98596,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[98596,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[98596,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[100283,'CALL_REGION'] = 'Inverness'
wildlife_data_clean.loc[100283,'CA_ANIMAL_TYPE'] = 'Bat'
wildlife_data_clean.loc[100283,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[101717,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[101717,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[101717,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[103067,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[103067,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[103067,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[105287,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[105287,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[105287,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[105580,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[105580,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[105580,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[105626,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[105626,'CA_ANIMAL_TYPE'] = 'Swan'
wildlife_data_clean.loc[105626,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[106953,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[106953,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[106953,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[107294,'CALL_REGION'] = 'Edinburgh'
wildlife_data_clean.loc[107294,'CA_ANIMAL_TYPE'] = 'Nestling'
wildlife_data_clean.loc[107294,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[107849,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[107849,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[107849,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[108976,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[108976,'CA_ANIMAL_TYPE'] = 'Gull'
wildlife_data_clean.loc[108976,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[116605,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[116605,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[116605,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[117133,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[117133,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[117133,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[122932,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[122932,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[122932,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[123230,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[123230,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[123230,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[125976,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[125976,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[125976,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[126070,'CALL_REGION'] = 'Inverness'
wildlife_data_clean.loc[126070,'CA_ANIMAL_TYPE'] = 'Fledgling'
wildlife_data_clean.loc[126070,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[126202,'CALL_REGION'] = 'Central'
wildlife_data_clean.loc[126202,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[126202,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[131319,'CALL_REGION'] = 'Glasgow'
wildlife_data_clean.loc[131319,'CA_ANIMAL_TYPE'] = 'Squirrel'
wildlife_data_clean.loc[131319,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[136952,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[136952,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[136952,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[142952,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[142952,'CA_ANIMAL_TYPE'] = 'Unknown'
wildlife_data_clean.loc[142952,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[143992,'CALL_REGION'] = 'Aberdeen'
wildlife_data_clean.loc[143992,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[143992,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[145845,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[145845,'CA_ANIMAL_TYPE'] = 'Gull'
wildlife_data_clean.loc[145845,'CALL_SAVED_TIME'] = 'Unknown'

wildlife_data_clean.loc[80820,'CALL_REGION'] = 'Unknown'
wildlife_data_clean.loc[80820,'CA_ANIMAL_TYPE'] = 'Wild Bird'
wildlife_data_clean.loc[80820,'CALL_SAVED_TIME'] = 'Unknown'

#--------------------------------------------------------------------------------------------------------
# Check date column
wildlife_data_clean.loc[:,'CALL_SAVED_TIME'] = pd.to_datetime(wildlife_data_clean['CALL_SAVED_TIME'], errors = 'coerce')

#remove sensitive data
wildlife_data_clean_final = wildlife_data_clean.drop(columns = ['CALL_DESCRIPTION', 'verb_inj']).copy()

#Asserting the data
assert wildlife_data_clean_final.loc[:,wildlife_data_clean_final.columns !='CALL_SAVED_TIME'].isnull().values.any()==False, "Missing values found"

#Write data ready for analysis
wildlife_data_clean_final.to_csv('../clean_data/wildlife_clean.csv')