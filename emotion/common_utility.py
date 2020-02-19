from constant import Constant
import pandas as pd
import numpy as np

class Commonutility:

    @classmethod
    def get_label(cls, labels_dict, threshold=None):
        if threshold == None:
            threshold = -np.inf
        max_label = None
        max_confidence = -np.inf
        for class_name, confidence in labels_dict.items():
            if confidence != None and confidence > max_confidence and confidence >= threshold:
                max_confidence = confidence
                max_label = class_name
        return str(max_label)

    def get_frame_labels(self, frame_feature, label_level, frame_similarity_id, frame_similarity_label,
                         threshold):
        _frame_label = {}
        if label_level == Constant.LABELS:
            for frame_label in frame_feature[Constant.LABEL]:
                frame_feature_class_name = frame_label[Constant.CLASS]
                frame_feature_class_confidence = frame_label[Constant.CONFIDENCE]
                _frame_label[frame_feature_class_name] = frame_feature_class_confidence
            frame_label_threshold_based = self.get_label(
                _frame_label, threshold)
        elif label_level == Constant.SIMILARITY:
            if frame_similarity_label != None:
                frame_label_threshold_based = frame_similarity_label
            else:
                if len(frame_similarity_id) == 0:
                    frame_label_threshold_based = None
                else:
                    frame_label_threshold_based = frame_similarity_id[0]
        elif label_level == Constant.LABELS_AND_SIMILARITY:
            for frame_label in frame_feature[Constant.LABEL]:
                frame_feature_class_name = frame_label[Constant.CLASS]
                frame_feature_class_confidence = frame_label[Constant.CONFIDENCE]
                _frame_label[frame_feature_class_name] = frame_feature_class_confidence
            frame_label_threshold_based = self.get_label(
                _frame_label, threshold)
            if frame_label_threshold_based == None:
                if frame_similarity_label != None:
                    frame_label_threshold_based = frame_similarity_label
                else:
                    if len(frame_similarity_id) == 0:
                        frame_label_threshold_based = None
                    else:
                        frame_label_threshold_based = frame_similarity_id[0]
        return _frame_label, frame_label_threshold_based

    def get_roi_labels(self, roi_feature, label_level, roi_similarity_id, roi_similarity_label,
                       threshold):
        _roi_label = {}
        if label_level == Constant.LABELS:
            for roi_label in roi_feature[Constant.LABEL]:
                roi_feature_class_name = roi_label[Constant.CLASS]
                roi_feature_class_confidence = roi_label[Constant.CONFIDENCE]
                _roi_label[roi_feature_class_name] = roi_feature_class_confidence
            roi_label_threshold_based = self.get_label(_roi_label, threshold)
        elif label_level == Constant.SIMILARITY:
            if roi_similarity_label != None:
                roi_label_threshold_based = roi_similarity_label
            else:
                if len(roi_similarity_id) == 0:
                    roi_label_threshold_based = None
                else:
                    roi_label_threshold_based = roi_similarity_id[0]
        elif label_level == Constant.LABELS_AND_SIMILARITY:
            for roi_label in roi_feature[Constant.LABEL]:
                roi_feature_class_name = roi_label[Constant.CLASS]
                roi_feature_class_confidence = roi_label[Constant.CONFIDENCE]
                _roi_label[roi_feature_class_name] = roi_feature_class_confidence
            roi_label_threshold_based = self.get_label(_roi_label, threshold)
            if roi_label_threshold_based == None:
                if roi_similarity_label != None:
                    roi_label_threshold_based = roi_similarity_label
                else:
                    if len(roi_similarity_id) == 0:
                        roi_label_threshold_based = None
                    else:
                        roi_label_threshold_based = roi_similarity_id[0]
        return _roi_label, roi_label_threshold_based

    def get_doi_labels(self, doi_feature, label_level, doi_similarity_id, doi_similarity_label,
                       threshold):
        _doi_label = {}
        if label_level == Constant.LABELS:
            for doi_label in doi_feature[Constant.LABEL]:
                doi_feature_class_name = doi_label[Constant.CLASS]
                doi_feature_class_confidence = doi_label[Constant.CONFIDENCE]
                _doi_label[doi_feature_class_name] = doi_feature_class_confidence
            doi_label_threshold_based = self.get_label(_doi_label, threshold)
        elif label_level == Constant.SIMILARITY:
            if doi_similarity_label != None:
                doi_label_threshold_based = doi_similarity_label
            else:
                if len(doi_similarity_id) == 0:
                    doi_label_threshold_based = None
                else:
                    doi_label_threshold_based = doi_similarity_id[0]
        elif label_level == Constant.LABELS_AND_SIMILARITY:
            for doi_label in doi_feature[Constant.LABEL]:
                doi_feature_class_name = doi_label[Constant.CLASS]
                doi_feature_class_confidence = doi_label[Constant.CONFIDENCE]
                _doi_label[doi_feature_class_name] = doi_feature_class_confidence
            doi_label_threshold_based = self.get_label(_doi_label, threshold)
            if doi_label_threshold_based == None:
                if doi_similarity_label != None:
                    doi_label_threshold_based = doi_similarity_label
                else:
                    if len(doi_similarity_id) == 0:
                        doi_label_threshold_based = None
                    else:
                        doi_label_threshold_based = doi_similarity_id[0]
        return _doi_label, doi_label_threshold_based

    def frame_level_df(self, frame_info_df, video_id, frame_zipfile_path, frame_embedding_path, frame_id,
                       threshold, frame, label_level):
        frame_similarity_id = frame[Constant.TAGS][Constant.FRAME_SIMILARITY_ID]
        frame_similarity_label = frame[Constant.TAGS][Constant.FRAME_SIMILARITY_LABEL]
        for frame_feature in frame[Constant.TAGS][Constant.FRAME_LABEL]:
            frame_feature_name = frame_feature[Constant.FEATURE_NAME]
            _frame_label, frame_label_threshold_based = self.get_frame_labels(frame_feature, label_level,
                                                                              frame_similarity_id,
                                                                              frame_similarity_label,
                                                                              threshold)
            frame_info_df_row = {Constant.VIDEO_ID: [video_id],
                                 Constant.FRAME_ZIPFILE_PATH: [frame_zipfile_path],
                                 Constant.FRAME_EMBEDDING_PATH: [frame_embedding_path],
                                 Constant.FRAME_ID: [frame_id],
                                 Constant.FRAME_FEATURE_NAME: [frame_feature_name],
                                 Constant.FRAME_LABEL: [_frame_label],
                                 Constant.FRAME_LABEL_THRESHOLD_BASED: [frame_label_threshold_based]}
            _frame_info_df = pd.DataFrame(frame_info_df_row)
            frame_info_df = frame_info_df.append(_frame_info_df)
        return frame_info_df

    def roi_level_df(self, roi_info_df, video_id, frame_zipfile_path, frame_id, threshold,
                     frame, label_level):
        for roi in frame[Constant.ROI]:
            xmin = roi[Constant.SPATIAL_FEATURE_LOCATOR][Constant.XMIN]
            ymin = roi[Constant.SPATIAL_FEATURE_LOCATOR][Constant.YMIN]
            xmax = roi[Constant.SPATIAL_FEATURE_LOCATOR][Constant.XMAX]
            ymax = roi[Constant.SPATIAL_FEATURE_LOCATOR][Constant.YMAX]
            roi_id = roi[Constant.ROI_ID]
            video_roi_embedding_path = roi[Constant.VIDEO_ROI_EMBEDDING_PATH]
            roi_similarity_id = roi[Constant.TAGS][Constant.ROI_SIMILARITY_ID]
            roi_similarity_label = roi[Constant.TAGS][Constant.ROI_SIMILARITY_LABEL]
            for roi_feature in roi[Constant.TAGS][Constant.ROI_LABEL]:
                roi_feature_name = roi_feature[Constant.FEATURE_NAME]
                _roi_label, roi_label_threshold_based = self.get_roi_labels(roi_feature, label_level,
                                                                            roi_similarity_id,
                                                                            roi_similarity_label,
                                                                            threshold)
                roi_info_df_row = {Constant.VIDEO_ID: [video_id],
                                   Constant.FRAME_ZIPFILE_PATH: [frame_zipfile_path],
                                   Constant.FRAME_ID: [frame_id],
                                   Constant.VIDEO_ROI_EMBEDDING_PATH: [video_roi_embedding_path],
                                   Constant.ROI_ID: [roi_id],
                                   Constant.XMIN: [xmin],
                                   Constant.XMAX: [xmax],
                                   Constant.YMIN: [ymin],
                                   Constant.YMAX: [ymax],
                                   Constant.ROI_FEATURE_NAME: [roi_feature_name],
                                   Constant.ROI_LABEL: [_roi_label],
                                   Constant.ROI_LABEL_THRESHOLD_BASED: [roi_label_threshold_based]}
                _roi_info_df = pd.DataFrame(roi_info_df_row)
                roi_info_df = roi_info_df.append(_roi_info_df)
        return roi_info_df

    def doi_level_df(self, doi_info_df, video_id, frame_zipfile_path, frame_id, threshold, frame,
                     label_level):
        for doi in frame[Constant.DOI]:
            feature_start_time = doi[Constant.TEMPORAL_FEATURE_LOCATOR][Constant.FEATURE_START_TIME]
            feature_end_time = doi[Constant.TEMPORAL_FEATURE_LOCATOR][Constant.FEATURE_END_TIME]
            doi_id = doi[Constant.DOI_ID]
            video_doi_embedding_path = doi[Constant.VIDEO_DOI_EMBEDDING_PATH]
            doi_similarity_id = doi[Constant.TAGS][Constant.DOI_SIMILARITY_ID]
            doi_similarity_label = doi[Constant.TAGS][Constant.DOI_SIMILARITY_ID]
            for doi_feature in doi[Constant.TAGS][Constant.DOI_LABEL]:
                doi_feature_name = doi_feature[Constant.FEATURE_NAME]
                _doi_label,  doi_label_threshold_based = self.get_doi_labels(doi_feature, label_level,
                                                                             doi_similarity_id,
                                                                             doi_similarity_label,
                                                                             threshold)
                doi_info_df_row = {Constant.VIDEO_ID: [video_id],
                                   Constant.FRAME_ZIPFILE_PATH: [frame_zipfile_path],
                                   Constant.FRAME_ID: [frame_id],
                                   Constant.VIDEO_DOI_EMBEDDING_PATH: [video_doi_embedding_path],
                                   Constant.DOI_ID: [doi_id],
                                   Constant.FEATURE_START_TIME: [feature_start_time],
                                   Constant.FEATURE_END_TIME: [feature_end_time],
                                   Constant.DOI_FEATURE_NAME: [doi_feature_name],
                                   Constant.DOI_LABEL: [_doi_label],
                                   Constant.DOI_LABEL_THRESHOLD_BASED: [doi_label_threshold_based]}
                _doi_info_df = pd.DataFrame(doi_info_df_row)
                doi_info_df = doi_info_df.append(_doi_info_df)
        return doi_info_df

    def prepare_metadata(self, vmd, obj_type, threshold, label_level=Constant.LABELS):
        vmd = vmd[Constant.COLLECTION][0]
        frame_info_df = pd.DataFrame(columns=[Constant.VIDEO_ID, Constant.FRAME_ZIPFILE_PATH,
                                              Constant.FRAME_EMBEDDING_PATH, Constant.FRAME_ID,
                                              Constant.FRAME_FEATURE_NAME, Constant.FRAME_LABEL,
                                              Constant.FRAME_LABEL_THRESHOLD_BASED])
        roi_info_df = pd.DataFrame(columns=[Constant.VIDEO_ID, Constant.FRAME_ZIPFILE_PATH,
                                            Constant.FRAME_ID, Constant.VIDEO_ROI_EMBEDDING_PATH,
                                            Constant.ROI_ID, Constant.XMIN, Constant.YMIN, Constant.XMAX,
                                            Constant.YMAX, Constant.ROI_FEATURE_NAME, Constant.ROI_LABEL,
                                            Constant.ROI_LABEL_THRESHOLD_BASED])
        doi_info_df = pd.DataFrame(columns=[Constant.VIDEO_ID,  Constant.FRAME_ZIPFILE_PATH,
                                            Constant.FRAME_ID, Constant.VIDEO_DOI_EMBEDDING_PATH,
                                            Constant.DOI_ID, Constant.FEATURE_START_TIME,
                                            Constant.FEATURE_END_TIME, Constant.DOI_FEATURE_NAME,
                                            Constant.DOI_LABEL, Constant.DOI_LABEL_THRESHOLD_BASED])
        video_id = vmd[Constant.VIDEO][Constant.VIDEO_ID]
        for frame in vmd[Constant.VIDEO][Constant.FRAMES]:
            frame_embedding_path = frame[Constant.FRAME_EMBEDDING_PATH]
            frame_zipfile_path = frame[Constant.VIDEO_FRAME_ASSET_PATH]
            frame_id = frame[Constant.FRAME_ID]
            if obj_type == Constant.FRAME:
                frame_info_df = self.frame_level_df(frame_info_df, video_id, frame_zipfile_path,
                                                    frame_embedding_path, frame_id, threshold,
                                                    frame, label_level)
            elif obj_type == Constant.ROI or obj_type == Constant.ENTITY:
                roi_info_df = self.roi_level_df(roi_info_df, video_id, frame_zipfile_path,
                                                frame_id, threshold, frame, label_level)
            elif obj_type == Constant.DOI:
                doi_info_df = self.doi_level_df(doi_info_df, video_id, frame_zipfile_path,
                                                frame_id, threshold, frame, label_level)
        if obj_type == Constant.FRAME:
            return frame_info_df
        elif obj_type == Constant.ROI or obj_type == Constant.ENTITY:
            return roi_info_df
        else:
            return doi_info_df
    
    