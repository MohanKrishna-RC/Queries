import os, cv2, glob, csv
import pandas as pd
import numpy as np
csv = "csvs/20200203_2_213002.047_220001.556.csv"
vmd_name = csv.split('/')[1].split('.csv')[0]
print(vmd_name)
df = pd.read_csv(csv)
# print(df.head())
df = df[df['roi_id'].notnull()]

a = np.unique(df['frame_zipfile_path'])
print(a)
def create_dir(folder):
    if not os.path.exists(folder):
                os.makedirs(folder)

# # input_frames_folder = "/home/aodev/demo_video_rois_and_frames/frames"
for i,j in enumerate(a):
    # print(i,j)
    # break
    b = "output_folder_{}".format(i)
    # print(b)
    # break
    b = os.path.join("/home/mohan/queries/emotion/emo_testing/",a[i].split('/')[-1].split(".")[0])
    # print(b)
    os.system("gsutil -m cp -r {} ./b_1".format(a[i]))
    c = b.split('/')[-1]
    # print(c)
    # break
    create_dir("/home/mohan/queries/emotion/emo_testing/frame_info/{}/".format(vmd_name))
    # break
    os.system("unzip b_1 -d /home/mohan/queries/emotion/emo_testing/frame_info/{}/{}/".format(vmd_name,c))

output_folder = "/home/mohan/queries/emotion/emo_testing/"
# csv = "/home/mohan/bbox_test_logo.csv"
# # csv = "/home/aodev/demo_video_rois_and_frames/predictions_18_apr_rois.csv"
input_frames_folder = "/home/mohan/queries/emotion/emo_testing/frame_info/{}".format(vmd_name)

for i in range(len(df)):
    # print(i)
    # break
    row = df[i:i+1]
    clip_name = row.frame_zipfile_path.to_list()[0].split('/')[-1].split('.')[0]
    # print(clip_name)
    image = os.path.join(input_frames_folder,clip_name,row.frame_id.to_list()[0])
    # print(image)

    img = cv2.imread(image)
    
    try:
        if not row.roi_id.to_list()[0] == "":
            # print(row)
            # print(row.roi_id)
            x1 = int(row.xmax)
            y1 = int(row.ymax)
            x2 = int(row.xmin)
            y2 = int(row.ymin)
            # a = img.shape[0]
            # b = img.shape[1]
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            # cv2.rectangle(img, (120,96), (600,480), (0,0,255), 2)
            # cv2.rectangle(img, (240,192), (480,384), (255,128,0), 2)
            
            
            print(img.shape)

            create_dir((output_folder + "/{}/" + clip_name + '/' +  row.roi_label_threshold_based.item()).format(vmd_name))
            # if not os.path.exists():
            #     os.makedirs((output_folder + "/" + {} + '/' + clip_name + '/' + row.roi_label_threshold_based.item()).format(vmd_name))

            cv2.imwrite((output_folder + "/{}/" + clip_name + '/' + row.roi_label_threshold_based.item() + '/' + row.frame_id.item().split('.')[0] + '_' + row.roi_id.item() + ".jpg").format(vmd_name),img)
            print("done")
        else:
            create_dir((output_folder + "/{}/" + clip_name + '/' + row.roi_label_threshold_based.item()).format(vmd_name))
            # if not os.path.exists():
            #     os.makedirs((output_folder + "/" + {} + '/' + clip_name + '/' +row.roi_label_threshold_based.item()).format(vmd_name))

            cv2.imwrite((output_folder + "/{}/" + clip_name + '/' + row.roi_label_threshold_based.item() + '/' + row.frame_id.item().split('.')[0] + ".jpg").format(vmd_name),img)
            print("Undone")
    except Exception as e:
        print(e)
        # cv2.putText(img, text, (x1,y2+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)