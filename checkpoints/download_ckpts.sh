#!/bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# Define the target download directory
DOWNLOAD_DIR="/kaggle/working/segsegseg/checkpoints"

# Create the target directory if it doesn't exist
mkdir -p $DOWNLOAD_DIR

# Define the URLs for the checkpoints
BASE_URL="https://dl.fbaipublicfiles.com/segment_anything_2/072824/"
sam2_hiera_t_url="${BASE_URL}sam2_hiera_tiny.pt"
sam2_hiera_s_url="${BASE_URL}sam2_hiera_small.pt"
sam2_hiera_b_plus_url="${BASE_URL}sam2_hiera_base_plus.pt"
sam2_hiera_l_url="${BASE_URL}sam2_hiera_large.pt"

# Download each of the four checkpoints using wget
echo "Downloading sam2_hiera_tiny.pt checkpoint..."
wget -P $DOWNLOAD_DIR $sam2_hiera_t_url || { echo "Failed to download checkpoint from $sam2_hiera_t_url"; exit 1; }
echo "Downloading sam2_hiera_small.pt checkpoint..."
wget -P $DOWNLOAD_DIR $sam2_hiera_s_url || { echo "Failed to download checkpoint from $sam2_hiera_s_url"; exit 1; }
echo "Downloading sam2_hiera_base_plus.pt checkpoint..."
wget -P $DOWNLOAD_DIR $sam2_hiera_b_plus_url || { echo "Failed to download checkpoint from $sam2_hiera_b_plus_url"; exit 1; }
echo "Downloading sam2_hiera_large.pt checkpoint..."
wget -P $DOWNLOAD_DIR $sam2_hiera_l_url || { echo "Failed to download checkpoint from $sam2_hiera_l_url"; exit 1; }
echo "All checkpoints are downloaded successfully to $DOWNLOAD_DIR."