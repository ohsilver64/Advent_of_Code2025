import pandas as pd

def read_file(filepath,sep=None):
    df = pd.read_csv(filepath, header=None,sep=sep)
    print(df.shape)
    # Rename columns numerically: 0, 1, 2, ...
    df.columns = [str(i) for i in range(df.shape[1])]
    return df

def calculate_col(col):
    op = col.iloc[4]
    product = 1
    if op == '+':
        return sum(int(i) for i in col.iloc[:4])
    if op == '*':
        for i in col.iloc[:4]:
            product *= int(i)
        return product
    else: 
        return 0

def solutionA(df):
    count = 0
    for i in range(df.shape[1]):
        col = df[str(i)]
        count += calculate_col(col)
    return count
def main(): 
    input = read_file("input.txt", sep="\\s+")
    print(solutionA(input))



if __name__ == "__main__":
    df = main()