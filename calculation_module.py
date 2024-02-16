import os
import shutil
import pandas as pd
from joblib import Parallel, delayed
from CM.CM_TUW0.rem_mk_dir import rm_mk_dir, rm_dir
from CM.CM_TUW40.f1_main_call import main
from CM.CM_TUW40.f4_results_summary import summary
from initialize import Param, Out_File_Path

nr_cores = 1

def logfile(P, OFP):
    logging_text = "\n\n"
    P_attr_dict = vars(P)
    col_width = 5 + max(len(key) for key in P_attr_dict.keys())
    for key in P_attr_dict.keys():
        logging_text = logging_text + "".join(key.ljust(col_width) + str(P_attr_dict[key]).ljust(col_width) + '\n')
    with open(OFP.logfile, 'w') as f:
        f.write(logging_text)


def unify_excels(output_directory):
    init_df = True
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            if "summary.csv" == file:
                f = os.path.join(root, "summary.csv")
                tmp_df = pd.read_csv(f)
                if init_df:
                    df = tmp_df.copy()
                    init_df = False
                else:
                    df = df.append(tmp_df, ignore_index=True)
    out_xlsx = os.path.join(output_directory, 'summary_all.xlsx')
    df.to_excel(out_xlsx, index=False)


def res_calculation(country, directory, in_dict):
    P = Param(country, in_dict)
    OFP = Out_File_Path(directory, P)
    print("#"*15 + country + ' - Case: ', P.case)
    #P.warnings()
    rm_mk_dir(OFP.dstDir)
    logfile(P, OFP)
    main(P, OFP)
    summary(P, OFP)


if __name__ == "__main__":
    output_directory = '/path/2/output_directory'
    scenario_input_csv = 'cm_input_ms.csv'
    output_directory = output_directory.replace("\\", "/")
    scenario_input_csv = scenario_input_csv.replace("\\", "/")
    
    country_path_dict = dict()
    d = pd.read_csv(scenario_input_csv, index_col=0, header=0).squeeze('columns').T.to_dict()
    for directory, foldernames, filenames in os.walk(output_directory):
        # find the right directory
        flag = False
        for fname in filenames:
            if "Energy_TOTAL_" in fname:
                flag = True
        if flag == False:
            continue
        # get country code, e.g. "AT", from Folder name, e.g. "1AT"
        country = directory.split("/")[-1][-2::]
        if country not in d.keys():
            continue
        country_path_dict[country] = directory

    # parallel computing
    Parallel(n_jobs=nr_cores)(delayed(res_calculation)(key, country_path_dict[key], d[key]) for key in country_path_dict.keys())
    unify_excels(output_directory)
    print('finished!')
