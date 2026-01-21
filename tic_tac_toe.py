{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8e722932-a4bb-487b-8c36-3731d7d32968",
   "metadata": {},
   "source": [
    "## 1. Board Creation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0d1f9e42-d74b-48ba-926d-2546395f1773",
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "\n",
    "def display_board(board):\n",
    "    clear_output()\n",
    "    print(board[7],'|',board[8],'|',board[9])\n",
    "    print(' --------')\n",
    "    print(board[4],'|',board[5],'|',board[6])\n",
    "    print(' --------')\n",
    "    print(board[1],'|',board[2],'|',board[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2719eb60-04e2-419f-8107-d9832ebfb80c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  |   |  \n",
      " --------\n",
      "  |   |  \n",
      " --------\n",
      "  |   |  \n"
     ]
    }
   ],
   "source": [
    "test_board = [' ']*10\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b99a02f-4cf3-4d04-bcb1-68f657131114",
   "metadata": {},
   "source": [
    "## 2. Mark Selection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ce12e355-9c21-45a4-b1eb-3bde14f0659a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_input():\n",
    "    marker = ''\n",
    "    \n",
    "    while not (marker == 'X' or marker == 'O'):\n",
    "        marker = input('Player 1: Do you want to be X or O? ').upper()\n",
    "\n",
    "    if marker == 'X':\n",
    "        return ('X', 'O')\n",
    "    else:\n",
    "        return ('O', 'X')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6b07a5e-b4c8-45bf-9677-3915bab572cf",
   "metadata": {},
   "source": [
    "## 3. Item Insertion "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c4653ac9-93e2-4bef-83b3-65d52d168837",
   "metadata": {},
   "outputs": [],
   "source": [
    "def place_marker(board, marker, position):\n",
    "    marker=input('Insert X or O')\n",
    "    \n",
    "    position = int(input('Select desired position'))\n",
    "    board[position]= marker\n",
    "    return (marker, position)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "76245141-6006-4223-933c-209b28fb6785",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  |   |  \n",
      " --------\n",
      "  |   | o\n",
      " --------\n",
      "  |   |  \n"
     ]
    }
   ],
   "source": [
    "place_marker(test_board,'$',8)\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fd7ab14-0262-45ed-93e0-891b6d6a7f6f",
   "metadata": {},
   "source": [
    "## 4. Win Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "84655c5c-09ca-4dac-8250-f589d6a4e3c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board,marker):\n",
    "    \n",
    "    return ((board[1]==board[2] and board[2]==board[3]) or\n",
    "    (board[4]==board[5] and board[5]==board[6]) or\n",
    "    (board[7]==board[8] and board[8]==board[9]) or\n",
    "    (board[1]==board[4] and board[4]==board[7]) or\n",
    "    (board[2]==board5[5] and board[5]==board[8]) or\n",
    "    (board[3]==board[6] and board[6]==board[9]) or\n",
    "    (board[3]==board[5] and board[5]==board[7]) or\n",
    "    (board[1]==board[5] and board[5]==board[9]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "85567648-8977-45da-b693-e7b807753f91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "win_check(test_board,'X')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a055f68f-9507-4685-b0dd-de905e8ac0f0",
   "metadata": {},
   "source": [
    "## 5. Randomized Player Selection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bb759b01-6f97-419f-8dd3-777b67721546",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def choose_first():\n",
    "    a=random.randint(0,1)\n",
    "    if a==0:\n",
    "        return ('Player 1 go first')\n",
    "    else:\n",
    "        return ('Player 2 go first')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8aef815c-2e3f-4d29-a971-701654436628",
   "metadata": {},
   "source": [
    "## 6. Space Vacancy Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b1fec143-91b9-49be-9884-eadefbb0e6a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def space_check(board, position):\n",
    "    b=board[position]\n",
    "    if b==' ':\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41d94411-795e-4eb3-b522-bf52de0f4a6c",
   "metadata": {},
   "source": [
    "## 7. Board Is Full or Not"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "af12a8c4-ce72-481c-becd-217ac6fa7398",
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "    free=' '\n",
    "    if free not in board:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1d6526e-5cf0-418b-807f-18701a83c32f",
   "metadata": {},
   "source": [
    "## 8. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1cdeffe1-7366-4f83-9bdf-1e10564b05ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_choice(board):\n",
    "    position = 0\n",
    "    \n",
    "    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):\n",
    "        position = int(input('Choose your next position: (1-9) '))\n",
    "\n",
    "\n",
    "    return position"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88631ca8-afb7-4ab8-bcfa-c7690ce4cd5f",
   "metadata": {},
   "source": [
    "## 9. Replay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "737b2b6c-f09f-4a03-b7a0-34115843b3ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "    r = int(input('Do you want to play again ? Y or N ?'))\n",
    "\n",
    "    if r=='Y':\n",
    "        return True\n",
    "    elif r=='N':\n",
    "        return False\n",
    "    \n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cabbb4b5-2c01-49fb-bf94-807985de7605",
   "metadata": {},
   "source": [
    "## 10. Compilation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ee6c16e-5a34-4028-8095-b8850f2ddd66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  |   | x\n",
      " --------\n",
      "  |   |  \n",
      " --------\n",
      "  |   |  \n",
      "Congratulations, Player 1 won.\n"
     ]
    }
   ],
   "source": [
    "print('Welcome to Tic Tac Toe!')\n",
    "\n",
    "while True:\n",
    "    test_board = [' ']*10\n",
    "    player1, player2 =player_input()\n",
    "    turn = choose_first()\n",
    "    print(turn)\n",
    "\n",
    "    play = input('Are you ready ? Yes or No ?')\n",
    "    if play.lower()[0]=='y':\n",
    "        game_on = True\n",
    "    else:\n",
    "        game_on = False\n",
    "\n",
    "    while game_on:\n",
    "        if turn=='Player 1 go first':\n",
    "            display_board(test_board)\n",
    "            position = player_choice(test_board)\n",
    "            place_marker(test_board, player1, position)\n",
    "            \n",
    "            if win_check(test_board,player1):\n",
    "                display_board(test_board)\n",
    "                print ('Congratulations, Player 1 won.')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(test_board):\n",
    "                    display_board(test_board)\n",
    "                    print('It is a draw.')\n",
    "                    break\n",
    "                else:\n",
    "                    turn='Player 2 go first'\n",
    "       \n",
    "        \n",
    "        else:\n",
    "            display_board(test_board)\n",
    "            position = player_choice(test_board)\n",
    "            place_marker(test_board, player2, position)\n",
    "            \n",
    "            if win_check(test_board,player2):\n",
    "                display_board(test_board)\n",
    "                print ('Congratulations, Player 2 won.')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(test_board):\n",
    "                    display_board(test_board)\n",
    "                    print('It is a draw.')\n",
    "                    break\n",
    "                else:\n",
    "                    turn='Player 1 go first'\n",
    "\n",
    "\n",
    "    if not replay():\n",
    "        break\n",
    "            \n",
    "                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0953efbc-67af-4180-aacb-5b275422f0b4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
