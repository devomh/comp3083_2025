# Prerequisites, Setup, and Introduction

## Prerequisites

Before starting this lab, ensure you have:

- **Completion of Lab 02** - Understanding of basic Python syntax and the input-compute-output paradigm
- **Familiarity with Jupyter notebooks** from Lab 02 exercises
- **Basic computer literacy** and web browser navigation skills
- **Internet connection** for software downloads and API access

## Required Software Installation

### Overview
In this lab, we'll install and configure a professional Python development environment. Unlike Lab 02 where we primarily used Google Colab, today we'll set up tools that professional developers use daily.

**What we'll install:**
- GitHub account (version control and collaboration)
- Miniconda (Python distribution and package manager)  
- Visual Studio Code (professional code editor)
- Git (version control system)

---

## 1. GitHub Account Setup

### Why GitHub?
- **Industry Standard:** Used by millions of developers worldwide
- **Portfolio Building:** Showcase your projects to potential employers
- **Collaboration:** Work on team projects and contribute to open source
- **Integration:** Seamlessly works with VS Code and other development tools

### Step-by-Step Setup

1. **Navigate to GitHub**
   - Go to [github.com](https://github.com)
   - Click "Sign up" in the top right corner

2. **Create Your Account**
   - **Username:** Choose carefully - this becomes your professional identity
     - Examples: `john-smith`, `jsmith-dev`, `johnsmith2025`
     - Avoid: `coolguy123`, `xxdragonslayerxx`, `tempaccount`
   - **Email:** Use a professional email address you check regularly
   - **Password:** Create a strong, unique password

3. **Verify Your Account**
   - Check your email and click the verification link
   - Complete any additional verification steps

4. **Profile Setup**
   - Add a professional profile photo (optional but recommended)
   - Add a brief bio mentioning you're a computer science student
   - Set your location (city/country)

### GitHub Best Practices
- **Professional Username:** This will appear on your resume and projects
- **Public Profile:** Keep it clean and professional
- **Repository Names:** Use clear, descriptive names
- **README Files:** Always include documentation for your projects

---

## 2. Miniconda Installation

### What is Miniconda?
- **Lightweight Python Distribution:** Includes Python + essential packages
- **Package Manager:** Install and manage Python libraries easily
- **Virtual Environments:** Keep projects isolated and organized
- **Cross-Platform:** Works on Windows, Mac, and Linux

### Installation Steps

#### Windows Users

1. **Download Miniconda**
   - Visit [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   - Click "Miniconda3 Windows 64-bit" (most common)
   - Save the `.exe` file to your Downloads folder

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - Click "Next" through the welcome screens
   - **Important:** Check "Add Miniconda3 to my PATH environment variable"
   - Complete the installation with default settings

3. **Verify Installation**
   - Open Command Prompt or PowerShell
   - Type: `conda --version`
   - You should see something like: `conda 23.7.4`

#### Mac Users

1. **Download Miniconda**
   - Visit [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   - Choose "Miniconda3 macOS Apple M1 64-bit" (M1/M2 Macs) or "Miniconda3 macOS Intel x86 64-bit" (Intel Macs)
   - Download the `.pkg` file

2. **Install Miniconda**
   - Double-click the downloaded `.pkg` file
   - Follow the installation wizard with default settings
   - Enter your password when prompted

3. **Verify Installation**
   - Open Terminal (Applications > Utilities > Terminal)
   - Type: `conda --version`
   - You should see the conda version number

#### Linux Users

1. **Download Miniconda**
   - Visit [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   - Download "Miniconda3 Linux 64-bit"

2. **Install via Terminal**
   ```bash
   bash ~/Downloads/Miniconda3-latest-Linux-x86_64.sh
   ```
   - Press Enter to read the license
   - Type "yes" to accept the license
   - Press Enter to confirm the installation location
   - Type "yes" to initialize conda

3. **Reload Terminal**
   ```bash
   source ~/.bashrc
   ```

4. **Verify Installation**
   ```bash
   conda --version
   ```

### Troubleshooting Miniconda
- **"conda not recognized":** Restart your terminal/command prompt
- **PATH issues:** Re-run installer and ensure PATH option is checked
- **Permission errors:** Run terminal as administrator (Windows) or use `sudo` (Mac/Linux)

---

## 3. Visual Studio Code Installation

### What is VS Code?
- **Free, Professional IDE:** Used by millions of developers
- **Extensible:** Thousands of extensions for every programming language
- **Integrated Terminal:** Run commands without leaving the editor
- **Git Integration:** Built-in version control features
- **IntelliSense:** Smart code completion and error detection

### Installation Steps

#### All Platforms

1. **Download VS Code**
   - Visit [code.visualstudio.com](https://code.visualstudio.com)
   - Click the download button for your operating system
   - The website automatically detects your OS

2. **Install VS Code**
   - **Windows:** Run the downloaded `.exe` file, follow the wizard
   - **Mac:** Open the downloaded `.zip`, drag VS Code to Applications folder
   - **Linux:** Install the `.deb` or `.rpm` package, or use snap: `sudo snap install code --classic`

3. **First Launch**
   - Open VS Code
   - Take the optional welcome tour
   - Explore the interface briefly

4. **Essential Settings**
   - **Theme:** Choose File > Preferences > Color Theme (try "Dark+ (default dark)")
   - **Font Size:** File > Preferences > Settings, search "font size"
   - **Auto-save:** File > Auto Save (enable this)

### VS Code Interface Overview
- **Explorer:** File and folder navigation (left sidebar)
- **Search:** Find and replace across files
- **Source Control:** Git integration
- **Extensions:** Install additional functionality
- **Terminal:** Built-in command line (View > Terminal)

---

## 4. Git Configuration

### What is Git?
- **Version Control System:** Track changes in your code over time
- **Collaboration Tool:** Work with others on the same codebase  
- **Backup System:** Never lose your work again
- **Professional Standard:** Essential skill for any developer

### Basic Git Setup

1. **Open Terminal/Command Prompt**
   - Windows: Command Prompt, PowerShell, or VS Code terminal
   - Mac/Linux: Terminal application

2. **Configure Your Identity**
   ```bash
   git config --global user.name "Your Full Name"
   git config --global user.email "your.email@example.com"
   ```
   - Use the same email as your GitHub account
   - Use quotes around your name if it contains spaces

3. **Verify Configuration**
   ```bash
   git config --global --list
   ```
   - You should see your name and email listed

4. **Optional: Set Default Editor**
   ```bash
   git config --global core.editor "code --wait"
   ```
   - This makes VS Code your default Git editor

### Git Best Practices
- **Commit Often:** Save your progress frequently
- **Meaningful Messages:** Write clear commit descriptions
- **Branching:** Create branches for new features
- **Pull Before Push:** Always sync with remote changes first

---

## Lab Context and Objectives

### Connection to Previous Labs

**From Lab 01:**
- We learned about AI tools and their impact on software development
- We explored professional workflows vs. "vibe coding"
- We discovered the importance of structured approaches

**From Lab 02:**
- We mastered the input-compute-output programming paradigm
- We practiced basic Python syntax and debugging
- We worked with Jupyter notebooks in Google Colab

**Today's Bridge:**
- We'll apply Lab 02's programming concepts in a professional IDE
- We'll extend input-compute-output to input-API-compute-output
- We'll implement Lab 01's professional workflows in practice

### Today's Learning Objectives

By the end of this lab, you will be able to:

1. **Professional Environment Setup**
   - Configure VS Code for Python development
   - Create and manage virtual environments
   - Organize projects with professional structure

2. **Library Integration**
   - Import and use Python libraries
   - Write reusable functions with proper documentation
   - Apply modular programming principles

3. **API Integration**
   - Understand APIs and HTTP requests
   - Build a complete weather application
   - Handle errors and edge cases gracefully

4. **Professional Practices**
   - Use version control (Git) for project management
   - Debug code effectively with IDE tools
   - Write clean, documented, maintainable code

### Session Overview

**Today's Journey:**
1. **Setup Complete:** Transform your computer into a professional development workstation
2. **IDE Mastery:** Learn VS Code features that boost productivity
3. **Real-World Project:** Build a weather app that connects to live data
4. **Professional Skills:** Apply industry-standard practices and workflows

### Success Criteria

You'll know you're successful when:
- ✅ All software is installed and configured correctly
- ✅ You can create and activate Python virtual environments
- ✅ Your weather app successfully retrieves and displays real weather data
- ✅ Your project is properly organized and documented
- ✅ Your code is committed to a Git repository

### Getting Help

**During Installation:**
- Ask instructors for immediate assistance
- Work with classmates - collaboration is encouraged
- Reference the troubleshooting section in each installation guide

**During Coding:**
- Test small pieces of code frequently
- Read error messages carefully - they contain important clues
- Use VS Code's built-in debugging tools
- Don't hesitate to ask for help - learning is collaborative

### Ready to Begin?

Once you've completed all the software installations and configurations above, you're ready to dive into professional Python development. The next section will guide you through mastering VS Code as your primary development environment.

**Verification Checklist:**
- [ ] GitHub account created and verified
- [ ] Miniconda installed and `conda --version` works
- [ ] VS Code installed and launches successfully
- [ ] Git configured with your name and email
- [ ] All software running without errors

**Time Investment:** This setup takes 20-30 minutes but creates the foundation for your entire programming career. Every professional developer uses these exact same tools.

---

**Next:** [Professional IDE Setup](02_IDE.md) - Master VS Code and create your first organized Python project.