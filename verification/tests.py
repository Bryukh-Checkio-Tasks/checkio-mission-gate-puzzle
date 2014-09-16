"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "Speak friend and enter.",
            "answer": "friend",
            "explanation": {'speak': 30.464285714285715, 'and': 30.253968253968253, 'friend': 38.57142857142857,
                            'enter': 36.33730158730159},
        },
        {
            "input": "Beard and Bread",
            "answer": "bread",
            "explanation": {'bread': 72.33333333333333, 'beard': 72.33333333333333, 'and': 44.666666666666664},
        },
        {
            "input": "The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs",
            "answer": "durin",
            "explanation": {'durin': 33.30362554112554, 'of': 24.290981240981242, 'signs': 29.11504329004329,
                            'moria': 32.647691197691195, 'them': 29.63454184704185, 'enter': 32.16455627705628,
                            'lord': 31.398430735930734, 'narvi': 31.33140331890332, 'the': 27.469209956709957,
                            'hollin': 28.391594516594516, 'speak': 27.601064213564214, 'i': 11.640530303030303,
                            'friend': 32.69047619047619, 'these': 31.550559163059162, 'drew': 30.624621212121212,
                            'and': 26.144805194805194, 'doors': 33.05146103896104, 'made': 30.710930735930734,
                            'celebrimbor': 20.3895202020202},
        },
        {
            "input": "Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy. According to a researcher at Cambridge University.One, two, two, three, three, three.",
            "answer": "three",
            "explanation": {'researcher': 28.953918888129415, 'a': 19.137426900584796, 'cmabrigde': 30.79851143009038,
                            'to': 30.014619883040936, 'two': 30.303030303030305, 'one': 24.93753322700691,
                            'aoccdrnig': 31.265778081567554, 'university': 27.395762132604236,
                            'cambridge': 30.79851143009038, 'uinervtisy': 27.395762132604236,
                            'rscheearch': 28.953918888129415, 'at': 29.494569757727653, 'according': 31.265778081567554,
                            'three': 35.56823877876509},
        },
    ],
    "Extra": [
        {
            "input": "All that is gold does not glitter,",
            "answer": "gold",
            "explanation": {'that': 29.31547619047619, 'glitter': 23.425925925925927, 'not': 28.878968253968253,
                            'all': 26.666666666666668, 'gold': 32.44047619047619, 'is': 20.11904761904762,
                            'does': 31.28306878306878},
        },
        {
            "input": "Not all those who wander are lost;",
            "answer": "are",
            "explanation": {'wander': 27.44047619047619, 'all': 30.857142857142858, 'who': 32.791666666666664,
                            'not': 34.736111111111114, 'lost': 34.55555555555556, 'are': 35.023809523809526,
                            'those': 33.57936507936508},
        },
        {
            "input": "The old that is strong does not wither,",
            "answer": "the",
            "explanation": {'the': 34.226190476190474, 'old': 27.321428571428573, 'that': 32.576530612244895,
                            'strong': 28.341836734693878, 'not': 33.51190476190476, 'wither': 27.604875283446713,
                            'is': 20.612244897959183, 'does': 32.46031746031746},
        },
        {
            "input": "Deep roots are not reached by the frost.",
            "answer": "roots",
            "explanation": {'reached': 25.895691609977323, 'frost': 32.48299319727891, 'by': 15.36734693877551,
                            'roots': 33.378684807256235, 'not': 29.717687074829932, 'deep': 25.989795918367346,
                            'the': 31.58843537414966, 'are': 31.69047619047619},
        },
        {
            "input": "From the ashes a fire shall be woken,",
            "answer": "ashes",
            "explanation": {'shall': 27.833333333333332, 'the': 29.329931972789115, 'be': 23.11904761904762,
                            'fire': 32.19897959183673, 'from': 25.702380952380953, 'ashes': 34.27040816326531,
                            'woken': 25.460884353741495, 'a': 13.285714285714286},
        },
        {
            "input": "A light from the shadows shall spring;",
            "answer": "shall",
            "explanation": {'shall': 34.42195767195767, 'shadows': 28.99500962000962, 'light': 28.582010582010582,
                            'spring': 27.08032708032708, 'from': 21.04232804232804, 'the': 21.267857142857142,
                            'a': 9.936507936507937},
        },
        {
            "input": "Renewed shall be blade that was broken,",
            "answer": "blade",
            "explanation": {'was': 25.107142857142858, 'shall': 30.785714285714285, 'be': 25.428571428571427,
                            'renewed': 25.64484126984127, 'blade': 38.76851851851852, 'that': 26.63095238095238,
                            'broken': 31.207010582010582},
        },
        {
            "input": "The crownless again shall be king.",
            "answer": "again",
            "explanation": {'shall': 25.228571428571428, 'the': 24.866666666666667, 'crownless': 18.595959595959595,
                            'be': 18.744444444444444, 'king': 26.675757575757576, 'again': 28.47099567099567},
        },
        {
            "input": "I don't know half of you half as well as I should like; and I like less than half of you half as well as you deserve.",
            "answer": "half",
            "explanation": {'less': 30.886243386243386, 'deserve': 17.752792475014697, 'you': 27.88800705467372,
                            'as': 30.149911816578484, 'than': 27.771898883009992, 'of': 26.322751322751323,
                            'half': 34.682539682539684, 'should': 23.22530864197531, 'don': 26.11552028218695,
                            'like': 29.802322163433274, 'i': 18.02910052910053, 't': 12.751322751322752,
                            'know': 25.430629041740154, 'and': 27.978395061728396, 'well': 28.137125220458554},
        },
        {
            "input": "Fantasy is escapist, and that is its glory. If a soldier is imprisioned by the enemy, don't we consider it his duty to escape?. If we value the freedom of mind and soul, if we're partisans of liberty, then it's our plain duty to escape, and to take as many people with us as we can!",
            "answer": "its",
            "explanation": {'escape': 25.832338159924365, 'partisans': 23.188846594019008, 'glory': 22.150980245807833,
                            'if': 27.573244762899936, 'with': 26.429361347464795, 'to': 28.349106831865452,
                            'soul': 24.84551176792556, 'imprisioned': 20.854164992096027, 'is': 30.849448922724786,
                            'consider': 22.659134447927553, 'take': 29.55778225605812, 'the': 30.494750460267703,
                            'escapist': 24.241429069015275, 'that': 27.682066975170425, 'our': 24.429790515997414,
                            'his': 28.450384385729212, 'many': 25.719585012688462, 'as': 29.1773088023088,
                            'value': 24.311169194789883, 's': 17.148349256107878, 'freedom': 20.85264591730109,
                            'then': 28.592090859332238, 'by': 22.22704881325571, 'its': 32.651602229188434,
                            'people': 23.5439680051749, 'it': 29.963433597054287, 'duty': 26.02056277056277,
                            'soldier': 24.01126411902274, 'can': 25.753371149922874, 'a': 15.485445588893866,
                            'enemy': 24.38131935114694, 't': 17.778138528138527, 'we': 27.629689754689753,
                            're': 26.17682987510574, 'of': 25.057850674229986, 'us': 25.71877021445987,
                            'plain': 24.961318853560233, 'liberty': 22.927548983583467, 'don': 26.30581678857541,
                            'and': 28.07408444046375, 'mind': 25.804672339155097, 'fantasy': 24.193742081673115},
        },
    ]
}
