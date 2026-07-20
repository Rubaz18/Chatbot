from flask import Flask, render_template, request, jsonify
import os
import re
import random
import ast
import operator as op
import math

app = Flask(__name__)

# Simple joke list
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
]


# Safe eval for math expressions using ast
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

ALLOWED_NAMES = {k: getattr(math, k) for k in [
    'sin','cos','tan','sqrt','log','log10','floor','ceil','factorial','fabs','pow'
] if hasattr(math, k)}


def safe_eval(expr: str):
    """Evaluate an arithmetic expression safely."""
    try:
        node = ast.parse(expr, mode='eval')

        def _eval(n):
            if isinstance(n, ast.Expression):
                return _eval(n.body)
            if isinstance(n, ast.Constant):
                return n.value
            if isinstance(n, ast.Num):
                return n.n
            if isinstance(n, ast.BinOp):
                left = _eval(n.left)
                right = _eval(n.right)
                op_func = ALLOWED_OPERATORS.get(type(n.op))
                if op_func is None:
                    raise ValueError('Operator not allowed')
                return op_func(left, right)
            if isinstance(n, ast.UnaryOp):
                operand = _eval(n.operand)
                op_func = ALLOWED_OPERATORS.get(type(n.op))
                if op_func is None:
                    raise ValueError('Unary operator not allowed')
                return op_func(operand)
            if isinstance(n, ast.Call):
                if isinstance(n.func, ast.Name):
                    func_name = n.func.id
                    func = ALLOWED_NAMES.get(func_name)
                    if func is None:
                        raise ValueError('Function not allowed')
                    args = [_eval(a) for a in n.args]
                    return func(*args)
            if isinstance(n, ast.Name):
                if n.id in ALLOWED_NAMES:
                    return ALLOWED_NAMES[n.id]
            raise ValueError('Unsupported expression')

        return _eval(node)
    except Exception as e:
        raise


def detect_intent(text: str):
    t = text.lower().strip()
    if any(word in t for word in ['joke', 'tell me a joke', 'make me laugh']):
        return 'joke'
    # simple calculation detection: contains digits and math operators
    if re.search(r'[0-9]+\s*[-+*/%^()]', text) or re.search(r'\d+\s*(\+|\-|\*|/|%|\^)', text):
        return 'calculate'
    if any(word in t for word in ['solve', 'how to', 'explain', 'fix', 'help with']):
        return 'solve'
    return 'chat'


def handle_message(text: str):
    intent = detect_intent(text)
    if intent == 'joke':
        return random.choice(JOKES)
    if intent == 'calculate':
        # try to extract expression
        expr = text
        # remove words
        expr = re.sub(r'[A-Za-z,?]+', '', expr)
        expr = expr.replace('^', '**')
        try:
            result = safe_eval(expr)
            return f'Result: {result}'
        except Exception:
            return "I couldn't parse that expression. Try something like '2+2*3' or 'sqrt(16)'."

    # For 'solve' and 'chat', prefer OpenAI if API key present, otherwise fallback
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            import openai
            openai.api_key = api_key
            resp = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': text},
                ],
                max_tokens=400,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            # fallback on error
            return "I tried to use the cloud service but couldn't — try again or set OPENAI_API_KEY."

    # Local fallback: brief guidance and ask clarifying question
    if intent == 'solve':
        return "I can help — could you describe the problem more specifically? If it's math, include the expression."
    return "Hi! I can tell jokes, do calculations (e.g. '2+2' or 'sqrt(16)'), or try to help with problems. What would you like?"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/message', methods=['POST'])
def api_message():
    data = request.get_json() or {}
    text = data.get('message', '')
    if not text:
        return jsonify({'reply': "Please send a message."})
    reply = handle_message(text)
    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
