import re

# Define the regex pattern for hashtags
hash_pattern = r'#\w+'

# Example text containing hashtags
text = "This is a sample text with some #hashtags and other #words."

# Perform the substitution
text = re.sub(hash_pattern, '[HASH]', text)

print(text)
