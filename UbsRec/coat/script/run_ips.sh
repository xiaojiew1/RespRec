data_dir=~/Downloads/data/coat_incl_0.05
all_reg=0.001
batch_norm=0
batch_size=128
eval_freq=10
i_input=0:2
i_input=0:10
inner_lr=0.01
base_model=fm
n_epoch=200
n_factor=128
n_trial=10
opt_type=adagrad
verbose=1
python -W ignore ../run_ips.py \
    --data_dir ${data_dir} \
    --all_reg ${all_reg} \
    --batch_norm ${batch_norm} \
    --batch_size ${batch_size} \
    --eval_freq ${eval_freq} \
    --i_input ${i_input} \
    --inner_lr ${inner_lr} \
    --base_model ${base_model} \
    --n_epoch ${n_epoch} \
    --n_factor ${n_factor} \
    --n_trial ${n_trial} \
    --opt_type ${opt_type} \
    --verbose ${verbose}

