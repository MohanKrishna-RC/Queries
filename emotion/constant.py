class Constant:
    """
    Constant is class used to store all string literals
    """

    # All file path
    LOCAL_LOCATION_OF_DOWNLOAD = '/tmp/vmd2tmd'

    FEATURE_PROCESS_MAPPING = {'locale': 'frame',
                               'shot_angle': 'frame',
                               'emotion': 'roi',
                               'age_gender': 'roi',
                               'entity': 'entity',
                               'logo': 'entity'}

    # Setting platform env
    PLATFORM_GCP = 'gs'
    PLATFORM_AWS = 's3'
    ENVIRONMENT = 'gs'

    # Single Characters
    FILE_SEPARATOR = '/'
    ENV_SEPARATOR = '://'
    FILE_EXTENSION_SEPARATOR = '.'
    PROPERTIES_FILE_SEPERATOR = '='
    BLANK = ''
    UNDERSCORE = '_'
    TS = 'ts'
    JSON_FILE_EXTENSION = '.json'
    WEIGHTS_EXTENSION = ".h5"
    YAML_EXTENSION = '.yaml'
    CSV = '.csv'
    VMD_SEPARATOR = '/vmd/'

    # file and folder names for tmd
    BEST_MODEL = 'best_model'
    SOURCE = 'source'
    DATASETS = 'datasets'
    DATASET = 'dataset'
    SUMMARY = 'summary'
    DEFAULT_VERSION = 'default'

    # default labels
    LABELS = 'labels'
    SIMILARITY = 'similarity'
    LABELS_AND_SIMILARITY = 'labels_and_similarity'

    # feature json keys
    COLLECTION = 'collection'
    TAGS = 'tags'
    FRAME_SIMILARITY_ID = 'frame_similarity_id'
    FRAME_SIMILARITY_LABEL = 'frame_similarity_label'
    FRAME_LABEL = 'frame_label'
    FEATURE_NAME = 'feature_name'
    SPATIAL_FEATURE_LOCATOR = 'spatial_feature_locator'
    ROI_SIMILARITY_ID = 'roi_similarity_id'
    ROI_SIMILARITY_LABEL = 'roi_similarity_label'
    ROI_LABEL = 'roi_label'
    DOI_SIMILARITY_ID = 'doi_similarity_id'
    DOI_SIMILARITY_LABEL = 'doi_similarity_label'
    LABEL = 'label'
    CLASS = 'class'
    CONFIDENCE = 'confidence'
    VIDEO = 'video'
    FRAMES = 'frames'
    VIDEO_FRAME_ASSET_PATH = 'video_frame_asset_path'
    TEMPORAL_FEATURE_LOCATOR = 'temporal_feature_locator'

    # Column names inside dataset
    VIDEO_ID = 'video_id'
    FRAME_ZIPFILE_PATH = 'frame_zipfile_path'
    FRAME_EMBEDDING_PATH = 'frame_embedding_path'
    FRAME_ID = 'frame_id'
    FRAME_FEATURE_NAME = 'frame_feature_name'
    FRAME_LABEL = 'frame_label'
    FRAME_LABEL_THRESHOLD_BASED = 'frame_label_threshold_based'
    ROI_ID = 'roi_id'
    VIDEO_ROI_EMBEDDING_PATH = 'video_roi_embedding_path'
    XMIN = 'xmin'
    XMAX = 'xmax'
    YMIN = 'ymin'
    YMAX = 'ymax'
    ROI_FEATURE_NAME = 'roi_feature_name'
    ROI_LABEL = 'roi_label'
    ROI_LABEL_THRESHOLD_BASED = 'roi_label_threshold_based'
    DOI_ID = 'doi_id'
    VIDEO_DOI_EMBEDDING_PATH = 'video_doi_embedding_path'
    FEATURE_START_TIME = 'feature_start_time'
    FEATURE_END_TIME = 'feature_end_time'
    DOI_FEATURE_NAME = 'doi_feature_name'
    DOI_LABEL = 'doi_label'
    DOI_LABEL_THRESHOLD_BASED = 'doi_label_threshold_based'

    # feature level
    FRAME = 'frame'
    ROI = 'roi'
    DOI = 'doi'
    ENTITY = 'entity'

    # join types
    OUTER_JOIN = 'outer'
    LEFT_JOIN = 'left'

    # folder names inside tmd folder structure
    TMD_BUCKET_NAME = 'ao-action-dectection/rohit/september19/'
    MODELS = 'models'

    # Log messages used in services
    STATUS_CODE_PROPERTIES = 'status_code.properties'

    # variables used in custom exception
    UTILITY_EXCEPTION = 'UTILITY_EXCEPTION'
    DOWNLOAD_EXCEPTION = 'DOWNLOAD_EXCEPTION'
    UPLOAD_EXCEPTION = 'UPLOAD_EXCEPTION'
    ENV_NOT_SUPPORTED_EXCEPTION = 'ENV_NOT_SUPPORTED_EXCEPTION'
    SERVICE_EXCEPTION = 'SERVICE_EXCEPTION'
    INVALID_VIDEO_EXCEPTION = 'INVALID_VIDEO_EXCEPTION'
    INVALID_JSON_KEY_REQUEST = 'INVALID_JSON_KEY_REQUEST'
    FRAME_GENERATION_EXCEPTION = 'FRAME_GENERATION_EXCEPTION'
    INVALID_LIBRARY_EXCEPTION = 'INVALID_LIBRARY_EXCEPTION'
    BUCKET_NAME = 'BUCKET_NAME'
    SOURCE_FILE_KEY = 'SOURCE_FILE_KEY'
    OUTPUT = 'OUTPUT'

