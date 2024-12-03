def display(fr):
    print("\n" + "\t".join(map(str, fr)))

def fifo_page_replacement(pages, frsize):
    fr = [-1] * frsize
    top = pf = 0
    for page in pages:
        if page not in fr:
            fr[top] = page
            top = (top + 1) % frsize
            pf += 1
        display(fr)
    print(f"Number of page faults: {pf}")

if __name__ == "__main__":
    n = int(input("Enter the number of pages: "))
    pages = [int(input(f"Enter page {i + 1}: ")) for i in range(n)]
    frsize = int(input("Enter frame size: "))
    fifo_page_replacement(pages, frsize)
