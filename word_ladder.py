#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.

    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472> for a discussion about a common memory management bug that causes the generated word ladders to be too long in some cases.
    '''
    dictionary = set()
    with open(dictionary_file) as prelim_dict:
        for line in prelim_dict:
            word = line.strip()
            dictionary.add(word)
    stack = [start_word]
    queue = deque()
    queue.append(stack)
    while queue:
        current_stack = queue.popleft()
        for word in list(dictionary):
            if _adjacent(current_stack[-1], word):
                if word == end_word:
                    return current_stack + [word]
                else:
                    new_stack = current_stack[:]
                    new_stack.append(word)
                    queue.append(new_stack)
                    dictionary.remove(word)
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    i = 0
    for word in range(len(ladder)):
        if i = len(ladder) - 1:
            return True
        if _adjacent(ladder[i], ladder[i+1]) is False:
            return False
        else:
            i += 1

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    for i in range(len(word1):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    if count == 0:
        return False
    if count == 1:
        return True
