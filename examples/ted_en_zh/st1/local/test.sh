#! /usr/bin/env bash

if [ $# != 3 ];then
    echo "usage: ${0} config_path decode_config_path ckpt_path_prefix"
    exit -1
fi

ngpu=$(echo $CUDA_VISIBLE_DEVICES | awk -F "," '{print NF}')
echo "using $ngpu gpus..."

config_path=$1
decode_config_path=$2
ckpt_prefix=$3

for type in fullsentence; do
    echo "decoding ${type}"
    python3 -u ${BIN_DIR}/test.py \
    --ngpu ${ngpu} \
    --config ${config_path} \
    --decode_cfg ${decode_config_path} \
    --result_file ${ckpt_prefix}.${type}.rsl \
    --checkpoint_path ${ckpt_prefix} \
<<<<<<< HEAD
    --opts decode.decoding_method ${type} \
    --opts decode.decode_batch_size ${batch_size}
=======
    --opts decoding.decoding_method ${type} \
>>>>>>> 6272496d9c26736750b577fd832ea9dd4ddc4e6e

    if [ $? -ne 0 ]; then
        echo "Failed in evaluation!"
        exit 1
    fi
done

exit 0
