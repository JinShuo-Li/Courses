import tkinter as tk
from tkinter import messagebox
import chess
import torch
import numpy as np
import glob
import os
from model import ChessNet

class PromotionDialog(tk.Toplevel):
    """
    Modal dialog for selecting promotion piece.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Promote to")
        self.geometry("300x100")
        self.selected_piece = chess.QUEEN # Default fallback
        
        # Promotion options: Queen, Rook, Bishop, Knight
        options = [
            (chess.QUEEN, '♕'), 
            (chess.ROOK, '♖'), 
            (chess.BISHOP, '♗'), 
            (chess.KNIGHT, '♘')
        ]
        
        # Create buttons
        for idx, (piece_type, symbol) in enumerate(options):
            btn = tk.Button(self, text=symbol, font=("Arial", 24),
                            command=lambda p=piece_type: self.select(p))
            btn.grid(row=0, column=idx, padx=10, pady=10)
            
        # Modal behavior: wait until window is closed
        self.transient(parent)
        self.grab_set() 
        parent.wait_window(self) 

    def select(self, piece_type):
        self.selected_piece = piece_type
        self.destroy()

class ChessAI:
    # ... (Same as before: __init__, load_latest_checkpoint, board_to_tensor) ...
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = ChessNet().to(self.device)
        self.load_latest_checkpoint()
        self.model.eval()

    def load_latest_checkpoint(self):
        list_of_files = glob.glob('*.pth') 
        if not list_of_files:
            print("No .pth files found. Using random weights.")
            return
        latest_file = max(list_of_files, key=os.path.getctime)
        print(f"Loading latest model: {latest_file}")
        self.model.load_state_dict(torch.load(latest_file, map_location=self.device))

    def board_to_tensor(self, board):
        layers = np.zeros((12, 8, 8), dtype=np.float32)
        piece_map = {
            chess.PAWN: 0, chess.KNIGHT: 1, chess.BISHOP: 2,
            chess.ROOK: 3, chess.QUEEN: 4, chess.KING: 5
        }
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                layer_idx = piece_map[piece.piece_type]
                if piece.color == chess.BLACK:
                    layer_idx += 6
                row, col = divmod(square, 8)
                layers[layer_idx, 7-row, col] = 1.0
        return torch.from_numpy(layers).unsqueeze(0).to(self.device)

    def get_best_move(self, board):
        # ... (Same as before) ...
        best_move = None
        best_value = -float('inf')
        legal_moves = list(board.legal_moves)
        if not legal_moves: return None

        for move in legal_moves:
            board.push(move)
            tensor = self.board_to_tensor(board)
            with torch.no_grad():
                value = -self.model(tensor).item()
            if value > best_value:
                best_value = value
                best_move = move
            board.pop()
        return best_move

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deep Learning Chess")
        self.board = chess.Board()
        self.ai = ChessAI()
        self.buttons = {}
        self.selected_square = None
        
        self.piece_unicode = {
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
        }
        self.draw_board()

    def draw_board(self):
        # ... (Same as before) ...
        for r in range(8):
            for c in range(8):
                square_idx = chess.square(c, 7-r)
                piece = self.board.piece_at(square_idx)
                text = self.piece_unicode.get(piece.symbol(), "") if piece else ""
                color = "#DDB88C" if (r + c) % 2 == 0 else "#A66D4F"
                btn = tk.Button(self.root, text=text, font=("Arial", 24), 
                                bg=color, height=2, width=4,
                                command=lambda s=square_idx: self.on_click(s))
                btn.grid(row=r, column=c)
                self.buttons[square_idx] = btn

    def update_board(self):
        # ... (Same as before) ...
        for square_idx, btn in self.buttons.items():
            piece = self.board.piece_at(square_idx)
            btn.config(text=self.piece_unicode.get(piece.symbol(), "") if piece else "")

    def on_click(self, square):
        """Modified click handler to support graphical promotion selection."""
        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE: 
                self.selected_square = square
                self.buttons[square].config(bg="#90EE90") # Light green for selection
        else:
            # Check for promotion condition: Pawn moving to last rank
            piece = self.board.piece_at(self.selected_square)
            is_pawn = piece.piece_type == chess.PAWN
            is_last_rank = chess.square_rank(square) == 7
            
            promotion_type = None
            if is_pawn and is_last_rank:
                # 1. Create temporary move to check legality (defaulting to Queen)
                temp_move = chess.Move(self.selected_square, square, promotion=chess.QUEEN)
                if temp_move in self.board.legal_moves:
                    # 2. Open graphical dialog to let user choose
                    dialog = PromotionDialog(self.root)
                    promotion_type = dialog.selected_piece # Code pauses here until dialog closes
                else:
                    # Invalid move logic handles the rest
                    pass

            # Create the final move object
            move = chess.Move(self.selected_square, square, promotion=promotion_type)

            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board()
                self.reset_colors()
                self.selected_square = None
                self.root.update() # Force UI refresh
                
                if not self.board.is_game_over():
                    self.root.after(100, self.ai_move) # Small delay for better UX
            else:
                self.reset_colors()
                self.selected_square = None

    def ai_move(self):
        # ... (Same as before) ...
        self.root.config(cursor="watch")
        move = self.ai.get_best_move(self.board)
        if move:
            self.board.push(move)
            self.update_board()
        self.root.config(cursor="")
        if self.board.is_game_over():
             messagebox.showinfo("Game Over", f"Result: {self.board.result()}")

    def reset_colors(self):
        # ... (Same as before) ...
        for r in range(8):
            for c in range(8):
                idx = chess.square(c, 7-r)
                color = "#DDB88C" if (r + c) % 2 == 0 else "#A66D4F"
                self.buttons[idx].config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()