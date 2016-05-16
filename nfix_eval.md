**\*fix conversion using stacks:**
===

# Conversion of infix expressions to \*fix:
For conversion to postfix expressions, read in the string holding the expression to evaluate character by character from left to right. If the character is an operand (number), move the character to the expression. If the character is an operator, push it to the stack if the stack is empty. If the operator on top of the stack is of greater or equal (`>=`) precedence than the current operator, pop the top operator off of the stack and move it to the expression. Then push the current operator to the stack. If the top operator's precedence is lower than the current operator's then push it to the stack. If the character is an opening parenthesis, push the parenthesis to the stack. If the character is a closing parenthesis, pop operators off the stack until an opening parenthesis is found, then discard the parenthesis.

### Postfix:
```python
for char in expr:
    if char in operands:
        #move to evaluate_expression
    if char in operators:
        if stack.is_empty():
            stack.push(char)
        if stack.top().precedence() >= precedence(char):
            #move stack.top() to expression
            #stack.push(char)
        else:
            stack.push(char)
    if char == '(':
        stack.push(char)
    if char == ')':
        #pop stack and move to expression until hit '(', and discard '('.
```
### Prefix:

Start from other end. Reverse parenthesis rule. Change `>=` to `>` in precedence rules.

# Evaluation of \*fix expressions with stacks:

For postfix, read the expression character by character from left to right. If the character is an operand, push to the stack. If it is an operator, pop the top two items from the stack and push the resulting number to the stack. Continue until end of the expression.
