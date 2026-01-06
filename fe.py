import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # 1. Length of URL
    features.append(len(url))

    # 2. Presence of IP address
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # 3. '@' symbol
    features.append(1 if '@' in url else 0)

    # 4. Number of subdomains
    parsed = urlparse(url)
    features.append(len(parsed.netloc.split('.')) - 2)

    # 5. HTTPS
    features.append(1 if parsed.scheme == 'https' else 0)

    # 6. Hyphen in domain
    features.append(1 if '-' in parsed.netloc else 0)

    return features
