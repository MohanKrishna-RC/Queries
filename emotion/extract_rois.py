import pandas as pd
import numpy as np
import json
from constant import Constant
# import CommonUtility
import os
import zipfile
import cv2

zip_frame_file_path = '/home/mohan/BIOGEC_frames_del/clip1/b0fdc352-075e-4a79-a1e7-0cf175ac0a9d.zip'
detection_csv_path = "/home/mohan/BIOGEC_frames_del/clip1/BIO-GEC_AGEGENDER - clip1.csv"
detection_csv = pd.read_csv(detection_csv_path)
_detection_csv = detection_csv[detection_csv.roi_id.notnull()]
print("Columns of the given csv:", _detection_csv.columns)

def unzip(zip_local_path):
    base_dir = os.path.dirname(zip_local_path)
    with zipfile.ZipFile(zip_local_path, 'r') as zipObj:
        zipObj.extractall(base_dir)
    return base_dir

def get_frames(zip_frame_file_path):
    frames_file_path = unzip(zip_frame_file_path)
    return frames_file_path

def _get_size_of_roi(zip_frame_file_path):
    frames_file_path = get_frames(zip_frame_file_path)
    try:
        for i in range(len(_detection_csv)):
            # print(i)
            row = _detection_csv[i:i+1]
            filename = frames_file_path + '/' + row.frame_id.tolist()[0]
            img = cv2.imread(filename)
            roi = img[int(row.ymin.tolist()[0]): int(row.ymax.tolist()[0]), int(row.xmin.tolist()[0]): int(row.xmax.tolist()[0])]
            # print(roi.shape)
            path = "/home/mohan/BIOGEC_frames_del/clip1/clip1_ROIs/{}".format(row.frame_id.tolist()[0])
            cv2.imwrite(path,roi)
            print(i)
    except Exception as e:
        print(e)

# def _merge_csvs():
#         df_1 = _detection_csv

#         df_3 = detection_csv

#         mask = df_3.roi_id.isin(df_1.roi_id)
#         extra_cols = list(set(df_1.columns)-set(df_3.columns))
#         print(extra_cols)
#         for i in extra_cols:
#             df_3.loc[mask, i] = df_1[i]

#         _final_csv = df_3

#         return _final_csv

_get_size_of_roi(zip_frame_file_path)
