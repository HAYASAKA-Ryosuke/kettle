import re


class Router:

    def __init__(self):
        self.url_patterns = []
        self.ROOT = '^/$'

    def register(self, method, path, view):
        action_keys = re.findall(':[a-zA-Z_]*', path)
        for action_key in action_keys:
            path = path.replace(action_key, '([a-z-A-Z0-9_]+)')
        path = path + '?' if path[-1] == '/' else path + '/?'
        path = '^' + path + '$'
        action_keys = [action_key.strip(':') for action_key in action_keys]
        self.url_patterns.append(
            dict(method=method, path=path, view=view, action_keys=action_keys)
        )

    def search(self, method, path):
        for url_pattern in self.url_patterns:
            if url_pattern.get('method') == method:
                match = re.compile(url_pattern.get('path')).match(path)
                if match:
                    action_values = match.groups()
                    return url_pattern.get('view'), dict(zip(url_pattern.get('action_keys'), action_values))
        return None, None
