ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

correct_ans = ["42", "forty-two", "forty two"]

if ans.lower().strip() in correct_ans:
    print("Yes")

else:
    print("No")