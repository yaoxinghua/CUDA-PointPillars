"""
author: hova88
date: 2021/03/16
"""
import sys
import numpy as np
from visual_tools import draw_clouds_with_boxes
import open3d as o3d

if __name__ == "__main__":
    cloud_path = '../data/000008.bin'
    boxes_path = '../data/box_prediction/result_000008.txt'
    score_thresh = 0.2
    if len(sys.argv) == 3:
        cloud_path = sys.argv[1]
        boxes_path = sys.argv[2]
    cloud = np.fromfile(cloud_path, dtype=np.float32).reshape(-1,4)
    boxes = np.loadtxt(boxes_path).reshape(-1,9)
    boxes = boxes[boxes[:, -1] > score_thresh]
    draw_clouds_with_boxes(cloud, boxes)
