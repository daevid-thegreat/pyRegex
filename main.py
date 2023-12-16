import re
import os

with open('text.txt', 'r') as f:
	za_text = f.read()


def get_phone_numbers(text):
	pattern = r'\b\d{11}\b'
	matches = re.findall(pattern, text)
	print(matches)


get_phone_numbers(za_text)


def get_phone_numbers_with_nigeria_code(text):
	pattern = r'\+234\d{10}\b'
	matches = re.findall(pattern, text)
	print(matches)


get_phone_numbers_with_nigeria_code(za_text)


def get_all_four_letter_words(text):
	pattern = r'\b\w{4}\b'
	matches = re.findall(pattern, text)
	print(matches)


get_all_four_letter_words(za_text)


def get_all_words_that_start_with_vowel(text):
	pattern = r'\b[aeiouAEIOU]\w+\b'
	matches = re.findall(pattern, text)
	print(matches)


get_all_words_that_start_with_vowel(za_text)


def get_emails(text):
	pattern = r'\b\w+@\w+\.\w+\b'
	matches = re.findall(pattern, text)
	print(matches)


get_emails(za_text)
