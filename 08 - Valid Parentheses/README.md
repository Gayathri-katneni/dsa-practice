# 08 - Valid Parentheses

> This README was written by an AI assistant (Claude) based on the existing `Solution.py`.

## Problem Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine whether the input string is valid.

A string is valid if:
1. Open brackets are closed by the same type of bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Approach

Use a **stack**. The most recently opened bracket must be the first one closed (last-in, first-out), which is exactly what a stack models.

The solution keeps a dictionary `mapping` from each *closing* bracket to its matching *opening* bracket:

```python
mapping = {")": "(", "}": "{", "]": "["}
```

## Step-by-Step Logic

1. Create an empty list `stack`.
2. Iterate over each character `char` in `s`:
   - **Opening bracket** (not a key of `mapping`): push it onto the stack.
   - **Closing bracket** (a key of `mapping`):
     - Pop the top of the stack. If the stack is empty, use the placeholder `'#'`, which never equals a real opening bracket.
     - If `mapping[char]` differs from the popped value, return `False` (wrong type, wrong order, or no opener).
3. After the loop, return `not stack`. The string is valid only if every opener was matched, so the stack must be empty.

## Example Walkthrough

Input: `s = "([)]"`

| char | action | stack after |
|------|--------|-------------|
| `(` | push | `['(']` |
| `[` | push | `['(', '[']` |
| `)` | pop `[`; expected `(` -> mismatch | return `False` |

Output: `False`

Input: `s = "{[]}"`

| char | action | stack after |
|------|--------|-------------|
| `{` | push | `['{']` |
| `[` | push | `['{', '[']` |
| `]` | pop `[`, matches `[` | `['{']` |
| `}` | pop `{`, matches `{` | `[]` |

The stack is empty at the end, so the output is `True`.

## Complexity

- **Time:** O(n). Each character is processed once, and push/pop are O(1).
- **Space:** O(n). In the worst case (for example `"((((("`) every character is on the stack.
