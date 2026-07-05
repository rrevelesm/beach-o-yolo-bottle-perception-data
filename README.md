# Beach-O YOLO Bottle Perception Dataset

Este repositorio documenta el **Beach-O YOLO Bottle Perception Dataset**: un dataset de detección de objetos en formato YOLO, de una sola clase (`bottle`), con partición secuencial libre de fuga (sequence-aware, leakage-free), junto con la documentación de la grabación RealSense (`.bag`) usada para evaluación offline.

## Qué contiene este repositorio

Acceso a **datos, metadatos, checksums y documentación** del dataset: tarjeta del dataset (`DATASET_CARD.md`), descripción del formato de anotación, reporte de auditoría de etiquetas, notas de adquisición, mapeo de clases, CSVs resumen, manifiestos SHA256 de integridad, y una pequeña muestra de vista previa (`sample_preview/`).

## Dónde están los datos completos

**El dataset completo YOLO (imágenes y etiquetas) y el archivo `.bag` se distribuyen mediante OneDrive público**, no a través de este repositorio, debido a su tamaño:

- **Enlace OneDrive:** <https://correoipn-my.sharepoint.com/:f:/g/personal/rrevelesm_ipn_mx/IgCiyaKrIn8QS7AkDMn75sorAT_U_HqmV9DvqAq2b6vq5Pg?e=xB7MCG>
- **DOI Zenodo:** [10.5281/zenodo.21209356](https://doi.org/10.5281/zenodo.21209356)

## Qué NO contiene este repositorio

**Este repositorio no contiene el manuscrito ni sus fuentes LaTeX.** No incluye `main.tex`, `sections/`, `references.bib`, la plantilla MDPI, ni el PDF compilado del artículo. El artículo asociado a este dataset se somete y revisa por separado.

## Estructura del repositorio

```text
README.md
DATASET_CARD.md
LICENSE_DATA.md
CITATION.cff
.gitignore
checksums/
  file_inventory.csv
  sha256_dataset_manifest.csv
  sha256_bag_manifest.csv
metadata/
  dataset_summary.csv
  sequence_split_summary.csv
  class_mapping.yaml
  acquisition_notes.md
  label_audit_report.md
bags/
  README_BAGS.md
  bag_manifest.csv
dataset_yolo/
  README_YOLO_FORMAT.md
sample_preview/
  sample_images/, sample_labels/, README_SAMPLE.md
release_notes/
  v1.0.md
scripts/
  verify_checksums.py       <- verifica una copia descargada contra los manifiestos SHA256
  summarize_manifest.py     <- resume checksums/file_inventory.csv (sin necesidad de descargar nada)
```

## Verificar una copia descargada

Después de descargar el dataset/BAG desde el enlace de OneDrive anterior:

```bash
python scripts/verify_checksums.py --root /ruta/a/beach-o-yolo-bottle-perception-data
```

## Citación

Ver `CITATION.cff`.

## Licencia

**License: Creative Commons Attribution 4.0 International (CC BY 4.0)**
**URL:** https://creativecommons.org/licenses/by/4.0/

Ver `LICENSE_DATA.md` para el texto completo y `CITATION.cff` para detalles de citación.
