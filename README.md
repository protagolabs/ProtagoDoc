# ProtagoDoc

A curated collection of useful tools organized as git submodules for easy management and deployment.

## 🛠️ Tools Collection

This repository serves as a centralized hub for various development and productivity tools, each maintained as a git submodule for easy version control and updates.

### Document Processing

#### [MinerU](https://github.com/opendatalab/MinerU)
**Location:** `tools/mineru` | **Version:** 1.3.10

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
pip install opencv-python openai ultralytics doclayout_yolo rapid_table ftfy

# Use MinerU (note: command is magic-pdf, not mineru in v1.3.10)
magic-pdf -p <input_path> -o <output_path>
```

**Example Usage:**
```bash
magic-pdf -p demo/pdfs/small_ocr.pdf -o output/
```

## 📦 Getting Started

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
git commit -m "Update MinerU to version 1.3.11"
```

**Reset submodule to specific commit:**
```bash
cd tools/mineru
git checkout 88026879343d7712f9f1729df6c110e3ee5d4333  # current pinned commit
cd ../..
git add tools/mineru
git commit -m "Reset MinerU to pinned version 1.3.10"
```

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