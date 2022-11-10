import json
import os

class Sessions:
    def __init__(self, base, sub_directory):
        self.base = base
        self.sub_directory = sub_directory

    def structure(self):
        return sorted(
            [Session(self.sub_directory, session) for session in os.listdir(self.directory()) if os.path.isdir(os.path.join(self.directory(), session)) and session.startswith('session')],
            key = lambda s: s.index
        )

    def directory(self):
        return os.path.join(self.base, self.sub_directory)

class Session:
    def parse(directory, input):
        url = os.path.join(directory, input, "index.html")
        parts = input.split('-')
        index = int(parts[1])
        name = parts[0].capitalize() + ' ' + str(index + 1)
        return {'name': name, 'url': url, 'index': index}

    def __init__(self, directory,  input):
        structure = Session.parse(directory, input)
        self.name = structure['name']
        self.url = structure['url']
        self.index = structure['index']
    
    def structure(self):
        return {'name': self.name, 'url': self.url, 'index': self.index}


class SessionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Session) or isinstance(obj, Sessions):
            return obj.structure()
        else:
            return json.JSONEncoder.default(self, obj) 


if __name__ == '__main__':
    directory = '../../docs/'
    sessions = Sessions(directory, 'presentation/')
    output = json.dumps(sessions, cls=SessionEncoder)

    f = open(os.path.join(directory, 'presentations.json'), 'w')
    f.write(output)
    f.close
    