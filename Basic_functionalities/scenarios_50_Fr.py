import numpy as np
from scipy.interpolate import interp1d
import pandas as pd
from Basic_functionalities import tech_eco_data

inputPath='Data/Raw_Ana/'

nHours = 8760
t = np.arange(1,nHours + 1)

zones = ['Fr']

yearZero = 2010
yearFinal = 2050
yearStep = 10
yearList = [yr for yr in range(yearZero, yearFinal+yearStep, yearStep)] # +1 to include the final year
nYears = len(yearList)

scenarioFr50 = {}

elec_demand=pd.read_csv(inputPath+'areaConsumption2010-2050_Fr_TIMExRESxYEAR.csv').set_index(['YEAR','TIMESTAMP','RESOURCES'])
anualElec={2020:492e6,2030:581.1e6,2040:625.1e6,2050:627.4e6}
hourlyH2={2020:[0],2030:[1825],2040:[2400],2050:[3710]}
scenarioFr50['resourceDemand'] =  pd.concat(
    (
        pd.DataFrame(data = {
              'YEAR': year,
              'TIMESTAMP': t, # We add the TIMESTAMP so that it can be used as an index later.
              'electricity': np.array(elec_demand.loc[(2020,slice(None),'electricity'),'areaConsumption']*anualElec[year]/anualElec[2020]), # incrising demand of electricity (hypothesis : ADEME)
              'hydrogen': np.array(hourlyH2[year]*nHours),
              'gaz': np.zeros(nHours),
              'uranium': np.zeros(nHours)
             }
        ) for k, year in enumerate(yearList[1:])
    )
) 

scenarioFr50['conversionTechs'] = []
for k, year in enumerate(yearList[:-1]):

    tech = "WindOffShore"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [0,5200,14300,22000]
    min_cumul_capacity = [0,5200,14300,22000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='high', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "WindOnShore"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [8000, 33200 , 39000, 43000]
    min_cumul_capacity = [8000, 33200 , 39000, 43000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='high', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech: 
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex, 
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "Solar"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity=[4000,35100,53200,70000]
    min_cumul_capacity =[4000,35100,53200,70000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='high', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "HydroReservoir"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity=[15000,15000,16000,17000]
    min_cumul_capacity = [15000,15000,16000,17000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='high', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 2100, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "HydroRiver"
    max_install_capacityacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [11000,11000,12000,13000]
    min_cumul_capacity = [11000,11000,12000,13000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='high', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "OldNuke"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [63100,63000,55800,24400]
    min_cumul_capacity = [63100,63000,55800,24400]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='low', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost':30, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'uranium':-3.03},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k],'RampConstraintPlus':0.04,'RampConstraintMoins':0.04}
            }
         )
    )

    tech = "NewNuke"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [0,0,7600,27300]
    min_cumul_capacity = [0,0,7600,27300]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='low', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'uranium':-3.03},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k],'RampConstraintPlus':0.04,'RampConstraintMoins':0.04}
            }
         )
    )

    tech = "Coal_p"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [6000,1000,0,0]
    min_cumul_capacity = [6000,1000,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 50, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 1000, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k],'RampConstraintPlus':0.06,'RampConstraintMoins':0.06}
            }
         )
    )

    tech = "TAC"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [7100,6500,0,0]
    min_cumul_capacity = [7100,6500,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost':0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'gaz':-2.7},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k] }
            }
         )
    )

    tech = "TAC_H2"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [0,0,0,0]
    min_cumul_capacity = [0,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost':0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'hydrogen':-2.7},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k] }
            }
         )
    )

    tech = "CCG"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [5000,5000,1400,0]
    min_cumul_capacity =[5000,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'gaz':-1.72},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k],'RampConstraintPlus':0.06,'RampConstraintMoins':0.06 }
            }
         )
    )

    tech = "CCG_H2"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [0,0,0,0]
    min_cumul_capacity =[0,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1, 'hydrogen':-1.72},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k],'RampConstraintPlus':0.06,'RampConstraintMoins':0.06 }
            }
         )
    )

    tech = "electrolysis_AEL"
    max_cumul_capacity= [0,6500,7500,9500]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Hydrogen production',
                'lifeSpan': lifespan, 'powerCost': 0, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': 0,'maxInstallCapacity': 100000,
                'EmissionCO2': 0, 'Conversion': {'hydrogen': 1,'electricity':-1.54},
                'minCumulCapacity': 0,'maxCumulCapacity': max_cumul_capacity[k]}
            }
         )
    )

    tech = "IntercoIn"
    max_install_capacity = [11000,22300,29700,39400]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [11000,22300,29700,39400]
    min_cumul_capacity =[0,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 150, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 290, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k] }
            }
         )
    )

    tech = "IntercoOut"
    max_install_capacity = [0,0,0,0]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [11000,22300,29700,39400]
    min_cumul_capacity =[0,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': -50, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': -1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k] }
            }
         )
    )

    tech = "curtailment"
    max_install_capacity = [100000,100000,100000,100000]
    min_install_capacity=[0,0,0,0]
    max_cumul_capacity= [100000,100000,100000,100000]
    min_cumul_capacity = [0,0,0,0]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['conversionTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year, 'Category': 'Electricity production',
                'lifeSpan': lifespan, 'powerCost': 3000, 'investCost': capex, 'operationCost': opex,
                'minInstallCapacity': min_install_capacity[k],'maxInstallCapacity': max_install_capacity[k],
                'EmissionCO2': 0, 'Conversion': {'electricity': 1},
                'EnergyNbhourCap': 0, # used for hydroelectricity
                'minCumulCapacity': min_cumul_capacity[k],'maxCumulCapacity': max_cumul_capacity[k] }
            }
         )
    )

