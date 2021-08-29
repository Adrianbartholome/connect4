import random
import sys

# build dict game board info
board = {0: {1: '1 ', 2: '2 ', 3: '3 ', 4: '4 ', 5: '5 ', 6: '6 ', 7: '7 '},
         1: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '},
         2: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '},
         3: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '},
         4: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '},
         5: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '},
         6: {1: '# ', 2: '# ', 3: '# ', 4: '# ', 5: '# ', 6: '# ', 7: '# '}}

win = 'O '
lose = '@ '


# draw the game board
def play():
    print()
    x = -1
    a = ''
    for i in range(7):
        x += 1
        y = 0
        for j in range(7):
            y += 1
            a = a + board[x][y]
        print(a)
        a = ''
    print()


# set up ai behavior
def ai():
    chose = False
    lastresort = True
    while not chose:
        k = 7
        while (k > 0):
            k -= 1
            l = 6
            while (l > 2):
                l -= 1

                # check for horizontal block from left
                if ((board[k][l] == 'O ') and (board[k][l + 1] == 'O ') and (board[k][l + 2] == 'O ')):
                    try:
                        if (board[k][l + 3] == '# '):
                            if (k == 6):
                                board[k][l + 3] = '@ '
                                chose = True
                                lastresort = False
                                break
                            if (k < 6):
                                if (board[k + 1][l + 3] != '# '):
                                    board[k][l + 3] = '@ '
                                    chose = True
                                    lastresort = False
                                    break
                    except KeyError:
                        pass
                    if (board[k][l - 1] == '# '):
                        try:
                            if (k == 6):
                                board[k][l - 1] = '@ '
                                chose = True
                                lastresort = False
                                break
                            if (k < 6):
                                if (board[k + 1][l - 1] != '# '):
                                    board[k][l - 1] = '@ '
                                    chose = True
                                    lastresort = False
                                    break
                        except KeyError:
                            pass

            # check for vertical block
            l = 8
            while (l > 1):
                l -= 1
                if (board[k][l] == 'O '):
                    if ((board[k - 1][l] == 'O ') and (board[k - 2][l] == 'O ') and (board[k - 3][l] == '# ')):
                        board[k - 3][l] = '@ '
                        chose = True
                        lastresort = False
                        break

        # if no block available, choose random
        if lastresort:
            anb = random.choice(range(1, 8))
            k = 6
            while (k > 0):
                if (board[k][anb] == '# '):
                    board[k][anb] = '@ '
                    check()
                    chose = True
                    break
                k -= 1


# force numeric input
def answer():
    while True:
        ans = input('Choose a position: ')
        try:
            ans = int(ans)
            return ans
        except ValueError:
            pass


# check for 4 in a row, mark the the winning row on the board
def check():
    end = False
    ex = False

    # horizontal check
    while True:
        if not end:
            b = 0
            while (b < 6):
                b += 1
                c = 0
                while (c < 4):
                    c += 1
                    if ((board[b][c] == 'O ') or (board[b][c] == '@ ')):
                        if ((c + 3) < 8):
                            a = board[b][c] + board[b][c + 1] + board[b][c + 2] + board[b][c + 3]
                            if (4 * win in a):
                                print('You win!')
                                board[b][c] = board[b][c + 1] = board[b][c + 2] = board[b][c + 3] = '! '
                                ex = True
                                break
                            if (4 * lose in a):
                                print('You lose!')
                                board[b][c] = board[b][c + 1] = board[b][c + 2] = board[b][c + 3] = '¡ '
                                ex = True
                                break

            # vertical check
            b = 0
            while (b < 6):
                b += 1
                c = 0
                while (c < 6):
                    c += 1
                    if ((board[b][c] == 'O ') or (board[b][c] == '@ ')):
                        if ((b - 3) > 0):
                            a = board[b][c] + board[b - 1][c] + board[b - 2][c] + board[b - 3][c]
                            if (4 * win in a):
                                print('You win!')
                                board[b][c] = board[b - 1][c] = board[b - 2][c] = board[b - 3][c] = '! '
                                ex = True
                                break
                            if (4 * lose in a):
                                print('You lose!')
                                board[b][c] = board[b - 1][c] = board[b - 2][c] = board[b - 3][c] = '¡ '
                                ex = True
                                break

            # diag down check
            b = 0
            while (b < 3):
                b += 1
                c = 0
                while (c < 4):
                    c += 1
                    if ((board[b][c] == 'O ') or (board[b][c] == '@ ')):
                        if (((b + 3) < 8) and ((c + 3) < 8)):
                            a = board[b][c] + board[b + 1][c + 1] + board[b + 2][c + 2] + board[b + 3][c + 3]
                            if (4 * win in a):
                                print('You win!')
                                board[b][c] = board[b + 1][c + 1] = board[b + 2][c + 2] = board[b + 3][c + 3] = '! '
                                ex = True
                                break
                            if (4 * lose in a):
                                print('You lose!')
                                board[b][c] = board[b + 1][c + 1] = board[b + 2][c + 2] = board[b + 3][c + 3] = '¡ '
                                ex = True
                                break

            # diag up check
            b = 0
            while (b < 6):
                b += 1
                c = 0
                while (c < 4):
                    c += 1
                    if ((board[b][c] == 'O ') or (board[b][c] == '@ ')):
                        if (((b - 3) > 0) and ((c + 3) < 8)):
                            a = board[b][c] + board[b - 1][c + 1] + board[b - 2][c + 2] + board[b - 3][c + 3]
                            if (4 * win in a):
                                print('You win!')
                                board[b][c] = board[b - 1][c + 1] = board[b - 2][c + 2] = board[b - 3][c + 3] = '! '
                                ex = True
                                break
                            if (4 * lose in a):
                                print('You lose!')
                                board[b][c] = board[b - 1][c + 1] = board[b - 2][c + 2] = board[b - 3][c + 3] = '¡ '
                                ex = True
                                break
        end = True
        break

    # end program if win or lose
    if ex:
        play()
        sys.exit(0)

    # game start


play()
while True:
    # drop a piece on the game board
    an = answer()
    j = 6
    while (j > 0):
        if ((an > 0) and (an < 8)):
            if (board[j][an] == '# '):
                board[j][an] = 'O '
                check()
                break
            j -= 1
        else:
            break
    ai()
    play()