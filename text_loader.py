import concurrent.futures
import re

def read_file(file_path):
    """Reads text file and returns content"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def split_text(text, chunk_size=1000):
    """Splits text into smaller chunks"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def pattern_filter(text_chunk, pattern=r'\b\w+\b'):
    """Finds words using regex pattern"""
    return re.findall(pattern, text_chunk)

def process_chunk(chunk):
    """Processes each chunk (pattern filtering)"""
    words = pattern_filter(chunk)
    return len(words)

def parallel_process(text_chunks):
    """Processes chunks in parallel"""
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk) for chunk in text_chunks]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results