scenarioFr50['conversionTechs'] =  pd.concat(scenarioFr50['conversionTechs'], axis=1)

scenarioFr50['storageTechs'] = []
for k, year in enumerate(yearList[:-1]):
    tech = "Battery"
    max_install_capacity = [0,5000,5000,5000]
    max_install_power=[0,500,500,500]
    capex1, opex1, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech + ' - 1h', hyp='ref', year=year)
    capex4, opex4, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech + ' - 4h', hyp='ref', year=year)
    capex_per_kWh = (capex4 - capex1) / 3
    capex_per_kW = capex1 - capex_per_kWh

    scenarioFr50['storageTechs'].append(
        pd.DataFrame(data={tech: 
                { 'YEAR': year, 'resource': 'electricity',
                'storagelifeSpan': lifespan, 
                'storagePowerCost': capex_per_kW,
                'storageEnergyCost': capex_per_kWh,
                'storageOperationCost': opex1, # TODO: according to RTE OPEX seems to vary with energy rather than power
                'p_max': max_install_power[k],
                'c_max': max_install_capacity[k],
                'chargeFactors': {'electricity': 0.9200},
                'dischargeFactors': {'electricity': 1.09},
                'dissipation': 0.0085,
                }, 
            }
         )
    )

    # tech = "STEP"
    # max_install_capacity = [30000,10000,20000,20000]
    # max_install_power=[3000,1000,2000,2000]
    # capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    # scenarioFr50['storageTechs'].append(
    #     pd.DataFrame(data={tech:
    #             { 'YEAR': year,
    #            'resource': 'electricity',
    #            'storagelifeSpan': lifespan,
    #             'storagePowerCost': capex*0.5,
    #             'storageEnergyCost': capex*0.5/10,
    #             'storageOperationCost': opex,
    #             'p_max': max_install_power[k],
    #             'c_max': max_install_capacity[k],
    #             'chargeFactors': {'electricity': 0.9},
    #             'dischargeFactors': {'electricity': 1.11},
    #             'dissipation': 0,
    #             },
    #         }
    #      )
    # )

    tech = "saltCavernH2_G"
    max_install_capacity = [100000,100000,100000,100000]
    max_install_power=[10000,10000,10000,10000]
    capex, opex, lifespan = tech_eco_data.get_capex_new_tech_RTE(tech, hyp='ref', year=year)
    scenarioFr50['storageTechs'].append(
        pd.DataFrame(data={tech:
                { 'YEAR': year,
               'resource': 'hydrogen',
               'storagelifeSpan': lifespan,
                'storagePowerCost': 1000,
                'storageEnergyCost': capex,
                'storageOperationCost': opex,
                'p_max': max_install_power[k],
                'c_max': max_install_capacity[k],
                'chargeFactors': {'electricity': 0.0168,'hydrogen':1},
                'dischargeFactors': {'hydrogen': 1},
                'dissipation': 0,
                },
            }
         )
    )

scenarioFr50['storageTechs'] =  pd.concat(scenarioFr50['storageTechs'], axis=1)

scenarioFr50['carbonTax'] = pd.DataFrame(data=np.linspace(0.0675,0.165, nYears),
    index=yearList, columns=('carbonTax',))

