# Acquisition Notes

## Location

The RealSense BAG sequence `20241128_133505.bag` was recorded at Zigzag, the interactive science and technology center associated with COZCyT (Consejo Zacatecano de Ciencia, Tecnología e Innovación) in Zacatecas, Mexico, using a controlled sandy-terrain test area to emulate beach-cleaning visual conditions (sandy background, outdoor-like lighting).

- Zigzag: <https://zigzag.gob.mx/>
- COZCyT: <https://www.zacatecas.gob.mx/gobierno/dependencias/cozcyt/>

## Acquisition pattern

The platform followed a **zigzag traversal pattern** around the target bottle during acquisition.

## Target

A single bottle prop, used consistently across the acquisition session as the detection target.

## Intended visual variability

The zigzag pattern was designed to introduce variability along several axes while recording:

- **Distance** to the target.
- **Viewing angle** relative to the target.
- **Relative position** of the target within the frame.
- **Sandy-background appearance** (different patches of sand texture/lighting).
- **Partial occlusion**, where present.

## Sensor and downstream use

An Intel RealSense camera recorded the RGB stream corresponding to this acquisition session. The still-image dataset (`../dataset_yolo/`) was extracted and annotated from material captured under this same protocol; the `.bag` recording in `../bags/` is used afterward as a fixed input for **offline replay** (see `../bags/README_BAGS.md`), allowing the same visual sequence to be reprocessed repeatedly with consistent, traceable detection logs.

## Scope

This acquisition protocol supports an offline evaluation of the visual-perception subsystem. It does not constitute validated autonomous navigation, closed-loop robot control, or validated physical waste collection.
