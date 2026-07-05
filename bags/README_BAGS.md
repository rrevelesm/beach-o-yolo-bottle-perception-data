# RealSense BAG Recording

## File

`20241128_133505.bag` — Intel RealSense `.bag` recording (RGB stream), approximately 4.5 GB.

## Acquisition

Recorded on a controlled sandy-terrain test area at COZCyT, used to emulate the visual conditions of the beach-cleaning scenario. The platform followed a zigzag traversal pattern around a target bottle during acquisition, intended to introduce visual variability in distance, viewing angle, relative position, sandy-background appearance, and partial occlusion where present. See `../metadata/acquisition_notes.md` for details.

## Intended use: offline RealSense BAG replay

This recording is used for **offline replay**: the same recorded RGB sequence is reprocessed by the YOLO detector, logging detections, confidence, inference time, and detection geometry per frame. This provides a repeatable, traceable evaluation of the visual-perception subsystem using a fixed, deterministic input.

## What this recording does NOT demonstrate

- It does **not** validate autonomous navigation.
- It does **not** validate physical waste collection.
- It does **not** constitute closed-loop robot validation.
- It has **no per-frame ground-truth bounding boxes**, so replay results describe detection activity and timing, not frame-by-frame accuracy.

## Conceptual usage with the Intel RealSense SDK

Conceptually (see the official Intel RealSense SDK documentation for exact APIs): a `.bag` file is loaded as a read-only, file-backed device using the SDK's playback mechanism (e.g., `rs2::config.enable_device_from_file(...)` in the C++/Python APIs), and frames are retrieved from it exactly as they would be from a live camera. Because a recorded file only contains a finite number of frames, playback code should poll for frames rather than block waiting for a live stream to continue indefinitely.

## Size warning

This file is large (~4.5 GB). It is distributed through the public OneDrive folder, not through GitHub. Verify the download against `../checksums/sha256_bag_manifest.csv` (SHA256) before use.