scenarioFr50['carbonGoals'] = pd.DataFrame(data=np.linspace(974e6, 205e6, nYears),
    index=yearList, columns=('carbonGoals',))

scenarioFr50['maxBiogasCap'] = pd.DataFrame(data=np.linspace(0, 310e6, nYears),
    index=yearList, columns=('maxBiogasCap',))

scenarioFr50['gridConnection'] = pd.read_csv(inputPath+'CalendrierHPHC_TIME.csv', sep=',', decimal='.', skiprows=0,
                                comment="#").set_index(["TIMESTAMP"])

scenarioFr50['economicParameters'] = pd.DataFrame({
    'discountRate':[0.04], 
    'financeRate': [0.04]
    }
)

df_res_ref = pd.read_csv(inputPath+'set2020-2050_horaire_TIMExRESxYEAR.csv',
    sep=',', decimal='.', skiprows=0,comment="#").set_index(["YEAR", "TIMESTAMP",'RESOURCES'])

gasPriceFactor=[1,2,2,2]
scenarioFr50['resourceImportPrices'] = pd.concat(
    (
        pd.DataFrame(data={
            'YEAR': year, 
            'TIMESTAMP': t, 
            'electricity': df_res_ref.loc[(year, slice(None), 'electricity'),'importCost'].values,
            'gazNat': df_res_ref.loc[(year, slice(None), 'gazNat'),'importCost'].values*gasPriceFactor[k],
            'gazBio': df_res_ref.loc[(year, slice(None), 'gazBio'),'importCost'].values,
            'uranium': df_res_ref.loc[(year, slice(None), 'uranium'),'importCost'].values,
            'hydrogen': df_res_ref.loc[(year, slice(None), 'hydrogen'),'importCost'].values,
            'gaz': df_res_ref.loc[(year, slice(None), 'gaz'),'importCost'].values
        }) for k, year in enumerate(yearList[1:])
    )
)

scenarioFr50['resourceImportCO2eq'] = pd.concat(
    (
        pd.DataFrame(data={
            'YEAR': year, 
            'TIMESTAMP': t, 
            'electricity': df_res_ref.loc[(year, slice(None), 'electricity'),'emission'].values,
            'gaz': max(0, 0.03 * (1 - (year - yearZero)/(2050 - yearZero))) * 29 / 13.1 + 203.5  * (1 - tech_eco_data.get_biogas_share_in_network_RTE(year)), # Taking 100 yr GWP of methane and 3% losses due to upstream leaks. Losses drop to zero in 2050.
            'gazNat': max(0, 0.03 * (1 - (year - yearZero)/(2050 - yearZero))) * 29 / 13.1 + 203.5  * (1 - tech_eco_data.get_biogas_share_in_network_RTE(year)), # Taking 100 yr GWP of methane and 3% losses due to upstream leaks. Losses drop to zero in 2050.
            'gazBio': max(0, 0.03 * (1 - (year - yearZero)/(2050 - yearZero))) * 29 / 13.1,
            'uranium': 0 * np.ones(nHours),
            'hydrogen': max(0, 0.05  - .03 * (year - yearZero)/(2050 - yearZero)) * 11 / 33, # Taking 100 yr GWP of H2 and 5% losses due to upstream leaks. Leaks fall to 2% in 2050 See: https://www.energypolicy.columbia.edu/research/commentary/hydrogen-leakage-potential-risk-hydrogen-economy
        }) for k, year in enumerate(yearList[1:])
    )
)

scenarioFr50['convTechList'] = ["WindOnShore", "WindOffShore", "Solar", "CCG", "TAC","Coal_p", "OldNuke","NewNuke","IntercoIn","IntercoOut","curtailment","HydroReservoir","HydroRiver","CCG_H2","TAC_H2","electrolysis_AEL"]
ctechs = scenarioFr50['convTechList']
availabilityFactor = pd.read_csv(inputPath+'availabilityFactor2010-2050_Fr_TIMExTECHxYEAR.csv',
                                 sep=',', decimal='.', skiprows=0).set_index(["YEAR", "TIMESTAMP", "TECHNOLOGIES"])
itechs = availabilityFactor.index.isin(ctechs, level=2)
scenarioFr50['availability'] = availabilityFactor.loc[(slice(None), slice(None), itechs)]

scenarioFr50["yearList"] = yearList
scenarioFr50["transitionFactors"] =pd.DataFrame(
    {'TECHNO1':[],
    'TECHNO2':[],
    'TransFactor': 1}).set_index(['TECHNO1','TECHNO2'])