import re


class Router:

    def __init__(self):
        self.url_patterns = []

    def register(self, method, path, view):
        self.url_patterns.append(
            dict(method=method, path=path, view=view)
        )

    def search(self, method, path):
        for url_pattern in self.url_patterns:
            if url_pattern.get('method') == method:
                if re.compile(url_pattern.get('path')).search(path):
                    return url_pattern.get('view')
        return None
