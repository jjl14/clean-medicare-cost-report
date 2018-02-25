#####define function for extracting a given list of desired variables from the raw dataset

def cost_data_reduce(costdata, varlist):
    costdata['varname'] = ''
    line_select = pd.Series(np.zeros(len(costdata))).astype(int)
    for i in range(len(varlist[0])):
        new_line_select = ((costdata['wksht_cd']==varlist[0][i]) & (costdata['line_num']==varlist[1][i]) & \
                           (costdata['clmn_num']==varlist[2][i]))
        costdata.loc[new_line_select, 'varname'] = varlist[3][i]
        line_select = line_select | new_line_select ###TODO: might be able to make faster here

    costdatasubset = costdata[['rep_rcd_num', 'varname', 'itm_val_num']][line_select].copy()
    costdatasubset = costdatasubset.pivot(index='rep_rcd_num', columns='varname', values='itm_val_num')
    costdatasubset.columns = [x for x in costdatasubset.columns]
    costdatasubset.reset_index(inplace=True)

    return costdatasubset



#####make the lists of worksheet, line, and column numbers and variable names, for the 1996 version

covar_list96 = []
covar_list96.append(['S200000', 100, 100, 'city'])
covar_list96.append(['S200000', 100, 200, 'state'])
covar_list96.append(['S200000', 101, 300, 'zip'])
covar_list96.append(['S200000', 101, 400, 'county'])

covar_list96.append(['S200000', 200, 100, 'hosp_name'])
covar_list96.append(['S200000', 200, 300, 'date_certified'])
covar_list96.append(['S200000', 1900, 100, 'hosp_provider_type'])
covar_list96.append(['S200000', 2101, 100, 'disproportionate_share'])
covar_list96.append(['S200000', 2104, 100, 'geo_type_start'])
covar_list96.append(['S200000', 2105, 100, 'geo_type_end'])
covar_list96.append(['S200000', 2108, 100, 'method_medicaid'])
covar_list96.append(['S200000', 2108, 200, 'method_medicaid_change'])

covar_list96.append(['S200000', 2200, 100, 'referralcenter'])
covar_list96.append(['S200000', 2300, 100, 'transplant'])
covar_list96.append(['S200000', 2500, 100, 'teaching'])
covar_list96.append(['S200000', 3000, 100, 'critical_access'])
covar_list96.append(['S200000', 4700, 100, 'exemptionA'])
covar_list96.append(['S200000', 4700, 200, 'exemptionB'])
covar_list96.append(['S200000', 5400, 100, 'malpractice_prem'])
covar_list96.append(['S200000', 5400, 200, 'malpractice_loss'])
covar_list96.append(['S200000', 5800, 100, 'inpatient_rehab'])
covar_list96.append(['S200000', 5900, 100, 'longterm_care_hosp'])
covar_list96.append(['S200000', 6000, 100, 'inpatient_psych'])
covar_list96.append(['S200000', 6100, 100, 'multicampus'])

#convenient way to add variables with same root in name
templines = [100, 500, 1200, 1400, 1700, 2500]
tempnames = ['bed_'+x for x in ['hosp_adultped', 'total_adultped', 'total', 'subprovider', 'longterm', 'total_plus']]
for i in range(len(templines)):
    covar_list96.append(['S300001', templines[i], 100, tempnames[i]])

#convenient way to add consecutive variables w/ same root in name
templines = [100]+list(range(500,1100,100))+list(range(1200,1500,100))
tempnames = ['q_'+x+'_mchs' for x in ['hosp_adultped', 'total_adultped', 'icu', 'ccu', 'burn', 'surgical', 'special', \
                                     'total', 'cah', 'subprovider']]
for i in range(len(templines)):
    covar_list96.append(['S300001', templines[i], 300, tempnames[i]])

templines = [100,200]+list(range(500,1100,100))+list(range(1200,1500,100))
tempnames = ['q_'+x+'_medicare' for x in ['hosp_adultped', 'hmo', 'total_adultped', 'icu', 'ccu', 'burn', 'surgical', 'special', \
                                     'total', 'cah', 'subprovider']]
for i in range(len(templines)):
    covar_list96.append(['S300001', templines[i], 400, tempnames[i]])
tempnames = ['q_'+x+'_medicaid' for x in ['hosp_adultped', 'hmo', 'total_adultped', 'icu', 'ccu', 'burn', 'surgical', 'special', \
                                     'total', 'cah', 'subprovider']]
for i in range(len(templines)):
    covar_list96.append(['S300001', templines[i], 500, tempnames[i]])

templines = [100]+list(range(500,1100,100))+list(range(1200,1500,100))+[1700]
tempnames = ['q_'+x+'_total' for x in ['hosp_adultped', 'total_adultped', 'icu', 'ccu', 'burn', 'surgical', 'special', \
                                     'total', 'cah', 'subprovider', 'longterm']]
for i in range(len(templines)):
    covar_list96.append(['S300001', templines[i], 600, tempnames[i]])

covar_list96.append(['S300001', 1100, 600, 'q_nursery'])
covar_list96.append(['S300001', 2900, 600, 'day_labor'])

