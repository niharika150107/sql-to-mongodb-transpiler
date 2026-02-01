import sqlparse
from sqlparse.tokens import Keyword, DML, Name, Operator, Number, String, Punctuation
from lexer.lexer import tokenize
def sqlparse_tokens(sql_query):
    parsed = sqlparse.parse(sql_query)[0]
    result = []

    for token in parsed.flatten():
        if token.is_whitespace:
            continue

        result.append({
            "type": str(token.ttype),
            "value": token.value
        })

    return result
query =input("Enter your query:")

print("----- PLY TOKENS -----")
ply_tokens = tokenize(query)
for t in ply_tokens:
    print(f"{t['type']:10} | {t['value']}")

print("\n----- SQLPARSE TOKENS -----")
sqlparse_out = sqlparse_tokens(query)
for t in sqlparse_out:
    print(f"{t['type']:30} | {t['value']}")
