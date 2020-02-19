import pandas as pd
import numpy as np

""" Provide the absolute paths of the for both Original and Tagger csvs generated from the jsons provided in the VMD """

original_csv_path = '/home/mohan/json_to_CSV/csvs/20191125_22_203000.449_210001.783.csv'
tagger_csv_path = '/home/mohan/json_to_CSV/csvs/20191125_22_203000.449_210001.783_taggers.csv'

original_csv = pd.read_csv(original_csv_path)
tag_csv = pd.read_csv(tagger_csv_path)

original_csv['roi_label_threshold_gender'] = original_csv['roi_label_threshold_based'].apply(lambda x: x.split('_')[0])
original_csv['roi_label_threshold_age'] = original_csv['roi_label_threshold_based'].apply(lambda x: 'None' if x=='None' else 'Child' if x=='Child' else x.split('_')[1])

tag_csv['roi_label_threshold_gender'] = tag_csv['roi_label_threshold_based'].apply(lambda x: 'None' if x=='None' or x =='others' else 'Child' if x=='Child' else x.split('_')[0])
tag_csv['roi_label_threshold_age'] = tag_csv['roi_label_threshold_based'].apply(lambda x: 'None' if x=='None' or x =='others' else 'Child' if x=='Child' else x.split('_')[1])


prec_gen = []
rec_gen = []
prec_age = []
rec_age = []
for i in range(len(original_csv)):
    if original_csv['roi_id'][i] != "":
        if tag_csv['roi_label_threshold_gender'][i] != 'None':
            if original_csv['roi_label_threshold_gender'][i] == tag_csv['roi_label_threshold_gender'][i]:
                prec_gen.append(1)
            else:
                prec_gen.append(0)
        if tag_csv['roi_label_threshold_age'][i] != 'None' :
            if original_csv['roi_label_threshold_age'][i] == tag_csv['roi_label_threshold_age'][i]:
                prec_age.append(1)
            else:
                prec_age.append(0)


""" Calculating Accuracy for Age and Gender """

precision_gender = np.average(prec_gen)
precision_age = np.average(prec_age)

print(precision_age)
print(precision_gender)