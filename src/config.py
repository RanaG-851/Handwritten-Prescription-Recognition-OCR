
common_config = {
    'data_dir': 'data/mnt/ramdisk/max/90kDICT32px/',
    'img_width': 100,
    'img_height': 32,
    'map_to_seq_hidden': 64,
    'rnn_hidden': 256,
    'leaky_relu': False,
}
train_config = {
    'epochs': 10000,
    'train_batch_size': 32,
    'eval_batch_size': 512,
    'lr': 0.0005,
    'show_interval': 10,
    'valid_interval': 500,
    'save_interval': 2000,
    'cpu_workers': 4,
    'reload_checkpoint': None,
    'valid_max_iter': 10,
    'decode_method': 'greedy',
    'beam_size': 10,
    'checkpoints_dir': 'checkpoints/'
}
# train_config = {
#     'epochs': 1,
#     'train_batch_size': 8,
#     'eval_batch_size': 32,
#     'lr': 0.0005,
#     'show_interval': 10,
#     'valid_interval': 50,
#     'save_interval': 50,
#     'cpu_workers': 2,
#     'reload_checkpoint': None,
#     'valid_max_iter': 10,
#     'decode_method': 'greedy',
#     'beam_size': 5,
#     'checkpoints_dir': 'checkpoints/'
# }

train_config.update(common_config)

evaluate_config = {
    # 'eval_batch_size': 512,
    'eval_batch_size': 256,
    'cpu_workers': 4,
    'reload_checkpoint': 'checkpoints/crnn_synth90k.pt',
    'decode_method': 'beam_search',
    'beam_size': 10,
}
evaluate_config.update(common_config)
