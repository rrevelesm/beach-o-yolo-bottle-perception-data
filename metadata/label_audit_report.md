# Label Audit Report

## Corrected six-column label defect

A preliminary version of this dataset had a subset of label files carrying a **spurious sixth column** — a leftover model-confidence score from an earlier inference pass — that is not part of the standard YOLO label format (`class_id x_center y_center width height`). Ultralytics silently treats such malformed files as corrupt and drops their annotations during dataset caching, so a large fraction of the intended supervision signal would have been discarded without an explicit audit. This defect was identified and corrected before producing the final dataset distributed here: every label file in `../dataset_yolo/` has exactly five columns per row.

## Sequence-aware, leakage-free split

The train/validation split distributed in `../dataset_yolo/` is **sequence-aware**: it was constructed so that near-duplicate video frames originating from the same recorded sequence are never split across the train and validation partitions. An earlier, naively-constructed random frame-level split allowed near-duplicate frames to leak across partitions, which would inflate validation metrics because the model could effectively be evaluated on samples it had already seen a near-copy of during training. See `dataset_summary.csv` in this same folder for the final, post-correction counts.

## Final audit results (this dataset)

| Split | Images | Labels | Boxes | Empty label files (negatives) | Missing labels | Orphan labels |
|---|---|---|---|---|---|---|
| train | 1267 | 1267 | 2478 | 14 | 0 | 0 |
| val | 318 | 318 | 689 | 0 | 0 | 0 |
| total | 1585 | 1585 | 3167 | 14 | 0 | 0 |

- **Zero missing labels**: every image has a corresponding label file.
- **Zero orphan labels**: every label file has a corresponding image.
- **14 negative images**: 14 label files in the training split are intentionally empty (zero-byte), representing images with no bottle instance. These are valid negatives, not annotation gaps — see `../dataset_yolo/README_YOLO_FORMAT.md`.

## Warning: do not mix with earlier, non-sequence-aware splits

Earlier working versions of this dataset used a random, non-sequence-aware train/validation split. **Do not combine images, labels, or reported metrics from any earlier random split with the sequence-aware split distributed here.** Mixing them would reintroduce near-duplicate-frame leakage between train and validation and invalidate any resulting evaluation. Only the split contained in `../dataset_yolo/`, and its associated `dataset_summary.csv`, corresponds to the final results reported in the manuscript.
