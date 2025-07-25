# ProtagoDoc Scripts

This directory contains utility scripts for ProtagoDoc setup and maintenance.

## Scripts

### `download_models_hf.py`
Downloads MinerU model weights from Hugging Face and configures the system for optimal performance.

**What it does:**
- Downloads PDF processing models (~2.5GB) to `tools/mineru/local_models/`
- Downloads layout reader models for document analysis
- Creates `~/magic-pdf.json` configuration file with local paths
- Enables GPU acceleration by default (`device-mode: cuda`)

**Usage:**
```bash
# From project root directory
python scripts/download_models_hf.py
```

**Requirements:**
- `huggingface_hub` package: `pip install huggingface_hub`
- Internet connection for model download
- ~3GB free disk space

**Output:**
- Models downloaded to: `tools/mineru/local_models/models/`
- Layout reader: `tools/mineru/local_models/layoutreader/`
- Config file: `~/magic-pdf.json`

**Features:**
- Downloads models to local project directory (not global cache)
- Automatically configures local paths in config file
- Enables GPU acceleration by default
- Preserves existing configuration settings when updating

**Note:** The `local_models/` directory is excluded from git via `.gitignore` due to its large size (2.5GB).

### `test_fresh_setup.py`
Validation script that checks if ProtagoDoc setup is working correctly.

**What it does:**
- Validates directory structure and required files
- Tests Python dependencies (PyTorch, Hugging Face Hub)
- Checks GPU availability and CUDA support
- Verifies MinerU installation
- Confirms model files are downloaded
- Validates configuration file settings

**Usage:**
```bash
# From project root directory, with conda environment activated
python scripts/test_fresh_setup.py
```

**Output:**
- ✅ Green checkmarks for successful validations
- ⚠️  Yellow warnings for missing but non-critical items
- ❌ Red errors for required items that need attention
- 🎉 Success summary with next steps

**Use Cases:**
- After fresh clone and setup
- Troubleshooting setup issues
- Verifying environment before processing documents
- CI/CD validation in automated deployments

## Model Organization

After running the download script:

```
tools/mineru/local_models/
├── models/
│   ├── Layout/YOLO/          # Document layout detection
│   ├── MFD/YOLO/            # Mathematical formula detection  
│   ├── MFR/unimernet_hf_small_2503/  # Formula recognition
│   └── OCR/paddleocr_torch/  # Text recognition
└── layoutreader/            # Document layout reading
    ├── config.json
    └── model.safetensors
```

Total size: ~2.5GB (excluded from git) 