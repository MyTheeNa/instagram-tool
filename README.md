# 🚀 Instagram Tool

<div align="center">

![Instagram Tool Banner](https://raw.githubusercontent.com/MyTheeNa/instagram-tool/main/.github/banner.png)

[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MyTheeNa/instagram-tool?style=social)](https://github.com/MyTheeNa/instagram-tool/stargazers)

*A powerful and elegant Instagram tool for story downloading and follower analysis*

</div>

## 🌟 Overview
A powerful command-line tool for Instagram data retrieval and analysis. Download stories, highlights, posts, and analyze follower relationships with ease.

## ✨ Features

- 📥 **Story Loader**
  - Download user stories
  - Save highlights
  - Archive posts
  - Configurable download options
  - Batch processing support

- 👥 **Following Checker**
  - Find users not following you back
  - Export results to file
  - Detailed analytics
  - Automated reporting

- 🎨 **Beautiful UI**
  - Modern command-line interface
  - Colorful animations
  - Progress indicators
  - User-friendly design

## 🛠️ Technical Details

### Core Components
- Written in Python 3.10+
- Powered by Instaloader
- Terminal UI with Colorama
- Advanced logging with Raducord
- Parallel processing capabilities

### Security Features
- Secure credential storage
- Session persistence
- Rate limit handling
- Error recovery system

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Instagram account
- Internet connection

### Installation
```bash
# Clone the repository
git clone https://github.com/MyTheeNa/instagram-tool.git
cd instagram-tool

# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp config.example.json config.json
# Edit config.json with your credentials
```

### Configuration
Edit `config.json`:
```json
{
    "username": "your_instagram_username",
    "password": "your_instagram_password"
}
```

## 💻 Usage

### Basic Commands
```bash
# Start the tool
python app.py

# Download stories
Select option [1] from the menu

# Check followers
Select option [2] from the menu
```

## ⚙️ Advanced Features

### Story Download Options
- Select specific users
- Choose date ranges
- Filter by content type
- Custom save locations

### Following Analysis Features
- Export to CSV
- Detailed statistics
- Custom filters
- Batch processing

## 🔧 Troubleshooting

### Common Issues
1. Authentication errors
   - Verify credentials
   - Check network connection
   - Clear session cache

2. Rate limiting
   - Use delay settings
   - Implement batch processing
   - Follow Instagram limits

## 📋 Best Practices

### Usage Guidelines
- Respect Instagram's terms of service
- Use reasonable download intervals
- Monitor rate limits
- Keep credentials secure

### Performance Tips
- Use batch processing for large downloads
- Enable caching when appropriate
- Monitor system resources

## 🤝 Contributing
Contributions are welcome! Please feel free to submit pull requests.

### Development Setup
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create pull request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✉️ Contact
MyTheeNa - [@MyTheeNa](https://github.com/MyTheeNa)

Project Link: [https://github.com/MyTheeNa/instagram-tool](https://github.com/MyTheeNa/instagram-tool)

## 🔐 Security
- Never share your credentials
- Use secure connection
- Keep software updated
- Report security issues

## 🔄 Updates
Check repository regularly for:
- Security updates
- New features
- Bug fixes
- Performance improvements

---
<div align="center">
Made with ❤️ by MyTheeNa
</div>
