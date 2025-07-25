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
cd tools/mineru
pip install -e .[core]
mineru -p <input_path> -o <output_path>
```

## 📦 Getting Started

### Clone with Submodules

To clone this repository with all submodules:

```bash
git clone --recursive https://github.com/your-username/ProtagoDoc.git
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
cd tools/<tool-name>
git pull origin main
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