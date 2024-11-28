# 🚀 Instagram Tool

<div align="center">

![Instagram Tool Banner](https://raw.githubusercontent.com/MyTheeNa/instagram-tool/main/.github/banner.png)

[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MyTheeNa/instagram-tool?style=social)](https://github.com/MyTheeNa/instagram-tool/stargazers)

*A powerful and elegant Instagram tool for story downloading and follower analysis*

</div>

## ✨ Features

- 📥 **Story Loader**
  - Download user stories
  - Save highlights
  - Archive posts
  - Configurable download options

- 👥 **Following Checker**
  - Find users not following you back
  - Export results to file
  - Detailed analytics

- 🎨 **Beautiful UI**
  - Modern command-line interface
  - Colorful animations
  - Progress indicators
  - User-friendly design

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/MyTheeNa/instagram-tool.git
cd instagram-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your credentials:
```bash
# Edit config.json with your Instagram credentials
{
    "username": "your_instagram_username",
    "password": "your_instagram_password"
}
```

## 🚀 Usage

Run the tool:
```bash
python app.py
```

### Story Loader
- Select option [1] from the menu
- Enter target username
- Choose download options:
  - Stories
  - Highlights
  - Posts

### Following Checker
- Select option [2] from the menu
- Enter target username
- Wait for analysis to complete
- Results will be saved in `log/checkfollowing/`

## 📸 Screenshots

<div align="center">

![Main Menu](https://raw.githubusercontent.com/MyTheeNa/instagram-tool/main/.github/menu.png)

*Main Menu*

![Story Loader](https://raw.githubusercontent.com/MyTheeNa/instagram-tool/main/.github/story.png)

*Story Loader in Action*

</div>

## ⚙️ Configuration

The tool uses `config.json` for credentials:
```json
{
    "username": "your_instagram_username",
    "password": "your_instagram_password"
}
```

## 🔒 Security

- Credentials are stored locally
- Session management for faster login
- Secure error handling
- Rate limiting protection

## 📝 Requirements

- Python 3.10+
- Required packages:
  - instaloader
  - colorama
  - raducord

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Instaloader](https://instaloader.github.io/) for the core functionality
- [Colorama](https://pypi.org/project/colorama/) for the beautiful colors
- Community contributors and testers

## 📞 Contact

MyTheeNa - [@MyTheeNa](https://github.com/MyTheeNa)

Project Link: [https://github.com/MyTheeNa/instagram-tool](https://github.com/MyTheeNa/instagram-tool)

---
<div align="center">
Made with ❤️ by MyTheeNa
</div>
