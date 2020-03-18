import EOS

composition = {'Component':['Hydrogen Sulfide', 'Nitrogen', 'Carbon Dioxide', 'Methane', 'Ethane', 'Propane', 'Isobutane', 'n-Butane', 'n-Pentane', 'n-Hexane', 'n-Heptane', 'n-Octane', 'n-Nonane', 'n-Decane', 'Benzene', 'Toluene', 'Xylenes', 'Cyclohexane'],
                'Mol%':[0, 0.0048, 0.0213, 0.6105, 2.7664, 8.2577, 1.8144, 7.8461, 6.9698, 71.7089, 0, 0, 0, 0, 0, 0,0 ,0]}

#All pressure and temp. inputs in psig and F

P_feed = 34
T_feed = 63

P_sep = 14.73
T_sep = 60

(EOSresult, Composition_result) = EOS.PR(composition,P_feed,T_feed,P_sep,T_sep)

print(EOSresult)
print(Composition_result)