# ProtagoDoc

A curated collection of useful tools organized as git submodules for easy management and deployment.

## 🛠️ Tools Collection

This repository serves as a centralized hub for various development and productivity tools, each maintained as a git submodule for easy version control and updates.

### Document Processing

#### [MinerU](https://github.com/opendatalab/MinerU)
**Location:** `tools/mineru` | **Version:** 1.3.10 (magic_pdf-1.3.11-released tag)

A high-quality tool for converting PDF to Markdown and JSON format. MinerU is a comprehensive solution for precise document content extraction with support for:

- ✅ Multiple output formats (Markdown, JSON)
- ✅ OCR support for 84 languages
- ✅ Layout and span visualization
- ✅ CPU and GPU acceleration support
- ✅ Cross-platform compatibility (Windows, Linux, macOS)

**Quick Start:**
```bash
# Activate conda environment
source /opt/conda/etc/profile.d/conda.sh && conda activate pd

# Navigate to MinerU directory
cd tools/mineru

# Install MinerU and dependencies
pip install -e .[full]

# Return to project root for model download
cd ../..

# Download required model weights (first time setup)
pip install huggingface_hub
python scripts/download_models_hf.py

# Use MinerU (note: command is magic-pdf, not mineru in v1.3.10)
magic-pdf -p <input_path> -o <output_path>
```

### 🚀 GPU Acceleration Setup

For optimal performance with CUDA GPU acceleration:

**1. Verify GPU Support:**
```bash
nvidia-smi  # Check GPU availability
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
```

**2. Configure GPU Acceleration:**
The model download script automatically creates a configuration file at `~/magic-pdf.json`. To enable GPU acceleration, ensure the device mode is set to `cuda`:

```json
{
    "device-mode": "cuda",
    "models-dir": "/path/to/downloaded/models"
}
```

> **📋 Configuration Template**: See [`configs/magic-pdf-gpu.template.json`](configs/magic-pdf-gpu.template.json) for a complete configuration template with all available options.

**3. Performance Comparison:**
- **CPU Mode**: ~16-17 it/s processing speed, language switched to `ch_lite`
- **GPU Mode**: ~130+ it/s processing speed (**8x faster**), full language support

**Example Usage:**
```bash
magic-pdf -p demo/pdfs/small_ocr.pdf -o output/
```

## 📦 Getting Started

### 🚀 Complete Fresh Setup (From Scratch)

Here's the complete process to reproduce the magic-pdf setup:

**1. Clone Repository with Submodules:**
```bash
git clone --recursive https://github.com/protagolabs/ProtagoDoc.git
cd ProtagoDoc
```

**2. Set up Conda Environment:**
```bash
source /opt/conda/etc/profile.d/conda.sh && conda activate pd
# or create new environment: conda create -n pd python=3.10 && conda activate pd
```

**3. Install MinerU:**
```bash
cd tools/mineru
pip install -e .[full]
cd ../..
```

**4. Download Models and Configure GPU:**
```bash
pip install huggingface_hub
python scripts/download_models_hf.py
```

**5. Verify Setup:**
```bash
python scripts/test_fresh_setup.py
```

**6. Test Magic-PDF:**
```bash
cd tools/mineru
magic-pdf -p demo/pdfs/small_ocr.pdf -o ../../output/
```

Expected result: **~130+ it/s GPU processing speed** 🔥

### Clone with Submodules

To clone this repository with all submodules:

```bash
git clone --recursive https://github.com/protagolabs/ProtagoDoc.git
```

If you've already cloned the repository, initialize and update submodules:

```bash
git submodule init
git submodule update
```

### Adding New Tools

To add a new tool as a submodule:

```bash
git submodule add <repository-url> tools/<tool-name>
git commit -m "Add <tool-name> submodule"
```

### Updating Submodules

To update all submodules to their latest versions:

```bash
git submodule update --remote
```

To update a specific submodule:

```bash
# For MinerU (uses master branch)
cd tools/mineru
git pull origin master
cd ../..
git add tools/mineru
git commit -m "Update MinerU submodule"

# For other tools that might use main branch
cd tools/<tool-name>
git pull origin main  # or master, depending on the repository
cd ../..
git add tools/<tool-name>
git commit -m "Update <tool-name> submodule"
```

## 📁 Repository Structure

```
ProtagoDoc/
├── tools/                  # All tool submodules
│   └── mineru/            # MinerU - PDF to Markdown/JSON converter
├── scripts/               # Utility scripts
│   ├── download_models_hf.py  # Model download script (local)
│   └── test_fresh_setup.py    # Setup validation script
├── configs/               # Configuration templates
│   ├── magic-pdf-gpu.template.json  # GPU configuration template
│   └── README.md          # Configuration documentation
├── .gitmodules            # Submodule configuration
└── README.md              # This file
```

## 🔧 Troubleshooting

### Submodule Update Issues

**Error: `fatal: couldn't find remote ref main`**
- Some repositories use `master` as the default branch instead of `main`
- For MinerU: use `git pull origin master`
- Check the default branch with: `git branch -r`

**Updating from a specific version:**
```bash
# To update MinerU to a newer version tag
cd tools/mineru
git fetch origin
git checkout magic_pdf-1.3.11-released  # or desired version
cd ../..
git add tools/mineru
git commit -m "Update MinerU to version 1.3.10 (magic_pdf-1.3.11-released tag)"
```

**Reset submodule to specific commit:**
```bash
cd tools/mineru
git checkout ea619281ef43577da91247a9df60f53b12d47cbc  # current pinned commit (magic_pdf-1.3.11-released)
cd ../..
git add tools/mineru
git commit -m "Reset MinerU to pinned version 1.3.10 (magic_pdf-1.3.11-released tag)"
```

### GPU Configuration Issues

**Error: `magic-pdf: command not found`**
- Ensure you've run the model download script: `python scripts/download_models_hf.py`
- Check if MinerU is properly installed: `pip show magic-pdf`

**Error: Still using CPU despite CUDA configuration**
1. Verify the configuration file exists: `ls -la ~/magic-pdf.json`
2. Check device mode setting:
   ```bash
   python -c "from magic_pdf.libs.config_reader import get_device; print('Device:', get_device())"
   ```
3. Ensure device-mode is set to "cuda" in `~/magic-pdf.json`:
   ```json
   {
       "device-mode": "cuda"
   }
   ```

**Error: Missing model weights**
```bash
# Re-download models if they're missing
python scripts/download_models_hf.py
```

**GPU Memory Issues**
- Reduce batch size by modifying the configuration
- Check available GPU memory: `nvidia-smi`
- For GPUs with <6GB VRAM, consider using CPU mode

**Performance Optimization**
- **Expected GPU Performance**: 130+ it/s for OCR processing
- **Expected CPU Performance**: 16-17 it/s for OCR processing
- If GPU performance is poor, check CUDA installation and drivers

## 🤝 Contributing

1. Fork the repository
2. Add your tool as a submodule in the `tools/` directory
3. Update this README with tool documentation
4. Submit a pull request

## 📝 License

This repository serves as a collection hub. Each tool maintains its own license:

- **MinerU**: AGPL-3.0 License

---

*Last updated: $(date +'%Y-%m-%d')*