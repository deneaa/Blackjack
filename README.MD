
# BLACKJACK

*Experience the thrill of winning with every hand!*

![last-commit](https://img.shields.io/github/last-commit/deneaa/Blackjack?style=flat&logo=git&logoColor=white&color=0080ff)
![repo-top-language](https://img.shields.io/github/languages/top/deneaa/Blackjack?style=flat&color=0080ff)
![repo-language-count](https://img.shields.io/github/languages/count/deneaa/Blackjack?style=flat&color=0080ff)

*Built with the tools and technologies:*

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB.svg?style=flat&logo=Tkinter&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3776AB.svg?style=flat&logo=Pillow&logoColor=white)

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
- [Features](#features)
- [Game Rules](#game-rules)
- [Screenshots](#screenshots)

---

## Overview

Blackjack is a dynamic graphical card game application that brings the classic casino experience to your desktop, built using Python's Tkinter library.

**Why Blackjack?**

This project provides an engaging platform for users to enjoy the classic card game while showcasing essential game development principles. The core features include:

- 🎨 **User Interface:** Engaging and visually appealing, enhancing user experience
- 💼 **Game Management:** Efficient tracking of player balance and game state
- 🃏 **Visual Elements:** Custom card images and themed backgrounds
- 🎲 **Interactive Gameplay:** Place bets and play against a dealer
- ⚙️ **Easy Setup:** Built with Python's Tkinter

---

## Getting Started

### Prerequisites

This project requires:
- Python 3.6+
- Pillow library (`pip install pillow`)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/Blackjack.git
```

2. **Navigate to the project directory:**
```bash
cd Blackjack
```

### Usage

Run the game with:
```bash
python blackjack.py
```

### Testing

The game includes basic functionality tests:
```bash
python -m unittest test_blackjack.py
```

---

## Features

- ♠️♥️♣️♦️ Authentic card graphics and animations
- 💰 Adjustable betting system with slider control
- 🎯 Dealer follows standard casino rules (stands on 17)
- 💵 Balance tracking with win/loss statistics
- 🔄 Double down option available

---

## Game Rules

1. **Objective:** Beat the dealer without exceeding 21 points
2. **Card Values:**
   - 2-10 = face value
   - J, Q, K = 10
   - Ace = 1 or 11
3. **Blackjack:** Ace + 10-value card (pays 3:2)
4. **Dealer Rules:** Must hit until 17 or higher
5. **Player Options:**
   - Hit: Take another card
   - Stand: Keep current hand
   - Double: Double your bet (available on first move)

---

⬆ [Return to Top](#blackjack)
