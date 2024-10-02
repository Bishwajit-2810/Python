balance=int(input())
transactions=list(map(int,input().split()))

for i in range(len(transactions)):
    print("initial balance: ",balance)
    balance=balance+transactions[i]
    print(f"transaction {i+1}: {str(transactions[i])}, new balance= {balance}")

print(f"final balance: ",balance)