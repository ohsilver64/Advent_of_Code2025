import pandas as pd

def read_file(filepath, sep=None):
    rows = []
    with open(filepath,'r') as f:
        for line in f:
            rows.append(list(line.strip("\n")))
    df = pd.DataFrame(rows)

    df.columns = range(df.shape[1])

    print(f'Shape: {df.shape}')
    return df

def make_num_from_col(col):

    seq = [str(i) for i in col[:4]]
    string = "".join(seq)
    return int(string)


def calculate_block(df): #should be the block of strings. columns -> int
    op = df.iloc[4,0]
    product = 1
    nums = []
    for i in range(df.shape[1]):
        col = df.iloc[:,i]
        num = make_num_from_col(col)
        nums.append(num)
    if op == "+":
        return sum(nums)
    elif op == "*":
        for i in nums:
            product *= i
        return product
    else:
        print(f"Could not parse the operation: got {op}")
        return 0


def get_separator_indices(df):
    separator_indices = []
    
    for i in range(df.shape[1]):
        col = df.iloc[:, i]
        
        # Strip whitespace and check whether all entries are empty
        if col.apply(lambda x: str(x).strip() == "").all():
            separator_indices.append(i)

    return separator_indices

def solutionB(df):
    sep_indices = get_separator_indices(df)
    sep_indices = sorted(sep_indices)  # ensure sorted!
    count = 0

    for i, sep in enumerate(sep_indices):
        if i == 0:
            start = 0
        else:
            start = sep_indices[i-1] + 1
    
        block = df.iloc[:, start:sep]
        count += calculate_block(block)
    end_block = df.iloc[:, sep_indices[-1] + 1 :]
    count += calculate_block(end_block)
    return count
        

def main():
    # Try sep='\\s+' if your data is space-separated
    df = read_file("input.txt")
    #print(df.head())
    print(solutionB(df))
    

if __name__ == "__main__":
    df = main()