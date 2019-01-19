def clean_tweet(tweet_text):
    emoticons_str = r"""
    (?:
    [<>]?
    [:;=8]                     # eyes
    [\-o\*\']?                 # optional nose
    [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
    |
    [\-o\*\']?                 # optional nose
    [:;=8]                     # eyes
    [<>]?
    |
    <3                         # heart
    )"""
    regex_str = [
        emoticons_str,
        r'(?:@[\w_]+)',  # @mentions
        r'(?:\#+[\w_]+[\w\'_\-]*[\w_]+)',  # hashtags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'  # URLs
        ]

    tokens_re = re.compile(
        r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)

    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(tweet_text)
    clean_tokens = []
    for token in tokens:
        if tokens_re.findall(token):
            clean_tokens.append(token)
        else:
            if not re.match(r'[^\w\s]', token):
            clean_tokens.append(token)

    return " ".join(clean_tokens)
