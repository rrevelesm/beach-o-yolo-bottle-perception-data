# Dataset Card

## Dataset name

Beach-O YOLO Bottle Perception Dataset (sequence-aware, leakage-free split)

## Task

One-class object detection: **bottle** (class id `0`).

## Sensor

Intel RealSense RGB stream (RealSense depth camera family; only the RGB stream is used for detection).

## Acquisition environment

Controlled sandy-terrain test area at COZCyT, used to emulate the visual conditions of the beach-cleaning scenario (sandy background, a single bottle target).

## Acquisition pattern

The platform followed a zigzag traversal pattern around the target bottle during acquisition, intended to introduce visual variability in distance, viewing angle, relative position, sandy-background appearance, and partial occlusion where present.

## Dataset statistics

| Metric | Train | Validation | Total |
|---|---|---|---|
| Images | 1267 | 318 | 1585 |
| Labels | 1267 | 318 | 1585 |
| Bounding boxes | 2478 | 689 | 3167 |
| Negative images (empty label file) | 14 | 0 | 14 |
| Missing labels | 0 | 0 | 0 |
| Orphan labels | 0 | 0 | 0 |

Split: sequence-aware and leakage-free — constructed so that near-duplicate video frames from the same recorded sequence never appear on both sides of the train/validation boundary (see `metadata/label_audit_report.md`).

## Annotation format

Standard YOLO format, one `.txt` file per image:

```
class_id x_center y_center width height
```

Coordinates normalized to image width/height. Class `0` is the only class (`bottle`). Empty label files represent valid negative images (no bottle present), not missing annotations.

## Known limitations

- **Single environment**: all images originate from one controlled test area (COZCyT sandy terrain), not multiple real beaches.
- **Sandy background**: visual domain is limited to sand-colored background; generalization to other substrates (rocks, vegetation, pavement, wet sand, etc.) is untested.
- **Single bottle target / narrow domain**: acquisition used one bottle prop; generalization to other bottle types, colors, materials, or partially crushed/deformed bottles is untested.
- **BAG replay without frame-level ground truth**: the accompanying `.bag` recording (see `bags/README_BAGS.md`) has no per-frame bounding-box ground truth; it supports qualitative/activity-level offline evaluation (detection counts, confidence, timing), not frame-by-frame accuracy measurement.
- **Not evidence of closed-loop robot autonomy**: this dataset and the BAG recording support an **offline** visual-perception evaluation only. They do not constitute evidence of autonomous navigation, closed-loop robot control, or physical waste-collection success.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0). See `LICENSE_DATA.md` for the full statement and `CITATION.cff` for citation details.
