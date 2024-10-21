import re
from collections import Counter
import socket

# File paths
file1_path = '/home/data/IF.txt'
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'
output_path = '/home/data/output/result.txt'

# Function to clean text without handling contractions
def clean_text_simple(text):
    # Remove non-alphabetic characters except spaces
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    return text.lower().split()

# Function to clean text and handle contractions (for AlwaysRememberUsThisWay.txt)
def clean_text_with_contractions(text):
    # Define common English contractions and their expansions
    contractions = {
        "I'm": "I am", "he's": "he is", "she's": "she is", "it's": "it is", "we're": "we are", "they're": "they are", "you're": "you are",
        "I've": "I have", "can't": "can not", "won't": "will not", "isn't": "is not", "wasn't": "was not", "don't": "do not", "that's": "that is",
        "doesn't": "does not", "didn't": "did not", "couldn't": "could not", "shouldn't": "should not", "wouldn't": "would not",
        "weren't": "were not", "I'll": "I will", "you'll": "you will", "they'll": "they will", "I'd": "I would", "he'd": "he would", 
        "she'd": "she would", "we'd": "we would", "you'd": "you would", "he'll": "he will", "she'll": "she will", "they've": "they have"
    }
    
    # Replace contractions with their expanded forms
    for contraction, expansion in contractions.items():
        text = re.sub(contraction, expansion, text)
    
    #text = re.sub(r'[^\w\s]', '', text.lower())
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Convert to lowercase
    return text.lower().split()

# Function to count words in a file (without handling contractions)
def count_words_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = clean_text_simple(file.read())
        word_count = len(words)
        word_freq = Counter(words)
    return word_count, word_freq

# Function to count words in AlwaysRememberUsThisWay.txt (with handling contractions)
def count_words_in_file_with_contractions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = clean_text_with_contractions(file.read())
        word_count = len(words)
        word_freq = Counter(words)
    return word_count, word_freq

# Count words and get frequency for IF.txt (simple word count, no contraction handling)
file1_word_count, file1_word_freq = count_words_in_file(file1_path)

# Count words and get frequency for AlwaysRememberUsThisWay.txt (handle contractions)
file2_word_count, file2_word_freq = count_words_in_file_with_contractions(file2_path)

# Grand total of words across both files
grand_total_words = file1_word_count + file2_word_count

# Top 3 most frequent words in IF.txt
file1_top3 = file1_word_freq.most_common(3)

# Top 3 most frequent words in AlwaysRememberUsThisWay.txt (with contractions handled)
file2_top3 = file2_word_freq.most_common(3)

# Determine the IP address of the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to output file
with open(output_path, 'w', encoding='utf-8') as result_file:
    result_file.write(f"File: IF.txt\nTotal words: {file1_word_count}\n")
    result_file.write(f"Top 3 words: {file1_top3}\n\n")

    result_file.write(f"File: AlwaysRememberUsThisWay.txt\nTotal words (with contractions handled): {file2_word_count}\n")
    result_file.write(f"Top 3 words (after handling contractions): {file2_top3}\n\n")

    result_file.write(f"Grand total of words across both files: {grand_total_words}\n")
    result_file.write(f"IP address of the container: {ip_address}\n")

# Print the contents of result.txt to the console
with open(output_path, 'r', encoding='utf-8') as result_file:
    print(result_file.read())
