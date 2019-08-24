from mpiigaze.config.config_node import ConfigNode

config = ConfigNode()

config.dataset = ConfigNode()
config.dataset.dataset_dir = 'datasets/preprocessed'

config.model = ConfigNode()
config.model.name = 'lenet'

config.train = ConfigNode()
config.train.device = 'cuda'
config.train.batch_size = 64
# optimizer (options: sgd, adam, amsgrad)
config.train.optimizer = 'sgd'
config.train.base_lr = 0.01
config.train.momentum = 0.9
config.train.nesterov = True
config.train.weight_decay = 1e-4
config.train.no_weight_decay_on_bn = False
config.train.seed = 0
config.train.val_first = True
config.train.val_period = 1

config.train.test_id = 0
config.train.val_ratio = 0.1

config.train.output_dir = 'experiments/exp00'
config.train.log_period = 100
config.train.checkpoint_period = 10

config.train.use_tensorboard = True
config.tensorboard = ConfigNode()
config.tensorboard.train_images = False
config.tensorboard.val_images = False
config.tensorboard.model_params = False

# optimizer
config.optim = ConfigNode()
# Adam
config.optim.adam = ConfigNode()
config.optim.adam.betas = (0.9, 0.999)

# scheduler
config.scheduler = ConfigNode()
config.scheduler.epochs = 40
# scheduler (options: multistep, cosine)
config.scheduler.type = 'multistep'
config.scheduler.milestones = [20, 30]
config.scheduler.lr_decay = 0.1
config.scheduler.lr_min_factor = 0.001

# train data loader
config.train.train_dataloader = ConfigNode()
config.train.train_dataloader.num_workers = 2
config.train.train_dataloader.drop_last = True
config.train.train_dataloader.pin_memory = False
config.train.val_dataloader = ConfigNode()
config.train.val_dataloader.num_workers = 1
config.train.val_dataloader.pin_memory = False

# test config
config.test = ConfigNode()
config.test.test_id = 0
config.test.checkpoint = ''
config.test.output_dir = ''
config.test.device = 'cuda'
config.test.batch_size = 256
# test data loader
config.test.dataloader = ConfigNode()
config.test.dataloader.num_workers = 2
config.test.dataloader.pin_memory = False

# Face detector
config.face_detector = ConfigNode()
config.face_detector.mode = 'dlib'
config.face_detector.dlib = ConfigNode()
config.face_detector.dlib.model = 'data/dlib/shape_predictor_68_face_landmarks.dat'

# demo
config.demo = ConfigNode()
config.demo.use_camera = True
config.demo.video_path = ''
config.demo.camera_params = ''
config.demo.normalized_camera_params = 'data/calib/normalized_camera_params_eye.yaml'
config.demo.checkpoint = ''
config.demo.device = 'cuda'
config.demo.normalized_camera_distance = 0.6
config.demo.gaze_visualization_length = 0.05

# cuDNN
config.cudnn = ConfigNode()
config.cudnn.benchmark = True
config.cudnn.deterministic = False


def get_default_config():
    return config.clone()