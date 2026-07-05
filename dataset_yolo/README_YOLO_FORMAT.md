# YOLO Annotation Format

Each image has a corresponding `.txt` label file with the same base filename (e.g., `image_0001.png` ↔ `image_0001.txt`).

## Label file format

Each line in a label file describes one bounding box:

```
class_id x_center y_center width height
```

- `class_id` — integer class index. This dataset has a single class:
  ```
  0: bottle
  ```
- `x_center`, `y_center`, `width`, `height` — normalized to the image's width and height (values in `[0, 1]`), following the standard Ultralytics YOLO convention.

## Negative images

Images with no bottle instance are represented by an **empty (zero-byte) `.txt` label file**, not by a missing file. Empty label files are valid negative examples and must be preserved when training or auditing this dataset — they should not be mistaken for missing annotations.

## Folder layout

```
train/images/   train/labels/
val/images/     val/labels/
```

`data_sequence_split.yaml` (and its alias `data.yaml`) in the parent `dataset_yolo/` folder point at this layout with `path: .` (relative to the YAML file itself).
