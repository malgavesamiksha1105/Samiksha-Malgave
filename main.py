from text_loader import read_file, split_text, parallel_process

def main():
    file_path = "data/sample.txt"

    print("Reading file...")
    text = read_file(file_path)

    print("Splitting text...")
    chunks = split_text(text, chunk_size=500)

    print("Processing in parallel...")
    results = parallel_process(chunks)

    print("Processing Complete!")
    print("Word count per chunk:", results)
    print("Total words:", sum(results))

if __name__ == "__main__":
    main()
