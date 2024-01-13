import mapper

def InputSplitter(combtext):
    words = combtext.replace("\n", " ").strip().lower().split(" ")
    final = "(" + words[0] + ",1)"
    for i in range(1, len(words)):
        final += " (" + words[i] + ",1)"
    path = f"./MapFiles/{mapper.MapperPort}"
    with open(path, "w") as f:
        f.write(final)
    return final