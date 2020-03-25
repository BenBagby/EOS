
import EOS

composition = {'Component':['Hydrogen Sulfide', 'Nitrogen', 'Carbon Dioxide', 'Methane', 'Ethane', 'Propane', 'Isobutane', 'n-Butane', 'n-Pentane', 'n-Hexane', 'n-Heptane', 'n-Octane', 'n-Nonane', 'n-Decane', 'Benzene', 'Toluene', 'Xylenes', 'Cyclohexane'],
                'Mol%':[0,0.0192644717405159, 0.176678992386017, 2.21649248551794, 2.13119487439681, 2.67287357163934, 1.53179051543505, 3.01741004015665, 5.66072307074221, 8.77782649473597, 73.7957454832494, 0, 0, 0, 0, 0,0 ,0]}

#All pressure and temp. inputs in psig and F
#pressure base is 14.73

P_feed = 108
T_feed = 74

P_sep = 0
T_sep = 60

(EOSresult, Composition_result) = EOS.PR(composition,P_feed,T_feed,P_sep,T_sep)

print(EOSresult)
print(Composition_result)