📧 MBOX Splitter
Show Image
Show Image
A Python utility for splitting large MBOX files into smaller chunks of specified size.
🚀 Features

📁 Split MBOX files into smaller chunks based on size in MB
✨ Maintains email integrity (doesn't split individual messages)
📊 Progress reporting for each chunk created
💻 Simple command-line interface

📋 Requirements

Python 3.x
Standard Python libraries (no additional dependencies)

🔧 Installation
bashCopygit clone https://github.com/YOUR-USERNAME/mbox-splitter.git
cd mbox-splitter
📖 Usage
bashCopypython mbox-splitter.py filename size
Arguments
ParameterDescriptionfilenamePath to the MBOX file to splitsizeDesired chunk size in megabytes (MB)
Example
bashCopypython mbox-splitter.py inbox.mbox 50
This will create multiple files:

inbox_1.mbox
inbox_2.mbox
etc.

Each file will be approximately 50MB in size.
📄 License
MIT License
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
⭐ Show Your Support
Give a ⭐️ if this project helped you!
