import sets as st

def main():
    n = int(input("Enter number of players: "))
    func = st.inputCharacteristicFunction(n)
    perm = st.getPermutation(n)
    for i in range(1, n + 1):
        print(st.calcShapleyValue(perm, func, i))

main()