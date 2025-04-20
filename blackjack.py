import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("♠️♥️♣️♦️ Blackjack ♦️♣️♥️♠️")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0a5c36")

        self.initial_balance = 1000
        self.balance = self.initial_balance
        self.bet_amount = 100
        self.game_active = False

        self.card_images = {}
        self.card_back = None
        self.load_card_images()

        self.setup_welcome_screen()

    def load_card_images(self):
        img = Image.new('RGB', (120, 170), color='darkred')
        draw = ImageDraw.Draw(img)
        draw.rectangle([5, 5, 115, 165], outline='gold', width=3)
        draw.rectangle([10, 10, 110, 160], outline='gold', width=2)

        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()

        draw.text((60, 85), "CASINO", fill="gold", anchor="mm", font=font)
        self.card_back = ImageTk.PhotoImage(img)

        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

        for suit in suits:
            for rank in ranks:
                try:
                    img = Image.open(f"cards/{rank}_of_{suit}.png")
                    img = img.resize((120, 170))
                    self.card_images[f"{rank}_of_{suit}"] = ImageTk.PhotoImage(img)
                except:
                    img = Image.new('RGB', (120, 170), color='white')
                    draw = ImageDraw.Draw(img)
                    draw.rectangle([5, 5, 115, 165], outline='black')
                    draw.text((10, 10), rank.upper(), fill="black", font=font)
                    draw.text((110, 160), rank.upper(), fill="black", font=font)
                    suit_symbol = {'hearts': '♥', 'diamonds': '♦', 'clubs': '♣', 'spades': '♠'}[suit]
                    color = 'red' if suit in ['hearts', 'diamonds'] else 'black'
                    draw.text((60, 85), suit_symbol, fill=color, anchor="mm", font=font)
                    self.card_images[f"{rank}_of_{suit}"] = ImageTk.PhotoImage(img)

    def setup_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.main_frame = tk.Frame(self.root, bg="#0a5c36")
        self.main_frame.pack(fill="both", expand=True)

        title_label = tk.Label(self.main_frame, text="BLACKJACK", font=("Arial", 36, "bold"), fg="gold", bg="#0a5c36")
        title_label.pack(pady=(50, 20))

        balance_frame = tk.Frame(self.main_frame, bg="#0a5c36")
        balance_frame.pack(pady=(0, 20))

        tk.Label(balance_frame, text="BALANCE:", font=("Arial", 14), fg="white", bg="#0a5c36").pack(side=tk.LEFT)

        self.balance_label = tk.Label(balance_frame, text=f" ${self.balance:,}", font=("Arial", 16, "bold"), fg="gold",
                                      bg="#0a5c36")
        self.balance_label.pack(side=tk.LEFT)

        reset_btn = tk.Button(balance_frame, text="↻", font=("Arial", 8), fg="white", bg="#e74c3c", bd=0,
                              command=self.reset_balance)
        reset_btn.pack(side=tk.LEFT, padx=5)

        bet_frame = tk.Frame(self.main_frame, bg="#0a5c36")
        bet_frame.pack(pady=(0, 30))

        tk.Label(bet_frame, text="BET:", font=("Arial", 14), fg="white", bg="#0a5c36").pack(side=tk.LEFT)

        self.bet_slider = tk.Scale(bet_frame, from_=10, to=min(500, self.balance),
                                   orient=tk.HORIZONTAL, length=300,
                                   troughcolor="#1e8449", activebackground="#d4af37",
                                   highlightthickness=0, bd=0, sliderlength=30,
                                   command=self.update_bet)
        self.bet_slider.config(bg="#0a5c36", fg="white", font=("Arial", 12),
                               highlightbackground="#0a5c36")
        self.bet_slider.set(self.bet_amount)
        self.bet_slider.pack(side=tk.LEFT, padx=10)

        self.bet_label = tk.Label(bet_frame, text=f"${self.bet_amount}",
                                  font=("Arial", 14, "bold"), fg="gold", bg="#0a5c36")
        self.bet_label.pack(side=tk.LEFT, padx=10)

        button_frame = tk.Frame(self.main_frame, bg="#0a5c36")
        button_frame.pack(pady=(0, 40))

        play_button = tk.Button(button_frame, text="PLAY", font=("Arial", 16), width=15, height=2,
                                bg="#d4af37", fg="black", bd=0, highlightthickness=0,
                                activebackground="#f1c40f", command=self.start_game)
        play_button.pack(side=tk.LEFT, padx=15)

        rules_button = tk.Button(button_frame, text="RULES", font=("Arial", 16), width=15, height=2,
                                 bg="#3498db", fg="white", bd=0, highlightthickness=0,
                                 activebackground="#5dade2", command=self.show_rules)
        rules_button.pack(side=tk.LEFT, padx=15)

        quit_button = tk.Button(button_frame, text="QUIT", font=("Arial", 16), width=15, height=2,
                                bg="#e74c3c", fg="white", bd=0, highlightthickness=0,
                                activebackground="#ec7063", command=self.root.quit)
        quit_button.pack(side=tk.LEFT, padx=15)

    def reset_balance(self):
        self.balance = self.initial_balance
        self.balance_label.config(text=f" ${self.balance:,}")
        self.bet_slider.config(to=min(500, self.balance))
        messagebox.showinfo("Balance Reset", f"Balance reset to ${self.initial_balance:,}")

    def update_bet(self, value):
        self.bet_amount = int(float(value))
        self.bet_label.config(text=f"${self.bet_amount}")

    def show_rules(self):
        rules = """
        BLACKJACK RULES:

        Goal: Get closer to 21 than dealer
        Cards 2-10 = face value
        J, Q, K = 10
        A = 1 or 11

        ACTIONS:
        HIT = take card
        STAND = keep hand
        DOUBLE = double bet

        Blackjack pays 3:2
        """
        messagebox.showinfo("Rules", rules)

    def start_game(self):
        if self.bet_amount > self.balance:
            messagebox.showerror("Error", "Not enough funds!")
            return
        if hasattr(self, 'stand_clicked'):
            del self.stand_clicked

        self.balance -= self.bet_amount
        self.update_balance()

        for widget in self.root.winfo_children():
            widget.destroy()

        self.game_frame = tk.Frame(self.root, bg="#0a5c36")
        self.game_frame.pack(fill="both", expand=True)

        self.game_active = True
        self.user_cards = []
        self.dealer_cards = []
        self.deck = self.create_deck()
        random.shuffle(self.deck)

        self.setup_game_ui()
        self.deal_initial_cards()

    def setup_game_ui(self):
        dealer_frame = tk.Frame(self.game_frame, bg="#0a5c36")
        dealer_frame.pack(fill=tk.X, pady=(20, 10))

        tk.Label(dealer_frame, text="DEALER", font=("Arial", 16), fg="white", bg="#0a5c36").pack()

        self.dealer_card_frame = tk.Frame(dealer_frame, bg="#0a5c36")
        self.dealer_card_frame.pack()

        tk.Frame(self.game_frame, bg="gold", height=2).pack(fill=tk.X, pady=10)

        player_frame = tk.Frame(self.game_frame, bg="#0a5c36")
        player_frame.pack(fill=tk.X, pady=(20, 10))

        tk.Label(player_frame, text="PLAYER", font=("Arial", 16), fg="white", bg="#0a5c36").pack()

        self.player_card_frame = tk.Frame(player_frame, bg="#0a5c36")
        self.player_card_frame.pack()

        score_frame = tk.Frame(self.game_frame, bg="#0a5c36")
        score_frame.pack(fill=tk.X, pady=20)

        self.dealer_score_label = tk.Label(score_frame, text="Dealer: ?", font=("Arial", 14), fg="white", bg="#0a5c36")
        self.dealer_score_label.pack(side=tk.LEFT, padx=40)

        self.player_score_label = tk.Label(score_frame, text="Player: 0", font=("Arial", 14), fg="white", bg="#0a5c36")
        self.player_score_label.pack(side=tk.RIGHT, padx=40)

        button_frame = tk.Frame(self.game_frame, bg="#0a5c36")
        button_frame.pack(pady=20)

        self.hit_button = tk.Button(button_frame, text="HIT", font=("Arial", 14), width=10, height=2, bg="#3498db",
                                    fg="white", command=self.hit)
        self.hit_button.pack(side=tk.LEFT, padx=15)

        self.stand_button = tk.Button(button_frame, text="STAND", font=("Arial", 14), width=10, height=2, bg="#e74c3c",
                                      fg="white", command=self.stand)
        self.stand_button.pack(side=tk.LEFT, padx=15)

        self.double_button = tk.Button(button_frame, text="DOUBLE", font=("Arial", 14), width=10, height=2,
                                       bg="#d4af37", fg="black", command=self.double_down)
        self.double_button.pack(side=tk.LEFT, padx=15)

        if self.balance < self.bet_amount:
            self.double_button.config(state=tk.DISABLED)

        info_frame = tk.Frame(self.game_frame, bg="#0a5c36")
        info_frame.pack(fill=tk.X, pady=10)

        self.balance_info = tk.Label(info_frame, text=f"Balance: ${self.balance:,} | Bet: ${self.bet_amount:,}",
                                     font=("Arial", 12), fg="gold", bg="#0a5c36")
        self.balance_info.pack()

    def update_balance(self):
        if hasattr(self, 'balance_label') and self.balance_label.winfo_exists():
            self.balance_label.config(text=f" ${self.balance:,}")
        if hasattr(self, 'balance_info') and self.balance_info.winfo_exists():
            self.balance_info.config(text=f"Balance: ${self.balance:,} | Bet: ${self.bet_amount:,}")

    def deal_initial_cards(self):
        # Deal first card to player
        self.user_cards.append(self.deal_card())
        card_img = self.card_images.get(self.user_cards[-1])
        tk.Label(self.player_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        # Deal first card to dealer (face down)
        self.dealer_cards.append(self.deal_card())
        tk.Label(self.dealer_card_frame, image=self.card_back, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        # Deal second card to player
        self.user_cards.append(self.deal_card())
        card_img = self.card_images.get(self.user_cards[-1])
        tk.Label(self.player_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        # Deal second card to dealer (face up)
        self.dealer_cards.append(self.deal_card())
        card_img = self.card_images.get(self.dealer_cards[-1])
        tk.Label(self.dealer_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        self.update_game_display()

        if self.calculate_score(self.user_cards) == 21:
            self.handle_blackjack()

    def update_game_display(self):
        for widget in self.dealer_card_frame.winfo_children():
            widget.destroy()
        for widget in self.player_card_frame.winfo_children():
            widget.destroy()

        for i, card in enumerate(self.dealer_cards):
            if i == 0 and not hasattr(self, 'stand_clicked'):
                tk.Label(self.dealer_card_frame, image=self.card_back, bg="#0a5c36").pack(side=tk.LEFT, padx=5)
            else:
                card_img = self.card_images.get(card)
                if card_img:
                    tk.Label(self.dealer_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)
                else:
                    tk.Label(self.dealer_card_frame, text=card.split('_')[0], font=("Arial", 12), width=5, height=2,
                             bg="white").pack(side=tk.LEFT, padx=5)

        for card in self.user_cards:
            card_img = self.card_images.get(card)
            if card_img:
                tk.Label(self.player_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)
            else:
                tk.Label(self.player_card_frame, text=card.split('_')[0], font=("Arial", 12), width=5, height=2,
                         bg="white").pack(side=tk.LEFT, padx=5)

        player_score = self.calculate_score(self.user_cards)
        dealer_score = self.calculate_score(self.dealer_cards) if hasattr(self, 'stand_clicked') else "?"

        self.player_score_label.config(text=f"Player: {player_score}")
        self.dealer_score_label.config(text=f"Dealer: {dealer_score}")

        if player_score > 21:
            self.handle_bust()

    def calculate_score(self, cards):
        score = 0
        aces = 0

        for card in cards:
            rank = card.split('_')[0]
            if rank in ['jack', 'queen', 'king']:
                score += 10
            elif rank == 'ace':
                score += 11
                aces += 1
            else:
                score += int(rank)

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def hit(self):
        if not self.game_active:
            return

        self.user_cards.append(self.deal_card())
        card_img = self.card_images.get(self.user_cards[-1])
        tk.Label(self.player_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        self.update_game_display()

        if self.calculate_score(self.user_cards) > 21:
            self.handle_bust()
        elif self.calculate_score(self.user_cards) == 21:
            self.stand()

    def stand(self):
        if not self.game_active:
            return

        self.stand_clicked = True
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.double_button.config(state=tk.DISABLED)

        # Flip dealer's hidden card
        if len(self.dealer_card_frame.winfo_children()) > 0:
            hidden_card = self.dealer_card_frame.winfo_children()[0]
            card_img = self.card_images.get(self.dealer_cards[0])
            hidden_card.config(image=card_img)

        self.update_game_display()
        self.dealer_play()

    def dealer_play(self):
        dealer_score = self.calculate_score(self.dealer_cards)
        player_score = self.calculate_score(self.user_cards)

        if dealer_score >= 17 or player_score > 21:
            self.determine_winner()
            return

        self.dealer_cards.append(self.deal_card())
        card_img = self.card_images.get(self.dealer_cards[-1])
        tk.Label(self.dealer_card_frame, image=card_img, bg="#0a5c36").pack(side=tk.LEFT, padx=5)

        self.update_game_display()
        self.root.after(1000, self.dealer_play)

    def double_down(self):
        if self.balance >= self.bet_amount and len(self.user_cards) == 2:
            self.balance -= self.bet_amount
            self.bet_amount *= 2
            self.update_balance()

            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)
            self.double_button.config(state=tk.DISABLED)

            self.user_cards.append(self.deal_card())
            self.update_game_display()

            if self.calculate_score(self.user_cards) > 21:
                self.handle_bust()
            else:
                self.stand()

    def handle_bust(self):
        self.game_active = False
        self.show_result("You busted! Dealer wins.")

    def handle_blackjack(self):
        dealer_score = self.calculate_score(self.dealer_cards)

        if dealer_score == 21:
            self.balance += self.bet_amount
            self.show_result("Both have blackjack! Push.")
        else:
            self.balance += int(self.bet_amount * 2.5)
            self.show_result("Blackjack! You win 3:2!")

    def determine_winner(self):
        player_score = self.calculate_score(self.user_cards)
        dealer_score = self.calculate_score(self.dealer_cards)

        self.game_active = False

        if dealer_score > 21:
            self.balance += self.bet_amount * 2
            self.show_result("Dealer busted! You win!")
        elif player_score > dealer_score:
            self.balance += self.bet_amount * 2
            self.show_result("You win!")
        elif player_score == dealer_score:
            self.balance += self.bet_amount
            self.show_result("It's a tie!")
        else:
            self.show_result("Dealer wins!")

    def show_result(self, message=None):
        self.update_balance()

        result_frame = tk.Frame(self.game_frame, bg="#0a5c36", bd=2, relief=tk.RAISED)
        result_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=200)

        if message:
            result_label = tk.Label(result_frame, text=message, font=("Arial", 14, "bold"),
                                    fg="gold", bg="#0a5c36", wraplength=380)
            result_label.pack(pady=(10, 20))

        button_frame = tk.Frame(result_frame, bg="#0a5c36")
        button_frame.pack(pady=(0, 10))

        tk.Button(button_frame, text="PLAY AGAIN", font=("Arial", 12), bg="#d4af37", fg="black",
                  command=self.start_game).pack(side=tk.LEFT, padx=20, pady=10)
        tk.Button(button_frame, text="MAIN MENU", font=("Arial", 12), bg="#3498db", fg="white",
                  command=self.setup_welcome_screen).pack(side=tk.LEFT, padx=20, pady=10)

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        return [f"{rank}_of_{suit}" for suit in suits for rank in ranks]

    def deal_card(self):
        return self.deck.pop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()