#convcenient way to get variables when you want the product set of the set of roots and the set of ends
tempclmns = [700, 1000, 1100]
templines = [1200, 1400, 1700, 2500]
tempclmnnames = ['intern_res_', 'employees_payroll_', 'workers_nonpaid_']
for j in range(len(tempclmns)):
    tempnames = [tempclmnnames[j]+x for x in ['total', 'subprovider', 'longterm', 'total_plus']]
    for i in range(len(templines)):
        covar_list96.append(['S300001', templines[i], tempclmns[j], tempnames[i]])

tempclmns = list(range(1200,1600,100))
templines = [1200, 1400]
tempclmnnames = ['_mchs', '_medicare', '_medicaid', '_total']
for j in range(len(tempclmns)):
    tempnames = [x+tempclmnnames[j] for x in ['discharge_total', 'discharge_subprovider']]
    for i in range(len(templines)):
        covar_list96.append(['S300001', templines[i], tempclmns[j], tempnames[i]])

covar_list96.append(['S300001', 1700, 1500, 'discharge_longterm_total'])

covar_list96.append(['S300002', 100, 500, 'avg_hr_wage_total'])
covar_list96.append(['S300002', 400, 500, 'avg_hr_wage_phys_a'])
covar_list96.append(['S300002', 500, 500, 'avg_hr_wage_phys_b'])
covar_list96.append(['S300002', 501, 500, 'avg_hr_wage_nonphys_b'])
covar_list96.append(['S300002', 600, 500, 'avg_hr_wage_res'])

covar_list96.append(['S300002', 100, 400, 'hrs_total'])
covar_list96.append(['S300002', 400, 400, 'hrs_phys_a'])
covar_list96.append(['S300002', 500, 400, 'hrs_phys_b'])
covar_list96.append(['S300002', 501, 400, 'hrs_nonphys_b'])
covar_list96.append(['S300002', 600, 400, 'hrs_res'])

covar_list96.append(['G200000', 2500, 100, 'patient_rev_inpatient'])
covar_list96.append(['G200000', 2500, 200, 'patient_rev_outpatient'])
covar_list96.append(['G200000', 2500, 300, 'patient_rev_total'])
covar_list96.append(['G200000', 4000, 200, 'operating_exp_total'])

covar_list96.append(['C000001', 10100, 600, 'charge_inpatient'])
covar_list96.append(['C000001', 10100, 700, 'charge_outpatent'])
covar_list96.append(['S100000', 3200, 100, 'uncompensated_cost'])

wksht_list96 = []
line_list96 = []
clmn_list96 = []
cost_varname_list96 = []

for item in covar_list96:
    wksht_list96.append(item[0])
    line_list96.append(item[1])
    clmn_list96.append(item[2])
    cost_varname_list96.append(item[3])


cost_var_list96 = [wksht_list96, line_list96, clmn_list96, cost_varname_list96]


#####extract the list of desired variables from the raw dataset, for all desired years

costdata96 = pd.DataFrame()

for y in range(6,12):
    costbasedata = pd.read_csv('medicare_cost_report/HOSPFY20'+str(y).zfill(2)+ '/hosp_20'+str(y).zfill(2)+ '_RPT.CSV', header=None, \
                              names=['rep_rcd_num', 'prvdr_ctrl_type_cd', 'ccn', 'npi', 'rpt_stus_cd', \
                                    'fy_bgn_dt', 'fy_end_dt', 'proc_dt', 'initl_rpt_sw', 'last_rpt_sw', \
                                    'trnsmtl_num', 'fi_num', 'adr_vndr_cd','fi_creat_dt', 'util_cd', \
                                    'npr_dt', 'spec_ind', 'fi_rcpt_dt'])

    costnumdatafull= pd.read_csv('medicare_cost_report/HOSPFY20'+str(y).zfill(2)+ '/hosp_20'+str(y).zfill(2)+ '_NMRC.CSV', header=None, \
                              names=['rep_rcd_num', 'wksht_cd', 'line_num', 'clmn_num', 'itm_val_num'])
    costnumdatafull['clmn_num'] = costnumdatafull['clmn_num'].str.replace('A', '1')
    costnumdatafull['clmn_num'] = pd.to_numeric(costnumdatafull['clmn_num'])

    costabcdatafull = pd.read_csv('medicare_cost_report/HOSPFY20'+str(y).zfill(2)+ '/hosp_20'+str(y).zfill(2)+ '_ALPHA.CSV', header=None, \
                              names=['rep_rcd_num', 'wksht_cd', 'line_num', 'clmn_num', 'itm_val_num'])


    costnumdata = timer(cost_data_reduce)(costnumdatafull, cost_var_list96)
    costabcdata = timer(cost_data_reduce)(costabcdatafull, cost_var_list96)
    costdata96temp = costnumdata.merge(costabcdata, on='rep_rcd_num')
    costdata96temp = costdata96temp.merge(costbasedata, on='rep_rcd_num')
    costdata96temp['year'] = 2000+y
    print(len(costdata96temp))
    costdata96 = pd.concat([costdata96, costdata96temp], ignore_index=True)
    print(len(costdata96))

costdata96.to_csv('medicare_cost_report/cleaned_ehr_network96.csv', index=False)
